"""The client: a key, a host, and the platform's resources.

Everything a caller reaches through this object is generated from the
platform's OpenAPI document. This file only builds it: reading the key from the
environment, naming each resource, and waiting for work the platform does
asynchronously.
"""

from __future__ import annotations

import os
import time
from typing import Any

import urllib3

from ._api_version import __api_version__
from ._errors import DeploymentFailed, WaitTimeout
from ._generated.api.access_policies_api import AccessPoliciesApi
from ._generated.api.api_keys_api import APIKeysApi
from ._generated.api.application_profiles_api import ApplicationProfilesApi
from ._generated.api.applications_api import ApplicationsApi
from ._generated.api.audit_api import AuditApi
from ._generated.api.availability_tiers_api import AvailabilityTiersApi
from ._generated.api.cloud_accounts_api import CloudAccountsApi
from ._generated.api.cloud_catalog_api import CloudCatalogApi
from ._generated.api.cluster_add_ons_api import ClusterAddOnsApi
from ._generated.api.clusters_api import ClustersApi
from ._generated.api.domains_api import DomainsApi
from ._generated.api.integrations_api import IntegrationsApi
from ._generated.api.notifications_api import NotificationsApi
from ._generated.api.organizations_api import OrganizationsApi
from ._generated.api.pricing_api import PricingApi
from ._generated.api.service_accounts_api import ServiceAccountsApi
from ._generated.api.users_api import UsersApi
from ._generated.api_client import ApiClient
from ._generated.configuration import Configuration
from ._generated.models.application import Application
from ._generated.models.application_status import ApplicationStatus
from ._version import __version__

DEFAULT_BASE_URL = "https://api.astropulse.io"

#: No request waits forever: a connect or read that stalls this long fails
#: rather than hanging the caller's process. Pass ``timeout=None`` for no limit.
#:
#: A (connect, read) pair, because that is what the generated client understands
#: -- it hands the value to urllib3 itself and drops anything else on the floor.
DEFAULT_TIMEOUT = (10.0, 60.0)

#: The API rate limits in layers and answers 429 with Retry-After; its own
#: documentation says to back off and retry. So the client does, for the
#: requests that are safe to repeat -- a failed POST is the caller's to decide
#: about, since repeating one can create a second thing.
DEFAULT_RETRIES = urllib3.Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=(429, 500, 502, 503, 504),
    allowed_methods=frozenset({"GET", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"}),
    respect_retry_after_header=True,
    raise_on_status=False,
    # Retry-After is obeyed as given; this stops a long one parking an
    # unattended client for the rest of the afternoon.
    backoff_max=30,
)

# The name each resource is reached through. The generated classes are named
# after the document's tags; these are what a caller types. Private, because it
# is construction machinery -- the attributes it produces are the public part.
_RESOURCES = {
    "access_policies": AccessPoliciesApi,
    "api_keys": APIKeysApi,
    "service_accounts": ServiceAccountsApi,
    "applications": ApplicationsApi,
    "application_profiles": ApplicationProfilesApi,
    "audit": AuditApi,
    "availability_tiers": AvailabilityTiersApi,
    "cloud_accounts": CloudAccountsApi,
    "cloud_catalog": CloudCatalogApi,
    "cluster_addons": ClusterAddOnsApi,
    "clusters": ClustersApi,
    "domains": DomainsApi,
    "integrations": IntegrationsApi,
    "notifications": NotificationsApi,
    "organizations": OrganizationsApi,
    "pricing": PricingApi,
    "users": UsersApi,
}

#: The status an application reports once it is up and serving.
SERVING = ApplicationStatus.Running
#: An application whose phase is one of these is still being worked on, even
#: when its status already says RUNNING: a redeploy of something that is
#: already serving keeps serving the old revision throughout.
IN_FLIGHT = frozenset(
    {
        ApplicationStatus.Provisioning,
        ApplicationStatus.InProgress,
    }
)
#: Statuses an application can reach without ever serving.
NOT_SERVING = frozenset(
    {
        ApplicationStatus.Failed,
        ApplicationStatus.Canceled,
        ApplicationStatus.NotFound,
        ApplicationStatus.DeleteFailed,
    }
)


class Client:
    """Talks to the AstroPulse Platform API.

    The API key is read from ``ASTROPULSE_API_KEY`` unless one is passed. A key
    carries its organization, so nothing else is needed:

        >>> from astropulse import Client
        >>> ap = Client()                          # doctest: +SKIP
        >>> ap.clusters.list_clusters()            # doctest: +SKIP
    """

    access_policies: AccessPoliciesApi
    api_keys: APIKeysApi
    service_accounts: ServiceAccountsApi
    applications: ApplicationsApi
    application_profiles: ApplicationProfilesApi
    audit: AuditApi
    availability_tiers: AvailabilityTiersApi
    cloud_accounts: CloudAccountsApi
    cloud_catalog: CloudCatalogApi
    cluster_addons: ClusterAddOnsApi
    clusters: ClustersApi
    domains: DomainsApi
    integrations: IntegrationsApi
    notifications: NotificationsApi
    organizations: OrganizationsApi
    pricing: PricingApi
    users: UsersApi

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float | tuple[float, float] | None = DEFAULT_TIMEOUT,
        retries: urllib3.Retry | int | None = DEFAULT_RETRIES,
        api_client: ApiClient | None = None,
    ) -> None:
        if api_client is not None and (
            api_key is not None
            or base_url is not None
            or timeout is not DEFAULT_TIMEOUT
            or retries is not DEFAULT_RETRIES
        ):
            raise TypeError(
                "api_client carries its own host, credentials, timeout and retries; "
                "pass it alone, or let the client build one from api_key/base_url."
            )

        key = api_key or os.environ.get("ASTROPULSE_API_KEY")
        if not key and api_client is None:
            raise ValueError(
                "No API key. Pass api_key=..., or set ASTROPULSE_API_KEY. "
                "Create a key in the console under Settings, API Keys."
            )

        if api_client is None:
            # The same variable astroctl reads, so one setting points every client at a host.
            host = base_url or os.environ.get("ASTROPULSE_API_ENDPOINT") or DEFAULT_BASE_URL
            configuration = Configuration(host=host.rstrip("/"), retries=retries)
            configuration.api_key["ApiKeyAuth"] = key or ""
            api_client = ApiClient(configuration)
            api_client.user_agent = f"astropulse-python/{__version__} (api {__api_version__})"
            if timeout is not None:
                _apply_timeout(api_client, timeout)

        self._api_client = api_client
        for attribute, resource in _RESOURCES.items():
            setattr(self, attribute, resource(api_client))

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def close(self) -> None:
        """Release the connection pool the generated client holds.

        The pool lives inside generated code, so this reaches for it and stays
        quiet if a regeneration moves it: failing to close a pool at the end of
        a program is not worth an exception in the caller's face.
        """
        pool = getattr(getattr(self._api_client, "rest_client", None), "pool_manager", None)
        if pool is not None:
            pool.clear()

    def wait_until_serving(
        self, application: str, *, timeout: float = 1800, poll_interval: float = 5
    ) -> Application:
        """Block until an application serves, and return it.

        A deploy is accepted long before it is finished -- weights are pulled
        and a node is scheduled -- so this is the piece a caller would
        otherwise write by hand every time.

        It settles on two things, not one: the application's status says it is
        serving, and its phase says no deployment work is still in flight.
        Redeploying something that is already serving leaves the status on
        Running throughout, so status alone would return the old revision's
        endpoint the moment it was asked.

        Raises :class:`WaitTimeout` (a :class:`TimeoutError`) if it has not
        settled within ``timeout`` seconds, and :class:`DeploymentFailed` if it
        reaches a state it cannot serve from.
        """
        if poll_interval <= 0:
            raise ValueError("poll_interval must be greater than zero")

        deadline = time.monotonic() + timeout
        while True:
            current = self.applications.get_application(application).data
            if current is None:
                raise DeploymentFailed(
                    application,
                    None,
                    f"the platform answered about {application} with no application",
                )
            status = current.status
            if status == SERVING and current.phase not in IN_FLIGHT:
                return current
            if status in NOT_SERVING:
                raise DeploymentFailed(application, status, current.status_reason or "")
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise WaitTimeout(application, status, timeout)
            time.sleep(min(poll_interval, remaining))


def _apply_timeout(api_client: ApiClient, timeout: float | tuple[float, float]) -> None:
    """Give every request through this client a deadline.

    The generated client takes a timeout per call and defaults it to None, and
    it passes that None to urllib3 explicitly -- which urllib3 reads as "no
    limit" rather than as "use the pool's default". So configuring the pool
    achieves nothing; the value has to arrive as the per-request argument, and
    it has to be a float or a (connect, read) pair, because anything else that
    code drops on the floor.
    """
    rest = api_client.rest_client
    original = rest.request

    def request(*args: Any, **kwargs: Any) -> Any:
        # The caller may pass its own per-request timeout; ours is the default.
        if not kwargs.get("_request_timeout"):
            kwargs["_request_timeout"] = timeout
        return original(*args, **kwargs)  # type: ignore[no-untyped-call]

    rest.request = request  # type: ignore[method-assign]


__all__ = [
    "Client",
    "SERVING",
    "NOT_SERVING",
    "IN_FLIGHT",
    "DEFAULT_RETRIES",
    "DEFAULT_TIMEOUT",
]

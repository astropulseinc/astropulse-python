# coding: utf-8

"""
    AstroPulse Platform API

    The programmable production foundation for applications, AI workloads, and infrastructure products.  AstroPulse provides a unified control plane for composing cloud infrastructure, deploying workloads, and operating their production lifecycle. Provision and manage Kubernetes clusters, deploy applications and AI models, and manage networking, scaling, access, integrations, observability, cost visibility, and governance.  **Keep your product. Skip rebuilding the production layer.** AstroPulse manages the production machinery underneath your application, runtime, scheduler, inference system, or infrastructure product, while you retain ownership of the capabilities that make it different.  ## Base URL All public API endpoints are served over HTTPS at `https://api.astropulse.io` and versioned under `/api/v1`.  ## Working with AstroPulse The API follows the operational lifecycle of your infrastructure and workloads: - **Connect infrastructure:** Configure cloud accounts, discover regions, machine types, and accelerators, and provision or register Kubernetes clusters. - **Configure environments:** Manage cluster add-ons, application profiles, availability tiers, domains, and endpoint access policies. - **Deploy workloads:** Deploy applications and supported AI models, inspect their state, and discover their serving endpoints. - **Operate and recover:** Monitor deployment progress, manage supported lifecycle operations, inspect version history, plan rollbacks, and recover deployments. - **Observe and govern:** Inspect operational metrics, cost and usage data, activity, integrations, identities, permissions, and audit records.  Resources are organized by their role in the platform. Each operation defines its own parameters, request and response schemas, authentication requirements, and failure conditions.  ## Authentication AstroPulse supports API keys and short-lived bearer tokens. Each endpoint declares which authentication methods it accepts.  **API keys — recommended for automation** Send `X-Astro-API-Key: <key>`. For production automation, use an organization-owned service-account key. Service accounts are managed by organization administrators through the Service Accounts API and do not depend on an individual user's session.  Personal API keys are available under Organization settings > API Keys. API keys are scoped to one organization.  **Bearer tokens — interactive sessions** Send `Authorization: Bearer <jwt>`. These credentials are short-lived access tokens issued by the configured authentication provider.  To print an access token for a direct API request, run `astroctl auth login --print-access-token` (`-p`). A standard `astroctl auth login` stores the authenticated session without printing the token.  For unattended integrations, use API keys instead of interactive session tokens. Store all credentials securely and never expose them in repositories, client-side code, or logs.  ## SDKs and API clients The generated OpenAPI 3 specification is the public contract for AstroPulse REST API consumers and generated clients.  AstroPulse provides operation-specific Python and TypeScript SDK examples in this reference. Each generated SDK exposes resources through typed clients, with method names derived from stable API operation IDs.  **Python SDK:** Install using `pip install \"git+https://github.com/astropulseinc/astropulse-python\"`.  Common operations include `client.clusters.list_clusters()` and `client.applications.deploy_application(...)`. Consult the SDK's documentation for client initialization, authentication, and complete examples.  The same platform capabilities can be accessed through the REST API, supported SDKs, astroctl, and the AstroPulse Console. Refer to the documentation for the supported workflows of each interface.  **Application runtime endpoints:** Applications deployed through AstroPulse expose runtime endpoints separate from the platform control-plane API. Model deployments supporting the OpenAI API protocol can be called with an OpenAI-compatible client configured for the deployed endpoint and its access requirements.  ## Lifecycle and asynchronous operations Infrastructure provisioning, deployment, and certain lifecycle changes can execute asynchronously. An accepted request does not necessarily mean the underlying operation has completed.  Use the operation's response, resource status, and available progress streams to determine completion and inspect failures.  Supported application operations include version history, rollback, resume, and GitOps reconciliation. Rollback operations can provide dry-run plans so callers can inspect an eligible change before applying it.  Consult each operation for its specific state transitions, mutation semantics, retry behavior, and concurrency restrictions.  ## Observability and cost Supported resources expose deployment state, application and cluster metrics, cost and usage series, and operational diagnostics.  Metrics and cost data represent collected observations. Missing samples, incomplete coverage, and unavailable reporting intervals must not be interpreted as zero resource consumption or zero spend.  Use the coverage information, time windows, and aggregation intervals documented by each operation when processing telemetry and cost responses.  ## Real-time streaming Supported application endpoints provide real-time status, event, and log streams over WebSocket connections.  Streaming requests have different connection and authentication semantics from ordinary JSON requests. Supported browser workflows can obtain a short-lived, single-use stream ticket before establishing a WebSocket connection.  Stream tickets are valid for at most 30 seconds. Follow the individual endpoint's documented handshake, authentication, and error-handling requirements.  ## Response format Successful JSON API responses use the documented resource schema, commonly wrapped in an envelope with the result under `data` and optional `id`, `status`, and `message` fields.  Consumers must follow each endpoint's declared response type. Streaming connections and other specialized responses may have different transport semantics.  ## Errors and diagnostics API failures use a consistent JSON error structure containing: - `message`: Human-readable explanation. - `code`: Stable, machine-readable error identifier. - `status`: HTTP response status. - `traceId`: Diagnostic request trace identifier. - `details`: Optional structured error details.  **Branch on HTTP status and `code`, never on the wording of `message`.**  The `X-Trace-ID` response header exposes the request's diagnostic trace identifier. Include it when reporting failures. It is not a distributed tracing propagation header.  Common HTTP errors include: - `400 Bad Request`: Invalid input or request. - `401 Unauthorized`: Missing, invalid, expired, or revoked credentials. - `402 Payment Required`: Requested capability is unavailable under the current plan. - `403 Forbidden`: Insufficient permissions. - `404 Not Found`: Resource or route not found. - `405 Method Not Allowed`: Unsupported HTTP method for a route. - `409 Conflict`: Resource state or concurrent operation conflict. - `429 Too Many Requests`: Rate limit exceeded. - `500 Internal Server Error`: Unexpected server failure. - `503 Service Unavailable`: A required service is temporarily unavailable.  The applicable status codes and response schemas are documented for each operation.  ## Versioning and compatibility Public API versions are identified by the URL path, beginning with `/api/v1`. The generated specification's `info.version` identifies the AstroPulse build from which the document was generated.  Within an API version, backward-compatible evolution can introduce new endpoints, optional request fields, response properties, and values in extensible enumerations.  Clients should tolerate unknown response properties and supported enum extensions. Consumers must not depend on undocumented list ordering or human-readable error messages.  Breaking changes, including removing or renaming fields, changing documented field types, or making previously optional request fields mandatory, require compatibility review and an appropriate API version transition.  The generated OpenAPI specification is the authoritative contract for client generation and compatibility validation.  ## Rate limiting and retries AstroPulse applies layered request rate limits: - Global service-wide limits. - Per-IP limits. - Additional per-API-key limits. - Per-authenticated-principal limits where enabled.  Exceeding an applicable limit returns `429 Too Many Requests`. Respect the `Retry-After` response header and implement bounded exponential backoff with jitter.  Temporary service failures may return `503 Service Unavailable` with retry guidance. Retry state-changing operations only when their documented semantics make repetition safe.  Global and per-IP limits remain applicable regardless of the credential used. Rotating credentials does not bypass those limits.  ## Identity, governance, and audit AstroPulse organizes platform resources within organizations. Authentication, authorization, and applicable plan restrictions govern access to resource operations.  Mutating API requests and designated sensitive reads are recorded for auditability. Audit records capture available actor, organization, resource, action, outcome, and request context without storing request bodies or secrets.  Organization-owned service accounts provide dedicated automation identities, while API keys and user sessions retain their associated authentication and authorization boundaries.  ## Developer documentation This API reference defines the public platform contract. The [AstroPulse Documentation](https://astropulse.io/docs) provides guided workflows, platform concepts, SDK integration, CLI usage, and end-to-end examples.  API schemas and operation definitions are the source of truth for clients, developer tools, and authorized automation.

    The version of the OpenAPI document: v1.0.1
    Contact: contact@astropulse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.application_status import ApplicationStatus
from astropulse._generated.models.cluster_addon_accelerator_readiness import ClusterAddonAcceleratorReadiness
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration
from astropulse._generated.models.cluster_addon_cost_pricing import ClusterAddonCostPricing
from astropulse._generated.models.cluster_addon_exposure import ClusterAddonExposure
from astropulse._generated.models.cluster_addon_health import ClusterAddonHealth
from astropulse._generated.models.cluster_addon_ingress_tls import ClusterAddonIngressTLS
from astropulse._generated.models.cluster_addon_model_cache_readiness import ClusterAddonModelCacheReadiness
from astropulse._generated.models.cluster_addon_queue_namespaces import ClusterAddonQueueNamespaces
from astropulse._generated.models.cluster_addon_resilience import ClusterAddonResilience
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus
from astropulse._generated.models.cluster_addon_support import ClusterAddonSupport
from astropulse._generated.models.cluster_addon_tls_readiness import ClusterAddonTLSReadiness
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddon(BaseModel):
    """
    ClusterAddon
    """ # noqa: E501
    accelerator: Optional[ClusterAddonAcceleratorReadiness] = Field(default=None, description="Reported for the accelerator-metrics add-on only: what this cluster has for the exporter to measure. See ClusterAddonAcceleratorReadiness.")
    available_upgrades: Optional[List[StrictStr]] = Field(default=None, description="The versions it can move to, ordered oldest to newest: the last one is the newest release on offer.", alias="availableUpgrades")
    configurable: Optional[StrictBool] = Field(default=None, description="Reports whether this add-on accepts a configuration. False means it installs with no settings of its own.")
    configuration: Optional[ClusterAddonConfiguration] = Field(default=None, description="The settings it is running with, as they were applied.")
    current_version: Optional[StrictStr] = Field(default=None, description="The Astro chart version installed -- what `apply --version` and rollback take. See UpstreamVersion for the release inside.", alias="currentVersion")
    deployed_at: Optional[StrictStr] = Field(default=None, description="When the add-on was first installed, RFC 3339.", alias="deployedAt")
    display_name: Optional[StrictStr] = Field(default=None, description="The add-on's name in front of a person.", alias="displayName")
    display_status: Optional[StrictStr] = Field(default=None, description="The short text to show for this add-on in a list when its notice changes what to show; absent otherwise, when its status's display name applies.", alias="displayStatus")
    endpoint_authentication: Optional[List[StrictStr]] = Field(default=None, description="Lists the access-policy mechanisms (jwt, apiKeys) the installed release enforces on model endpoints. Absent when the add-on cannot enforce any: an exposure add-on that only routes, or a release the catalog does not declare.", alias="endpointAuthentication")
    exposure: Optional[ClusterAddonExposure] = Field(default=None, description="How the add-on can be reached, for the exposure add-ons (gateway, nginx-ingress) only, as the cluster agent last observed it. Absent on every other add-on.")
    findings_policy: Optional[StrictStr] = Field(default=None, description="Says which findings the vulnerability-scanning add-on leaves out of its results. Absent on every other add-on.", alias="findingsPolicy")
    health: Optional[ClusterAddonHealth] = Field(default=None, description="What the cluster reports about the add-on's own workload.")
    ingress_tls: Optional[ClusterAddonIngressTLS] = Field(default=None, description="Reported for the nginx-ingress add-on only: the TLS modes it offers applications.", alias="ingressTls")
    last_updated_at: Optional[StrictStr] = Field(default=None, description="When it was last changed, RFC 3339.", alias="lastUpdatedAt")
    model_cache: Optional[ClusterAddonModelCacheReadiness] = Field(default=None, description="Reported for the model-serving add-on only: what its weight cache holds on this cluster, and how the cluster's models read private artifacts. See ClusterAddonModelCacheReadiness.", alias="modelCache")
    name: Optional[StrictStr] = Field(default=None, description="The name of the Application serving this add-on on the cluster.")
    phase: Optional[ApplicationStatus] = Field(default=None, description="What the add-on's workload is doing now, in the same words as an application's phase. Absent before the add-on has a workload.")
    pricing: Optional[ClusterAddonCostPricing] = Field(default=None, description="Reported for the cost-visibility add-on only: the price-sheet rates its configuration sets that this cluster does not apply yet. Absent when every rate applies.")
    queue_namespaces: Optional[ClusterAddonQueueNamespaces] = Field(default=None, description="Is, for the workload-queueing add-on, where the namespaces it gives a queue differ from those of the queued applications; absent when they agree.", alias="queueNamespaces")
    resilience: Optional[ClusterAddonResilience] = Field(default=None, description="How the add-on runs on this cluster: its effective availability, how many copies run and why, and its main component's sizing.")
    status: Optional[ClusterAddonStatus] = Field(default=None, description="The lifecycle answer: is this add-on installed and working? A resync or upgrade of a working add-on leaves it `Deployed`, because it is still installed and still serving.")
    status_notice: Optional[Notice] = Field(default=None, description="Says what a failed or unhealthy status, or an unfinished rollback, means and the one step that resolves it; absent otherwise.", alias="statusNotice")
    status_reason: Optional[StrictStr] = Field(default=None, description="A sentence explaining the add-on's status, such as why it failed or why no upgrade is offered. Empty when there is nothing to explain.", alias="statusReason")
    support: Optional[ClusterAddonSupport] = Field(default=None, description="Says whether the installed version is supported and until when. Absent when the installed version is not known.")
    syncing: Optional[StrictBool] = Field(default=None, description="The operation answer: is deployment work in flight right now? `status` stays `Deployed` while a working add-on is resynced or upgraded.")
    tls: Optional[ClusterAddonTLSReadiness] = Field(default=None, description="Reported for the cert-manager add-on only: what its configuration can mint on this cluster. See ClusterAddonTLSReadiness.")
    type: Optional[ClusterAddonType] = Field(default=None, description="The add-on's public name, and what every add-on command takes.")
    upstream_version: Optional[StrictStr] = Field(default=None, description="The third-party release the installed version runs, such as \"cert-manager v1.21.2\" or \"KServe v0.20.0\". Empty when there is none.", alias="upstreamVersion")
    __properties: ClassVar[List[str]] = ["accelerator", "availableUpgrades", "configurable", "configuration", "currentVersion", "deployedAt", "displayName", "displayStatus", "endpointAuthentication", "exposure", "findingsPolicy", "health", "ingressTls", "lastUpdatedAt", "modelCache", "name", "phase", "pricing", "queueNamespaces", "resilience", "status", "statusNotice", "statusReason", "support", "syncing", "tls", "type", "upstreamVersion"]

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClusterAddon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of accelerator
        if self.accelerator:
            _dict['accelerator'] = self.accelerator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposure
        if self.exposure:
            _dict['exposure'] = self.exposure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of health
        if self.health:
            _dict['health'] = self.health.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ingress_tls
        if self.ingress_tls:
            _dict['ingressTls'] = self.ingress_tls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_cache
        if self.model_cache:
            _dict['modelCache'] = self.model_cache.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue_namespaces
        if self.queue_namespaces:
            _dict['queueNamespaces'] = self.queue_namespaces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resilience
        if self.resilience:
            _dict['resilience'] = self.resilience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_notice
        if self.status_notice:
            _dict['statusNotice'] = self.status_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support
        if self.support:
            _dict['support'] = self.support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": ClusterAddonAcceleratorReadiness.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "availableUpgrades": obj.get("availableUpgrades"),
            "configurable": obj.get("configurable"),
            "configuration": ClusterAddonConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "currentVersion": obj.get("currentVersion"),
            "deployedAt": obj.get("deployedAt"),
            "displayName": obj.get("displayName"),
            "displayStatus": obj.get("displayStatus"),
            "endpointAuthentication": obj.get("endpointAuthentication"),
            "exposure": ClusterAddonExposure.from_dict(obj["exposure"]) if obj.get("exposure") is not None else None,
            "findingsPolicy": obj.get("findingsPolicy"),
            "health": ClusterAddonHealth.from_dict(obj["health"]) if obj.get("health") is not None else None,
            "ingressTls": ClusterAddonIngressTLS.from_dict(obj["ingressTls"]) if obj.get("ingressTls") is not None else None,
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "modelCache": ClusterAddonModelCacheReadiness.from_dict(obj["modelCache"]) if obj.get("modelCache") is not None else None,
            "name": obj.get("name"),
            "phase": obj.get("phase"),
            "pricing": ClusterAddonCostPricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "queueNamespaces": ClusterAddonQueueNamespaces.from_dict(obj["queueNamespaces"]) if obj.get("queueNamespaces") is not None else None,
            "resilience": ClusterAddonResilience.from_dict(obj["resilience"]) if obj.get("resilience") is not None else None,
            "status": obj.get("status"),
            "statusNotice": Notice.from_dict(obj["statusNotice"]) if obj.get("statusNotice") is not None else None,
            "statusReason": obj.get("statusReason"),
            "support": ClusterAddonSupport.from_dict(obj["support"]) if obj.get("support") is not None else None,
            "syncing": obj.get("syncing"),
            "tls": ClusterAddonTLSReadiness.from_dict(obj["tls"]) if obj.get("tls") is not None else None,
            "type": obj.get("type"),
            "upstreamVersion": obj.get("upstreamVersion")
        })
        return _obj



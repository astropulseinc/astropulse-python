from __future__ import annotations

import inspect
import socket
import threading
import time

import pytest
import urllib3

from astropulse import (
    DEFAULT_RETRIES,
    Client,
    DeploymentFailed,
    OpenApiException,
    WaitTimeout,
)
from astropulse._client import _RESOURCES
from astropulse._generated.api.applications_api import ApplicationsApi
from astropulse._generated.api.cluster_add_ons_api import ClusterAddOnsApi
from astropulse._generated.api.clusters_api import ClustersApi
from astropulse.models import (
    Application,
    ApplicationResponse,
    ApplicationStatus,
)


def test_every_resource_in_the_document_is_reachable() -> None:
    ap = Client("test-key", base_url="http://localhost:9080")
    for attribute in _RESOURCES:
        assert hasattr(ap, attribute), f"{attribute} is missing from the client"
    assert hasattr(ap.applications, "deploy_application")
    assert hasattr(ap.clusters, "list_clusters")
    # Registering the organization's Hugging Face token is an API call like any
    # other, so it is here rather than being a per-deploy argument.
    assert hasattr(ap.integrations, "connect_huggingface")


def test_the_key_and_host_reach_the_generated_client() -> None:
    ap = Client("test-key", base_url="http://localhost:9080/")
    configuration = ap._api_client.configuration
    assert configuration.api_key["ApiKeyAuth"] == "test-key"
    assert configuration.host == "http://localhost:9080"
    assert ap._api_client.user_agent.startswith("astropulse-python/")


def test_the_key_can_come_from_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTROPULSE_API_KEY", "from-env")
    assert Client()._api_client.configuration.api_key["ApiKeyAuth"] == "from-env"

    monkeypatch.delenv("ASTROPULSE_API_KEY")
    with pytest.raises(ValueError, match="ASTROPULSE_API_KEY"):
        Client()


def test_the_host_comes_from_the_cli_variable(monkeypatch: pytest.MonkeyPatch) -> None:
    """ASTROPULSE_API_ENDPOINT is the variable astroctl reads: one setting points both."""
    monkeypatch.setenv("ASTROPULSE_API_ENDPOINT", "http://localhost:9080")
    assert Client("test-key")._api_client.configuration.host == "http://localhost:9080"


def test_an_explicit_base_url_wins_over_the_variable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ASTROPULSE_API_ENDPOINT", "http://from-api-endpoint:9080")
    explicit = Client("test-key", base_url="http://explicit:9080")
    assert explicit._api_client.configuration.host == "http://explicit:9080"


def test_no_other_variable_sets_the_host(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ASTROPULSE_API_ENDPOINT", raising=False)
    monkeypatch.setenv("ASTROPULSE_BASE_URL", "http://ignored:9080")
    assert Client("test-key")._api_client.configuration.host == "https://api.astropulse.io"


def test_a_prepared_client_cannot_be_half_configured() -> None:
    """Passing api_client alongside api_key used to ignore the key in silence."""
    prepared = Client("test-key", base_url="http://localhost:9080")._api_client
    with pytest.raises(TypeError, match="api_client"):
        Client("another-key", api_client=prepared)


class _Applications:
    """Answers get_application the way the API does: an envelope around the app."""

    def __init__(self, states: tuple[tuple[str, str | None], ...]) -> None:
        self._remaining = iter(states)

    def get_application(self, app_name: str) -> ApplicationResponse:
        status, phase = next(self._remaining)
        return ApplicationResponse(
            status="success",
            data=Application(
                appName=app_name,
                status=ApplicationStatus(status),
                phase=ApplicationStatus(phase) if phase else None,
                statusReason="the image cannot be pulled" if status == "Failed" else None,
            ),
        )


def _client_with_states(monkeypatch: pytest.MonkeyPatch, *states: tuple[str, str | None]) -> Client:
    """A client whose application reports these status/phase pairs, one per poll."""
    monkeypatch.setattr(time, "sleep", lambda _: None)
    ap = Client("test-key", base_url="http://localhost:9080")
    ap.applications = _Applications(states)  # type: ignore[assignment]
    return ap


def test_wait_until_serving_returns_the_application(monkeypatch: pytest.MonkeyPatch) -> None:
    ap = _client_with_states(
        monkeypatch, ("Provisioning", "Provisioning"), ("InProgress", None), ("Running", None)
    )
    application = ap.wait_until_serving("qwen-chat", poll_interval=0.01)
    assert application.app_name == "qwen-chat"


def test_a_redeploy_is_not_finished_while_work_is_in_flight(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Redeploying an application that already serves keeps its status on
    RUNNING while the new revision rolls out, so status alone would hand back
    the old revision's endpoint on the first poll."""
    ap = _client_with_states(
        monkeypatch,
        ("Running", "InProgress"),
        ("Running", "Provisioning"),
        ("Running", "Completed"),
    )
    application = ap.wait_until_serving("qwen-chat", poll_interval=0.01)
    assert application.phase == ApplicationStatus("Completed")


def test_a_deploy_that_cannot_serve_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    ap = _client_with_states(monkeypatch, ("Provisioning", None), ("Failed", None))
    with pytest.raises(DeploymentFailed) as raised:
        ap.wait_until_serving("qwen-chat", poll_interval=0.01)
    assert raised.value.application == "qwen-chat"
    assert raised.value.status == ApplicationStatus("Failed")
    assert "the image cannot be pulled" in str(raised.value)
    # code written against the previous release still catches it
    assert isinstance(raised.value, RuntimeError)


def test_waiting_gives_up_rather_than_hanging(monkeypatch: pytest.MonkeyPatch) -> None:
    ap = _client_with_states(monkeypatch, ("InProgress", None))
    with pytest.raises(WaitTimeout, match="InProgress"):
        ap.wait_until_serving("qwen-chat", timeout=0, poll_interval=0.01)


def test_polling_faster_than_zero_is_refused() -> None:
    ap = Client("test-key", base_url="http://localhost:9080")
    with pytest.raises(ValueError, match="poll_interval"):
        ap.wait_until_serving("qwen-chat", poll_interval=0)
    ap.close()


def test_a_request_that_never_answers_fails_rather_than_hanging() -> None:
    """A socket that accepts and then says nothing. Without a timeout on the
    request itself this blocks until the kernel gives up, which is what the
    pool's own timeout setting does NOT prevent: the generated client passes a
    timeout explicitly on every call.
    """
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    port = listener.getsockname()[1]
    accepted: list[socket.socket] = []
    threading.Thread(target=lambda: accepted.append(listener.accept()[0]), daemon=True).start()

    ap = Client(
        "test-key",
        base_url=f"http://127.0.0.1:{port}",
        timeout=(1.0, 0.5),
        retries=None,
    )
    started = time.monotonic()
    # urllib3 raises its own error for a timeout; the SDK's exceptions are for
    # answers the API gave.
    with pytest.raises((OpenApiException, urllib3.exceptions.HTTPError)):
        ap.clusters.list_clusters()
    elapsed = time.monotonic() - started
    ap.close()
    for connection in accepted:
        connection.close()
    listener.close()

    assert elapsed < 5, f"the request took {elapsed:.1f}s, so the read timeout did not apply"


def test_the_client_retries_a_rate_limit_but_never_a_post() -> None:
    ap = Client("test-key", base_url="http://localhost:9080")
    retries = ap._api_client.configuration.retries
    assert retries is not None
    assert retries.respect_retry_after_header
    assert 429 in retries.status_forcelist
    # Repeating a POST can create a second thing, so that call is the caller's.
    assert "POST" not in retries.allowed_methods
    ap.close()


def test_retries_can_be_turned_off() -> None:
    ap = Client("test-key", base_url="http://localhost:9080", retries=None)
    assert ap._api_client.configuration.retries is None
    ap.close()


def test_the_generated_internals_this_client_reaches_for_are_still_there() -> None:
    """close() and the timeout both reach into generated code. If a
    regeneration moves either, this fails here rather than silently doing
    nothing at runtime."""
    ap = Client("test-key", base_url="http://localhost:9080")
    assert hasattr(ap._api_client, "rest_client")
    assert hasattr(ap._api_client.rest_client, "request")
    assert hasattr(ap._api_client.rest_client, "pool_manager")
    assert ap._api_client.configuration.retries is DEFAULT_RETRIES
    ap.close()


def _path_keys(api: type) -> set[str]:
    keys: set[str] = set()
    for name, method in inspect.getmembers(api, inspect.isfunction):
        if not name.startswith("_"):
            keys.update(inspect.signature(method).parameters)
    return keys


def test_application_methods_take_the_application_name() -> None:
    """Every application route is keyed by name, so no method asks for an id."""
    keys = _path_keys(ApplicationsApi)
    assert "app_id" not in keys
    assert "app_name" in inspect.signature(ApplicationsApi.get_application).parameters


def test_cluster_methods_take_the_cluster_name() -> None:
    """Every cluster route is keyed by name, so no method asks for an id."""
    for api in (ClustersApi, ClusterAddOnsApi):
        assert "cluster_id" not in _path_keys(api), api.__name__
    assert "cluster_name" in inspect.signature(ClustersApi.get_cluster).parameters

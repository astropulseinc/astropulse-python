"""The examples print the API's words, never a raw enum.

Each example runs against a stub client that answers with the API's JSON, and
nothing it prints may be an enum's repr (``ClusterStatus.Ready``).
"""

from __future__ import annotations

import enum
import inspect
import runpy
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest
import requests

import astropulse
from astropulse import models

EXAMPLES = Path(__file__).parent.parent / "examples"

ENUMS = [c for c in vars(models).values() if inspect.isclass(c) and issubclass(c, enum.Enum)]
ENUM_REPRS = sorted(f"{cls.__name__}.{member.name}" for cls in ENUMS for member in cls)

# What each API call answers, as the JSON the API sends.
ANSWERS: dict[str, Any] = {
    "list_clusters": models.K8sClusterListResponse.from_dict(
        {"data": [{"clusterName": "prod", "state": "Ready"}]}
    ),
    "get_application_endpoint": models.EndpointStatusResponse.from_dict(
        {
            "data": {
                "url": "https://qwen.test/v1",
                "policy": "keys",
                "phase": "Ready",
            }
        }
    ),
    "get_application": models.ApplicationResponse.from_dict(
        {"data": {"model": {"servedModelName": "qwen"}}}
    ),
    "connect_huggingface": None,
    "get_huggingface_integration": models.HuggingFaceIntegrationResponse.from_dict(
        {"data": {"connected": True, "state": "Connected"}}
    ),
    "get_application_metrics_series": models.ApplicationMetricsSeriesResponse.from_dict(
        {"data": {"inferenceSummary": {"runtime": "vllm", "runtimeName": "vLLM"}}}
    ),
    "deploy_application": SimpleNamespace(data=None),
}


class _Resource:
    def __getattr__(self, method: str) -> Any:
        return lambda *args, **kwargs: ANSWERS[method]


class _Client:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def __getattr__(self, resource: str) -> _Resource:
        return _Resource()

    def wait_until_serving(self, application: str, **kwargs: Any) -> Any:
        return models.Application.from_dict({"appName": application, "status": "Running"})


class _HTTPAnswer:
    status_code = 200

    def raise_for_status(self) -> None:
        pass

    def json(self) -> dict[str, Any]:
        return {"data": [{"id": "qwen"}], "choices": [{"message": {"content": "hi"}}]}


# Each example, its arguments, a word from the API it must print, and whether it exits.
CASES = [
    ("list_clusters.py", [], "Ready", False),
    ("call_a_model.py", ["qwen-chat"], "Ready", True),
    ("connect_huggingface.py", ["hf_test"], "Connected", False),
    ("read_model_metrics.py", ["qwen-chat"], "vLLM", True),
    ("deploy_a_model.py", [], "serving", False),
]


def test_every_example_is_covered() -> None:
    assert sorted(c[0] for c in CASES) == sorted(p.name for p in EXAMPLES.glob("*.py"))


@pytest.mark.parametrize(("name", "argv", "expected", "exits"), CASES, ids=[c[0] for c in CASES])
def test_example_prints_the_api_words(
    name: str,
    argv: list[str],
    expected: str,
    exits: bool,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(astropulse, "Client", _Client)
    monkeypatch.setattr(requests, "get", lambda *a, **k: _HTTPAnswer())
    monkeypatch.setattr(requests, "post", lambda *a, **k: _HTTPAnswer())
    monkeypatch.setenv("MODEL_KEY", "test-key")
    monkeypatch.setattr(sys, "argv", [name, *argv])
    # Python 3.12 formats an enum in an f-string as its repr; do so on every version.
    for cls in ENUMS:
        monkeypatch.setattr(cls, "__format__", lambda self, spec: format(str(self), spec))

    if exits:
        with pytest.raises(SystemExit) as exited:
            runpy.run_path(str(EXAMPLES / name), run_name="__main__")
        assert exited.value.code in (0, None)  # an example that fails after printing must not pass
    else:
        runpy.run_path(str(EXAMPLES / name), run_name="__main__")

    printed = capsys.readouterr().out
    assert expected in printed
    assert [r for r in ENUM_REPRS if r in printed] == []

"""What a model deploy puts on the wire.

The types are generated, so the risk is not that they exist but that the body
they build is the one the platform documents: the manifest envelope, the model
source, and camelCase field names throughout.
"""

from __future__ import annotations

from astropulse.models import (
    ApplicationManifest,
    ApplicationRequest,
    ApplicationSource,
    ExternalAccess,
    Model,
    ModelAccelerator,
    ModelGPU,
    ModelResources,
    ModelScaling,
)


def _deploy_body() -> ApplicationManifest:
    return ApplicationManifest(
        api_version="platform.astropulse.io/v1",
        kind="Application",
        spec=ApplicationRequest(
            name="qwen-chat",
            profile_name="prod-inference",
            source=ApplicationSource(
                type="Model",
                model=Model(
                    uri="hf://Qwen/Qwen3-8B",
                    resources=ModelResources(
                        accelerator=ModelAccelerator(
                            gpu=ModelGPU(model="l4", count_per_replica=1),
                        ),
                    ),
                    scaling=ModelScaling(min_replicas=1, max_replicas=4),
                ),
            ),
            external_access=ExternalAccess(domain="acme.ai"),
        ),
    )


def test_the_body_is_the_manifest_the_platform_documents() -> None:
    assert _deploy_body().to_dict() == {
        "apiVersion": "platform.astropulse.io/v1",
        "kind": "Application",
        "spec": {
            "name": "qwen-chat",
            "profileName": "prod-inference",
            "source": {
                "type": "Model",
                "model": {
                    "uri": "hf://Qwen/Qwen3-8B",
                    "resources": {"accelerator": {"gpu": {"model": "l4", "countPerReplica": 1}}},
                    "scaling": {"minReplicas": 1, "maxReplicas": 4},
                },
            },
            "externalAccess": {"domain": "acme.ai"},
        },
    }


def test_nothing_unset_is_sent() -> None:
    """The platform fills in what a caller leaves out, so the SDK must not
    send a wall of nulls that would overwrite those defaults."""
    body = _deploy_body().to_dict()
    assert "identity" not in body["spec"]["source"]["model"]
    assert "runtime" not in body["spec"]["source"]["model"]
    assert "accessPolicyRef" not in body["spec"]["externalAccess"]

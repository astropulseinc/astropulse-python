"""Deploy a model, wait for it, then call it.

Run it with::

    export ASTROPULSE_API_KEY=...
    python examples/deploy_a_model.py
"""

from astropulse import Client
from astropulse.models import (
    ApplicationManifest,
    ApplicationRequest,
    ApplicationSource,
    EndpointAccessPolicyReference,
    ExternalAccess,
    Model,
    ModelAccelerator,
    ModelGPU,
    ModelResources,
    ModelScaling,
)

ap = Client()

deployed = ap.applications.deploy_application(
    ApplicationManifest(
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
            external_access=ExternalAccess(
                domain="acme.ai",
                # Exposing a model publishes an inference endpoint, so the
                # platform makes you say who may call it.
                access_policy_ref=EndpointAccessPolicyReference(name="partner-keys"),
            ),
        ),
    )
)
# A real deploy answers 201 with the application it created; ?dryRun=true
# answers 200 with a validation result instead, which is why the generated
# return type covers both.
created = deployed.data
print(f"deploying {getattr(created, 'name', 'qwen-chat')}")

application = ap.wait_until_serving("qwen-chat")
# model is present for a model source, and None for every other kind.
endpoint = application.model.external_endpoint if application.model else None
print(f"serving at {endpoint}")

# Calling it is not this SDK's job: the endpoint speaks the OpenAI API.
#
#     from openai import OpenAI
#
#     chat = OpenAI(base_url=endpoint, api_key="<access-policy key>")
#     served = chat.models.list().data[0].id
#     chat.chat.completions.create(
#         model=served,
#         messages=[{"role": "user", "content": "hello"}],
#     )

<p align="center">
  <a href="https://astropulse.io">
    <img src="https://astropulse.io/images/logo.svg" alt="AstroPulse" width="96">
  </a>
</p>

<h1 align="center">AstroPulse Python SDK</h1>

<p align="center">
  Deploy models onto your own Kubernetes clusters from Python, and get an endpoint back.
</p>

<p align="center">
  <a href="https://github.com/astropulseinc/astropulse-python/actions/workflows/ci.yml"><img src="https://github.com/astropulseinc/astropulse-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue" alt="Python 3.10 to 3.13">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="License: Apache-2.0"></a>
</p>

<p align="center">
  <a href="https://astropulse.io/docs/latest/platform/python-sdk"><b>Documentation</b></a> ·
  <a href="https://astropulse.io/docs/api/">API reference</a> ·
  <a href="examples/">Examples</a> ·
  <a href="https://astropulse.io">astropulse.io</a>
</p>

---

The official client for the [AstroPulse Platform](https://astropulse.io). Every method and type
is generated from the platform's OpenAPI document, so the SDK always matches the API. The client,
its retry and timeout policy, and `wait_until_serving` are hand-written.

## Install

```bash
pip install "git+https://github.com/astropulseinc/astropulse-python"
```

To run the [examples](examples/), install the `examples` extra too:

```bash
pip install "astropulse[examples] @ git+https://github.com/astropulseinc/astropulse-python"
```

Requires Python 3.10 or later. Create an API key in the [console](https://astropulse.io) under
**Settings → API Keys**, and export it:

```bash
export ASTROPULSE_API_KEY=...
```

## Quickstart

```python
from astropulse import Client
from astropulse.models import (
    ApplicationManifest, ApplicationRequest, EndpointAccessPolicyReference, ExternalAccess,
    Model, ModelAccelerator, ModelGPU, ModelResources, ModelScaling, ApplicationSource,
)

ap = Client()  # reads ASTROPULSE_API_KEY

ap.applications.deploy_application(
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
                        accelerator=ModelAccelerator(gpu=ModelGPU(model="l4", count_per_replica=1)),
                    ),
                    scaling=ModelScaling(min_replicas=1, max_replicas=4),
                ),
            ),
            external_access=ExternalAccess(
                domain="acme.ai",
                access_policy_ref=EndpointAccessPolicyReference(name="partner-keys"),
            ),
        ),
    )
)

application = ap.wait_until_serving("qwen-chat")
print(application.model.external_endpoint)
```

- `profile_name` names an [application profile](https://astropulse.io/docs/latest/platform/application-pipeline/application-profile):
  the cluster and resource tier the model runs on.
- `access_policy_ref` names an [access policy](https://astropulse.io/docs/latest/platform/access-policies/overview):
  who may call the endpoint. Leave out `external_access` to keep the model inside the cluster.
- `wait_until_serving` blocks until the new revision is serving. It raises `DeploymentFailed` or
  `WaitTimeout` if it can't get there.

## Call the model

The endpoint speaks the OpenAI API, so use the `openai` package:

```python
from openai import OpenAI

chat = OpenAI(base_url=application.model.external_endpoint, api_key=endpoint_key)
chat.chat.completions.create(
    model=application.model.served_model_name,
    messages=[{"role": "user", "content": "hello"}],
)
```

Send `served_model_name` as the model. The runtime answers to that id only, not to the
application name or the Hugging Face repository.

## Errors

```python
from astropulse import NotFoundException, OpenApiException

try:
    ap.applications.get_application("qwen-chat")
except NotFoundException as error:
    print(error.data.code)      # NOT_FOUND: branch on this, not on the message
    print(error.data.trace_id)  # include this in a support request
except OpenApiException as error:
    print(error)                # anything else the client raises
```

## Configuration

```python
ap = Client(timeout=(5, 30), retries=None)
```

| Option     | Default                     | Notes                                                                     |
| ---------- | --------------------------- | ------------------------------------------------------------------------- |
| `api_key`  | `$ASTROPULSE_API_KEY`       |                                                                           |
| `base_url` | `https://api.astropulse.io` | Or `$ASTROPULSE_API_ENDPOINT`.                                            |
| `timeout`  | `(10, 60)`                  | Connect and read seconds; `None` for no deadline.                         |
| `retries`  | `3`                         | Retries `429` and `5xx` and honours `Retry-After`. `POST` is never retried. |

A `Client` is thread-safe and meant to be reused for the life of the process.

The host defaults to `https://api.astropulse.io`. To point at another one — a local stack, say —
pass `base_url=...`, or set `ASTROPULSE_API_ENDPOINT`, the same variable
[astroctl](https://astropulse.io/docs/cli), the platform's CLI, reads. `base_url` wins when both are set.

## Service accounts

For CI and long-running integrations, use an organization-owned service-account key: set
`ASTROPULSE_API_KEY` to it and use `Client()` as usual. The key belongs to the organization, so it
keeps working when the person who created it leaves.

An organization admin or owner manages accounts with `ap.service_accounts`: create the account,
issue a key, and store the returned secret in your secret manager (it is returned only once).
Viewer accounts can read, editor accounts can deploy applications, and admin accounts can also
administer clusters; no service account can manage credentials or ownership. Rotate by issuing a
replacement key, switching your integration over, then revoking the old key. Archiving an account
disables all its keys. See the
[service-account guide](https://astropulse.io/docs/platform/organization/service-accounts) and the
[API reference](docs/ServiceAccountsApi.md).

## Beyond models

Clusters, application profiles, domains, add-ons, cloud accounts, access policies, API keys,
service accounts and audit are all on the same client:

```python
for cluster in ap.clusters.list_clusters().data or []:
    print(cluster.cluster_name, cluster.state.value if cluster.state else "")
```

The [examples](examples/) run end to end. Every resource and type has a reference page under
[docs/](docs/). If you type-check your code, enable pydantic's mypy plugin
(`plugins = ["pydantic.mypy"]`).

## Support

- Documentation: [astropulse.io/docs](https://astropulse.io/docs)
- Bugs and feature requests: [GitHub issues](https://github.com/astropulseinc/astropulse-python/issues)
- Security: see [SECURITY.md](SECURITY.md)

## Contributing

This SDK is generated from the platform's API document. See [CONTRIBUTING.md](CONTRIBUTING.md)
for how to regenerate it and what is safe to edit by hand.

## License

[Apache-2.0](LICENSE) © AstroPulse

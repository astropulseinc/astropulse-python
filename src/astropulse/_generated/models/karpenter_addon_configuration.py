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
from typing_extensions import Annotated
from astropulse._generated.models.aws_addon_config import AWSAddonConfig
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.karpenter_capacity_reservations import KarpenterCapacityReservations
from astropulse._generated.models.karpenter_disruption import KarpenterDisruption
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class KarpenterAddonConfiguration(BaseModel):
    """
    KarpenterAddonConfiguration
    """ # noqa: E501
    allowed_accelerators: Optional[List[StrictStr]] = Field(default=None, description="The GPU models GPU nodes may have, as the machine catalog names them, such as l4 or a10g. Left out, every model is allowed.", alias="allowedAccelerators")
    ami_alias: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The machine image new nodes start from, as family@version such as al2023@v20260818; changing it replaces existing nodes. Left out, AstroPulse's default applies; with the GPU node pool on, pin a version rather than @latest.", alias="amiAlias")
    aws: Optional[AWSAddonConfig] = Field(default=None, description="Node Autoscaling's AWS settings, on EKS only.")
    cpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="How the default pool's nodes may be bought; Spot costs less but needs the interruption queue. Left out, it keeps the last value set, or buys both, Spot first, where the cluster has the queue and `OnDemand` elsewhere.", alias="cpuCapacityTypes")
    cpu_limit: Optional[Annotated[int, Field(le=100000, strict=True, ge=1)]] = Field(default=100, description="The most CPU cores the default node pool may run in total, from 1 to 100000; pods wait once it is reached.", alias="cpuLimit")
    disruption: Optional[KarpenterDisruption] = Field(default=None, description="When nodes in the default pool are removed or replaced to save cost.")
    enable_gpu_node_pool: Optional[StrictBool] = Field(default=None, description="Lets Node Autoscaling start GPU nodes. They take only pods that tolerate nvidia.com/gpu:NoSchedule, and AstroPulse runs the NVIDIA device plugin on them, so remove any you installed yourself.", alias="enableGpuNodePool")
    gpu_capacity_reservations: Optional[KarpenterCapacityReservations] = Field(default=None, description="EC2 capacity reservations, Capacity Blocks included, that GPU nodes use before Spot or On-Demand. On a cluster AstroPulse created, each is checked before install to exist, be active, be a g or p instance type of generation 4 or later, and be in one of the cluster's zones.", alias="gpuCapacityReservations")
    gpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="How GPU nodes may be bought; Spot costs less, but a node can be reclaimed at short notice and needs `interruptionQueue` on a registered cluster. Left out, a new pool buys `OnDemand` and an existing one keeps its current value.", alias="gpuCapacityTypes")
    gpu_disruption: Optional[KarpenterDisruption] = Field(default=None, description="When GPU nodes are removed or replaced to save cost; `gpuLimit` still caps GPU spend.", alias="gpuDisruption")
    gpu_instance_families: Optional[List[StrictStr]] = Field(default=None, description="The instance families GPU nodes may use, such as g6 or g5, at most 32.", alias="gpuInstanceFamilies")
    gpu_instance_sizes: Optional[List[StrictStr]] = Field(default=None, description="The instance sizes GPU nodes may use, such as xlarge or 2xlarge, at most 32.", alias="gpuInstanceSizes")
    gpu_limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=10, description="The most GPUs the GPU node pool may run in total, from 1 to 1000.", alias="gpuLimit")
    gpu_max_memory_gi_b_per_node: Optional[Annotated[int, Field(le=32768, strict=True, ge=1)]] = Field(default=None, description="The most memory one GPU node may have, in GiB, from 1 to 32768.", alias="gpuMaxMemoryGiBPerNode")
    gpu_max_vcpu_per_node: Optional[Annotated[int, Field(le=1024, strict=True, ge=1)]] = Field(default=None, description="The most CPU cores one GPU node may have, from 1 to 1024. Left out, the smallest size that fits each workload and your quota is chosen.", alias="gpuMaxVcpuPerNode")
    gpu_node_drain_timeout: Optional[StrictStr] = Field(default=None, description="How long a GPU node being removed waits for its pods to finish, up to 24h, or `None` for no limit. Left out, a new pool uses 1h and an existing one keeps its current value.", alias="gpuNodeDrainTimeout", json_schema_extra={"examples": ["1h"]})
    gpu_node_expiry: Optional[StrictStr] = Field(default=None, description="How long a GPU node runs before it is replaced, even while busy: `Never`, or days or hours such as 30d or 12h. Left out, a new pool uses `Never` and an existing one keeps its current value.", alias="gpuNodeExpiry", json_schema_extra={"examples": ["Never"]})
    interruption_queue: Optional[StrictBool] = Field(default=None, description="Turn on when your registered cluster has Node Autoscaling's interruption queue, from the prerequisites stack AstroPulse generates: Spot nodes are then drained before they are reclaimed, and Spot may be bought. Clusters AstroPulse created always have it.", alias="interruptionQueue")
    memory_limit: Optional[StrictStr] = Field(default='400Gi', description="The most memory the default node pool may run in total, such as 400Gi; the pool stops adding nodes at this or `cpuLimit`, whichever comes first.", alias="memoryLimit", json_schema_extra={"examples": ["400Gi"]})
    service_account_name: Optional[StrictStr] = Field(default=None, description="The Kubernetes service account Node Autoscaling runs as. Left out, AstroPulse's default applies.", alias="serviceAccountName")
    __properties: ClassVar[List[str]] = ["allowedAccelerators", "amiAlias", "aws", "cpuCapacityTypes", "cpuLimit", "disruption", "enableGpuNodePool", "gpuCapacityReservations", "gpuCapacityTypes", "gpuDisruption", "gpuInstanceFamilies", "gpuInstanceSizes", "gpuLimit", "gpuMaxMemoryGiBPerNode", "gpuMaxVcpuPerNode", "gpuNodeDrainTimeout", "gpuNodeExpiry", "interruptionQueue", "memoryLimit", "serviceAccountName"]

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
        """Create an instance of KarpenterAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws
        if self.aws:
            _dict['aws'] = self.aws.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disruption
        if self.disruption:
            _dict['disruption'] = self.disruption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpu_capacity_reservations
        if self.gpu_capacity_reservations:
            _dict['gpuCapacityReservations'] = self.gpu_capacity_reservations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpu_disruption
        if self.gpu_disruption:
            _dict['gpuDisruption'] = self.gpu_disruption.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KarpenterAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedAccelerators": obj.get("allowedAccelerators"),
            "amiAlias": obj.get("amiAlias"),
            "aws": AWSAddonConfig.from_dict(obj["aws"]) if obj.get("aws") is not None else None,
            "cpuCapacityTypes": obj.get("cpuCapacityTypes"),
            "cpuLimit": obj.get("cpuLimit") if obj.get("cpuLimit") is not None else 100,
            "disruption": KarpenterDisruption.from_dict(obj["disruption"]) if obj.get("disruption") is not None else None,
            "enableGpuNodePool": obj.get("enableGpuNodePool"),
            "gpuCapacityReservations": KarpenterCapacityReservations.from_dict(obj["gpuCapacityReservations"]) if obj.get("gpuCapacityReservations") is not None else None,
            "gpuCapacityTypes": obj.get("gpuCapacityTypes"),
            "gpuDisruption": KarpenterDisruption.from_dict(obj["gpuDisruption"]) if obj.get("gpuDisruption") is not None else None,
            "gpuInstanceFamilies": obj.get("gpuInstanceFamilies"),
            "gpuInstanceSizes": obj.get("gpuInstanceSizes"),
            "gpuLimit": obj.get("gpuLimit") if obj.get("gpuLimit") is not None else 10,
            "gpuMaxMemoryGiBPerNode": obj.get("gpuMaxMemoryGiBPerNode"),
            "gpuMaxVcpuPerNode": obj.get("gpuMaxVcpuPerNode"),
            "gpuNodeDrainTimeout": obj.get("gpuNodeDrainTimeout"),
            "gpuNodeExpiry": obj.get("gpuNodeExpiry"),
            "interruptionQueue": obj.get("interruptionQueue"),
            "memoryLimit": obj.get("memoryLimit") if obj.get("memoryLimit") is not None else '400Gi',
            "serviceAccountName": obj.get("serviceAccountName")
        })
        return _obj



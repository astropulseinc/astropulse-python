# coding: utf-8

"""
    AstroPulse Platform API

    The programmable production foundation for applications, AI workloads, and infrastructure products.  AstroPulse provides a unified control plane for composing cloud infrastructure, deploying workloads, and operating their production lifecycle. Provision and manage Kubernetes clusters, deploy applications and AI models, and manage networking, scaling, access, integrations, observability, cost visibility, and governance.  **Keep your product. Skip rebuilding the production layer.** AstroPulse manages the production machinery underneath your application, runtime, scheduler, inference system, or infrastructure product, while you retain ownership of the capabilities that make it different.  ## Base URL All public API endpoints are served over HTTPS at `https://api.astropulse.io` and versioned under `/api/v1`.  ## Working with AstroPulse The API follows the operational lifecycle of your infrastructure and workloads: - **Connect infrastructure:** Configure cloud accounts, discover regions, machine types, and accelerators, and provision or register Kubernetes clusters. - **Configure environments:** Manage cluster add-ons, application profiles, availability tiers, domains, and endpoint access policies. - **Deploy workloads:** Deploy applications and supported AI models, inspect their state, and discover their serving endpoints. - **Operate and recover:** Monitor deployment progress, manage supported lifecycle operations, inspect version history, plan rollbacks, and recover deployments. - **Observe and govern:** Inspect operational metrics, cost and usage data, activity, integrations, identities, permissions, and audit records.  Resources are organized by their role in the platform. Each operation defines its own parameters, request and response schemas, authentication requirements, and failure conditions.  ## Authentication AstroPulse supports API keys and short-lived bearer tokens. Each endpoint declares which authentication methods it accepts.  **API keys — recommended for automation** Send `X-Astro-API-Key: <key>`. For production automation, use an organization-owned service-account key. Service accounts are managed by organization administrators through the Service Accounts API and do not depend on an individual user's session.  Personal API keys are available under Organization settings > API Keys. API keys are scoped to one organization.  **Bearer tokens — interactive sessions** Send `Authorization: Bearer <jwt>`. These credentials are short-lived access tokens issued by the configured authentication provider.  To print an access token for a direct API request, run `astroctl auth login --print-access-token` (`-p`). A standard `astroctl auth login` stores the authenticated session without printing the token.  For unattended integrations, use API keys instead of interactive session tokens. Store all credentials securely and never expose them in repositories, client-side code, or logs.  ## SDKs and API clients The generated OpenAPI 3 specification is the public contract for AstroPulse REST API consumers and generated clients.  AstroPulse provides operation-specific Python and TypeScript SDK examples in this reference. Each generated SDK exposes resources through typed clients, with method names derived from stable API operation IDs.  **Python SDK:** Install using `pip install \"git+https://github.com/astropulseinc/astropulse-python\"`.  Common operations include `client.clusters.list_clusters()` and `client.applications.deploy_application(...)`. Consult the SDK's documentation for client initialization, authentication, and complete examples.  The same platform capabilities can be accessed through the REST API, supported SDKs, astroctl, and the AstroPulse Console. Refer to the documentation for the supported workflows of each interface.  **Application runtime endpoints:** Applications deployed through AstroPulse expose runtime endpoints separate from the platform control-plane API. Model deployments supporting the OpenAI API protocol can be called with an OpenAI-compatible client configured for the deployed endpoint and its access requirements.  ## Lifecycle and asynchronous operations Infrastructure provisioning, deployment, and certain lifecycle changes can execute asynchronously. An accepted request does not necessarily mean the underlying operation has completed.  Use the operation's response, resource status, and available progress streams to determine completion and inspect failures.  Supported application operations include version history, rollback, resume, and GitOps reconciliation. Rollback operations can provide dry-run plans so callers can inspect an eligible change before applying it.  Consult each operation for its specific state transitions, mutation semantics, retry behavior, and concurrency restrictions.  ## Observability and cost Supported resources expose deployment state, application and cluster metrics, cost and usage series, and operational diagnostics.  Metrics and cost data represent collected observations. Missing samples, incomplete coverage, and unavailable reporting intervals must not be interpreted as zero resource consumption or zero spend.  Use the coverage information, time windows, and aggregation intervals documented by each operation when processing telemetry and cost responses.  ## Real-time streaming Supported application endpoints provide real-time status, event, and log streams over WebSocket connections.  Streaming requests have different connection and authentication semantics from ordinary JSON requests. Supported browser workflows can obtain a short-lived, single-use stream ticket before establishing a WebSocket connection.  Stream tickets are valid for at most 30 seconds. Follow the individual endpoint's documented handshake, authentication, and error-handling requirements.  ## Response format Successful JSON API responses use the documented resource schema, commonly wrapped in an envelope with the result under `data` and optional `id`, `status`, and `message` fields.  Consumers must follow each endpoint's declared response type. Streaming connections and other specialized responses may have different transport semantics.  ## Errors and diagnostics API failures use a consistent JSON error structure containing: - `message`: Human-readable explanation. - `code`: Stable, machine-readable error identifier. - `status`: HTTP response status. - `traceId`: Diagnostic request trace identifier. - `details`: Optional structured error details.  **Branch on HTTP status and `code`, never on the wording of `message`.**  The `X-Trace-ID` response header exposes the request's diagnostic trace identifier. Include it when reporting failures. It is not a distributed tracing propagation header.  Common HTTP errors include: - `400 Bad Request`: Invalid input or request. - `401 Unauthorized`: Missing, invalid, expired, or revoked credentials. - `402 Payment Required`: Requested capability is unavailable under the current plan. - `403 Forbidden`: Insufficient permissions. - `404 Not Found`: Resource or route not found. - `405 Method Not Allowed`: Unsupported HTTP method for a route. - `409 Conflict`: Resource state or concurrent operation conflict. - `429 Too Many Requests`: Rate limit exceeded. - `500 Internal Server Error`: Unexpected server failure. - `503 Service Unavailable`: A required service is temporarily unavailable.  The applicable status codes and response schemas are documented for each operation.  ## Versioning and compatibility Public API versions are identified by the URL path, beginning with `/api/v1`. The generated specification's `info.version` identifies the AstroPulse build from which the document was generated.  Within an API version, backward-compatible evolution can introduce new endpoints, optional request fields, response properties, and values in extensible enumerations.  Clients should tolerate unknown response properties and supported enum extensions. Consumers must not depend on undocumented list ordering or human-readable error messages.  Breaking changes, including removing or renaming fields, changing documented field types, or making previously optional request fields mandatory, require compatibility review and an appropriate API version transition.  The generated OpenAPI specification is the authoritative contract for client generation and compatibility validation.  ## Rate limiting and retries AstroPulse applies layered request rate limits: - Global service-wide limits. - Per-IP limits. - Additional per-API-key limits. - Per-authenticated-principal limits where enabled.  Exceeding an applicable limit returns `429 Too Many Requests`. Respect the `Retry-After` response header and implement bounded exponential backoff with jitter.  Temporary service failures may return `503 Service Unavailable` with retry guidance. Retry state-changing operations only when their documented semantics make repetition safe.  Global and per-IP limits remain applicable regardless of the credential used. Rotating credentials does not bypass those limits.  ## Identity, governance, and audit AstroPulse organizes platform resources within organizations. Authentication, authorization, and applicable plan restrictions govern access to resource operations.  Mutating API requests and designated sensitive reads are recorded for auditability. Audit records capture available actor, organization, resource, action, outcome, and request context without storing request bodies or secrets.  Organization-owned service accounts provide dedicated automation identities, while API keys and user sessions retain their associated authentication and authorization boundaries.  ## Developer documentation This API reference defines the public platform contract. The [AstroPulse Documentation](https://astropulse.io/docs) provides guided workflows, platform concepts, SDK integration, CLI usage, and end-to-end examples.  API schemas and operation definitions are the source of truth for clients, developer tools, and authorized automation.

    The version of the OpenAPI document: v0.0.178
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
    allowed_accelerators: Optional[List[StrictStr]] = Field(default=None, description="Limits the GPU node pool to these GPU models, as the machine catalog names them (l4, a10g); omit it to allow every model. Leaving out the largest GPUs keeps the most expensive instances out of reach.", alias="allowedAccelerators")
    ami_alias: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The machine image Node Autoscaling launches nodes from, as family@version (for example al2023@v20260818); omit it to take the AstroPulse default. Changing it replaces existing nodes, and with the GPU node pool enabled it must be pinned rather than a floating @latest, so GPU driver updates happen when you choose.", alias="amiAlias")
    aws: Optional[AWSAddonConfig] = Field(default=None, description="The AWS-specific settings Node Autoscaling needs. EKS only.")
    cpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="The purchase options the default node pool may buy: OnDemand, Spot or both; Spot needs the interruption queue (see interruptionQueue). Until it is set, the pool buys both, Spot first, where the cluster has the queue, and OnDemand elsewhere; an apply that leaves it out keeps the value it was last set to.", alias="cpuCapacityTypes")
    cpu_limit: Optional[Annotated[int, Field(le=100000, strict=True, ge=1)]] = Field(default=100, description="The most vCPU the default node pool runs at once across its nodes (optional, 1-100000, default 100). It caps what the pool spends on CPU nodes; pods wait once it is reached.", alias="cpuLimit")
    disruption: Optional[KarpenterDisruption] = Field(default=None, description="When nodes of the default pool are removed or replaced to save cost (optional; defaults: WhenEmptyOrUnderutilized, 5m, 10%).")
    enable_gpu_node_pool: Optional[StrictBool] = Field(default=None, description="Lets Node Autoscaling provision GPU instances (optional, default false). GPU nodes are tainted nvidia.com/gpu:NoSchedule, so pods need a matching toleration; AstroPulse manages the NVIDIA device plugin on the pool's nodes, so remove or exclude any cluster-wide plugin you installed yourself.", alias="enableGpuNodePool")
    gpu_capacity_reservations: Optional[KarpenterCapacityReservations] = Field(default=None, description="The EC2 capacity reservations, Capacity Blocks included, that the GPU node pool fills before spot or on-demand (optional; requires enableGpuNodePool). Before installing, AstroPulse checks each exists in the cluster's account and region, is active, is a g or p instance type (generation 4 or later) and is in one of the cluster's zones. Registered clusters are not checked.", alias="gpuCapacityReservations")
    gpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="The purchase options the GPU node pool may buy: OnDemand, Spot or both; a new pool buys OnDemand, and an existing one keeps what it buys unless this is set. Spot costs less, but a node can be reclaimed at short notice, restarting its pods, and needs interruptionQueue on a registered cluster.", alias="gpuCapacityTypes")
    gpu_disruption: Optional[KarpenterDisruption] = Field(default=None, description="When GPU nodes are removed or replaced to save cost (optional; defaults: WhenEmpty, 10m, 10%; requires enableGpuNodePool). gpuLimit stays the hard cap on GPU spend whatever these say.", alias="gpuDisruption")
    gpu_instance_families: Optional[List[StrictStr]] = Field(default=None, description="Limits the GPU node pool to these instance families, such as g6 or g5 (optional, at most 32).", alias="gpuInstanceFamilies")
    gpu_instance_sizes: Optional[List[StrictStr]] = Field(default=None, description="Limits the GPU node pool to these instance sizes, such as xlarge or 2xlarge (optional, at most 32).", alias="gpuInstanceSizes")
    gpu_limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=10, description="The maximum number of GPUs the GPU node pool may provision, counted across the pool (optional, 1-1000, default 10). Ignored unless the GPU node pool is enabled.", alias="gpuLimit")
    gpu_max_memory_gi_b_per_node: Optional[Annotated[int, Field(le=32768, strict=True, ge=1)]] = Field(default=None, description="The most memory one GPU node may have, in GiB (optional, 1-32768).", alias="gpuMaxMemoryGiBPerNode")
    gpu_max_vcpu_per_node: Optional[Annotated[int, Field(le=1024, strict=True, ge=1)]] = Field(default=None, description="The most vCPU one GPU node may have (optional, 1-1024); unset, the GPU pool picks the smallest sizes that fit each model and the account's quota.", alias="gpuMaxVcpuPerNode")
    gpu_node_drain_timeout: Optional[StrictStr] = Field(default=None, description="The most time a GPU node being removed waits for its pods before they are deleted: hours and minutes up to 24h, such as 1h, or None for no limit. A new pool uses 1h; an existing one keeps its own unless this is set.", alias="gpuNodeDrainTimeout", json_schema_extra={"examples": ["1h"]})
    gpu_node_expiry: Optional[StrictStr] = Field(default=None, description="How long a GPU node runs before it is replaced, even while busy: Never, or whole days or hours such as 30d or 12h. A new pool uses Never; an existing one keeps its own unless this is set.", alias="gpuNodeExpiry", json_schema_extra={"examples": ["Never"]})
    interruption_queue: Optional[StrictBool] = Field(default=None, description="Set to true when a registered cluster has Node Autoscaling's interruption queue, created by the Node Autoscaling prerequisites stack AstroPulse generates for your AWS account: nodes are drained before Spot reclaims them, the default pool may buy Spot, and gpuCapacityTypes may list spot. Clusters AstroPulse creates always have the queue.", alias="interruptionQueue")
    memory_limit: Optional[StrictStr] = Field(default='400Gi', description="The most memory the default node pool runs at once across its nodes, as a quantity such as 400Gi (optional, default 400Gi). The pool stops adding nodes at whichever of cpuLimit and memoryLimit it reaches first.", alias="memoryLimit", json_schema_extra={"examples": ["400Gi"]})
    service_account_name: Optional[StrictStr] = Field(default=None, description="The Kubernetes service account Node Autoscaling runs as. Empty takes the AstroPulse default.", alias="serviceAccountName")
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



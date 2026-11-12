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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.accelerator_attachment import AcceleratorAttachment
from astropulse._generated.models.capacity_block_status import CapacityBlockStatus
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.node_group_removal import NodeGroupRemoval
from astropulse._generated.models.node_group_state import NodeGroupState
from astropulse._generated.models.tainted import Tainted
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NodeGroup(BaseModel):
    """
    NodeGroup
    """ # noqa: E501
    accelerator: Optional[AcceleratorAttachment] = Field(default=None, description="Requests accelerator hardware for this node group (optional). Exactly one member of the union must be set; gpu is the supported member. Not available on selfHosted clusters.")
    availability_zones: Optional[List[StrictStr]] = Field(default=None, description="The list of availability zones for this node group (optional). Default behavior: if omitted, the server auto-selects the first 3 sorted zones in the region (or fewer if the region has < 3 zones). For aks, Azure manages zone placement automatically. Constraints:   - Maximum 3 zones per node group.   - Zones must be valid for the cluster's region (validated server-side).   - Zones must be a subset of the cluster/control plane zones (eks, gke).   - Zones are immutable after creation — changing zones requires deleting and recreating the node group. Example for eks: [\"us-west-2a\", \"us-west-2b\"] Example for gke: [\"us-central1-a\", \"us-central1-b\", \"us-central1-c\"]", alias="availabilityZones")
    capacity_block: Optional[CapacityBlockStatus] = Field(default=None, description="The Capacity Block a CapacityBlock node group runs on (read-only; ignored on input).", alias="capacityBlock")
    disk_size_gb: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The root disk of every node in this group, in whole gigabytes (optional). It holds the operating system, the images the node pulls and anything written to the node's local disk, including the model weight cache. Accepted range: 20 to 16384 on eks and selfHosted, 20 to 65536 on gke, 30 to 2048 on aks; omitted, the provider's default applies (100 on eks and gke, 20 on selfHosted, the machine type's own size on aks). Changing it replaces the group's nodes, and is refused on gke.", alias="diskSizeGB")
    instance_type: InstanceType = Field(description="How the node group's nodes are bought; OnDemand when omitted. It cannot change on an existing node group.", alias="instanceType")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Kubernetes labels applied to nodes in this group (optional), such as {\"tier\": \"frontend\", \"team.example.com/owner\": \"ml\"}. Keys are Kubernetes label keys, not under kubernetes.io or k8s.io (at most 63 characters in all on eks); values are 1-63 letters, digits, '-', '_' and '.', starting and ending with a letter or digit.")
    machine_types: Optional[List[StrictStr]] = Field(default=None, description="The list of machine types for nodes. Provider-specific formats: eks (e.g. \"t3.medium\"), gke (e.g. \"n1-standard-1\"), aks (e.g. \"Standard_D2s_v3\"). Required unless Accelerator is set. Supplying only machineTypes keeps explicit machine selection; supplying only accelerator lets AstroPulse resolve compatible machine types; supplying both requires every listed machine to satisfy the accelerator; supplying neither is invalid. Multiple entries are honoured on eks, where the node group may draw from every listed type. gke, aks and selfHosted node groups run a single machine type — supply exactly one there; a longer list is rejected.", alias="machineTypes")
    max_node: StrictInt = Field(description="The maximum number of nodes in the group (required, minimum: 1). Must be >= MinNode. For control plane node groups, must be an odd number.  On gke, aks and selfHosted the provider's autoscaler scales the group between minNode and maxNode. On eks maxNode has no effect: the group runs at minNode, and elastic capacity, GPUs included, comes from the karpenter add-on.", alias="maxNode")
    min_node: Optional[StrictInt] = Field(default=None, description="The minimum number of nodes in the group. Must be <= MaxNode.  Zero means the group holds no nodes while idle and is scaled up when a pod needs one, which is only honoured where an autoscaler watches the group: gke, aks (except its first node group, which becomes the system pool), and selfHosted. It is rejected on eks, where managed node groups are fixed capacity and Karpenter provides elastic capacity instead.  To undo it, set minNode back to 1 or more and apply again — the same update path, no separate operation.", alias="minNode")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The node group name (required, 1-50 characters, valid DNS name). Format: lowercase alphanumeric and hyphens, must start with a letter. Example: \"ng-workers-1\"")
    removal: Optional[NodeGroupRemoval] = Field(default=None, description="Says whether an update can remove this node group now (read-only; ignored on input). Present on worker node groups.")
    state: Optional[NodeGroupState] = Field(default=None, description="Adding while a running update creates the node group, and absent otherwise (read-only; ignored on input).")
    taints: Optional[List[Tainted]] = Field(default=None, description="Kubernetes taints applied to nodes in this group (optional)")
    __properties: ClassVar[List[str]] = ["accelerator", "availabilityZones", "capacityBlock", "diskSizeGB", "instanceType", "labels", "machineTypes", "maxNode", "minNode", "name", "removal", "state", "taints"]

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
        """Create an instance of NodeGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of capacity_block
        if self.capacity_block:
            _dict['capacityBlock'] = self.capacity_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of removal
        if self.removal:
            _dict['removal'] = self.removal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in taints (list)
        _items = []
        if self.taints:
            for _item_taints in self.taints:
                if _item_taints:
                    _items.append(_item_taints.to_dict())
            _dict['taints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": AcceleratorAttachment.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "availabilityZones": obj.get("availabilityZones"),
            "capacityBlock": CapacityBlockStatus.from_dict(obj["capacityBlock"]) if obj.get("capacityBlock") is not None else None,
            "diskSizeGB": obj.get("diskSizeGB"),
            "instanceType": obj.get("instanceType"),
            "labels": obj.get("labels"),
            "machineTypes": obj.get("machineTypes"),
            "maxNode": obj.get("maxNode"),
            "minNode": obj.get("minNode"),
            "name": obj.get("name"),
            "removal": NodeGroupRemoval.from_dict(obj["removal"]) if obj.get("removal") is not None else None,
            "state": obj.get("state"),
            "taints": [Tainted.from_dict(_item) for _item in obj["taints"]] if obj.get("taints") is not None else None
        })
        return _obj



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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.agent_capability_status import AgentCapabilityStatus
from astropulse._generated.models.agent_certificate_status import AgentCertificateStatus
from astropulse._generated.models.attempt_status_info import AttemptStatusInfo
from astropulse._generated.models.cluster_addon_summary import ClusterAddonSummary
from astropulse._generated.models.cluster_application import ClusterApplication
from astropulse._generated.models.cluster_cancellation import ClusterCancellation
from astropulse._generated.models.cluster_cloud_identity import ClusterCloudIdentity
from astropulse._generated.models.cluster_compute_mode import ClusterComputeMode
from astropulse._generated.models.cluster_connectivity import ClusterConnectivity
from astropulse._generated.models.cluster_exposure import ClusterExposure
from astropulse._generated.models.cluster_group import ClusterGroup
from astropulse._generated.models.cluster_observed_nodes import ClusterObservedNodes
from astropulse._generated.models.cluster_operation import ClusterOperation
from astropulse._generated.models.cluster_status import ClusterStatus
from astropulse._generated.models.cluster_upgrade_offer import ClusterUpgradeOffer
from astropulse._generated.models.cluster_version_support import ClusterVersionSupport
from astropulse._generated.models.cpu_architecture import CPUArchitecture
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel
from astropulse._generated.models.kubeconfig_access import KubeconfigAccess
from astropulse._generated.models.node_group import NodeGroup
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.observed_nodes_unavailable_reason import ObservedNodesUnavailableReason
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_type import ProvisionerType
from astropulse._generated.models.state_tone import StateTone
from astropulse._generated.models.workload_identity_status import WorkloadIdentityStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class K8sCluster(BaseModel):
    """
    K8sCluster
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, description="The cloud provider account identifier. For GKE: GCP project ID. For EKS: AWS account ID. For AKS: Azure subscription ID. Used to generate provider-specific cleanup commands after cluster deletion.", alias="accountId")
    addons: Optional[List[ClusterAddonSummary]] = Field(default=None, description="Lists the add-ons installed on the cluster, with each one's version and status. Present on a single-cluster read.")
    agent_capabilities: Optional[List[StrictStr]] = Field(default=None, description="The protocol features advertised by the live agent.", alias="agentCapabilities")
    agent_capability_statuses: Optional[List[AgentCapabilityStatus]] = Field(default=None, description="The state of each capability of the cluster's agent (registered clusters only).", alias="agentCapabilityStatuses")
    agent_certificate: Optional[AgentCertificateStatus] = Field(default=None, description="When the AstroPulse agent's certificate on this cluster expires and whether it needs attention; omitted when not known.", alias="agentCertificate")
    agent_namespace: Optional[StrictStr] = Field(default=None, description="Where the registered-cluster agent is installed.", alias="agentNamespace")
    agent_version: Optional[StrictStr] = Field(default=None, description="The version of the agent running on the cluster (registered clusters only).", alias="agentVersion")
    application: Optional[List[ClusterApplication]] = Field(default=None, description="Represents the applications deployed on the cluster")
    approval_token: Optional[StrictStr] = Field(default=None, description="A single-use token for approving or rejecting this cluster request. Present only to the organization owner, while the state is ApprovalPending; it is used with the approval API.", alias="approvalToken")
    architecture: Optional[CPUArchitecture] = Field(default=None, description="The CPU architecture the cluster's nodes run.")
    capacity_label: Optional[StrictStr] = Field(default=None, description="How many worker nodes the cluster's node groups run, such as \"4 nodes\" or \"up to 10 nodes\", with \"when ready\" while the cluster is being created. Absent on a registered cluster, one with no node groups, and one that does not exist, such as a failed create or a deleted cluster.", alias="capacityLabel", json_schema_extra={"examples": ["up to 10 nodes"]})
    cloud_identity: Optional[ClusterCloudIdentity] = Field(default=None, description="Who the cluster is in its cloud, so you can grant it access on your side (a registry, a bucket, a key). Read from what the platform created; omitted until read.", alias="cloudIdentity")
    cluster_fqdn: Optional[StrictStr] = Field(default=None, description="The fully qualified domain name of the cluster", alias="clusterFQDN")
    cluster_id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the cluster", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The name of the cluster", alias="clusterName")
    compute_mode: Optional[ClusterComputeMode] = Field(default=None, description="Who manages this cluster's worker nodes. Omitted for registered clusters and wherever it is not known.", alias="computeMode")
    connectivity: Optional[ClusterConnectivity] = Field(default=None, description="Whether AstroPulse can currently reach and manage this cluster; omitted before its AstroPulse agent first connects and while the cluster does not exist. A registered cluster whose agent is reporting but cannot carry requests is Disconnected.")
    connectivity_notice: Optional[Notice] = Field(default=None, description="ConnectivityReason as a notice, with the one step that resolves it when there is one; absent when connectivityReason is empty.", alias="connectivityNotice")
    connectivity_reason: Optional[StrictStr] = Field(default=None, description="Says why Connectivity is not Connected, such as an agent that cannot carry requests or a missing stored key, and what to do; empty otherwise.", alias="connectivityReason")
    control_plane_node: Optional[NodeGroup] = Field(default=None, description="Represents the control plane node configuration (read-only in GET response). Includes the availability zones where the control plane is deployed. eks: auto-selected control plane AZs (first 3 sorted zones in region). gke: cluster-level zones from the regional cluster. aks: omitted because the control plane is fully managed by Azure and zones are not user-visible. selfHosted: zones match the control plane node group specification.", alias="controlPlaneNode")
    created_timestamp: Optional[datetime] = Field(default=None, description="The timestamp when the cluster was first created", alias="createdTimestamp")
    current_operation: Optional[ClusterOperation] = Field(default=None, description="The operation running on the cluster now and the step it is on. Omitted when none runs.", alias="currentOperation")
    exists: Optional[StrictBool] = Field(default=None, description="Says whether the cluster is there to use: false while it is being created or registered, when a create stopped before the cluster existed or a registration failed, and once it is deleted or unregistered.")
    exposure: Optional[ClusterExposure] = Field(default=None, description="How this cluster exposes applications over TLS: the ClusterIssuer their certificates come from and whether the cluster's agent observed it Ready, who runs cert-manager and external-dns, and whether an exposed application takes the gateway path. Reported on a single-cluster read only.")
    group: Optional[ClusterGroup] = Field(default=None, description="The group of the fleet view the cluster belongs to, decided by its state; a fleet's counts are its clusters' groups.")
    kubeconfig_access: Optional[KubeconfigAccess] = Field(default=None, description="Says how a kubeconfig generated for this cluster signs in and which lifetimes it can be generated with.", alias="kubeconfigAccess")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The version of Kubernetes running on the cluster", alias="kubernetesVersion")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="The key/value pairs attached to the cluster when it was registered.")
    last_cancellation: Optional[ClusterCancellation] = Field(default=None, description="The last cancel of an operation on the cluster and what it removed. Omitted when none was cancelled since the last operation started. Present on a single-cluster read.", alias="lastCancellation")
    last_seen: Optional[StrictStr] = Field(default=None, description="The RFC 3339 timestamp when the AstroPulse agent on this cluster last reported in, empty if it never has. It can be recent while Connectivity is Disconnected (see ConnectivityReason).", alias="lastSeen")
    last_updated_timestamp: Optional[datetime] = Field(default=None, description="The timestamp of the last update to the cluster", alias="lastUpdatedTimestamp")
    latest_agent_version: Optional[StrictStr] = Field(default=None, description="The latest available agent version from the container registry. Only populated for registered clusters. Compare with agentVersion to detect outdated agents.", alias="latestAgentVersion")
    observed_nodes: Optional[ClusterObservedNodes] = Field(default=None, description="The cluster's nodes as its agent last reported them, grouped by pool, beside the node groups declared in workerNodes. Omitted when there is no report to show; observedNodesUnavailable says why.", alias="observedNodes")
    observed_nodes_unavailable: Optional[ObservedNodesUnavailableReason] = Field(default=None, description="Why observedNodes is omitted. Empty when observedNodes is present.", alias="observedNodesUnavailable")
    observed_nodes_unavailable_message: Optional[StrictStr] = Field(default=None, description="One sentence saying why observedNodes is omitted. Set whenever observedNodesUnavailable is.", alias="observedNodesUnavailableMessage")
    provider: Optional[Provider] = Field(default=None, description="The cloud the cluster runs in; absent for a cluster outside a cloud, or one whose cloud is not known.")
    provisioner_type: Optional[ProvisionerType] = Field(default=None, description="The provisioner and its configuration.", alias="provisionerType")
    region: Optional[StrictStr] = Field(default=None, description="The geographical region where the cluster is deployed")
    registry_access: Optional[List[StrictStr]] = Field(default=None, description="Says which private images the cluster's nodes pull with no secret, and what to grant for others.", alias="registryAccess")
    release_channel: Optional[GKEReleaseChannel] = Field(default=None, description="The GKE release channel the cluster is enrolled in. Empty for non-GKE clusters.", alias="releaseChannel")
    resource_group: Optional[StrictStr] = Field(default=None, description="The Azure resource group for AKS clusters. Used to generate cleanup commands after cluster deletion.", alias="resourceGroup")
    rollback_status: Optional[AttemptStatusInfo] = Field(default=None, description="The status of the last/current rollback attempt.", alias="rollbackStatus")
    state: Optional[ClusterStatus] = Field(default=None, description="Represents the current state of the cluster.")
    state_tone: Optional[StateTone] = Field(default=None, description="How state reads at a glance.", alias="stateTone")
    status_notice: Optional[Notice] = Field(default=None, description="Says what a failed state means and the one step that resolves it; absent when the state is not a failure.", alias="statusNotice")
    status_reason: Optional[StrictStr] = Field(default=None, description="Explains the cluster's current state when an operation failed: what failed and how to fix it. Empty when the state needs no reason.", alias="statusReason")
    total_monthly_cost: Optional[StrictStr] = Field(default=None, description="Represents the estimated monthly cost of the cluster", alias="totalMonthlyCost")
    update_available: Optional[StrictBool] = Field(default=None, description="Indicates that a newer agent version is available and the cluster should be re-registered to update it (astroctl infra k8s register --cluster-name <name>).", alias="updateAvailable")
    upgrade: Optional[ClusterUpgradeOffer] = Field(default=None, description="The Kubernetes upgrade AstroPulse offers this cluster. Omitted while an operation runs or when it cannot be determined right now.")
    upgrade_status: Optional[AttemptStatusInfo] = Field(default=None, description="The status of the last/current upgrade attempt.", alias="upgradeStatus")
    version_support: Optional[ClusterVersionSupport] = Field(default=None, description="Reports whether AstroPulse can still manage this cluster at its current Kubernetes version. Present on a single-cluster read.", alias="versionSupport")
    worker_nodes: Optional[List[NodeGroup]] = Field(default=None, description="Represents the worker node configurations. Each node group includes the availability zones where it is deployed.", alias="workerNodes")
    workload_identity: Optional[WorkloadIdentityStatus] = Field(default=None, description="Whether workloads on this cluster can sign in to its cloud as an identity of their own. Omitted for registered clusters and other cases where it isn't known.", alias="workloadIdentity")
    __properties: ClassVar[List[str]] = ["accountId", "addons", "agentCapabilities", "agentCapabilityStatuses", "agentCertificate", "agentNamespace", "agentVersion", "application", "approvalToken", "architecture", "capacityLabel", "cloudIdentity", "clusterFQDN", "clusterId", "clusterName", "computeMode", "connectivity", "connectivityNotice", "connectivityReason", "controlPlaneNode", "createdTimestamp", "currentOperation", "exists", "exposure", "group", "kubeconfigAccess", "kubernetesVersion", "labels", "lastCancellation", "lastSeen", "lastUpdatedTimestamp", "latestAgentVersion", "observedNodes", "observedNodesUnavailable", "observedNodesUnavailableMessage", "provider", "provisionerType", "region", "registryAccess", "releaseChannel", "resourceGroup", "rollbackStatus", "state", "stateTone", "statusNotice", "statusReason", "totalMonthlyCost", "updateAvailable", "upgrade", "upgradeStatus", "versionSupport", "workerNodes", "workloadIdentity"]

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
        """Create an instance of K8sCluster from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in addons (list)
        _items = []
        if self.addons:
            for _item_addons in self.addons:
                if _item_addons:
                    _items.append(_item_addons.to_dict())
            _dict['addons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in agent_capability_statuses (list)
        _items = []
        if self.agent_capability_statuses:
            for _item_agent_capability_statuses in self.agent_capability_statuses:
                if _item_agent_capability_statuses:
                    _items.append(_item_agent_capability_statuses.to_dict())
            _dict['agentCapabilityStatuses'] = _items
        # override the default output from pydantic by calling `to_dict()` of agent_certificate
        if self.agent_certificate:
            _dict['agentCertificate'] = self.agent_certificate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in application (list)
        _items = []
        if self.application:
            for _item_application in self.application:
                if _item_application:
                    _items.append(_item_application.to_dict())
            _dict['application'] = _items
        # override the default output from pydantic by calling `to_dict()` of cloud_identity
        if self.cloud_identity:
            _dict['cloudIdentity'] = self.cloud_identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connectivity_notice
        if self.connectivity_notice:
            _dict['connectivityNotice'] = self.connectivity_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of control_plane_node
        if self.control_plane_node:
            _dict['controlPlaneNode'] = self.control_plane_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_operation
        if self.current_operation:
            _dict['currentOperation'] = self.current_operation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposure
        if self.exposure:
            _dict['exposure'] = self.exposure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kubeconfig_access
        if self.kubeconfig_access:
            _dict['kubeconfigAccess'] = self.kubeconfig_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_cancellation
        if self.last_cancellation:
            _dict['lastCancellation'] = self.last_cancellation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of observed_nodes
        if self.observed_nodes:
            _dict['observedNodes'] = self.observed_nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rollback_status
        if self.rollback_status:
            _dict['rollbackStatus'] = self.rollback_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_notice
        if self.status_notice:
            _dict['statusNotice'] = self.status_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of upgrade
        if self.upgrade:
            _dict['upgrade'] = self.upgrade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of upgrade_status
        if self.upgrade_status:
            _dict['upgradeStatus'] = self.upgrade_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_support
        if self.version_support:
            _dict['versionSupport'] = self.version_support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in worker_nodes (list)
        _items = []
        if self.worker_nodes:
            for _item_worker_nodes in self.worker_nodes:
                if _item_worker_nodes:
                    _items.append(_item_worker_nodes.to_dict())
            _dict['workerNodes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of K8sCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "addons": [ClusterAddonSummary.from_dict(_item) for _item in obj["addons"]] if obj.get("addons") is not None else None,
            "agentCapabilities": obj.get("agentCapabilities"),
            "agentCapabilityStatuses": [AgentCapabilityStatus.from_dict(_item) for _item in obj["agentCapabilityStatuses"]] if obj.get("agentCapabilityStatuses") is not None else None,
            "agentCertificate": AgentCertificateStatus.from_dict(obj["agentCertificate"]) if obj.get("agentCertificate") is not None else None,
            "agentNamespace": obj.get("agentNamespace"),
            "agentVersion": obj.get("agentVersion"),
            "application": [ClusterApplication.from_dict(_item) for _item in obj["application"]] if obj.get("application") is not None else None,
            "approvalToken": obj.get("approvalToken"),
            "architecture": obj.get("architecture"),
            "capacityLabel": obj.get("capacityLabel"),
            "cloudIdentity": ClusterCloudIdentity.from_dict(obj["cloudIdentity"]) if obj.get("cloudIdentity") is not None else None,
            "clusterFQDN": obj.get("clusterFQDN"),
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "computeMode": obj.get("computeMode"),
            "connectivity": obj.get("connectivity"),
            "connectivityNotice": Notice.from_dict(obj["connectivityNotice"]) if obj.get("connectivityNotice") is not None else None,
            "connectivityReason": obj.get("connectivityReason"),
            "controlPlaneNode": NodeGroup.from_dict(obj["controlPlaneNode"]) if obj.get("controlPlaneNode") is not None else None,
            "createdTimestamp": obj.get("createdTimestamp"),
            "currentOperation": ClusterOperation.from_dict(obj["currentOperation"]) if obj.get("currentOperation") is not None else None,
            "exists": obj.get("exists"),
            "exposure": ClusterExposure.from_dict(obj["exposure"]) if obj.get("exposure") is not None else None,
            "group": obj.get("group"),
            "kubeconfigAccess": KubeconfigAccess.from_dict(obj["kubeconfigAccess"]) if obj.get("kubeconfigAccess") is not None else None,
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "labels": obj.get("labels"),
            "lastCancellation": ClusterCancellation.from_dict(obj["lastCancellation"]) if obj.get("lastCancellation") is not None else None,
            "lastSeen": obj.get("lastSeen"),
            "lastUpdatedTimestamp": obj.get("lastUpdatedTimestamp"),
            "latestAgentVersion": obj.get("latestAgentVersion"),
            "observedNodes": ClusterObservedNodes.from_dict(obj["observedNodes"]) if obj.get("observedNodes") is not None else None,
            "observedNodesUnavailable": obj.get("observedNodesUnavailable"),
            "observedNodesUnavailableMessage": obj.get("observedNodesUnavailableMessage"),
            "provider": obj.get("provider"),
            "provisionerType": obj.get("provisionerType"),
            "region": obj.get("region"),
            "registryAccess": obj.get("registryAccess"),
            "releaseChannel": obj.get("releaseChannel"),
            "resourceGroup": obj.get("resourceGroup"),
            "rollbackStatus": AttemptStatusInfo.from_dict(obj["rollbackStatus"]) if obj.get("rollbackStatus") is not None else None,
            "state": obj.get("state"),
            "stateTone": obj.get("stateTone"),
            "statusNotice": Notice.from_dict(obj["statusNotice"]) if obj.get("statusNotice") is not None else None,
            "statusReason": obj.get("statusReason"),
            "totalMonthlyCost": obj.get("totalMonthlyCost"),
            "updateAvailable": obj.get("updateAvailable"),
            "upgrade": ClusterUpgradeOffer.from_dict(obj["upgrade"]) if obj.get("upgrade") is not None else None,
            "upgradeStatus": AttemptStatusInfo.from_dict(obj["upgradeStatus"]) if obj.get("upgradeStatus") is not None else None,
            "versionSupport": ClusterVersionSupport.from_dict(obj["versionSupport"]) if obj.get("versionSupport") is not None else None,
            "workerNodes": [NodeGroup.from_dict(_item) for _item in obj["workerNodes"]] if obj.get("workerNodes") is not None else None,
            "workloadIdentity": obj.get("workloadIdentity")
        })
        return _obj



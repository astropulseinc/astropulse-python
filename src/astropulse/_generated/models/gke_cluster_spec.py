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
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel
from astropulse._generated.models.gke_subnet_config import GKESubnetConfig
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GKEClusterSpec(BaseModel):
    """
    GKEClusterSpec
    """ # noqa: E501
    authorized_networks: Optional[Annotated[List[StrictStr], Field(max_length=50)]] = Field(default=None, description="CIDR blocks allowed to access the Kubernetes API server (optional, max 50 entries). Each entry must be a valid CIDR block (e.g. \"10.0.0.0/8\", \"203.0.113.5/32\"). If omitted, API access is unrestricted (not recommended for production).", alias="authorizedNetworks")
    autopilot: Optional[StrictBool] = Field(default=None, description="Enables GKE Autopilot mode where Google manages nodes, scaling, and security (optional, default: false). When disabled, uses Standard GKE with traditional node management.")
    credentials: Optional[Credentials] = Field(default=None, description="The GCP credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones.")
    enable_workload_identity: Optional[StrictBool] = Field(default=None, description="Enables Workload Identity for secure pod-to-GCP service authentication (optional, default: true). When enabled, pods can securely access GCP services using IAM without service account keys.", alias="enableWorkloadIdentity")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The Kubernetes version to create the cluster at (optional): \"1.30\", \"1.30.14\" or a full GKE version such as \"1.30.14-gke.1096000\". A shorter form selects the newest matching version the release channel offers; if omitted, the channel's default version is used.", alias="kubernetesVersion")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Google Cloud labels applied to the cluster (optional, at most 64). Keys are 1-63 and values at most 63 lowercase letters, digits, '_' and '-'; keys start with a lowercase letter.")
    master_ipv4_cidr_block: Optional[StrictStr] = Field(default=None, description="The IP range for the GKE control plane of a private cluster (optional, default: \"172.16.0.0/28\"). Must be exactly /28 CIDR in RFC 1918 private range (10.x, 172.16-31.x, 192.168.x). Change only if the default conflicts with your network. Examples: \"172.16.0.0/28\", \"10.0.0.0/28\", \"192.168.0.0/28\"", alias="masterIPv4CidrBlock")
    network_cidr: Optional[StrictStr] = Field(default=None, description="The node IP range of the subnet created for the cluster, for example \"10.50.0.0/20\"; it is allowed only when networkId is omitted (optional; if omitted, a free range is chosen). It must be a /8 to /29 block inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 or 100.64.0.0/10 that no other subnet in the network uses.", alias="networkCIDR")
    network_id: Optional[StrictStr] = Field(default=None, description="The existing GCP VPC network name (optional). Format: 1-63 lowercase letters, digits, or hyphens. If omitted, the cluster joins the project's default network on a subnet created for it.", alias="networkId")
    private_cluster: Optional[StrictBool] = Field(default=None, description="Gives the nodes internal IPs only (optional, default: false; requires credentials.type `Dynamic`). The Kubernetes API server keeps its public endpoint: restrict it with authorizedNetworks. On the default network (no networkId) AstroPulse adds a Cloud NAT for the nodes' egress; on your own network (networkId), the subnet must already have one.", alias="privateCluster")
    project_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The GCP project ID (required). Format: 6-30 lowercase letters, digits, or hyphens; must start with a letter. Example: \"my-gcp-project\"", alias="projectId")
    release_channel: Optional[GKEReleaseChannel] = Field(default=None, description="The release channel the cluster takes its Kubernetes versions from. Defaults to `Stable`.", alias="releaseChannel")
    subnet: Optional[GKESubnetConfig] = Field(default=None, description="The regional subnet configuration for BYOVPC (required when NetworkId is provided). GKE uses regional subnets with secondary IP ranges for pods and services.")
    __properties: ClassVar[List[str]] = ["authorizedNetworks", "autopilot", "credentials", "enableWorkloadIdentity", "kubernetesVersion", "labels", "masterIPv4CidrBlock", "networkCIDR", "networkId", "privateCluster", "projectId", "releaseChannel", "subnet"]

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
        """Create an instance of GKEClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subnet
        if self.subnet:
            _dict['subnet'] = self.subnet.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GKEClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorizedNetworks": obj.get("authorizedNetworks"),
            "autopilot": obj.get("autopilot"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "enableWorkloadIdentity": obj.get("enableWorkloadIdentity"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "labels": obj.get("labels"),
            "masterIPv4CidrBlock": obj.get("masterIPv4CidrBlock"),
            "networkCIDR": obj.get("networkCIDR"),
            "networkId": obj.get("networkId"),
            "privateCluster": obj.get("privateCluster"),
            "projectId": obj.get("projectId"),
            "releaseChannel": obj.get("releaseChannel"),
            "subnet": GKESubnetConfig.from_dict(obj["subnet"]) if obj.get("subnet") is not None else None
        })
        return _obj



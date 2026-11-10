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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.ami_family import AMIFamily
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.eks_auto_mode_config import EKSAutoModeConfig
from astropulse._generated.models.eks_compute_mode import EKSComputeMode
from astropulse._generated.models.subnet_spec import SubnetSpec
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EKSClusterSpec(BaseModel):
    """
    EKSClusterSpec
    """ # noqa: E501
    account_id: StrictStr = Field(description="The AWS account ID (required, 12-digit numeric string, e.g. \"123456789012\")", alias="accountId")
    ami_family: Optional[AMIFamily] = Field(default=None, description="The operating system image of the cluster's nodes. Defaults to `AmazonLinux2023`.", alias="amiFamily")
    auto_mode: Optional[EKSAutoModeConfig] = Field(default=None, description="Configures EKS Auto Mode extensions (optional). Valid only when computeMode is AutoMode; on ManagedNodeGroups, provision GPU capacity through the self-managed Karpenter add-on instead.", alias="autoMode")
    compute_mode: Optional[EKSComputeMode] = Field(default=None, description="Who creates and manages the worker nodes. `AutoMode` cannot be used with the Karpenter add-on.", alias="computeMode")
    credentials: Optional[Credentials] = Field(default=None, description="The AWS credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones.")
    ecr_account_ids: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = Field(default=None, description="Other AWS accounts whose ECR the nodes pull from (optional, max 20). Their repository policies must allow the cluster's node roles, which the cluster reports.", alias="ecrAccountIds")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The target Kubernetes version (optional). Accepts major.minor (e.g. \"1.30\") or major.minor.patch (e.g. \"1.30.14\") format. If omitted, AstroPulse uses the latest default version.", alias="kubernetesVersion")
    subnets: Optional[Dict[str, List[SubnetSpec]]] = Field(default=None, description="Maps availability zone names to subnet specifications for BYOVPC (optional). Required when VPCId is provided. Key is the zone name (e.g. \"us-west-2a\"), value is a list of SubnetSpec.")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="AWS tags applied to the cluster's node groups (optional, at most 40). Keys are 1-128 and values at most 256 letters, digits, spaces and _ . : / = + - @; keys may not start with aws:, platform.astropulse.io/, alpha.eksctl.io/, eksctl.cluster.k8s.io/ or karpenter.sh/.")
    vpc_cidr: Optional[StrictStr] = Field(default=None, description="The VPC's IPv4 range: required with vpcId, where it must equal the existing VPC's CIDR, and optional without it, where it sets the new VPC's range (e.g. \"10.0.0.0/16\"). It must be a /16 to /24 inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10 or 198.19.0.0/16.", alias="vpcCIDR")
    vpc_id: Optional[StrictStr] = Field(default=None, description="The existing AWS VPC ID (optional, format: vpc-xxxxxxxx). If omitted, a new VPC is created. Provide for BYOVPC deployments.", alias="vpcId")
    __properties: ClassVar[List[str]] = ["accountId", "amiFamily", "autoMode", "computeMode", "credentials", "ecrAccountIds", "kubernetesVersion", "subnets", "tags", "vpcCIDR", "vpcId"]

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
        """Create an instance of EKSClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto_mode
        if self.auto_mode:
            _dict['autoMode'] = self.auto_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in subnets (dict of array)
        _field_dict_of_array = {}
        if self.subnets:
            for _key_subnets in self.subnets:
                if self.subnets[_key_subnets] is not None:
                    _field_dict_of_array[_key_subnets] = [
                        _item.to_dict() for _item in self.subnets[_key_subnets]
                    ]
            _dict['subnets'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EKSClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "amiFamily": obj.get("amiFamily"),
            "autoMode": EKSAutoModeConfig.from_dict(obj["autoMode"]) if obj.get("autoMode") is not None else None,
            "computeMode": obj.get("computeMode"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "ecrAccountIds": obj.get("ecrAccountIds"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "subnets": {
                _k: [SubnetSpec.from_dict(_item) for _item in _v] if _v is not None else None
                for _k, _v in obj["subnets"].items()
            }
            if obj.get("subnets") is not None
            else None,
            "tags": obj.get("tags"),
            "vpcCIDR": obj.get("vpcCIDR"),
            "vpcId": obj.get("vpcId")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.addon_availability import AddonAvailability
from astropulse._generated.models.addon_component_sizing import AddonComponentSizing
from astropulse._generated.models.addon_resource_requirements import AddonResourceRequirements
from astropulse._generated.models.cert_manager_addon_configuration import CertManagerAddonConfiguration
from astropulse._generated.models.cost_visibility_addon_configuration import CostVisibilityAddonConfiguration
from astropulse._generated.models.external_dns_addon_configuration import ExternalDNSAddonConfiguration
from astropulse._generated.models.gateway_addon_configuration import GatewayAddonConfiguration
from astropulse._generated.models.karpenter_addon_configuration import KarpenterAddonConfiguration
from astropulse._generated.models.model_serving_addon_configuration import ModelServingAddonConfiguration
from astropulse._generated.models.nginx_addon_configuration import NginxAddonConfiguration
from astropulse._generated.models.vulnerability_scanning_addon_configuration import VulnerabilityScanningAddonConfiguration
from astropulse._generated.models.workload_autoscaling_addon_configuration import WorkloadAutoscalingAddonConfiguration
from astropulse._generated.models.workload_queueing_addon_configuration import WorkloadQueueingAddonConfiguration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonConfiguration(BaseModel):
    """
    ClusterAddonConfiguration
    """ # noqa: E501
    availability: Optional[AddonAvailability] = Field(default=None, description="How many copies of the add-on's components run; choose `High` to keep it serving when a node fails, where the cluster has the nodes for it. Left out, an update keeps the current value and a new add-on runs `Standard`.")
    cert_manager: Optional[CertManagerAddonConfiguration] = Field(default=None, description="Configures the cert-manager add-on.", alias="certManager")
    components: Optional[Dict[str, AddonComponentSizing]] = Field(default=None, description="CPU and memory for each of the add-on's other components, by component name; change one only if it runs out of memory or the cluster is small. A component left out keeps its sizing, and `{}` returns it to AstroPulse's sizing.")
    cost_visibility: Optional[CostVisibilityAddonConfiguration] = Field(default=None, description="Configures the cost-visibility add-on.", alias="costVisibility")
    external_dns: Optional[ExternalDNSAddonConfiguration] = Field(default=None, description="Configures the external-dns add-on.", alias="externalDns")
    gateway: Optional[GatewayAddonConfiguration] = Field(default=None, description="Configures the gateway add-on.")
    karpenter: Optional[KarpenterAddonConfiguration] = Field(default=None, description="Configures the Node Autoscaling add-on.")
    model_serving: Optional[ModelServingAddonConfiguration] = Field(default=None, description="Configures the model-serving add-on.", alias="modelServing")
    nginx: Optional[NginxAddonConfiguration] = Field(default=None, description="Configures the nginx-ingress add-on.")
    resources: Optional[AddonResourceRequirements] = Field(default=None, description="CPU and memory for the add-on's main component; change them only if it runs out of memory or the cluster is small. Settings left out keep their current value, and `{}` returns to AstroPulse's sizing.")
    vulnerability_scanning: Optional[VulnerabilityScanningAddonConfiguration] = Field(default=None, description="Configures the vulnerability-scanning add-on.", alias="vulnerabilityScanning")
    workload_autoscaling: Optional[WorkloadAutoscalingAddonConfiguration] = Field(default=None, description="Configures the workload-autoscaling add-on.", alias="workloadAutoscaling")
    workload_queueing: Optional[WorkloadQueueingAddonConfiguration] = Field(default=None, description="Configures the workload-queueing add-on.", alias="workloadQueueing")
    __properties: ClassVar[List[str]] = ["availability", "certManager", "components", "costVisibility", "externalDns", "gateway", "karpenter", "modelServing", "nginx", "resources", "vulnerabilityScanning", "workloadAutoscaling", "workloadQueueing"]

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
        """Create an instance of ClusterAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cert_manager
        if self.cert_manager:
            _dict['certManager'] = self.cert_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in components (dict)
        _field_dict = {}
        if self.components:
            for _key_components in self.components:
                if self.components[_key_components]:
                    _field_dict[_key_components] = self.components[_key_components].to_dict()
            _dict['components'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of cost_visibility
        if self.cost_visibility:
            _dict['costVisibility'] = self.cost_visibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_dns
        if self.external_dns:
            _dict['externalDns'] = self.external_dns.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gateway
        if self.gateway:
            _dict['gateway'] = self.gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of karpenter
        if self.karpenter:
            _dict['karpenter'] = self.karpenter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_serving
        if self.model_serving:
            _dict['modelServing'] = self.model_serving.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nginx
        if self.nginx:
            _dict['nginx'] = self.nginx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vulnerability_scanning
        if self.vulnerability_scanning:
            _dict['vulnerabilityScanning'] = self.vulnerability_scanning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workload_autoscaling
        if self.workload_autoscaling:
            _dict['workloadAutoscaling'] = self.workload_autoscaling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workload_queueing
        if self.workload_queueing:
            _dict['workloadQueueing'] = self.workload_queueing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability": obj.get("availability"),
            "certManager": CertManagerAddonConfiguration.from_dict(obj["certManager"]) if obj.get("certManager") is not None else None,
            "components": dict(
                (_k, AddonComponentSizing.from_dict(_v))
                for _k, _v in obj["components"].items()
            )
            if obj.get("components") is not None
            else None,
            "costVisibility": CostVisibilityAddonConfiguration.from_dict(obj["costVisibility"]) if obj.get("costVisibility") is not None else None,
            "externalDns": ExternalDNSAddonConfiguration.from_dict(obj["externalDns"]) if obj.get("externalDns") is not None else None,
            "gateway": GatewayAddonConfiguration.from_dict(obj["gateway"]) if obj.get("gateway") is not None else None,
            "karpenter": KarpenterAddonConfiguration.from_dict(obj["karpenter"]) if obj.get("karpenter") is not None else None,
            "modelServing": ModelServingAddonConfiguration.from_dict(obj["modelServing"]) if obj.get("modelServing") is not None else None,
            "nginx": NginxAddonConfiguration.from_dict(obj["nginx"]) if obj.get("nginx") is not None else None,
            "resources": AddonResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "vulnerabilityScanning": VulnerabilityScanningAddonConfiguration.from_dict(obj["vulnerabilityScanning"]) if obj.get("vulnerabilityScanning") is not None else None,
            "workloadAutoscaling": WorkloadAutoscalingAddonConfiguration.from_dict(obj["workloadAutoscaling"]) if obj.get("workloadAutoscaling") is not None else None,
            "workloadQueueing": WorkloadQueueingAddonConfiguration.from_dict(obj["workloadQueueing"]) if obj.get("workloadQueueing") is not None else None
        })
        return _obj



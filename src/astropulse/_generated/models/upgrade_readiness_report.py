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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_health_check import ClusterHealthCheck
from astropulse._generated.models.k8s_version_analysis import K8sVersionAnalysis
from astropulse._generated.models.readiness_report_section import ReadinessReportSection
from astropulse._generated.models.resource_capacity_check import ResourceCapacityCheck
from astropulse._generated.models.upgrade_risk_level import UpgradeRiskLevel
from astropulse._generated.models.validation_issue import ValidationIssue
from astropulse._generated.models.workload_impact_analysis import WorkloadImpactAnalysis
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpgradeReadinessReport(BaseModel):
    """
    UpgradeReadinessReport
    """ # noqa: E501
    can_proceed: Optional[StrictBool] = Field(default=None, description="Indicates whether the upgrade can safely proceed", alias="canProceed")
    cluster_health: Optional[ClusterHealthCheck] = Field(default=None, description="The current cluster health assessment; absent when not evaluated.", alias="clusterHealth")
    critical_issues: Optional[List[ValidationIssue]] = Field(default=None, description="Blocking issues that must be resolved before upgrading", alias="criticalIssues")
    estimated_time: Optional[StrictStr] = Field(default=None, description="The estimated upgrade duration (e.g. \"45-60 minutes\")", alias="estimatedTime")
    not_evaluated: Optional[List[ReadinessReportSection]] = Field(default=None, description="Names the analysis sections this report does not include.", alias="notEvaluated")
    nothing_to_upgrade: Optional[StrictBool] = Field(default=None, description="True when the cluster is already at the newest version the requested target resolves to, so there is no upgrade to perform.", alias="nothingToUpgrade")
    nothing_to_upgrade_summary: Optional[StrictStr] = Field(default=None, description="The message to show when nothingToUpgrade is true; empty otherwise.", alias="nothingToUpgradeSummary")
    readiness_score: Optional[StrictInt] = Field(default=None, description="The overall readiness score (0-100, higher is better); absent when the report did not assess readiness.", alias="readinessScore")
    recommendations: Optional[List[StrictStr]] = Field(default=None, description="Suggested actions to improve upgrade safety")
    report_summary: Optional[StrictStr] = Field(default=None, description="A human-readable summary of the readiness analysis", alias="reportSummary")
    resource_analysis: Optional[ResourceCapacityCheck] = Field(default=None, description="Contains resource capacity validation; absent when not evaluated.", alias="resourceAnalysis")
    risk_level: Optional[UpgradeRiskLevel] = Field(default=None, description="The assessed risk, Unknown when the report did not assess readiness.", alias="riskLevel")
    version_analysis: Optional[K8sVersionAnalysis] = Field(default=None, description="Contains Kubernetes version compatibility analysis; absent when not evaluated.", alias="versionAnalysis")
    warnings: Optional[List[ValidationIssue]] = Field(default=None, description="Non-blocking issues to be aware of")
    workload_analysis: Optional[WorkloadImpactAnalysis] = Field(default=None, description="Contains workload impact assessment; absent when not evaluated.", alias="workloadAnalysis")
    __properties: ClassVar[List[str]] = ["canProceed", "clusterHealth", "criticalIssues", "estimatedTime", "notEvaluated", "nothingToUpgrade", "nothingToUpgradeSummary", "readinessScore", "recommendations", "reportSummary", "resourceAnalysis", "riskLevel", "versionAnalysis", "warnings", "workloadAnalysis"]

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
        """Create an instance of UpgradeReadinessReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster_health
        if self.cluster_health:
            _dict['clusterHealth'] = self.cluster_health.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in critical_issues (list)
        _items = []
        if self.critical_issues:
            for _item_critical_issues in self.critical_issues:
                if _item_critical_issues:
                    _items.append(_item_critical_issues.to_dict())
            _dict['criticalIssues'] = _items
        # override the default output from pydantic by calling `to_dict()` of resource_analysis
        if self.resource_analysis:
            _dict['resourceAnalysis'] = self.resource_analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of version_analysis
        if self.version_analysis:
            _dict['versionAnalysis'] = self.version_analysis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of workload_analysis
        if self.workload_analysis:
            _dict['workloadAnalysis'] = self.workload_analysis.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradeReadinessReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canProceed": obj.get("canProceed"),
            "clusterHealth": ClusterHealthCheck.from_dict(obj["clusterHealth"]) if obj.get("clusterHealth") is not None else None,
            "criticalIssues": [ValidationIssue.from_dict(_item) for _item in obj["criticalIssues"]] if obj.get("criticalIssues") is not None else None,
            "estimatedTime": obj.get("estimatedTime"),
            "notEvaluated": obj.get("notEvaluated"),
            "nothingToUpgrade": obj.get("nothingToUpgrade"),
            "nothingToUpgradeSummary": obj.get("nothingToUpgradeSummary"),
            "readinessScore": obj.get("readinessScore"),
            "recommendations": obj.get("recommendations"),
            "reportSummary": obj.get("reportSummary"),
            "resourceAnalysis": ResourceCapacityCheck.from_dict(obj["resourceAnalysis"]) if obj.get("resourceAnalysis") is not None else None,
            "riskLevel": obj.get("riskLevel"),
            "versionAnalysis": K8sVersionAnalysis.from_dict(obj["versionAnalysis"]) if obj.get("versionAnalysis") is not None else None,
            "warnings": [ValidationIssue.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "workloadAnalysis": WorkloadImpactAnalysis.from_dict(obj["workloadAnalysis"]) if obj.get("workloadAnalysis") is not None else None
        })
        return _obj



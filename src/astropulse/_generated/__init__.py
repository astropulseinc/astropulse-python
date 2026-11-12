# coding: utf-8

# flake8: noqa

"""
    AstroPulse Platform API

    The programmable production foundation for applications, AI workloads, and infrastructure products.  AstroPulse provides a unified control plane for composing cloud infrastructure, deploying workloads, and operating their production lifecycle. Provision and manage Kubernetes clusters, deploy applications and AI models, and manage networking, scaling, access, integrations, observability, cost visibility, and governance.  **Keep your product. Skip rebuilding the production layer.** AstroPulse manages the production machinery underneath your application, runtime, scheduler, inference system, or infrastructure product, while you retain ownership of the capabilities that make it different.  ## Base URL All public API endpoints are served over HTTPS at `https://api.astropulse.io` and versioned under `/api/v1`.  ## Working with AstroPulse The API follows the operational lifecycle of your infrastructure and workloads: - **Connect infrastructure:** Configure cloud accounts, discover regions, machine types, and accelerators, and provision or register Kubernetes clusters. - **Configure environments:** Manage cluster add-ons, application profiles, availability tiers, domains, and endpoint access policies. - **Deploy workloads:** Deploy applications and supported AI models, inspect their state, and discover their serving endpoints. - **Operate and recover:** Monitor deployment progress, manage supported lifecycle operations, inspect version history, plan rollbacks, and recover deployments. - **Observe and govern:** Inspect operational metrics, cost and usage data, activity, integrations, identities, permissions, and audit records.  Resources are organized by their role in the platform. Each operation defines its own parameters, request and response schemas, authentication requirements, and failure conditions.  ## Authentication AstroPulse supports API keys and short-lived bearer tokens. Each endpoint declares which authentication methods it accepts.  **API keys — recommended for automation** Send `X-Astro-API-Key: <key>`. For production automation, use an organization-owned service-account key. Service accounts are managed by organization administrators through the Service Accounts API and do not depend on an individual user's session.  Personal API keys are available under Organization settings > API Keys. API keys are scoped to one organization.  **Bearer tokens — interactive sessions** Send `Authorization: Bearer <jwt>`. These credentials are short-lived access tokens issued by the configured authentication provider.  To print an access token for a direct API request, run `astroctl auth login --print-access-token` (`-p`). A standard `astroctl auth login` stores the authenticated session without printing the token.  For unattended integrations, use API keys instead of interactive session tokens. Store all credentials securely and never expose them in repositories, client-side code, or logs.  ## SDKs and API clients The generated OpenAPI 3 specification is the public contract for AstroPulse REST API consumers and generated clients.  AstroPulse provides operation-specific Python and TypeScript SDK examples in this reference. Each generated SDK exposes resources through typed clients, with method names derived from stable API operation IDs.  **Python SDK:** Install using `pip install \"git+https://github.com/astropulseinc/astropulse-python\"`.  Common operations include `client.clusters.list_clusters()` and `client.applications.deploy_application(...)`. Consult the SDK's documentation for client initialization, authentication, and complete examples.  The same platform capabilities can be accessed through the REST API, supported SDKs, astroctl, and the AstroPulse Console. Refer to the documentation for the supported workflows of each interface.  **Application runtime endpoints:** Applications deployed through AstroPulse expose runtime endpoints separate from the platform control-plane API. Model deployments supporting the OpenAI API protocol can be called with an OpenAI-compatible client configured for the deployed endpoint and its access requirements.  ## Lifecycle and asynchronous operations Infrastructure provisioning, deployment, and certain lifecycle changes can execute asynchronously. An accepted request does not necessarily mean the underlying operation has completed.  Use the operation's response, resource status, and available progress streams to determine completion and inspect failures.  Supported application operations include version history, rollback, resume, and GitOps reconciliation. Rollback operations can provide dry-run plans so callers can inspect an eligible change before applying it.  Consult each operation for its specific state transitions, mutation semantics, retry behavior, and concurrency restrictions.  ## Observability and cost Supported resources expose deployment state, application and cluster metrics, cost and usage series, and operational diagnostics.  Metrics and cost data represent collected observations. Missing samples, incomplete coverage, and unavailable reporting intervals must not be interpreted as zero resource consumption or zero spend.  Use the coverage information, time windows, and aggregation intervals documented by each operation when processing telemetry and cost responses.  ## Real-time streaming Supported application endpoints provide real-time status, event, and log streams over WebSocket connections.  Streaming requests have different connection and authentication semantics from ordinary JSON requests. Supported browser workflows can obtain a short-lived, single-use stream ticket before establishing a WebSocket connection.  Stream tickets are valid for at most 30 seconds. Follow the individual endpoint's documented handshake, authentication, and error-handling requirements.  ## Response format Successful JSON API responses use the documented resource schema, commonly wrapped in an envelope with the result under `data` and optional `id`, `status`, and `message` fields.  Consumers must follow each endpoint's declared response type. Streaming connections and other specialized responses may have different transport semantics.  ## Errors and diagnostics API failures use a consistent JSON error structure containing: - `message`: Human-readable explanation. - `code`: Stable, machine-readable error identifier. - `status`: HTTP response status. - `traceId`: Diagnostic request trace identifier. - `details`: Optional structured error details.  **Branch on HTTP status and `code`, never on the wording of `message`.**  The `X-Trace-ID` response header exposes the request's diagnostic trace identifier. Include it when reporting failures. It is not a distributed tracing propagation header.  Common HTTP errors include: - `400 Bad Request`: Invalid input or request. - `401 Unauthorized`: Missing, invalid, expired, or revoked credentials. - `402 Payment Required`: Requested capability is unavailable under the current plan. - `403 Forbidden`: Insufficient permissions. - `404 Not Found`: Resource or route not found. - `405 Method Not Allowed`: Unsupported HTTP method for a route. - `409 Conflict`: Resource state or concurrent operation conflict. - `429 Too Many Requests`: Rate limit exceeded. - `500 Internal Server Error`: Unexpected server failure. - `503 Service Unavailable`: A required service is temporarily unavailable.  The applicable status codes and response schemas are documented for each operation.  ## Versioning and compatibility Public API versions are identified by the URL path, beginning with `/api/v1`. The generated specification's `info.version` identifies the AstroPulse build from which the document was generated.  Within an API version, backward-compatible evolution can introduce new endpoints, optional request fields, response properties, and values in extensible enumerations.  Clients should tolerate unknown response properties and supported enum extensions. Consumers must not depend on undocumented list ordering or human-readable error messages.  Breaking changes, including removing or renaming fields, changing documented field types, or making previously optional request fields mandatory, require compatibility review and an appropriate API version transition.  The generated OpenAPI specification is the authoritative contract for client generation and compatibility validation.  ## Rate limiting and retries AstroPulse applies layered request rate limits: - Global service-wide limits. - Per-IP limits. - Additional per-API-key limits. - Per-authenticated-principal limits where enabled.  Exceeding an applicable limit returns `429 Too Many Requests`. Respect the `Retry-After` response header and implement bounded exponential backoff with jitter.  Temporary service failures may return `503 Service Unavailable` with retry guidance. Retry state-changing operations only when their documented semantics make repetition safe.  Global and per-IP limits remain applicable regardless of the credential used. Rotating credentials does not bypass those limits.  ## Identity, governance, and audit AstroPulse organizes platform resources within organizations. Authentication, authorization, and applicable plan restrictions govern access to resource operations.  Mutating API requests and designated sensitive reads are recorded for auditability. Audit records capture available actor, organization, resource, action, outcome, and request context without storing request bodies or secrets.  Organization-owned service accounts provide dedicated automation identities, while API keys and user sessions retain their associated authentication and authorization boundaries.  ## Developer documentation This API reference defines the public platform contract. The [AstroPulse Documentation](https://astropulse.io/docs) provides guided workflows, platform concepts, SDK integration, CLI usage, and end-to-end examples.  API schemas and operation definitions are the source of truth for clients, developer tools, and authorized automation.

    The version of the OpenAPI document: v1.0.1
    Contact: contact@astropulse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "APIDocumentApi",
    "APIKeysApi",
    "AccessPoliciesApi",
    "ApplicationProfilesApi",
    "ApplicationsApi",
    "AuditApi",
    "AvailabilityTiersApi",
    "CloudAccountsApi",
    "CloudCatalogApi",
    "ClusterAddOnsApi",
    "ClustersApi",
    "DomainsApi",
    "IntegrationsApi",
    "NotificationsApi",
    "OrganizationsApi",
    "PricingApi",
    "ServiceAccountsApi",
    "UsersApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AKSAutoUpgradeChannel",
    "AKSClusterSpec",
    "AKSNetworkPlugin",
    "AKSNetworkPluginMode",
    "AKSNodeOSUpgradeChannel",
    "AKSUpdateSpec",
    "AMIFamiliesForVersion",
    "AMIFamily",
    "AMIFamilyOffer",
    "APIKeyCreated",
    "APIKeyCreatedResponse",
    "APIKeyExpiration",
    "APIKeyFeatureFlags",
    "APIKeyLifecycleStatus",
    "APIKeyListResponse",
    "APIKeyMetadata",
    "APIKeyRequest",
    "APIKeyResponse",
    "APIKeyServiceAccount",
    "APIKeySource",
    "APIKeySummary",
    "APIKeySummaryResponse",
    "APIKeyValidation",
    "APIKeyValidationResponse",
    "AWSAddonConfig",
    "AWSConnectRequest",
    "AWSConnectStatus",
    "AWSConnectStatusResponse",
    "AWSCredentialsRequest",
    "AWSTemporaryCredential",
    "AWSTemporaryCredentialResponse",
    "Accelerator",
    "AcceleratorAttachment",
    "AcceleratorKind",
    "AcceleratorMetrics",
    "AcceleratorMetricsSummary",
    "AcceleratorOffer",
    "AcceleratorOfferAvailability",
    "AcceleratorOfferInstance",
    "AcceleratorOfferQuota",
    "AcceleratorOfferReasonCode",
    "AcceleratorOfferSource",
    "AcceleratorOffering",
    "AcceleratorOfferingListResponse",
    "AcceleratorOffersIncompleteReason",
    "AcceleratorOffersUnavailableReason",
    "AcceleratorVendor",
    "AccessPolicy",
    "AccessPolicyAPIKeys",
    "AccessPolicyClaim",
    "AccessPolicyClaimType",
    "AccessPolicyIdentity",
    "AccessPolicyJWT",
    "AccessPolicyKey",
    "AccessPolicyKeyCreated",
    "AccessPolicyKeyCreatedResponse",
    "AccessPolicyKeyListResponse",
    "AccessPolicyKeyRequest",
    "AccessPolicyListResponse",
    "AccessPolicyResponse",
    "AccessPolicySecretRef",
    "AccessPolicySpec",
    "AccessPolicyTokenRejection",
    "AccessPolicyTokenResult",
    "AccessPolicyTokenResultResponse",
    "AccessPolicyTokenTest",
    "AccountSetup",
    "AddUserToOrganizationRequest",
    "AddonAutoScalingConfig",
    "AddonAvailability",
    "AddonCloudAccess",
    "AddonComponentSizing",
    "AddonConfigurationField",
    "AddonConfigurationFormat",
    "AddonFieldCondition",
    "AddonFieldType",
    "AddonResourceRequirements",
    "AddonResources",
    "AddonServiceAccount",
    "AddonUnavailableValue",
    "AddonWorkloadIdentity",
    "AffinityType",
    "AgentCapabilityState",
    "AgentCapabilityStatus",
    "AgentCertificateBundle",
    "AgentCertificateBundleResponse",
    "AgentCertificateSigningRequest",
    "AgentCertificateState",
    "AgentCertificateStatus",
    "AppResource",
    "Application",
    "ApplicationContainerTermination",
    "ApplicationCostSummary",
    "ApplicationCostSummaryResponse",
    "ApplicationDeployment",
    "ApplicationDeploymentResponse",
    "ApplicationHistory",
    "ApplicationHistoryResponse",
    "ApplicationListResponse",
    "ApplicationManifest",
    "ApplicationMetricsAllocationItem",
    "ApplicationMetricsSeries",
    "ApplicationMetricsSeriesResponse",
    "ApplicationModelStatus",
    "ApplicationOperation",
    "ApplicationOperationResponse",
    "ApplicationProfile",
    "ApplicationProfileBulkDeleteRequest",
    "ApplicationProfileListResponse",
    "ApplicationProfileManifest",
    "ApplicationProfileRequest",
    "ApplicationProfileResponse",
    "ApplicationRequest",
    "ApplicationRequestResponse",
    "ApplicationResponse",
    "ApplicationResumePlan",
    "ApplicationResumePlanResponse",
    "ApplicationResync",
    "ApplicationResyncRequest",
    "ApplicationResyncResponse",
    "ApplicationResyncStatus",
    "ApplicationRollbackPlan",
    "ApplicationRollbackPlanResponse",
    "ApplicationRollbackRequest",
    "ApplicationRollbackState",
    "ApplicationSource",
    "ApplicationStatus",
    "ApplicationVersionEntry",
    "ApplicationVersionState",
    "ApplyDryRunAction",
    "ApplyDryRunResult",
    "ApplyDryRunResultResponse",
    "ArchitectureType",
    "AttemptStatus",
    "AttemptStatusInfo",
    "AuditAction",
    "AuditActorType",
    "AuditEvent",
    "AuditEventList",
    "AuditEventListResponse",
    "AuditEventResponse",
    "AuditEventType",
    "AuditExportFormat",
    "AuditSource",
    "AuditStats",
    "AuditStatsResponse",
    "AutoscalingMetricsSource",
    "AutoscalingPrometheusSource",
    "AvailabilityTier",
    "AzureConnectRequest",
    "AzureConnectStatus",
    "AzureConnectStatusResponse",
    "AzureTemporaryCredential",
    "AzureTemporaryCredentialResponse",
    "BooleanResponse",
    "CPUArchitecture",
    "CPUResources",
    "CancelCleanupItem",
    "CancelCleanupKind",
    "CancelCleanupOutcome",
    "CancelClusterOperationRequest",
    "CapacityBlockPhase",
    "CapacityBlockStatus",
    "CapacityReservation",
    "CapacityReservationKind",
    "CapacityReservationListResponse",
    "CertManagerAddonConfiguration",
    "CertManagerDNSProvider",
    "CertManagerDNSSolver",
    "CertManagerIssuerType",
    "ChannelVersions",
    "CloudAccessMode",
    "CloudAccount",
    "CloudAccountCluster",
    "CloudAccountListResponse",
    "CloudAccountPendingConnection",
    "CloudAccountState",
    "CloudAccountStatus",
    "CloudConnectAttemptError",
    "CloudConnectFailureReason",
    "CloudConnection",
    "CloudConnectionListResponse",
    "CloudConnectionResponse",
    "CloudConnectionState",
    "CloudProvider",
    "CloudProviderConfig",
    "CloudProviderName",
    "Cluster",
    "ClusterAccelerators",
    "ClusterAcceleratorsResponse",
    "ClusterAccessToken",
    "ClusterAccessTokenResponse",
    "ClusterAddon",
    "ClusterAddonAcceleratorReadiness",
    "ClusterAddonApplyOptions",
    "ClusterAddonCatalogEntry",
    "ClusterAddonCatalogEntryListResponse",
    "ClusterAddonConfiguration",
    "ClusterAddonCostPricing",
    "ClusterAddonCostSeries",
    "ClusterAddonCostSeriesResponse",
    "ClusterAddonCostSummary",
    "ClusterAddonCostSummaryResponse",
    "ClusterAddonDeploymentOptions",
    "ClusterAddonExposure",
    "ClusterAddonHealth",
    "ClusterAddonHealthCheck",
    "ClusterAddonHistoryEntry",
    "ClusterAddonHistoryResponse",
    "ClusterAddonHistoryResponseEnvelope",
    "ClusterAddonIngressTLS",
    "ClusterAddonListResponse",
    "ClusterAddonMetricsSeries",
    "ClusterAddonMetricsSeriesResponse",
    "ClusterAddonModelCacheNodeGroup",
    "ClusterAddonModelCacheReadiness",
    "ClusterAddonNodeAddress",
    "ClusterAddonOperation",
    "ClusterAddonOperationMetadata",
    "ClusterAddonOperationResponse",
    "ClusterAddonQueueNamespaces",
    "ClusterAddonResilience",
    "ClusterAddonResponse",
    "ClusterAddonResyncResponse",
    "ClusterAddonResyncResponseEnvelope",
    "ClusterAddonStatus",
    "ClusterAddonSummary",
    "ClusterAddonSupport",
    "ClusterAddonSupportStatus",
    "ClusterAddonTLSChallenge",
    "ClusterAddonTLSChallenges",
    "ClusterAddonTLSExposure",
    "ClusterAddonTLSIssuer",
    "ClusterAddonTLSMode",
    "ClusterAddonTLSReadiness",
    "ClusterAddonType",
    "ClusterAddonUpdateOptions",
    "ClusterAddonUpdateStrategy",
    "ClusterAddonVersion",
    "ClusterAddonVersionListResponse",
    "ClusterApplication",
    "ClusterApproval",
    "ClusterApprovalAction",
    "ClusterApprovalOutcome",
    "ClusterApprovalResponse",
    "ClusterCancellation",
    "ClusterCancellationStatus",
    "ClusterCloudIdentity",
    "ClusterComputeMode",
    "ClusterConnectivity",
    "ClusterCostAllocation",
    "ClusterCostAllocationResponse",
    "ClusterCostSeries",
    "ClusterCostSeriesResponse",
    "ClusterCostSummary",
    "ClusterCostSummaryResponse",
    "ClusterCreation",
    "ClusterCreationResponse",
    "ClusterDeleteDryRun",
    "ClusterDeleteGroup",
    "ClusterDeleteGroupKind",
    "ClusterDeleteItem",
    "ClusterDeleteOutcome",
    "ClusterDeletion",
    "ClusterDeletionResponse",
    "ClusterDryRun",
    "ClusterDryRunResponse",
    "ClusterExposure",
    "ClusterExposureBrick",
    "ClusterExposureCertificates",
    "ClusterExposureIssuer",
    "ClusterExposureOwner",
    "ClusterExposureResponse",
    "ClusterExposureSettings",
    "ClusterGroup",
    "ClusterHealthCheck",
    "ClusterInfrastructureCharge",
    "ClusterInfrastructureEstimate",
    "ClusterInfrastructureEstimateResponse",
    "ClusterInfrastructureItem",
    "ClusterInfrastructureUnpriced",
    "ClusterIssuerKind",
    "ClusterLoadBalancerExposure",
    "ClusterMetricsAllocation",
    "ClusterMetricsAllocationResponse",
    "ClusterMetricsSortField",
    "ClusterMetricsSummary",
    "ClusterMetricsSummaryResponse",
    "ClusterObservedNodes",
    "ClusterOperation",
    "ClusterOperationKind",
    "ClusterOperationResult",
    "ClusterOperationResultResponse",
    "ClusterOperationStep",
    "ClusterPriceSource",
    "ClusterProgress",
    "ClusterProgressPage",
    "ClusterProgressPageResponse",
    "ClusterProgressResponse",
    "ClusterRegistration",
    "ClusterRegistrationResponse",
    "ClusterRegistrationStatus",
    "ClusterRegistrationStatusResponse",
    "ClusterScanFindingsSummary",
    "ClusterScanFindingsSummaryResponse",
    "ClusterSelection",
    "ClusterSelectionType",
    "ClusterStatus",
    "ClusterStorage",
    "ClusterStorageBinding",
    "ClusterStorageBindingUse",
    "ClusterStorageClass",
    "ClusterStorageResponse",
    "ClusterUpdate",
    "ClusterUpdateDryRun",
    "ClusterUpdateResult",
    "ClusterUpgradeOffer",
    "ClusterVersionSupport",
    "ClusterVersionSupportState",
    "ComputeType",
    "Constraints",
    "Container",
    "ControlPlaneNode",
    "ControlPlaneNodeGroup",
    "CostAllocationGroupBy",
    "CostAllocationItem",
    "CostAllocationSortBy",
    "CostDimensions",
    "CostGroup",
    "CostMetricsSource",
    "CostPriceSheet",
    "CostPricing",
    "CostPricingSource",
    "CostRowKind",
    "CostSeriesPoint",
    "CostTotal",
    "CostVisibilityAddonConfiguration",
    "CostVisibilityPrometheusConfiguration",
    "CostVisibilityPrometheusStorageConfiguration",
    "CostWindow",
    "CreateDomainBindingRequest",
    "CreateDomainRequest",
    "CredentialType",
    "Credentials",
    "CurrentOrganization",
    "CurrentOrganizationResponse",
    "DataPlane",
    "DeleteAPIKeyRequest",
    "DeleteAPIKeyResponse",
    "DeleteAPIKeyResponseEnvelope",
    "DeployClusterAddonRequest",
    "DeployValidationResult",
    "DeployValidationResultResponse",
    "DeploymentDiffItem",
    "Domain",
    "DomainBinding",
    "DomainBindingResponse",
    "DomainBindingStatus",
    "DomainHostnameSource",
    "DomainListResponse",
    "DomainResponse",
    "DomainStatus",
    "DryRunVerdict",
    "EKSAutoModeConfig",
    "EKSClusterSpec",
    "EKSComputeMode",
    "EKSUpdateSpec",
    "EndpointAccessPolicyNone",
    "EndpointAccessPolicyReference",
    "EndpointChangeRequest",
    "EndpointDNSObservation",
    "EndpointDesiredState",
    "EndpointExposure",
    "EndpointExposureStatus",
    "EndpointOrigin",
    "EndpointOriginSource",
    "EndpointPhase",
    "EndpointProbe",
    "EndpointProbeReach",
    "EndpointProbeResult",
    "EndpointProbeVantage",
    "EndpointStatus",
    "EndpointStatusResponse",
    "ErrorCode",
    "ErrorReason",
    "ErrorResponse",
    "ExposureSource",
    "ExternalAccess",
    "ExternalAccessTLS",
    "ExternalAccessType",
    "ExternalDNSAddonConfiguration",
    "ExternalDNSPolicy",
    "ExternalDNSProvider",
    "Failure",
    "GCPConnectRequest",
    "GCPConnectStatus",
    "GCPConnectStatusResponse",
    "GCPCredentialsRequest",
    "GCPTemporaryCredential",
    "GCPTemporaryCredentialResponse",
    "GKEClusterSpec",
    "GKEImageType",
    "GKEReleaseChannel",
    "GKESubnetConfig",
    "GKEUpdateSpec",
    "GPUAttachment",
    "GPUQuotaHeadroom",
    "GPUQuotaState",
    "GPUQuotaUnverifiedReason",
    "GatewayAddonConfiguration",
    "GatewayAutoScalingConfig",
    "GatewayProgrammedState",
    "GatewayScalingMetric",
    "GitHubAccountType",
    "GitHubBranch",
    "GitHubBranchCommit",
    "GitHubBranchListResponse",
    "GitHubContent",
    "GitHubContentListResponse",
    "GitHubContentType",
    "GitHubDetectRequest",
    "GitHubDetectedInstallation",
    "GitHubDetectedInstallations",
    "GitHubDetectedInstallationsResponse",
    "GitHubFileContent",
    "GitHubFileContentResponse",
    "GitHubInstallState",
    "GitHubInstallStateResponse",
    "GitHubInstallation",
    "GitHubInstallationClaimRequest",
    "GitHubInstallationDeleted",
    "GitHubInstallationDeletedResponse",
    "GitHubInstallationListResponse",
    "GitHubInstallationResponse",
    "GitHubInstallationResult",
    "GitHubInstallationResultResponse",
    "GitHubInstallationStatus",
    "GitHubPathType",
    "GitHubPathValidation",
    "GitHubPathValidationRequest",
    "GitHubPathValidationResponse",
    "GitHubRepository",
    "GitHubRepositoryListResponse",
    "GitHubRepositoryTokenRequest",
    "GitHubToken",
    "GitHubTokenResponse",
    "HPA",
    "Helm",
    "HelmRepo",
    "HelmValueType",
    "HuggingFaceIntegration",
    "HuggingFaceIntegrationRequest",
    "HuggingFaceIntegrationResponse",
    "HuggingFaceIntegrationState",
    "Image",
    "ImageScanFinding",
    "InferenceMetrics",
    "InferenceMetricsSummary",
    "InferenceRuntime",
    "InstanceType",
    "K8sCluster",
    "K8sClusterAddonManifest",
    "K8sClusterAddonManifestResponse",
    "K8sClusterAddonManifestSpec",
    "K8sClusterListResponse",
    "K8sClusterManifest",
    "K8sClusterManifestResponse",
    "K8sClusterRegistration",
    "K8sClusterRequest",
    "K8sClusterResponse",
    "K8sClusterSpec",
    "K8sClusterUpdate",
    "K8sUpgradePath",
    "K8sVersionAnalysis",
    "KarpenterAddonConfiguration",
    "KarpenterCapacityReservations",
    "KarpenterConsolidationPolicy",
    "KarpenterDisruption",
    "KarpenterDisruptionBudget",
    "KubeClientAuth",
    "Kubeconfig",
    "KubeconfigAccess",
    "KubeconfigGeneration",
    "KubeconfigGenerationResponse",
    "KubeconfigRequest",
    "KubeconfigResponse",
    "KubeconfigState",
    "LogLevel",
    "MachineType",
    "MachineTypeListResponse",
    "MachineTypeResponse",
    "MaintenanceWindow",
    "MemResources",
    "Member",
    "MetricsDimensions",
    "MetricsSeriesPoint",
    "Model",
    "ModelAPIFormat",
    "ModelAccelerator",
    "ModelCache",
    "ModelCacheBacking",
    "ModelCapacityType",
    "ModelFormat",
    "ModelGPU",
    "ModelMultimodal",
    "ModelPlacement",
    "ModelPlacementInstance",
    "ModelPlacementQuota",
    "ModelQueue",
    "ModelResources",
    "ModelRuntime",
    "ModelRuntimeChoice",
    "ModelScaling",
    "ModelScalingMetric",
    "ModelScalingRule",
    "ModelScalingSignal",
    "ModelScalingTarget",
    "ModelServing",
    "ModelServingAddonConfiguration",
    "ModelServingCacheConfiguration",
    "ModelTask",
    "NetworkTraffic",
    "NextStep",
    "NginxAddonConfiguration",
    "NginxWildcardCertificate",
    "NodeGroup",
    "NodeGroupChangeType",
    "NodeGroupRemoval",
    "NodeGroupState",
    "NodeGroupUpdateStrategy",
    "NodeRole",
    "NodeRoleKind",
    "Notice",
    "NoticeCode",
    "NoticeOperation",
    "NoticeSeverity",
    "NotificationChannelAvailability",
    "NotificationChannelAvailabilityListResponse",
    "NotificationChannelType",
    "NotificationChannelTypeListResponse",
    "NotificationIntegration",
    "NotificationIntegrationConfig",
    "NotificationIntegrationConfigRequest",
    "NotificationIntegrationListResponse",
    "NotificationIntegrationRequest",
    "NotificationIntegrationResponse",
    "NotificationSubscription",
    "NotificationSubscriptionListResponse",
    "NotificationSubscriptionRequest",
    "NotificationSubscriptionResponse",
    "NotificationTopic",
    "NotificationTopicListResponse",
    "ObjectMeta",
    "ObservedNodeGPU",
    "ObservedNodePool",
    "ObservedNodePoolChange",
    "ObservedNodePoolChangeReason",
    "ObservedNodePoolKind",
    "ObservedNodeSet",
    "ObservedNodesUnavailableReason",
    "OperationStatus",
    "OperationType",
    "Operator",
    "OrgFeatureFlags",
    "OrgServiceAccount",
    "OrgServiceAccountListResponse",
    "OrgServiceAccountResponse",
    "Organization",
    "OrganizationListResponse",
    "OrganizationMember",
    "OrganizationMemberResponse",
    "OrganizationMembersPage",
    "OrganizationMembersPageResponse",
    "OrganizationOwnershipTransfer",
    "OrganizationOwnershipTransferResponse",
    "OrganizationRequest",
    "OrganizationResponse",
    "OrganizationRole",
    "Outcome",
    "Pagination",
    "PaginationResponse",
    "Permission",
    "PlanId",
    "PreflightCategory",
    "PreflightCheck",
    "PreflightReasonCode",
    "PreflightStatus",
    "PricingCategory",
    "PricingCta",
    "PricingData",
    "PricingDataResponse",
    "PricingFeature",
    "PricingFeatureValue",
    "PricingPlan",
    "PricingPlanListResponse",
    "PricingPrice",
    "PriorityClassType",
    "ProgressEvent",
    "ProgressEventLevel",
    "Provider",
    "ProviderListResponse",
    "ProviderProvisioners",
    "ProviderProvisionersListResponse",
    "Provisioner",
    "ProvisionerInfo",
    "ProvisionerType",
    "Quantity",
    "QueueMetrics",
    "QueueMetricsSummary",
    "ReadinessReportSection",
    "RegisterClusterRequest",
    "RegistrationInstructions",
    "RemoveUserFromOrganizationRequest",
    "Repo",
    "Repository",
    "ResolvedNodeGroup",
    "ResourceCapacityCheck",
    "ResourceMinMax",
    "ResourceRequirement",
    "ResourceRequirements",
    "RevokeAPIKeyRequest",
    "Role",
    "RoleListResponse",
    "RollbackClusterAddonRequest",
    "RollingUpdateStrategy",
    "ScanFindingOwner",
    "ScanFindingOwnerType",
    "ScanFindingsNoResult",
    "ScanFindingsNoResultReason",
    "ScanFindingsSeverityCounts",
    "ScanFindingsUnscannedImages",
    "ScanScopeMode",
    "SelfHostedConnectRequest",
    "SelfHostedConnectStep",
    "SelfHostedConnection",
    "SelfHostedConnectionResponse",
    "SelfHostedCredentialRevocation",
    "SelfHostedCredentialRevocationResponse",
    "SelfHostedCredentialState",
    "SelfHostedCredentialStatus",
    "SelfHostedCredentialStatusResponse",
    "SelfHostedSetup",
    "SelfHostedSetupRequest",
    "SelfHostedSetupResponse",
    "SelfHostedSetupState",
    "SelfHostedSpec",
    "SelfHostedTemplate",
    "SelfHostedTemplateResponse",
    "SelfHostedUpdateSpec",
    "ServiceAccountKeyCreated",
    "ServiceAccountKeyCreatedResponse",
    "ServiceAccountKeyRequest",
    "ServiceAccountRequest",
    "SetClusterStorageRequest",
    "SetOrganizationMemberRoleRequest",
    "SettingFormat",
    "SettingOptions",
    "SettingValueRequirement",
    "SetupStep",
    "SetupStepState",
    "ShellCommand",
    "SlackConfigType",
    "SortOrder",
    "SourceIdentity",
    "SourceType",
    "StateTone",
    "StorageBindingState",
    "StorageKind",
    "StorageObserver",
    "StreamTicket",
    "StringListResponse",
    "StringResponse",
    "SubnetSpec",
    "SubnetType",
    "SupportedK8sVersionsResponse",
    "SupportedK8sVersionsResponseEnvelope",
    "SwitchOrgRequest",
    "SyncType",
    "TLSMode",
    "TaintEffect",
    "Tainted",
    "TemplateFormat",
    "TierConfig",
    "TierConfigResponse",
    "TierType",
    "TimelineEvent",
    "TimelineEventKind",
    "TransferOrganizationOwnershipRequest",
    "UnsubscribeFromNotificationsRequest",
    "UpdateClusterAddonRequest",
    "UpdateClusterSpec",
    "UpdateConfig",
    "UpdateNodeGroup",
    "UpgradeKind",
    "UpgradePlan",
    "UpgradePlanNodePool",
    "UpgradePlanNodePoolState",
    "UpgradePlanPhase",
    "UpgradeReadinessReport",
    "UpgradeRiskLevel",
    "UserEventCount",
    "UserProfile",
    "UserProfileResponse",
    "VPA",
    "ValidationIssue",
    "Values",
    "VaultLease",
    "VaultLeaseKind",
    "VaultLeaseList",
    "VaultLeaseListResponse",
    "VaultLeaseReplaceRequest",
    "VaultLeaseResponse",
    "VaultLeaseScope",
    "VaultLeaseState",
    "VaultRevocation",
    "VaultRevocationCallback",
    "VaultRevocationOutcome",
    "VaultRevocationResponse",
    "VaultValidation",
    "VaultValidationResult",
    "VersionFloorSource",
    "VulnerabilityFinding",
    "VulnerabilityFindingDetail",
    "VulnerabilityFindingDetailResponse",
    "VulnerabilityScanningAddonConfiguration",
    "VulnerabilityScanningScanResources",
    "VulnerabilityScanningScanScope",
    "VulnerabilitySeverity",
    "WorkloadAutoscalingAddonConfiguration",
    "WorkloadClusterQueue",
    "WorkloadIdentityCloud",
    "WorkloadIdentityStatus",
    "WorkloadImpactAnalysis",
    "WorkloadKind",
    "WorkloadLocalQueue",
    "WorkloadQueuePreemption",
    "WorkloadQueueQuota",
    "WorkloadQueueingAddonConfiguration",
    "WorkloadQueueingGangScheduling",
    "WorkloadQueueingIntegration",
    "WorkloadScanFinding",
    "YAML",
]

# import apis into sdk package
from astropulse._generated.api.api_document_api import APIDocumentApi as APIDocumentApi
from astropulse._generated.api.api_keys_api import APIKeysApi as APIKeysApi
from astropulse._generated.api.access_policies_api import AccessPoliciesApi as AccessPoliciesApi
from astropulse._generated.api.application_profiles_api import ApplicationProfilesApi as ApplicationProfilesApi
from astropulse._generated.api.applications_api import ApplicationsApi as ApplicationsApi
from astropulse._generated.api.audit_api import AuditApi as AuditApi
from astropulse._generated.api.availability_tiers_api import AvailabilityTiersApi as AvailabilityTiersApi
from astropulse._generated.api.cloud_accounts_api import CloudAccountsApi as CloudAccountsApi
from astropulse._generated.api.cloud_catalog_api import CloudCatalogApi as CloudCatalogApi
from astropulse._generated.api.cluster_add_ons_api import ClusterAddOnsApi as ClusterAddOnsApi
from astropulse._generated.api.clusters_api import ClustersApi as ClustersApi
from astropulse._generated.api.domains_api import DomainsApi as DomainsApi
from astropulse._generated.api.integrations_api import IntegrationsApi as IntegrationsApi
from astropulse._generated.api.notifications_api import NotificationsApi as NotificationsApi
from astropulse._generated.api.organizations_api import OrganizationsApi as OrganizationsApi
from astropulse._generated.api.pricing_api import PricingApi as PricingApi
from astropulse._generated.api.service_accounts_api import ServiceAccountsApi as ServiceAccountsApi
from astropulse._generated.api.users_api import UsersApi as UsersApi

# import ApiClient
from astropulse._generated.api_response import ApiResponse as ApiResponse
from astropulse._generated.api_client import ApiClient as ApiClient
from astropulse._generated.configuration import Configuration as Configuration
from astropulse._generated.exceptions import OpenApiException as OpenApiException
from astropulse._generated.exceptions import ApiTypeError as ApiTypeError
from astropulse._generated.exceptions import ApiValueError as ApiValueError
from astropulse._generated.exceptions import ApiKeyError as ApiKeyError
from astropulse._generated.exceptions import ApiAttributeError as ApiAttributeError
from astropulse._generated.exceptions import ApiException as ApiException

# import models into sdk package
from astropulse._generated.models.aks_auto_upgrade_channel import AKSAutoUpgradeChannel as AKSAutoUpgradeChannel
from astropulse._generated.models.aks_cluster_spec import AKSClusterSpec as AKSClusterSpec
from astropulse._generated.models.aks_network_plugin import AKSNetworkPlugin as AKSNetworkPlugin
from astropulse._generated.models.aks_network_plugin_mode import AKSNetworkPluginMode as AKSNetworkPluginMode
from astropulse._generated.models.aks_node_os_upgrade_channel import AKSNodeOSUpgradeChannel as AKSNodeOSUpgradeChannel
from astropulse._generated.models.aks_update_spec import AKSUpdateSpec as AKSUpdateSpec
from astropulse._generated.models.ami_families_for_version import AMIFamiliesForVersion as AMIFamiliesForVersion
from astropulse._generated.models.ami_family import AMIFamily as AMIFamily
from astropulse._generated.models.ami_family_offer import AMIFamilyOffer as AMIFamilyOffer
from astropulse._generated.models.api_key_created import APIKeyCreated as APIKeyCreated
from astropulse._generated.models.api_key_created_response import APIKeyCreatedResponse as APIKeyCreatedResponse
from astropulse._generated.models.api_key_expiration import APIKeyExpiration as APIKeyExpiration
from astropulse._generated.models.api_key_feature_flags import APIKeyFeatureFlags as APIKeyFeatureFlags
from astropulse._generated.models.api_key_lifecycle_status import APIKeyLifecycleStatus as APIKeyLifecycleStatus
from astropulse._generated.models.api_key_list_response import APIKeyListResponse as APIKeyListResponse
from astropulse._generated.models.api_key_metadata import APIKeyMetadata as APIKeyMetadata
from astropulse._generated.models.api_key_request import APIKeyRequest as APIKeyRequest
from astropulse._generated.models.api_key_response import APIKeyResponse as APIKeyResponse
from astropulse._generated.models.api_key_service_account import APIKeyServiceAccount as APIKeyServiceAccount
from astropulse._generated.models.api_key_source import APIKeySource as APIKeySource
from astropulse._generated.models.api_key_summary import APIKeySummary as APIKeySummary
from astropulse._generated.models.api_key_summary_response import APIKeySummaryResponse as APIKeySummaryResponse
from astropulse._generated.models.api_key_validation import APIKeyValidation as APIKeyValidation
from astropulse._generated.models.api_key_validation_response import APIKeyValidationResponse as APIKeyValidationResponse
from astropulse._generated.models.aws_addon_config import AWSAddonConfig as AWSAddonConfig
from astropulse._generated.models.aws_connect_request import AWSConnectRequest as AWSConnectRequest
from astropulse._generated.models.aws_connect_status import AWSConnectStatus as AWSConnectStatus
from astropulse._generated.models.aws_connect_status_response import AWSConnectStatusResponse as AWSConnectStatusResponse
from astropulse._generated.models.aws_credentials_request import AWSCredentialsRequest as AWSCredentialsRequest
from astropulse._generated.models.aws_temporary_credential import AWSTemporaryCredential as AWSTemporaryCredential
from astropulse._generated.models.aws_temporary_credential_response import AWSTemporaryCredentialResponse as AWSTemporaryCredentialResponse
from astropulse._generated.models.accelerator import Accelerator as Accelerator
from astropulse._generated.models.accelerator_attachment import AcceleratorAttachment as AcceleratorAttachment
from astropulse._generated.models.accelerator_kind import AcceleratorKind as AcceleratorKind
from astropulse._generated.models.accelerator_metrics import AcceleratorMetrics as AcceleratorMetrics
from astropulse._generated.models.accelerator_metrics_summary import AcceleratorMetricsSummary as AcceleratorMetricsSummary
from astropulse._generated.models.accelerator_offer import AcceleratorOffer as AcceleratorOffer
from astropulse._generated.models.accelerator_offer_availability import AcceleratorOfferAvailability as AcceleratorOfferAvailability
from astropulse._generated.models.accelerator_offer_instance import AcceleratorOfferInstance as AcceleratorOfferInstance
from astropulse._generated.models.accelerator_offer_quota import AcceleratorOfferQuota as AcceleratorOfferQuota
from astropulse._generated.models.accelerator_offer_reason_code import AcceleratorOfferReasonCode as AcceleratorOfferReasonCode
from astropulse._generated.models.accelerator_offer_source import AcceleratorOfferSource as AcceleratorOfferSource
from astropulse._generated.models.accelerator_offering import AcceleratorOffering as AcceleratorOffering
from astropulse._generated.models.accelerator_offering_list_response import AcceleratorOfferingListResponse as AcceleratorOfferingListResponse
from astropulse._generated.models.accelerator_offers_incomplete_reason import AcceleratorOffersIncompleteReason as AcceleratorOffersIncompleteReason
from astropulse._generated.models.accelerator_offers_unavailable_reason import AcceleratorOffersUnavailableReason as AcceleratorOffersUnavailableReason
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor as AcceleratorVendor
from astropulse._generated.models.access_policy import AccessPolicy as AccessPolicy
from astropulse._generated.models.access_policy_api_keys import AccessPolicyAPIKeys as AccessPolicyAPIKeys
from astropulse._generated.models.access_policy_claim import AccessPolicyClaim as AccessPolicyClaim
from astropulse._generated.models.access_policy_claim_type import AccessPolicyClaimType as AccessPolicyClaimType
from astropulse._generated.models.access_policy_identity import AccessPolicyIdentity as AccessPolicyIdentity
from astropulse._generated.models.access_policy_jwt import AccessPolicyJWT as AccessPolicyJWT
from astropulse._generated.models.access_policy_key import AccessPolicyKey as AccessPolicyKey
from astropulse._generated.models.access_policy_key_created import AccessPolicyKeyCreated as AccessPolicyKeyCreated
from astropulse._generated.models.access_policy_key_created_response import AccessPolicyKeyCreatedResponse as AccessPolicyKeyCreatedResponse
from astropulse._generated.models.access_policy_key_list_response import AccessPolicyKeyListResponse as AccessPolicyKeyListResponse
from astropulse._generated.models.access_policy_key_request import AccessPolicyKeyRequest as AccessPolicyKeyRequest
from astropulse._generated.models.access_policy_list_response import AccessPolicyListResponse as AccessPolicyListResponse
from astropulse._generated.models.access_policy_response import AccessPolicyResponse as AccessPolicyResponse
from astropulse._generated.models.access_policy_secret_ref import AccessPolicySecretRef as AccessPolicySecretRef
from astropulse._generated.models.access_policy_spec import AccessPolicySpec as AccessPolicySpec
from astropulse._generated.models.access_policy_token_rejection import AccessPolicyTokenRejection as AccessPolicyTokenRejection
from astropulse._generated.models.access_policy_token_result import AccessPolicyTokenResult as AccessPolicyTokenResult
from astropulse._generated.models.access_policy_token_result_response import AccessPolicyTokenResultResponse as AccessPolicyTokenResultResponse
from astropulse._generated.models.access_policy_token_test import AccessPolicyTokenTest as AccessPolicyTokenTest
from astropulse._generated.models.account_setup import AccountSetup as AccountSetup
from astropulse._generated.models.add_user_to_organization_request import AddUserToOrganizationRequest as AddUserToOrganizationRequest
from astropulse._generated.models.addon_auto_scaling_config import AddonAutoScalingConfig as AddonAutoScalingConfig
from astropulse._generated.models.addon_availability import AddonAvailability as AddonAvailability
from astropulse._generated.models.addon_cloud_access import AddonCloudAccess as AddonCloudAccess
from astropulse._generated.models.addon_component_sizing import AddonComponentSizing as AddonComponentSizing
from astropulse._generated.models.addon_configuration_field import AddonConfigurationField as AddonConfigurationField
from astropulse._generated.models.addon_configuration_format import AddonConfigurationFormat as AddonConfigurationFormat
from astropulse._generated.models.addon_field_condition import AddonFieldCondition as AddonFieldCondition
from astropulse._generated.models.addon_field_type import AddonFieldType as AddonFieldType
from astropulse._generated.models.addon_resource_requirements import AddonResourceRequirements as AddonResourceRequirements
from astropulse._generated.models.addon_resources import AddonResources as AddonResources
from astropulse._generated.models.addon_service_account import AddonServiceAccount as AddonServiceAccount
from astropulse._generated.models.addon_unavailable_value import AddonUnavailableValue as AddonUnavailableValue
from astropulse._generated.models.addon_workload_identity import AddonWorkloadIdentity as AddonWorkloadIdentity
from astropulse._generated.models.affinity_type import AffinityType as AffinityType
from astropulse._generated.models.agent_capability_state import AgentCapabilityState as AgentCapabilityState
from astropulse._generated.models.agent_capability_status import AgentCapabilityStatus as AgentCapabilityStatus
from astropulse._generated.models.agent_certificate_bundle import AgentCertificateBundle as AgentCertificateBundle
from astropulse._generated.models.agent_certificate_bundle_response import AgentCertificateBundleResponse as AgentCertificateBundleResponse
from astropulse._generated.models.agent_certificate_signing_request import AgentCertificateSigningRequest as AgentCertificateSigningRequest
from astropulse._generated.models.agent_certificate_state import AgentCertificateState as AgentCertificateState
from astropulse._generated.models.agent_certificate_status import AgentCertificateStatus as AgentCertificateStatus
from astropulse._generated.models.app_resource import AppResource as AppResource
from astropulse._generated.models.application import Application as Application
from astropulse._generated.models.application_container_termination import ApplicationContainerTermination as ApplicationContainerTermination
from astropulse._generated.models.application_cost_summary import ApplicationCostSummary as ApplicationCostSummary
from astropulse._generated.models.application_cost_summary_response import ApplicationCostSummaryResponse as ApplicationCostSummaryResponse
from astropulse._generated.models.application_deployment import ApplicationDeployment as ApplicationDeployment
from astropulse._generated.models.application_deployment_response import ApplicationDeploymentResponse as ApplicationDeploymentResponse
from astropulse._generated.models.application_history import ApplicationHistory as ApplicationHistory
from astropulse._generated.models.application_history_response import ApplicationHistoryResponse as ApplicationHistoryResponse
from astropulse._generated.models.application_list_response import ApplicationListResponse as ApplicationListResponse
from astropulse._generated.models.application_manifest import ApplicationManifest as ApplicationManifest
from astropulse._generated.models.application_metrics_allocation_item import ApplicationMetricsAllocationItem as ApplicationMetricsAllocationItem
from astropulse._generated.models.application_metrics_series import ApplicationMetricsSeries as ApplicationMetricsSeries
from astropulse._generated.models.application_metrics_series_response import ApplicationMetricsSeriesResponse as ApplicationMetricsSeriesResponse
from astropulse._generated.models.application_model_status import ApplicationModelStatus as ApplicationModelStatus
from astropulse._generated.models.application_operation import ApplicationOperation as ApplicationOperation
from astropulse._generated.models.application_operation_response import ApplicationOperationResponse as ApplicationOperationResponse
from astropulse._generated.models.application_profile import ApplicationProfile as ApplicationProfile
from astropulse._generated.models.application_profile_bulk_delete_request import ApplicationProfileBulkDeleteRequest as ApplicationProfileBulkDeleteRequest
from astropulse._generated.models.application_profile_list_response import ApplicationProfileListResponse as ApplicationProfileListResponse
from astropulse._generated.models.application_profile_manifest import ApplicationProfileManifest as ApplicationProfileManifest
from astropulse._generated.models.application_profile_request import ApplicationProfileRequest as ApplicationProfileRequest
from astropulse._generated.models.application_profile_response import ApplicationProfileResponse as ApplicationProfileResponse
from astropulse._generated.models.application_request import ApplicationRequest as ApplicationRequest
from astropulse._generated.models.application_request_response import ApplicationRequestResponse as ApplicationRequestResponse
from astropulse._generated.models.application_response import ApplicationResponse as ApplicationResponse
from astropulse._generated.models.application_resume_plan import ApplicationResumePlan as ApplicationResumePlan
from astropulse._generated.models.application_resume_plan_response import ApplicationResumePlanResponse as ApplicationResumePlanResponse
from astropulse._generated.models.application_resync import ApplicationResync as ApplicationResync
from astropulse._generated.models.application_resync_request import ApplicationResyncRequest as ApplicationResyncRequest
from astropulse._generated.models.application_resync_response import ApplicationResyncResponse as ApplicationResyncResponse
from astropulse._generated.models.application_resync_status import ApplicationResyncStatus as ApplicationResyncStatus
from astropulse._generated.models.application_rollback_plan import ApplicationRollbackPlan as ApplicationRollbackPlan
from astropulse._generated.models.application_rollback_plan_response import ApplicationRollbackPlanResponse as ApplicationRollbackPlanResponse
from astropulse._generated.models.application_rollback_request import ApplicationRollbackRequest as ApplicationRollbackRequest
from astropulse._generated.models.application_rollback_state import ApplicationRollbackState as ApplicationRollbackState
from astropulse._generated.models.application_source import ApplicationSource as ApplicationSource
from astropulse._generated.models.application_status import ApplicationStatus as ApplicationStatus
from astropulse._generated.models.application_version_entry import ApplicationVersionEntry as ApplicationVersionEntry
from astropulse._generated.models.application_version_state import ApplicationVersionState as ApplicationVersionState
from astropulse._generated.models.apply_dry_run_action import ApplyDryRunAction as ApplyDryRunAction
from astropulse._generated.models.apply_dry_run_result import ApplyDryRunResult as ApplyDryRunResult
from astropulse._generated.models.apply_dry_run_result_response import ApplyDryRunResultResponse as ApplyDryRunResultResponse
from astropulse._generated.models.architecture_type import ArchitectureType as ArchitectureType
from astropulse._generated.models.attempt_status import AttemptStatus as AttemptStatus
from astropulse._generated.models.attempt_status_info import AttemptStatusInfo as AttemptStatusInfo
from astropulse._generated.models.audit_action import AuditAction as AuditAction
from astropulse._generated.models.audit_actor_type import AuditActorType as AuditActorType
from astropulse._generated.models.audit_event import AuditEvent as AuditEvent
from astropulse._generated.models.audit_event_list import AuditEventList as AuditEventList
from astropulse._generated.models.audit_event_list_response import AuditEventListResponse as AuditEventListResponse
from astropulse._generated.models.audit_event_response import AuditEventResponse as AuditEventResponse
from astropulse._generated.models.audit_event_type import AuditEventType as AuditEventType
from astropulse._generated.models.audit_export_format import AuditExportFormat as AuditExportFormat
from astropulse._generated.models.audit_source import AuditSource as AuditSource
from astropulse._generated.models.audit_stats import AuditStats as AuditStats
from astropulse._generated.models.audit_stats_response import AuditStatsResponse as AuditStatsResponse
from astropulse._generated.models.autoscaling_metrics_source import AutoscalingMetricsSource as AutoscalingMetricsSource
from astropulse._generated.models.autoscaling_prometheus_source import AutoscalingPrometheusSource as AutoscalingPrometheusSource
from astropulse._generated.models.availability_tier import AvailabilityTier as AvailabilityTier
from astropulse._generated.models.azure_connect_request import AzureConnectRequest as AzureConnectRequest
from astropulse._generated.models.azure_connect_status import AzureConnectStatus as AzureConnectStatus
from astropulse._generated.models.azure_connect_status_response import AzureConnectStatusResponse as AzureConnectStatusResponse
from astropulse._generated.models.azure_temporary_credential import AzureTemporaryCredential as AzureTemporaryCredential
from astropulse._generated.models.azure_temporary_credential_response import AzureTemporaryCredentialResponse as AzureTemporaryCredentialResponse
from astropulse._generated.models.boolean_response import BooleanResponse as BooleanResponse
from astropulse._generated.models.cpu_architecture import CPUArchitecture as CPUArchitecture
from astropulse._generated.models.cpu_resources import CPUResources as CPUResources
from astropulse._generated.models.cancel_cleanup_item import CancelCleanupItem as CancelCleanupItem
from astropulse._generated.models.cancel_cleanup_kind import CancelCleanupKind as CancelCleanupKind
from astropulse._generated.models.cancel_cleanup_outcome import CancelCleanupOutcome as CancelCleanupOutcome
from astropulse._generated.models.cancel_cluster_operation_request import CancelClusterOperationRequest as CancelClusterOperationRequest
from astropulse._generated.models.capacity_block_phase import CapacityBlockPhase as CapacityBlockPhase
from astropulse._generated.models.capacity_block_status import CapacityBlockStatus as CapacityBlockStatus
from astropulse._generated.models.capacity_reservation import CapacityReservation as CapacityReservation
from astropulse._generated.models.capacity_reservation_kind import CapacityReservationKind as CapacityReservationKind
from astropulse._generated.models.capacity_reservation_list_response import CapacityReservationListResponse as CapacityReservationListResponse
from astropulse._generated.models.cert_manager_addon_configuration import CertManagerAddonConfiguration as CertManagerAddonConfiguration
from astropulse._generated.models.cert_manager_dns_provider import CertManagerDNSProvider as CertManagerDNSProvider
from astropulse._generated.models.cert_manager_dns_solver import CertManagerDNSSolver as CertManagerDNSSolver
from astropulse._generated.models.cert_manager_issuer_type import CertManagerIssuerType as CertManagerIssuerType
from astropulse._generated.models.channel_versions import ChannelVersions as ChannelVersions
from astropulse._generated.models.cloud_access_mode import CloudAccessMode as CloudAccessMode
from astropulse._generated.models.cloud_account import CloudAccount as CloudAccount
from astropulse._generated.models.cloud_account_cluster import CloudAccountCluster as CloudAccountCluster
from astropulse._generated.models.cloud_account_list_response import CloudAccountListResponse as CloudAccountListResponse
from astropulse._generated.models.cloud_account_pending_connection import CloudAccountPendingConnection as CloudAccountPendingConnection
from astropulse._generated.models.cloud_account_state import CloudAccountState as CloudAccountState
from astropulse._generated.models.cloud_account_status import CloudAccountStatus as CloudAccountStatus
from astropulse._generated.models.cloud_connect_attempt_error import CloudConnectAttemptError as CloudConnectAttemptError
from astropulse._generated.models.cloud_connect_failure_reason import CloudConnectFailureReason as CloudConnectFailureReason
from astropulse._generated.models.cloud_connection import CloudConnection as CloudConnection
from astropulse._generated.models.cloud_connection_list_response import CloudConnectionListResponse as CloudConnectionListResponse
from astropulse._generated.models.cloud_connection_response import CloudConnectionResponse as CloudConnectionResponse
from astropulse._generated.models.cloud_connection_state import CloudConnectionState as CloudConnectionState
from astropulse._generated.models.cloud_provider import CloudProvider as CloudProvider
from astropulse._generated.models.cloud_provider_config import CloudProviderConfig as CloudProviderConfig
from astropulse._generated.models.cloud_provider_name import CloudProviderName as CloudProviderName
from astropulse._generated.models.cluster import Cluster as Cluster
from astropulse._generated.models.cluster_accelerators import ClusterAccelerators as ClusterAccelerators
from astropulse._generated.models.cluster_accelerators_response import ClusterAcceleratorsResponse as ClusterAcceleratorsResponse
from astropulse._generated.models.cluster_access_token import ClusterAccessToken as ClusterAccessToken
from astropulse._generated.models.cluster_access_token_response import ClusterAccessTokenResponse as ClusterAccessTokenResponse
from astropulse._generated.models.cluster_addon import ClusterAddon as ClusterAddon
from astropulse._generated.models.cluster_addon_accelerator_readiness import ClusterAddonAcceleratorReadiness as ClusterAddonAcceleratorReadiness
from astropulse._generated.models.cluster_addon_apply_options import ClusterAddonApplyOptions as ClusterAddonApplyOptions
from astropulse._generated.models.cluster_addon_catalog_entry import ClusterAddonCatalogEntry as ClusterAddonCatalogEntry
from astropulse._generated.models.cluster_addon_catalog_entry_list_response import ClusterAddonCatalogEntryListResponse as ClusterAddonCatalogEntryListResponse
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration as ClusterAddonConfiguration
from astropulse._generated.models.cluster_addon_cost_pricing import ClusterAddonCostPricing as ClusterAddonCostPricing
from astropulse._generated.models.cluster_addon_cost_series import ClusterAddonCostSeries as ClusterAddonCostSeries
from astropulse._generated.models.cluster_addon_cost_series_response import ClusterAddonCostSeriesResponse as ClusterAddonCostSeriesResponse
from astropulse._generated.models.cluster_addon_cost_summary import ClusterAddonCostSummary as ClusterAddonCostSummary
from astropulse._generated.models.cluster_addon_cost_summary_response import ClusterAddonCostSummaryResponse as ClusterAddonCostSummaryResponse
from astropulse._generated.models.cluster_addon_deployment_options import ClusterAddonDeploymentOptions as ClusterAddonDeploymentOptions
from astropulse._generated.models.cluster_addon_exposure import ClusterAddonExposure as ClusterAddonExposure
from astropulse._generated.models.cluster_addon_health import ClusterAddonHealth as ClusterAddonHealth
from astropulse._generated.models.cluster_addon_health_check import ClusterAddonHealthCheck as ClusterAddonHealthCheck
from astropulse._generated.models.cluster_addon_history_entry import ClusterAddonHistoryEntry as ClusterAddonHistoryEntry
from astropulse._generated.models.cluster_addon_history_response import ClusterAddonHistoryResponse as ClusterAddonHistoryResponse
from astropulse._generated.models.cluster_addon_history_response_envelope import ClusterAddonHistoryResponseEnvelope as ClusterAddonHistoryResponseEnvelope
from astropulse._generated.models.cluster_addon_ingress_tls import ClusterAddonIngressTLS as ClusterAddonIngressTLS
from astropulse._generated.models.cluster_addon_list_response import ClusterAddonListResponse as ClusterAddonListResponse
from astropulse._generated.models.cluster_addon_metrics_series import ClusterAddonMetricsSeries as ClusterAddonMetricsSeries
from astropulse._generated.models.cluster_addon_metrics_series_response import ClusterAddonMetricsSeriesResponse as ClusterAddonMetricsSeriesResponse
from astropulse._generated.models.cluster_addon_model_cache_node_group import ClusterAddonModelCacheNodeGroup as ClusterAddonModelCacheNodeGroup
from astropulse._generated.models.cluster_addon_model_cache_readiness import ClusterAddonModelCacheReadiness as ClusterAddonModelCacheReadiness
from astropulse._generated.models.cluster_addon_node_address import ClusterAddonNodeAddress as ClusterAddonNodeAddress
from astropulse._generated.models.cluster_addon_operation import ClusterAddonOperation as ClusterAddonOperation
from astropulse._generated.models.cluster_addon_operation_metadata import ClusterAddonOperationMetadata as ClusterAddonOperationMetadata
from astropulse._generated.models.cluster_addon_operation_response import ClusterAddonOperationResponse as ClusterAddonOperationResponse
from astropulse._generated.models.cluster_addon_queue_namespaces import ClusterAddonQueueNamespaces as ClusterAddonQueueNamespaces
from astropulse._generated.models.cluster_addon_resilience import ClusterAddonResilience as ClusterAddonResilience
from astropulse._generated.models.cluster_addon_response import ClusterAddonResponse as ClusterAddonResponse
from astropulse._generated.models.cluster_addon_resync_response import ClusterAddonResyncResponse as ClusterAddonResyncResponse
from astropulse._generated.models.cluster_addon_resync_response_envelope import ClusterAddonResyncResponseEnvelope as ClusterAddonResyncResponseEnvelope
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus as ClusterAddonStatus
from astropulse._generated.models.cluster_addon_summary import ClusterAddonSummary as ClusterAddonSummary
from astropulse._generated.models.cluster_addon_support import ClusterAddonSupport as ClusterAddonSupport
from astropulse._generated.models.cluster_addon_support_status import ClusterAddonSupportStatus as ClusterAddonSupportStatus
from astropulse._generated.models.cluster_addon_tls_challenge import ClusterAddonTLSChallenge as ClusterAddonTLSChallenge
from astropulse._generated.models.cluster_addon_tls_challenges import ClusterAddonTLSChallenges as ClusterAddonTLSChallenges
from astropulse._generated.models.cluster_addon_tls_exposure import ClusterAddonTLSExposure as ClusterAddonTLSExposure
from astropulse._generated.models.cluster_addon_tls_issuer import ClusterAddonTLSIssuer as ClusterAddonTLSIssuer
from astropulse._generated.models.cluster_addon_tls_mode import ClusterAddonTLSMode as ClusterAddonTLSMode
from astropulse._generated.models.cluster_addon_tls_readiness import ClusterAddonTLSReadiness as ClusterAddonTLSReadiness
from astropulse._generated.models.cluster_addon_type import ClusterAddonType as ClusterAddonType
from astropulse._generated.models.cluster_addon_update_options import ClusterAddonUpdateOptions as ClusterAddonUpdateOptions
from astropulse._generated.models.cluster_addon_update_strategy import ClusterAddonUpdateStrategy as ClusterAddonUpdateStrategy
from astropulse._generated.models.cluster_addon_version import ClusterAddonVersion as ClusterAddonVersion
from astropulse._generated.models.cluster_addon_version_list_response import ClusterAddonVersionListResponse as ClusterAddonVersionListResponse
from astropulse._generated.models.cluster_application import ClusterApplication as ClusterApplication
from astropulse._generated.models.cluster_approval import ClusterApproval as ClusterApproval
from astropulse._generated.models.cluster_approval_action import ClusterApprovalAction as ClusterApprovalAction
from astropulse._generated.models.cluster_approval_outcome import ClusterApprovalOutcome as ClusterApprovalOutcome
from astropulse._generated.models.cluster_approval_response import ClusterApprovalResponse as ClusterApprovalResponse
from astropulse._generated.models.cluster_cancellation import ClusterCancellation as ClusterCancellation
from astropulse._generated.models.cluster_cancellation_status import ClusterCancellationStatus as ClusterCancellationStatus
from astropulse._generated.models.cluster_cloud_identity import ClusterCloudIdentity as ClusterCloudIdentity
from astropulse._generated.models.cluster_compute_mode import ClusterComputeMode as ClusterComputeMode
from astropulse._generated.models.cluster_connectivity import ClusterConnectivity as ClusterConnectivity
from astropulse._generated.models.cluster_cost_allocation import ClusterCostAllocation as ClusterCostAllocation
from astropulse._generated.models.cluster_cost_allocation_response import ClusterCostAllocationResponse as ClusterCostAllocationResponse
from astropulse._generated.models.cluster_cost_series import ClusterCostSeries as ClusterCostSeries
from astropulse._generated.models.cluster_cost_series_response import ClusterCostSeriesResponse as ClusterCostSeriesResponse
from astropulse._generated.models.cluster_cost_summary import ClusterCostSummary as ClusterCostSummary
from astropulse._generated.models.cluster_cost_summary_response import ClusterCostSummaryResponse as ClusterCostSummaryResponse
from astropulse._generated.models.cluster_creation import ClusterCreation as ClusterCreation
from astropulse._generated.models.cluster_creation_response import ClusterCreationResponse as ClusterCreationResponse
from astropulse._generated.models.cluster_delete_dry_run import ClusterDeleteDryRun as ClusterDeleteDryRun
from astropulse._generated.models.cluster_delete_group import ClusterDeleteGroup as ClusterDeleteGroup
from astropulse._generated.models.cluster_delete_group_kind import ClusterDeleteGroupKind as ClusterDeleteGroupKind
from astropulse._generated.models.cluster_delete_item import ClusterDeleteItem as ClusterDeleteItem
from astropulse._generated.models.cluster_delete_outcome import ClusterDeleteOutcome as ClusterDeleteOutcome
from astropulse._generated.models.cluster_deletion import ClusterDeletion as ClusterDeletion
from astropulse._generated.models.cluster_deletion_response import ClusterDeletionResponse as ClusterDeletionResponse
from astropulse._generated.models.cluster_dry_run import ClusterDryRun as ClusterDryRun
from astropulse._generated.models.cluster_dry_run_response import ClusterDryRunResponse as ClusterDryRunResponse
from astropulse._generated.models.cluster_exposure import ClusterExposure as ClusterExposure
from astropulse._generated.models.cluster_exposure_brick import ClusterExposureBrick as ClusterExposureBrick
from astropulse._generated.models.cluster_exposure_certificates import ClusterExposureCertificates as ClusterExposureCertificates
from astropulse._generated.models.cluster_exposure_issuer import ClusterExposureIssuer as ClusterExposureIssuer
from astropulse._generated.models.cluster_exposure_owner import ClusterExposureOwner as ClusterExposureOwner
from astropulse._generated.models.cluster_exposure_response import ClusterExposureResponse as ClusterExposureResponse
from astropulse._generated.models.cluster_exposure_settings import ClusterExposureSettings as ClusterExposureSettings
from astropulse._generated.models.cluster_group import ClusterGroup as ClusterGroup
from astropulse._generated.models.cluster_health_check import ClusterHealthCheck as ClusterHealthCheck
from astropulse._generated.models.cluster_infrastructure_charge import ClusterInfrastructureCharge as ClusterInfrastructureCharge
from astropulse._generated.models.cluster_infrastructure_estimate import ClusterInfrastructureEstimate as ClusterInfrastructureEstimate
from astropulse._generated.models.cluster_infrastructure_estimate_response import ClusterInfrastructureEstimateResponse as ClusterInfrastructureEstimateResponse
from astropulse._generated.models.cluster_infrastructure_item import ClusterInfrastructureItem as ClusterInfrastructureItem
from astropulse._generated.models.cluster_infrastructure_unpriced import ClusterInfrastructureUnpriced as ClusterInfrastructureUnpriced
from astropulse._generated.models.cluster_issuer_kind import ClusterIssuerKind as ClusterIssuerKind
from astropulse._generated.models.cluster_load_balancer_exposure import ClusterLoadBalancerExposure as ClusterLoadBalancerExposure
from astropulse._generated.models.cluster_metrics_allocation import ClusterMetricsAllocation as ClusterMetricsAllocation
from astropulse._generated.models.cluster_metrics_allocation_response import ClusterMetricsAllocationResponse as ClusterMetricsAllocationResponse
from astropulse._generated.models.cluster_metrics_sort_field import ClusterMetricsSortField as ClusterMetricsSortField
from astropulse._generated.models.cluster_metrics_summary import ClusterMetricsSummary as ClusterMetricsSummary
from astropulse._generated.models.cluster_metrics_summary_response import ClusterMetricsSummaryResponse as ClusterMetricsSummaryResponse
from astropulse._generated.models.cluster_observed_nodes import ClusterObservedNodes as ClusterObservedNodes
from astropulse._generated.models.cluster_operation import ClusterOperation as ClusterOperation
from astropulse._generated.models.cluster_operation_kind import ClusterOperationKind as ClusterOperationKind
from astropulse._generated.models.cluster_operation_result import ClusterOperationResult as ClusterOperationResult
from astropulse._generated.models.cluster_operation_result_response import ClusterOperationResultResponse as ClusterOperationResultResponse
from astropulse._generated.models.cluster_operation_step import ClusterOperationStep as ClusterOperationStep
from astropulse._generated.models.cluster_price_source import ClusterPriceSource as ClusterPriceSource
from astropulse._generated.models.cluster_progress import ClusterProgress as ClusterProgress
from astropulse._generated.models.cluster_progress_page import ClusterProgressPage as ClusterProgressPage
from astropulse._generated.models.cluster_progress_page_response import ClusterProgressPageResponse as ClusterProgressPageResponse
from astropulse._generated.models.cluster_progress_response import ClusterProgressResponse as ClusterProgressResponse
from astropulse._generated.models.cluster_registration import ClusterRegistration as ClusterRegistration
from astropulse._generated.models.cluster_registration_response import ClusterRegistrationResponse as ClusterRegistrationResponse
from astropulse._generated.models.cluster_registration_status import ClusterRegistrationStatus as ClusterRegistrationStatus
from astropulse._generated.models.cluster_registration_status_response import ClusterRegistrationStatusResponse as ClusterRegistrationStatusResponse
from astropulse._generated.models.cluster_scan_findings_summary import ClusterScanFindingsSummary as ClusterScanFindingsSummary
from astropulse._generated.models.cluster_scan_findings_summary_response import ClusterScanFindingsSummaryResponse as ClusterScanFindingsSummaryResponse
from astropulse._generated.models.cluster_selection import ClusterSelection as ClusterSelection
from astropulse._generated.models.cluster_selection_type import ClusterSelectionType as ClusterSelectionType
from astropulse._generated.models.cluster_status import ClusterStatus as ClusterStatus
from astropulse._generated.models.cluster_storage import ClusterStorage as ClusterStorage
from astropulse._generated.models.cluster_storage_binding import ClusterStorageBinding as ClusterStorageBinding
from astropulse._generated.models.cluster_storage_binding_use import ClusterStorageBindingUse as ClusterStorageBindingUse
from astropulse._generated.models.cluster_storage_class import ClusterStorageClass as ClusterStorageClass
from astropulse._generated.models.cluster_storage_response import ClusterStorageResponse as ClusterStorageResponse
from astropulse._generated.models.cluster_update import ClusterUpdate as ClusterUpdate
from astropulse._generated.models.cluster_update_dry_run import ClusterUpdateDryRun as ClusterUpdateDryRun
from astropulse._generated.models.cluster_update_result import ClusterUpdateResult as ClusterUpdateResult
from astropulse._generated.models.cluster_upgrade_offer import ClusterUpgradeOffer as ClusterUpgradeOffer
from astropulse._generated.models.cluster_version_support import ClusterVersionSupport as ClusterVersionSupport
from astropulse._generated.models.cluster_version_support_state import ClusterVersionSupportState as ClusterVersionSupportState
from astropulse._generated.models.compute_type import ComputeType as ComputeType
from astropulse._generated.models.constraints import Constraints as Constraints
from astropulse._generated.models.container import Container as Container
from astropulse._generated.models.control_plane_node import ControlPlaneNode as ControlPlaneNode
from astropulse._generated.models.control_plane_node_group import ControlPlaneNodeGroup as ControlPlaneNodeGroup
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy as CostAllocationGroupBy
from astropulse._generated.models.cost_allocation_item import CostAllocationItem as CostAllocationItem
from astropulse._generated.models.cost_allocation_sort_by import CostAllocationSortBy as CostAllocationSortBy
from astropulse._generated.models.cost_dimensions import CostDimensions as CostDimensions
from astropulse._generated.models.cost_group import CostGroup as CostGroup
from astropulse._generated.models.cost_metrics_source import CostMetricsSource as CostMetricsSource
from astropulse._generated.models.cost_price_sheet import CostPriceSheet as CostPriceSheet
from astropulse._generated.models.cost_pricing import CostPricing as CostPricing
from astropulse._generated.models.cost_pricing_source import CostPricingSource as CostPricingSource
from astropulse._generated.models.cost_row_kind import CostRowKind as CostRowKind
from astropulse._generated.models.cost_series_point import CostSeriesPoint as CostSeriesPoint
from astropulse._generated.models.cost_total import CostTotal as CostTotal
from astropulse._generated.models.cost_visibility_addon_configuration import CostVisibilityAddonConfiguration as CostVisibilityAddonConfiguration
from astropulse._generated.models.cost_visibility_prometheus_configuration import CostVisibilityPrometheusConfiguration as CostVisibilityPrometheusConfiguration
from astropulse._generated.models.cost_visibility_prometheus_storage_configuration import CostVisibilityPrometheusStorageConfiguration as CostVisibilityPrometheusStorageConfiguration
from astropulse._generated.models.cost_window import CostWindow as CostWindow
from astropulse._generated.models.create_domain_binding_request import CreateDomainBindingRequest as CreateDomainBindingRequest
from astropulse._generated.models.create_domain_request import CreateDomainRequest as CreateDomainRequest
from astropulse._generated.models.credential_type import CredentialType as CredentialType
from astropulse._generated.models.credentials import Credentials as Credentials
from astropulse._generated.models.current_organization import CurrentOrganization as CurrentOrganization
from astropulse._generated.models.current_organization_response import CurrentOrganizationResponse as CurrentOrganizationResponse
from astropulse._generated.models.data_plane import DataPlane as DataPlane
from astropulse._generated.models.delete_api_key_request import DeleteAPIKeyRequest as DeleteAPIKeyRequest
from astropulse._generated.models.delete_api_key_response import DeleteAPIKeyResponse as DeleteAPIKeyResponse
from astropulse._generated.models.delete_api_key_response_envelope import DeleteAPIKeyResponseEnvelope as DeleteAPIKeyResponseEnvelope
from astropulse._generated.models.deploy_cluster_addon_request import DeployClusterAddonRequest as DeployClusterAddonRequest
from astropulse._generated.models.deploy_validation_result import DeployValidationResult as DeployValidationResult
from astropulse._generated.models.deploy_validation_result_response import DeployValidationResultResponse as DeployValidationResultResponse
from astropulse._generated.models.deployment_diff_item import DeploymentDiffItem as DeploymentDiffItem
from astropulse._generated.models.domain import Domain as Domain
from astropulse._generated.models.domain_binding import DomainBinding as DomainBinding
from astropulse._generated.models.domain_binding_response import DomainBindingResponse as DomainBindingResponse
from astropulse._generated.models.domain_binding_status import DomainBindingStatus as DomainBindingStatus
from astropulse._generated.models.domain_hostname_source import DomainHostnameSource as DomainHostnameSource
from astropulse._generated.models.domain_list_response import DomainListResponse as DomainListResponse
from astropulse._generated.models.domain_response import DomainResponse as DomainResponse
from astropulse._generated.models.domain_status import DomainStatus as DomainStatus
from astropulse._generated.models.dry_run_verdict import DryRunVerdict as DryRunVerdict
from astropulse._generated.models.eks_auto_mode_config import EKSAutoModeConfig as EKSAutoModeConfig
from astropulse._generated.models.eks_cluster_spec import EKSClusterSpec as EKSClusterSpec
from astropulse._generated.models.eks_compute_mode import EKSComputeMode as EKSComputeMode
from astropulse._generated.models.eks_update_spec import EKSUpdateSpec as EKSUpdateSpec
from astropulse._generated.models.endpoint_access_policy_none import EndpointAccessPolicyNone as EndpointAccessPolicyNone
from astropulse._generated.models.endpoint_access_policy_reference import EndpointAccessPolicyReference as EndpointAccessPolicyReference
from astropulse._generated.models.endpoint_change_request import EndpointChangeRequest as EndpointChangeRequest
from astropulse._generated.models.endpoint_dns_observation import EndpointDNSObservation as EndpointDNSObservation
from astropulse._generated.models.endpoint_desired_state import EndpointDesiredState as EndpointDesiredState
from astropulse._generated.models.endpoint_exposure import EndpointExposure as EndpointExposure
from astropulse._generated.models.endpoint_exposure_status import EndpointExposureStatus as EndpointExposureStatus
from astropulse._generated.models.endpoint_origin import EndpointOrigin as EndpointOrigin
from astropulse._generated.models.endpoint_origin_source import EndpointOriginSource as EndpointOriginSource
from astropulse._generated.models.endpoint_phase import EndpointPhase as EndpointPhase
from astropulse._generated.models.endpoint_probe import EndpointProbe as EndpointProbe
from astropulse._generated.models.endpoint_probe_reach import EndpointProbeReach as EndpointProbeReach
from astropulse._generated.models.endpoint_probe_result import EndpointProbeResult as EndpointProbeResult
from astropulse._generated.models.endpoint_probe_vantage import EndpointProbeVantage as EndpointProbeVantage
from astropulse._generated.models.endpoint_status import EndpointStatus as EndpointStatus
from astropulse._generated.models.endpoint_status_response import EndpointStatusResponse as EndpointStatusResponse
from astropulse._generated.models.error_code import ErrorCode as ErrorCode
from astropulse._generated.models.error_reason import ErrorReason as ErrorReason
from astropulse._generated.models.error_response import ErrorResponse as ErrorResponse
from astropulse._generated.models.exposure_source import ExposureSource as ExposureSource
from astropulse._generated.models.external_access import ExternalAccess as ExternalAccess
from astropulse._generated.models.external_access_tls import ExternalAccessTLS as ExternalAccessTLS
from astropulse._generated.models.external_access_type import ExternalAccessType as ExternalAccessType
from astropulse._generated.models.external_dns_addon_configuration import ExternalDNSAddonConfiguration as ExternalDNSAddonConfiguration
from astropulse._generated.models.external_dns_policy import ExternalDNSPolicy as ExternalDNSPolicy
from astropulse._generated.models.external_dns_provider import ExternalDNSProvider as ExternalDNSProvider
from astropulse._generated.models.failure import Failure as Failure
from astropulse._generated.models.gcp_connect_request import GCPConnectRequest as GCPConnectRequest
from astropulse._generated.models.gcp_connect_status import GCPConnectStatus as GCPConnectStatus
from astropulse._generated.models.gcp_connect_status_response import GCPConnectStatusResponse as GCPConnectStatusResponse
from astropulse._generated.models.gcp_credentials_request import GCPCredentialsRequest as GCPCredentialsRequest
from astropulse._generated.models.gcp_temporary_credential import GCPTemporaryCredential as GCPTemporaryCredential
from astropulse._generated.models.gcp_temporary_credential_response import GCPTemporaryCredentialResponse as GCPTemporaryCredentialResponse
from astropulse._generated.models.gke_cluster_spec import GKEClusterSpec as GKEClusterSpec
from astropulse._generated.models.gke_image_type import GKEImageType as GKEImageType
from astropulse._generated.models.gke_release_channel import GKEReleaseChannel as GKEReleaseChannel
from astropulse._generated.models.gke_subnet_config import GKESubnetConfig as GKESubnetConfig
from astropulse._generated.models.gke_update_spec import GKEUpdateSpec as GKEUpdateSpec
from astropulse._generated.models.gpu_attachment import GPUAttachment as GPUAttachment
from astropulse._generated.models.gpu_quota_headroom import GPUQuotaHeadroom as GPUQuotaHeadroom
from astropulse._generated.models.gpu_quota_state import GPUQuotaState as GPUQuotaState
from astropulse._generated.models.gpu_quota_unverified_reason import GPUQuotaUnverifiedReason as GPUQuotaUnverifiedReason
from astropulse._generated.models.gateway_addon_configuration import GatewayAddonConfiguration as GatewayAddonConfiguration
from astropulse._generated.models.gateway_auto_scaling_config import GatewayAutoScalingConfig as GatewayAutoScalingConfig
from astropulse._generated.models.gateway_programmed_state import GatewayProgrammedState as GatewayProgrammedState
from astropulse._generated.models.gateway_scaling_metric import GatewayScalingMetric as GatewayScalingMetric
from astropulse._generated.models.git_hub_account_type import GitHubAccountType as GitHubAccountType
from astropulse._generated.models.git_hub_branch import GitHubBranch as GitHubBranch
from astropulse._generated.models.git_hub_branch_commit import GitHubBranchCommit as GitHubBranchCommit
from astropulse._generated.models.git_hub_branch_list_response import GitHubBranchListResponse as GitHubBranchListResponse
from astropulse._generated.models.git_hub_content import GitHubContent as GitHubContent
from astropulse._generated.models.git_hub_content_list_response import GitHubContentListResponse as GitHubContentListResponse
from astropulse._generated.models.git_hub_content_type import GitHubContentType as GitHubContentType
from astropulse._generated.models.git_hub_detect_request import GitHubDetectRequest as GitHubDetectRequest
from astropulse._generated.models.git_hub_detected_installation import GitHubDetectedInstallation as GitHubDetectedInstallation
from astropulse._generated.models.git_hub_detected_installations import GitHubDetectedInstallations as GitHubDetectedInstallations
from astropulse._generated.models.git_hub_detected_installations_response import GitHubDetectedInstallationsResponse as GitHubDetectedInstallationsResponse
from astropulse._generated.models.git_hub_file_content import GitHubFileContent as GitHubFileContent
from astropulse._generated.models.git_hub_file_content_response import GitHubFileContentResponse as GitHubFileContentResponse
from astropulse._generated.models.git_hub_install_state import GitHubInstallState as GitHubInstallState
from astropulse._generated.models.git_hub_install_state_response import GitHubInstallStateResponse as GitHubInstallStateResponse
from astropulse._generated.models.git_hub_installation import GitHubInstallation as GitHubInstallation
from astropulse._generated.models.git_hub_installation_claim_request import GitHubInstallationClaimRequest as GitHubInstallationClaimRequest
from astropulse._generated.models.git_hub_installation_deleted import GitHubInstallationDeleted as GitHubInstallationDeleted
from astropulse._generated.models.git_hub_installation_deleted_response import GitHubInstallationDeletedResponse as GitHubInstallationDeletedResponse
from astropulse._generated.models.git_hub_installation_list_response import GitHubInstallationListResponse as GitHubInstallationListResponse
from astropulse._generated.models.git_hub_installation_response import GitHubInstallationResponse as GitHubInstallationResponse
from astropulse._generated.models.git_hub_installation_result import GitHubInstallationResult as GitHubInstallationResult
from astropulse._generated.models.git_hub_installation_result_response import GitHubInstallationResultResponse as GitHubInstallationResultResponse
from astropulse._generated.models.git_hub_installation_status import GitHubInstallationStatus as GitHubInstallationStatus
from astropulse._generated.models.git_hub_path_type import GitHubPathType as GitHubPathType
from astropulse._generated.models.git_hub_path_validation import GitHubPathValidation as GitHubPathValidation
from astropulse._generated.models.git_hub_path_validation_request import GitHubPathValidationRequest as GitHubPathValidationRequest
from astropulse._generated.models.git_hub_path_validation_response import GitHubPathValidationResponse as GitHubPathValidationResponse
from astropulse._generated.models.git_hub_repository import GitHubRepository as GitHubRepository
from astropulse._generated.models.git_hub_repository_list_response import GitHubRepositoryListResponse as GitHubRepositoryListResponse
from astropulse._generated.models.git_hub_repository_token_request import GitHubRepositoryTokenRequest as GitHubRepositoryTokenRequest
from astropulse._generated.models.git_hub_token import GitHubToken as GitHubToken
from astropulse._generated.models.git_hub_token_response import GitHubTokenResponse as GitHubTokenResponse
from astropulse._generated.models.hpa import HPA as HPA
from astropulse._generated.models.helm import Helm as Helm
from astropulse._generated.models.helm_repo import HelmRepo as HelmRepo
from astropulse._generated.models.helm_value_type import HelmValueType as HelmValueType
from astropulse._generated.models.hugging_face_integration import HuggingFaceIntegration as HuggingFaceIntegration
from astropulse._generated.models.hugging_face_integration_request import HuggingFaceIntegrationRequest as HuggingFaceIntegrationRequest
from astropulse._generated.models.hugging_face_integration_response import HuggingFaceIntegrationResponse as HuggingFaceIntegrationResponse
from astropulse._generated.models.hugging_face_integration_state import HuggingFaceIntegrationState as HuggingFaceIntegrationState
from astropulse._generated.models.image import Image as Image
from astropulse._generated.models.image_scan_finding import ImageScanFinding as ImageScanFinding
from astropulse._generated.models.inference_metrics import InferenceMetrics as InferenceMetrics
from astropulse._generated.models.inference_metrics_summary import InferenceMetricsSummary as InferenceMetricsSummary
from astropulse._generated.models.inference_runtime import InferenceRuntime as InferenceRuntime
from astropulse._generated.models.instance_type import InstanceType as InstanceType
from astropulse._generated.models.k8s_cluster import K8sCluster as K8sCluster
from astropulse._generated.models.k8s_cluster_addon_manifest import K8sClusterAddonManifest as K8sClusterAddonManifest
from astropulse._generated.models.k8s_cluster_addon_manifest_response import K8sClusterAddonManifestResponse as K8sClusterAddonManifestResponse
from astropulse._generated.models.k8s_cluster_addon_manifest_spec import K8sClusterAddonManifestSpec as K8sClusterAddonManifestSpec
from astropulse._generated.models.k8s_cluster_list_response import K8sClusterListResponse as K8sClusterListResponse
from astropulse._generated.models.k8s_cluster_manifest import K8sClusterManifest as K8sClusterManifest
from astropulse._generated.models.k8s_cluster_manifest_response import K8sClusterManifestResponse as K8sClusterManifestResponse
from astropulse._generated.models.k8s_cluster_registration import K8sClusterRegistration as K8sClusterRegistration
from astropulse._generated.models.k8s_cluster_request import K8sClusterRequest as K8sClusterRequest
from astropulse._generated.models.k8s_cluster_response import K8sClusterResponse as K8sClusterResponse
from astropulse._generated.models.k8s_cluster_spec import K8sClusterSpec as K8sClusterSpec
from astropulse._generated.models.k8s_cluster_update import K8sClusterUpdate as K8sClusterUpdate
from astropulse._generated.models.k8s_upgrade_path import K8sUpgradePath as K8sUpgradePath
from astropulse._generated.models.k8s_version_analysis import K8sVersionAnalysis as K8sVersionAnalysis
from astropulse._generated.models.karpenter_addon_configuration import KarpenterAddonConfiguration as KarpenterAddonConfiguration
from astropulse._generated.models.karpenter_capacity_reservations import KarpenterCapacityReservations as KarpenterCapacityReservations
from astropulse._generated.models.karpenter_consolidation_policy import KarpenterConsolidationPolicy as KarpenterConsolidationPolicy
from astropulse._generated.models.karpenter_disruption import KarpenterDisruption as KarpenterDisruption
from astropulse._generated.models.karpenter_disruption_budget import KarpenterDisruptionBudget as KarpenterDisruptionBudget
from astropulse._generated.models.kube_client_auth import KubeClientAuth as KubeClientAuth
from astropulse._generated.models.kubeconfig import Kubeconfig as Kubeconfig
from astropulse._generated.models.kubeconfig_access import KubeconfigAccess as KubeconfigAccess
from astropulse._generated.models.kubeconfig_generation import KubeconfigGeneration as KubeconfigGeneration
from astropulse._generated.models.kubeconfig_generation_response import KubeconfigGenerationResponse as KubeconfigGenerationResponse
from astropulse._generated.models.kubeconfig_request import KubeconfigRequest as KubeconfigRequest
from astropulse._generated.models.kubeconfig_response import KubeconfigResponse as KubeconfigResponse
from astropulse._generated.models.kubeconfig_state import KubeconfigState as KubeconfigState
from astropulse._generated.models.log_level import LogLevel as LogLevel
from astropulse._generated.models.machine_type import MachineType as MachineType
from astropulse._generated.models.machine_type_list_response import MachineTypeListResponse as MachineTypeListResponse
from astropulse._generated.models.machine_type_response import MachineTypeResponse as MachineTypeResponse
from astropulse._generated.models.maintenance_window import MaintenanceWindow as MaintenanceWindow
from astropulse._generated.models.mem_resources import MemResources as MemResources
from astropulse._generated.models.member import Member as Member
from astropulse._generated.models.metrics_dimensions import MetricsDimensions as MetricsDimensions
from astropulse._generated.models.metrics_series_point import MetricsSeriesPoint as MetricsSeriesPoint
from astropulse._generated.models.model import Model as Model
from astropulse._generated.models.model_api_format import ModelAPIFormat as ModelAPIFormat
from astropulse._generated.models.model_accelerator import ModelAccelerator as ModelAccelerator
from astropulse._generated.models.model_cache import ModelCache as ModelCache
from astropulse._generated.models.model_cache_backing import ModelCacheBacking as ModelCacheBacking
from astropulse._generated.models.model_capacity_type import ModelCapacityType as ModelCapacityType
from astropulse._generated.models.model_format import ModelFormat as ModelFormat
from astropulse._generated.models.model_gpu import ModelGPU as ModelGPU
from astropulse._generated.models.model_multimodal import ModelMultimodal as ModelMultimodal
from astropulse._generated.models.model_placement import ModelPlacement as ModelPlacement
from astropulse._generated.models.model_placement_instance import ModelPlacementInstance as ModelPlacementInstance
from astropulse._generated.models.model_placement_quota import ModelPlacementQuota as ModelPlacementQuota
from astropulse._generated.models.model_queue import ModelQueue as ModelQueue
from astropulse._generated.models.model_resources import ModelResources as ModelResources
from astropulse._generated.models.model_runtime import ModelRuntime as ModelRuntime
from astropulse._generated.models.model_runtime_choice import ModelRuntimeChoice as ModelRuntimeChoice
from astropulse._generated.models.model_scaling import ModelScaling as ModelScaling
from astropulse._generated.models.model_scaling_metric import ModelScalingMetric as ModelScalingMetric
from astropulse._generated.models.model_scaling_rule import ModelScalingRule as ModelScalingRule
from astropulse._generated.models.model_scaling_signal import ModelScalingSignal as ModelScalingSignal
from astropulse._generated.models.model_scaling_target import ModelScalingTarget as ModelScalingTarget
from astropulse._generated.models.model_serving import ModelServing as ModelServing
from astropulse._generated.models.model_serving_addon_configuration import ModelServingAddonConfiguration as ModelServingAddonConfiguration
from astropulse._generated.models.model_serving_cache_configuration import ModelServingCacheConfiguration as ModelServingCacheConfiguration
from astropulse._generated.models.model_task import ModelTask as ModelTask
from astropulse._generated.models.network_traffic import NetworkTraffic as NetworkTraffic
from astropulse._generated.models.next_step import NextStep as NextStep
from astropulse._generated.models.nginx_addon_configuration import NginxAddonConfiguration as NginxAddonConfiguration
from astropulse._generated.models.nginx_wildcard_certificate import NginxWildcardCertificate as NginxWildcardCertificate
from astropulse._generated.models.node_group import NodeGroup as NodeGroup
from astropulse._generated.models.node_group_change_type import NodeGroupChangeType as NodeGroupChangeType
from astropulse._generated.models.node_group_removal import NodeGroupRemoval as NodeGroupRemoval
from astropulse._generated.models.node_group_state import NodeGroupState as NodeGroupState
from astropulse._generated.models.node_group_update_strategy import NodeGroupUpdateStrategy as NodeGroupUpdateStrategy
from astropulse._generated.models.node_role import NodeRole as NodeRole
from astropulse._generated.models.node_role_kind import NodeRoleKind as NodeRoleKind
from astropulse._generated.models.notice import Notice as Notice
from astropulse._generated.models.notice_code import NoticeCode as NoticeCode
from astropulse._generated.models.notice_operation import NoticeOperation as NoticeOperation
from astropulse._generated.models.notice_severity import NoticeSeverity as NoticeSeverity
from astropulse._generated.models.notification_channel_availability import NotificationChannelAvailability as NotificationChannelAvailability
from astropulse._generated.models.notification_channel_availability_list_response import NotificationChannelAvailabilityListResponse as NotificationChannelAvailabilityListResponse
from astropulse._generated.models.notification_channel_type import NotificationChannelType as NotificationChannelType
from astropulse._generated.models.notification_channel_type_list_response import NotificationChannelTypeListResponse as NotificationChannelTypeListResponse
from astropulse._generated.models.notification_integration import NotificationIntegration as NotificationIntegration
from astropulse._generated.models.notification_integration_config import NotificationIntegrationConfig as NotificationIntegrationConfig
from astropulse._generated.models.notification_integration_config_request import NotificationIntegrationConfigRequest as NotificationIntegrationConfigRequest
from astropulse._generated.models.notification_integration_list_response import NotificationIntegrationListResponse as NotificationIntegrationListResponse
from astropulse._generated.models.notification_integration_request import NotificationIntegrationRequest as NotificationIntegrationRequest
from astropulse._generated.models.notification_integration_response import NotificationIntegrationResponse as NotificationIntegrationResponse
from astropulse._generated.models.notification_subscription import NotificationSubscription as NotificationSubscription
from astropulse._generated.models.notification_subscription_list_response import NotificationSubscriptionListResponse as NotificationSubscriptionListResponse
from astropulse._generated.models.notification_subscription_request import NotificationSubscriptionRequest as NotificationSubscriptionRequest
from astropulse._generated.models.notification_subscription_response import NotificationSubscriptionResponse as NotificationSubscriptionResponse
from astropulse._generated.models.notification_topic import NotificationTopic as NotificationTopic
from astropulse._generated.models.notification_topic_list_response import NotificationTopicListResponse as NotificationTopicListResponse
from astropulse._generated.models.object_meta import ObjectMeta as ObjectMeta
from astropulse._generated.models.observed_node_gpu import ObservedNodeGPU as ObservedNodeGPU
from astropulse._generated.models.observed_node_pool import ObservedNodePool as ObservedNodePool
from astropulse._generated.models.observed_node_pool_change import ObservedNodePoolChange as ObservedNodePoolChange
from astropulse._generated.models.observed_node_pool_change_reason import ObservedNodePoolChangeReason as ObservedNodePoolChangeReason
from astropulse._generated.models.observed_node_pool_kind import ObservedNodePoolKind as ObservedNodePoolKind
from astropulse._generated.models.observed_node_set import ObservedNodeSet as ObservedNodeSet
from astropulse._generated.models.observed_nodes_unavailable_reason import ObservedNodesUnavailableReason as ObservedNodesUnavailableReason
from astropulse._generated.models.operation_status import OperationStatus as OperationStatus
from astropulse._generated.models.operation_type import OperationType as OperationType
from astropulse._generated.models.operator import Operator as Operator
from astropulse._generated.models.org_feature_flags import OrgFeatureFlags as OrgFeatureFlags
from astropulse._generated.models.org_service_account import OrgServiceAccount as OrgServiceAccount
from astropulse._generated.models.org_service_account_list_response import OrgServiceAccountListResponse as OrgServiceAccountListResponse
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse as OrgServiceAccountResponse
from astropulse._generated.models.organization import Organization as Organization
from astropulse._generated.models.organization_list_response import OrganizationListResponse as OrganizationListResponse
from astropulse._generated.models.organization_member import OrganizationMember as OrganizationMember
from astropulse._generated.models.organization_member_response import OrganizationMemberResponse as OrganizationMemberResponse
from astropulse._generated.models.organization_members_page import OrganizationMembersPage as OrganizationMembersPage
from astropulse._generated.models.organization_members_page_response import OrganizationMembersPageResponse as OrganizationMembersPageResponse
from astropulse._generated.models.organization_ownership_transfer import OrganizationOwnershipTransfer as OrganizationOwnershipTransfer
from astropulse._generated.models.organization_ownership_transfer_response import OrganizationOwnershipTransferResponse as OrganizationOwnershipTransferResponse
from astropulse._generated.models.organization_request import OrganizationRequest as OrganizationRequest
from astropulse._generated.models.organization_response import OrganizationResponse as OrganizationResponse
from astropulse._generated.models.organization_role import OrganizationRole as OrganizationRole
from astropulse._generated.models.outcome import Outcome as Outcome
from astropulse._generated.models.pagination import Pagination as Pagination
from astropulse._generated.models.pagination_response import PaginationResponse as PaginationResponse
from astropulse._generated.models.permission import Permission as Permission
from astropulse._generated.models.plan_id import PlanId as PlanId
from astropulse._generated.models.preflight_category import PreflightCategory as PreflightCategory
from astropulse._generated.models.preflight_check import PreflightCheck as PreflightCheck
from astropulse._generated.models.preflight_reason_code import PreflightReasonCode as PreflightReasonCode
from astropulse._generated.models.preflight_status import PreflightStatus as PreflightStatus
from astropulse._generated.models.pricing_category import PricingCategory as PricingCategory
from astropulse._generated.models.pricing_cta import PricingCta as PricingCta
from astropulse._generated.models.pricing_data import PricingData as PricingData
from astropulse._generated.models.pricing_data_response import PricingDataResponse as PricingDataResponse
from astropulse._generated.models.pricing_feature import PricingFeature as PricingFeature
from astropulse._generated.models.pricing_feature_value import PricingFeatureValue as PricingFeatureValue
from astropulse._generated.models.pricing_plan import PricingPlan as PricingPlan
from astropulse._generated.models.pricing_plan_list_response import PricingPlanListResponse as PricingPlanListResponse
from astropulse._generated.models.pricing_price import PricingPrice as PricingPrice
from astropulse._generated.models.priority_class_type import PriorityClassType as PriorityClassType
from astropulse._generated.models.progress_event import ProgressEvent as ProgressEvent
from astropulse._generated.models.progress_event_level import ProgressEventLevel as ProgressEventLevel
from astropulse._generated.models.provider import Provider as Provider
from astropulse._generated.models.provider_list_response import ProviderListResponse as ProviderListResponse
from astropulse._generated.models.provider_provisioners import ProviderProvisioners as ProviderProvisioners
from astropulse._generated.models.provider_provisioners_list_response import ProviderProvisionersListResponse as ProviderProvisionersListResponse
from astropulse._generated.models.provisioner import Provisioner as Provisioner
from astropulse._generated.models.provisioner_info import ProvisionerInfo as ProvisionerInfo
from astropulse._generated.models.provisioner_type import ProvisionerType as ProvisionerType
from astropulse._generated.models.quantity import Quantity as Quantity
from astropulse._generated.models.queue_metrics import QueueMetrics as QueueMetrics
from astropulse._generated.models.queue_metrics_summary import QueueMetricsSummary as QueueMetricsSummary
from astropulse._generated.models.readiness_report_section import ReadinessReportSection as ReadinessReportSection
from astropulse._generated.models.register_cluster_request import RegisterClusterRequest as RegisterClusterRequest
from astropulse._generated.models.registration_instructions import RegistrationInstructions as RegistrationInstructions
from astropulse._generated.models.remove_user_from_organization_request import RemoveUserFromOrganizationRequest as RemoveUserFromOrganizationRequest
from astropulse._generated.models.repo import Repo as Repo
from astropulse._generated.models.repository import Repository as Repository
from astropulse._generated.models.resolved_node_group import ResolvedNodeGroup as ResolvedNodeGroup
from astropulse._generated.models.resource_capacity_check import ResourceCapacityCheck as ResourceCapacityCheck
from astropulse._generated.models.resource_min_max import ResourceMinMax as ResourceMinMax
from astropulse._generated.models.resource_requirement import ResourceRequirement as ResourceRequirement
from astropulse._generated.models.resource_requirements import ResourceRequirements as ResourceRequirements
from astropulse._generated.models.revoke_api_key_request import RevokeAPIKeyRequest as RevokeAPIKeyRequest
from astropulse._generated.models.role import Role as Role
from astropulse._generated.models.role_list_response import RoleListResponse as RoleListResponse
from astropulse._generated.models.rollback_cluster_addon_request import RollbackClusterAddonRequest as RollbackClusterAddonRequest
from astropulse._generated.models.rolling_update_strategy import RollingUpdateStrategy as RollingUpdateStrategy
from astropulse._generated.models.scan_finding_owner import ScanFindingOwner as ScanFindingOwner
from astropulse._generated.models.scan_finding_owner_type import ScanFindingOwnerType as ScanFindingOwnerType
from astropulse._generated.models.scan_findings_no_result import ScanFindingsNoResult as ScanFindingsNoResult
from astropulse._generated.models.scan_findings_no_result_reason import ScanFindingsNoResultReason as ScanFindingsNoResultReason
from astropulse._generated.models.scan_findings_severity_counts import ScanFindingsSeverityCounts as ScanFindingsSeverityCounts
from astropulse._generated.models.scan_findings_unscanned_images import ScanFindingsUnscannedImages as ScanFindingsUnscannedImages
from astropulse._generated.models.scan_scope_mode import ScanScopeMode as ScanScopeMode
from astropulse._generated.models.self_hosted_connect_request import SelfHostedConnectRequest as SelfHostedConnectRequest
from astropulse._generated.models.self_hosted_connect_step import SelfHostedConnectStep as SelfHostedConnectStep
from astropulse._generated.models.self_hosted_connection import SelfHostedConnection as SelfHostedConnection
from astropulse._generated.models.self_hosted_connection_response import SelfHostedConnectionResponse as SelfHostedConnectionResponse
from astropulse._generated.models.self_hosted_credential_revocation import SelfHostedCredentialRevocation as SelfHostedCredentialRevocation
from astropulse._generated.models.self_hosted_credential_revocation_response import SelfHostedCredentialRevocationResponse as SelfHostedCredentialRevocationResponse
from astropulse._generated.models.self_hosted_credential_state import SelfHostedCredentialState as SelfHostedCredentialState
from astropulse._generated.models.self_hosted_credential_status import SelfHostedCredentialStatus as SelfHostedCredentialStatus
from astropulse._generated.models.self_hosted_credential_status_response import SelfHostedCredentialStatusResponse as SelfHostedCredentialStatusResponse
from astropulse._generated.models.self_hosted_setup import SelfHostedSetup as SelfHostedSetup
from astropulse._generated.models.self_hosted_setup_request import SelfHostedSetupRequest as SelfHostedSetupRequest
from astropulse._generated.models.self_hosted_setup_response import SelfHostedSetupResponse as SelfHostedSetupResponse
from astropulse._generated.models.self_hosted_setup_state import SelfHostedSetupState as SelfHostedSetupState
from astropulse._generated.models.self_hosted_spec import SelfHostedSpec as SelfHostedSpec
from astropulse._generated.models.self_hosted_template import SelfHostedTemplate as SelfHostedTemplate
from astropulse._generated.models.self_hosted_template_response import SelfHostedTemplateResponse as SelfHostedTemplateResponse
from astropulse._generated.models.self_hosted_update_spec import SelfHostedUpdateSpec as SelfHostedUpdateSpec
from astropulse._generated.models.service_account_key_created import ServiceAccountKeyCreated as ServiceAccountKeyCreated
from astropulse._generated.models.service_account_key_created_response import ServiceAccountKeyCreatedResponse as ServiceAccountKeyCreatedResponse
from astropulse._generated.models.service_account_key_request import ServiceAccountKeyRequest as ServiceAccountKeyRequest
from astropulse._generated.models.service_account_request import ServiceAccountRequest as ServiceAccountRequest
from astropulse._generated.models.set_cluster_storage_request import SetClusterStorageRequest as SetClusterStorageRequest
from astropulse._generated.models.set_organization_member_role_request import SetOrganizationMemberRoleRequest as SetOrganizationMemberRoleRequest
from astropulse._generated.models.setting_format import SettingFormat as SettingFormat
from astropulse._generated.models.setting_options import SettingOptions as SettingOptions
from astropulse._generated.models.setting_value_requirement import SettingValueRequirement as SettingValueRequirement
from astropulse._generated.models.setup_step import SetupStep as SetupStep
from astropulse._generated.models.setup_step_state import SetupStepState as SetupStepState
from astropulse._generated.models.shell_command import ShellCommand as ShellCommand
from astropulse._generated.models.slack_config_type import SlackConfigType as SlackConfigType
from astropulse._generated.models.sort_order import SortOrder as SortOrder
from astropulse._generated.models.source_identity import SourceIdentity as SourceIdentity
from astropulse._generated.models.source_type import SourceType as SourceType
from astropulse._generated.models.state_tone import StateTone as StateTone
from astropulse._generated.models.storage_binding_state import StorageBindingState as StorageBindingState
from astropulse._generated.models.storage_kind import StorageKind as StorageKind
from astropulse._generated.models.storage_observer import StorageObserver as StorageObserver
from astropulse._generated.models.stream_ticket import StreamTicket as StreamTicket
from astropulse._generated.models.string_list_response import StringListResponse as StringListResponse
from astropulse._generated.models.string_response import StringResponse as StringResponse
from astropulse._generated.models.subnet_spec import SubnetSpec as SubnetSpec
from astropulse._generated.models.subnet_type import SubnetType as SubnetType
from astropulse._generated.models.supported_k8s_versions_response import SupportedK8sVersionsResponse as SupportedK8sVersionsResponse
from astropulse._generated.models.supported_k8s_versions_response_envelope import SupportedK8sVersionsResponseEnvelope as SupportedK8sVersionsResponseEnvelope
from astropulse._generated.models.switch_org_request import SwitchOrgRequest as SwitchOrgRequest
from astropulse._generated.models.sync_type import SyncType as SyncType
from astropulse._generated.models.tls_mode import TLSMode as TLSMode
from astropulse._generated.models.taint_effect import TaintEffect as TaintEffect
from astropulse._generated.models.tainted import Tainted as Tainted
from astropulse._generated.models.template_format import TemplateFormat as TemplateFormat
from astropulse._generated.models.tier_config import TierConfig as TierConfig
from astropulse._generated.models.tier_config_response import TierConfigResponse as TierConfigResponse
from astropulse._generated.models.tier_type import TierType as TierType
from astropulse._generated.models.timeline_event import TimelineEvent as TimelineEvent
from astropulse._generated.models.timeline_event_kind import TimelineEventKind as TimelineEventKind
from astropulse._generated.models.transfer_organization_ownership_request import TransferOrganizationOwnershipRequest as TransferOrganizationOwnershipRequest
from astropulse._generated.models.unsubscribe_from_notifications_request import UnsubscribeFromNotificationsRequest as UnsubscribeFromNotificationsRequest
from astropulse._generated.models.update_cluster_addon_request import UpdateClusterAddonRequest as UpdateClusterAddonRequest
from astropulse._generated.models.update_cluster_spec import UpdateClusterSpec as UpdateClusterSpec
from astropulse._generated.models.update_config import UpdateConfig as UpdateConfig
from astropulse._generated.models.update_node_group import UpdateNodeGroup as UpdateNodeGroup
from astropulse._generated.models.upgrade_kind import UpgradeKind as UpgradeKind
from astropulse._generated.models.upgrade_plan import UpgradePlan as UpgradePlan
from astropulse._generated.models.upgrade_plan_node_pool import UpgradePlanNodePool as UpgradePlanNodePool
from astropulse._generated.models.upgrade_plan_node_pool_state import UpgradePlanNodePoolState as UpgradePlanNodePoolState
from astropulse._generated.models.upgrade_plan_phase import UpgradePlanPhase as UpgradePlanPhase
from astropulse._generated.models.upgrade_readiness_report import UpgradeReadinessReport as UpgradeReadinessReport
from astropulse._generated.models.upgrade_risk_level import UpgradeRiskLevel as UpgradeRiskLevel
from astropulse._generated.models.user_event_count import UserEventCount as UserEventCount
from astropulse._generated.models.user_profile import UserProfile as UserProfile
from astropulse._generated.models.user_profile_response import UserProfileResponse as UserProfileResponse
from astropulse._generated.models.vpa import VPA as VPA
from astropulse._generated.models.validation_issue import ValidationIssue as ValidationIssue
from astropulse._generated.models.values import Values as Values
from astropulse._generated.models.vault_lease import VaultLease as VaultLease
from astropulse._generated.models.vault_lease_kind import VaultLeaseKind as VaultLeaseKind
from astropulse._generated.models.vault_lease_list import VaultLeaseList as VaultLeaseList
from astropulse._generated.models.vault_lease_list_response import VaultLeaseListResponse as VaultLeaseListResponse
from astropulse._generated.models.vault_lease_replace_request import VaultLeaseReplaceRequest as VaultLeaseReplaceRequest
from astropulse._generated.models.vault_lease_response import VaultLeaseResponse as VaultLeaseResponse
from astropulse._generated.models.vault_lease_scope import VaultLeaseScope as VaultLeaseScope
from astropulse._generated.models.vault_lease_state import VaultLeaseState as VaultLeaseState
from astropulse._generated.models.vault_revocation import VaultRevocation as VaultRevocation
from astropulse._generated.models.vault_revocation_callback import VaultRevocationCallback as VaultRevocationCallback
from astropulse._generated.models.vault_revocation_outcome import VaultRevocationOutcome as VaultRevocationOutcome
from astropulse._generated.models.vault_revocation_response import VaultRevocationResponse as VaultRevocationResponse
from astropulse._generated.models.vault_validation import VaultValidation as VaultValidation
from astropulse._generated.models.vault_validation_result import VaultValidationResult as VaultValidationResult
from astropulse._generated.models.version_floor_source import VersionFloorSource as VersionFloorSource
from astropulse._generated.models.vulnerability_finding import VulnerabilityFinding as VulnerabilityFinding
from astropulse._generated.models.vulnerability_finding_detail import VulnerabilityFindingDetail as VulnerabilityFindingDetail
from astropulse._generated.models.vulnerability_finding_detail_response import VulnerabilityFindingDetailResponse as VulnerabilityFindingDetailResponse
from astropulse._generated.models.vulnerability_scanning_addon_configuration import VulnerabilityScanningAddonConfiguration as VulnerabilityScanningAddonConfiguration
from astropulse._generated.models.vulnerability_scanning_scan_resources import VulnerabilityScanningScanResources as VulnerabilityScanningScanResources
from astropulse._generated.models.vulnerability_scanning_scan_scope import VulnerabilityScanningScanScope as VulnerabilityScanningScanScope
from astropulse._generated.models.vulnerability_severity import VulnerabilitySeverity as VulnerabilitySeverity
from astropulse._generated.models.workload_autoscaling_addon_configuration import WorkloadAutoscalingAddonConfiguration as WorkloadAutoscalingAddonConfiguration
from astropulse._generated.models.workload_cluster_queue import WorkloadClusterQueue as WorkloadClusterQueue
from astropulse._generated.models.workload_identity_cloud import WorkloadIdentityCloud as WorkloadIdentityCloud
from astropulse._generated.models.workload_identity_status import WorkloadIdentityStatus as WorkloadIdentityStatus
from astropulse._generated.models.workload_impact_analysis import WorkloadImpactAnalysis as WorkloadImpactAnalysis
from astropulse._generated.models.workload_kind import WorkloadKind as WorkloadKind
from astropulse._generated.models.workload_local_queue import WorkloadLocalQueue as WorkloadLocalQueue
from astropulse._generated.models.workload_queue_preemption import WorkloadQueuePreemption as WorkloadQueuePreemption
from astropulse._generated.models.workload_queue_quota import WorkloadQueueQuota as WorkloadQueueQuota
from astropulse._generated.models.workload_queueing_addon_configuration import WorkloadQueueingAddonConfiguration as WorkloadQueueingAddonConfiguration
from astropulse._generated.models.workload_queueing_gang_scheduling import WorkloadQueueingGangScheduling as WorkloadQueueingGangScheduling
from astropulse._generated.models.workload_queueing_integration import WorkloadQueueingIntegration as WorkloadQueueingIntegration
from astropulse._generated.models.workload_scan_finding import WorkloadScanFinding as WorkloadScanFinding
from astropulse._generated.models.yaml import YAML as YAML


# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NoticeOperation(str, Enum):
    """
    NoticeOperation
    """

    """
    allowed enum values
    """
    AddOrganizationMember = 'addOrganizationMember'
    ArchiveServiceAccount = 'archiveServiceAccount'
    BindDomainHostname = 'bindDomainHostname'
    BrowseGithubRepository = 'browseGithubRepository'
    BulkDeleteApplicationProfiles = 'bulkDeleteApplicationProfiles'
    CancelClusterOperation = 'cancelClusterOperation'
    ClaimDomain = 'claimDomain'
    ClaimGithubInstallation = 'claimGithubInstallation'
    CloseApplicationEndpoint = 'closeApplicationEndpoint'
    CompleteGithubInstallation = 'completeGithubInstallation'
    ConnectAwsAccount = 'connectAwsAccount'
    ConnectAzureSubscription = 'connectAzureSubscription'
    ConnectGcpProject = 'connectGcpProject'
    ConnectHuggingface = 'connectHuggingface'
    ConnectSelfHosted = 'connectSelfHosted'
    CreateAccessPolicyKey = 'createAccessPolicyKey'
    CreateApiKey = 'createApiKey'
    CreateCluster = 'createCluster'
    CreateClusterAccessToken = 'createClusterAccessToken'
    CreateGithubInstallationToken = 'createGithubInstallationToken'
    CreateGithubRepositoryToken = 'createGithubRepositoryToken'
    CreateOrganization = 'createOrganization'
    CreateServiceAccount = 'createServiceAccount'
    CreateServiceAccountKey = 'createServiceAccountKey'
    CreateUserProfile = 'createUserProfile'
    DeleteAccessPolicy = 'deleteAccessPolicy'
    DeleteApiKey = 'deleteApiKey'
    DeleteApplication = 'deleteApplication'
    DeleteApplicationProfile = 'deleteApplicationProfile'
    DeleteCluster = 'deleteCluster'
    DeleteClusterAddon = 'deleteClusterAddon'
    DeleteDomain = 'deleteDomain'
    DeleteGithubInstallation = 'deleteGithubInstallation'
    DeleteNotificationIntegration = 'deleteNotificationIntegration'
    DeleteNotificationSubscription = 'deleteNotificationSubscription'
    DeleteSelfHostedCredentials = 'deleteSelfHostedCredentials'
    DeployApplication = 'deployApplication'
    DeployClusterAddon = 'deployClusterAddon'
    DetectGithubInstallations = 'detectGithubInstallations'
    DisconnectHuggingface = 'disconnectHuggingface'
    DismissCloudConnection = 'dismissCloudConnection'
    ExportAuditEvents = 'exportAuditEvents'
    ForgetSelfHostedSetup = 'forgetSelfHostedSetup'
    GenerateClusterKubeconfig = 'generateClusterKubeconfig'
    GetAccessPolicy = 'getAccessPolicy'
    GetApiKey = 'getApiKey'
    GetApiKeySummary = 'getApiKeySummary'
    GetApplication = 'getApplication'
    GetApplicationCostSeries = 'getApplicationCostSeries'
    GetApplicationCostSummary = 'getApplicationCostSummary'
    GetApplicationEndpoint = 'getApplicationEndpoint'
    GetApplicationMetricsSeries = 'getApplicationMetricsSeries'
    GetApplicationProfile = 'getApplicationProfile'
    GetApplicationSpec = 'getApplicationSpec'
    GetAuditEvent = 'getAuditEvent'
    GetAuditStats = 'getAuditStats'
    GetAvailabilityTier = 'getAvailabilityTier'
    GetAwsConnectionStatus = 'getAwsConnectionStatus'
    GetAwsCredentials = 'getAwsCredentials'
    GetAzureConnectionStatus = 'getAzureConnectionStatus'
    GetAzureCredentials = 'getAzureCredentials'
    GetCloudConnection = 'getCloudConnection'
    GetCluster = 'getCluster'
    GetClusterAccelerators = 'getClusterAccelerators'
    GetClusterAddon = 'getClusterAddon'
    GetClusterAddonCatalog = 'getClusterAddonCatalog'
    GetClusterAddonCostSeries = 'getClusterAddonCostSeries'
    GetClusterAddonCostSummary = 'getClusterAddonCostSummary'
    GetClusterAddonFindingDetail = 'getClusterAddonFindingDetail'
    GetClusterAddonFindings = 'getClusterAddonFindings'
    GetClusterAddonMetricsSeries = 'getClusterAddonMetricsSeries'
    GetClusterAddonSpec = 'getClusterAddonSpec'
    GetClusterAgent = 'getClusterAgent'
    GetClusterCostAllocation = 'getClusterCostAllocation'
    GetClusterCostSeries = 'getClusterCostSeries'
    GetClusterCostSummary = 'getClusterCostSummary'
    GetClusterExposure = 'getClusterExposure'
    GetClusterInfrastructureEstimate = 'getClusterInfrastructureEstimate'
    GetClusterKubeconfig = 'getClusterKubeconfig'
    GetClusterMetricsAllocation = 'getClusterMetricsAllocation'
    GetClusterMetricsSummary = 'getClusterMetricsSummary'
    GetClusterProgress = 'getClusterProgress'
    GetClusterSpec = 'getClusterSpec'
    GetClusterStorage = 'getClusterStorage'
    GetDomain = 'getDomain'
    GetGcpConnectionStatus = 'getGcpConnectionStatus'
    GetGcpCredentials = 'getGcpCredentials'
    GetGithubInstallation = 'getGithubInstallation'
    GetGithubRepositoryFile = 'getGithubRepositoryFile'
    GetHuggingfaceIntegration = 'getHuggingfaceIntegration'
    GetMachineType = 'getMachineType'
    GetNotificationIntegration = 'getNotificationIntegration'
    GetNotificationSubscription = 'getNotificationSubscription'
    GetOpenApiDocument = 'getOpenApiDocument'
    GetOrganization = 'getOrganization'
    GetOrganizationPlan = 'getOrganizationPlan'
    GetOrganizationUsage = 'getOrganizationUsage'
    GetPricing = 'getPricing'
    GetSelfHostedAwsTemplate = 'getSelfHostedAwsTemplate'
    GetSelfHostedCloudConnection = 'getSelfHostedCloudConnection'
    GetSelfHostedCredentialsStatus = 'getSelfHostedCredentialsStatus'
    GetSelfHostedSetup = 'getSelfHostedSetup'
    GetServiceAccount = 'getServiceAccount'
    GetUserProfile = 'getUserProfile'
    GetVaultLease = 'getVaultLease'
    IssueClusterAgentCertificate = 'issueClusterAgentCertificate'
    ListAccessPolicies = 'listAccessPolicies'
    ListAccessPolicyKeys = 'listAccessPolicyKeys'
    ListApiKeys = 'listApiKeys'
    ListApplicationHistory = 'listApplicationHistory'
    ListApplicationProfiles = 'listApplicationProfiles'
    ListApplications = 'listApplications'
    ListAuditEvents = 'listAuditEvents'
    ListAvailabilityTiers = 'listAvailabilityTiers'
    ListAwsCapacityReservations = 'listAwsCapacityReservations'
    ListCloudAccounts = 'listCloudAccounts'
    ListCloudConnections = 'listCloudConnections'
    ListClusterAddonHistory = 'listClusterAddonHistory'
    ListClusterAddonVersions = 'listClusterAddonVersions'
    ListClusterAddons = 'listClusterAddons'
    ListClusterOperations = 'listClusterOperations'
    ListClusterProgress = 'listClusterProgress'
    ListClusters = 'listClusters'
    ListDomains = 'listDomains'
    ListGithubInstallationRepositories = 'listGithubInstallationRepositories'
    ListGithubInstallations = 'listGithubInstallations'
    ListGithubRepositoryBranches = 'listGithubRepositoryBranches'
    ListKubernetesVersions = 'listKubernetesVersions'
    ListMachineTypes = 'listMachineTypes'
    ListNotificationChannelAvailability = 'listNotificationChannelAvailability'
    ListNotificationChannels = 'listNotificationChannels'
    ListNotificationIntegrations = 'listNotificationIntegrations'
    ListNotificationSubscriptions = 'listNotificationSubscriptions'
    ListNotificationTopics = 'listNotificationTopics'
    ListOrganizationMembers = 'listOrganizationMembers'
    ListOrganizationRoles = 'listOrganizationRoles'
    ListOrganizations = 'listOrganizations'
    ListPlans = 'listPlans'
    ListProviderProvisioners = 'listProviderProvisioners'
    ListProviderRegions = 'listProviderRegions'
    ListProviders = 'listProviders'
    ListRegionAccelerators = 'listRegionAccelerators'
    ListRegionZones = 'listRegionZones'
    ListServiceAccountKeys = 'listServiceAccountKeys'
    ListServiceAccounts = 'listServiceAccounts'
    ListVaultLeases = 'listVaultLeases'
    MapGithubInstallation = 'mapGithubInstallation'
    RegisterClusterAgent = 'registerClusterAgent'
    RemoveOrganizationMember = 'removeOrganizationMember'
    ReopenApplicationEndpoint = 'reopenApplicationEndpoint'
    ReplaceVaultLease = 'replaceVaultLease'
    RequestClusterApproval = 'requestClusterApproval'
    ResumeApplication = 'resumeApplication'
    ResyncApplication = 'resyncApplication'
    ResyncClusterAddon = 'resyncClusterAddon'
    RevokeAccessPolicyKey = 'revokeAccessPolicyKey'
    RevokeApiKey = 'revokeApiKey'
    RevokeServiceAccountKey = 'revokeServiceAccountKey'
    RevokeVaultLease = 'revokeVaultLease'
    RollbackApplication = 'rollbackApplication'
    RollbackClusterAddon = 'rollbackClusterAddon'
    SetOrganizationMemberRole = 'setOrganizationMemberRole'
    StartGithubInstallation = 'startGithubInstallation'
    StartSelfHostedSetup = 'startSelfHostedSetup'
    StreamApplicationEvents = 'streamApplicationEvents'
    StreamApplicationLogs = 'streamApplicationLogs'
    StreamApplicationStatus = 'streamApplicationStatus'
    StreamClusterProgress = 'streamClusterProgress'
    SwitchCurrentOrganization = 'switchCurrentOrganization'
    SyncClusterAuth = 'syncClusterAuth'
    TestAccessPolicyToken = 'testAccessPolicyToken'
    TestNotificationIntegration = 'testNotificationIntegration'
    TransferOrganizationOwnership = 'transferOrganizationOwnership'
    UnbindDomainHostname = 'unbindDomainHostname'
    UnregisterClusterAgent = 'unregisterClusterAgent'
    UnsubscribeNotifications = 'unsubscribeNotifications'
    UpdateCluster = 'updateCluster'
    UpdateClusterAddon = 'updateClusterAddon'
    UpdateClusterExposure = 'updateClusterExposure'
    UpdateClusterStorage = 'updateClusterStorage'
    UpdateServiceAccount = 'updateServiceAccount'
    UpsertAccessPolicy = 'upsertAccessPolicy'
    UpsertApplicationProfile = 'upsertApplicationProfile'
    UpsertNotificationIntegration = 'upsertNotificationIntegration'
    UpsertNotificationSubscription = 'upsertNotificationSubscription'
    ValidateApiKey = 'validateApiKey'
    ValidateGithubPath = 'validateGithubPath'
    VerifyDomain = 'verifyDomain'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NoticeOperation from a JSON string"""
        return cls(json.loads(json_str))

    @classmethod
    def _missing_(cls, value: object) -> Self | None:
        """Accept a value this version does not know, keeping it as given.

        The API may add values to this enum at any time. One this version does
        not list parses to a member whose ``value`` is the string received, so
        it is never lost and is sent back unchanged; it equals no listed member.
        """
        if not isinstance(value, str):
            return None
        member = str.__new__(cls, value)
        member._name_ = str(value)
        member._value_ = value
        return member

    @property
    def label(self) -> str | None:
        """The display name the API document gives this value.

        ``None`` for a value this version of the package does not list.
        """
        return _LABELS.get(self._value_)

    @property
    def description(self) -> str | None:
        """What this value means, as the API document describes it.

        ``None`` for a value this version of the package does not list.
        """
        return _DESCRIPTIONS.get(self._value_)

    @classmethod
    def label_for(cls, value: str) -> str | None:
        """The display name of a value, or ``None`` for one this version does not list."""
        return _LABELS.get(value)

    @classmethod
    def description_for(cls, value: str) -> str | None:
        """What a value means, or ``None`` for one this version does not list."""
        return _DESCRIPTIONS.get(value)



# The API document lists the labels and descriptions in the order of the values,
# which is also the order of the members above.
_LABELS: dict[str, str] = dict(zip(
    [member._value_ for member in NoticeOperation],
    [
        "Add user to organization",
        "Archive service account",
        "Bind a domain hostname to an app",
        "Browse repository content",
        "Bulk delete application profiles",
        "Cancel the running cluster operation",
        "Claim a domain",
        "Claim a GitHub installation",
        "Close an application's managed endpoint",
        "Process GitHub App installation callback",
        "Connect AWS account for cluster provisioning",
        "Connect Azure subscription for cluster provisioning",
        "Connect GCP project for cluster provisioning",
        "Connect Hugging Face",
        "Store self-hosted cluster credentials",
        "Create an API key for an access policy",
        "Create API key for an organization",
        "Deploy a new Kubernetes cluster",
        "Get a cluster access token",
        "Generate installation token",
        "Generate repository token",
        "Create an organization",
        "Create service account",
        "Create service account key",
        "Create a new user profile",
        "Delete an unreferenced access policy",
        "Delete API key for an organization",
        "Delete an application",
        "Delete application profile",
        "Delete a Kubernetes cluster",
        "Delete a managed cluster add-on",
        "Delete a domain",
        "Delete GitHub installation",
        "Delete notification integration",
        "Delete notification subscription",
        "Delete self-hosted cluster credentials",
        "Deploy an application",
        "Deploy a managed cluster add-on",
        "Detect and sync GitHub installations",
        "Disconnect Hugging Face",
        "Dismiss a failed or unfinished cloud connection",
        "Download audit events as a file",
        "Forget a self-hosted cluster's setup",
        "Generate kubeconfig for a cluster",
        "Get an access policy revision",
        "Get API key by ID",
        "Get API key summary",
        "Get an application",
        "Get one application's cost time series",
        "Get one application's cost summary",
        "Get an application's managed endpoint",
        "Get one application's live resource-usage series",
        "Get application profile",
        "Get application request specification",
        "Get audit event details",
        "Get audit statistics for an organization",
        "Get availability tier information",
        "Get AWS cloud account connection status",
        "Get AWS temporary credentials",
        "Get Azure cloud account connection status",
        "Get Azure temporary credentials",
        "Check a cloud account connection",
        "Get cluster details",
        "List the GPUs a cluster can provide",
        "Get a managed cluster add-on",
        "Get the add-on catalog for a cluster",
        "Get managed cluster add-on cost over time",
        "Get managed cluster add-on cost summary",
        "Get live per-CVE detail for one scanned workload",
        "Get the latest vulnerability scan findings for a cluster",
        "Get managed cluster add-on resource usage",
        "Get a managed cluster add-on's manifest",
        "Get agent status for a cluster",
        "Get cluster cost allocation",
        "Get cluster cost time series",
        "Get cluster cost summary",
        "Get a cluster's exposure",
        "Get what a new cluster gets around it, at list price",
        "Get cluster kubeconfig",
        "Get cluster metrics allocation",
        "Get cluster metrics summary",
        "Get cluster progress",
        "Get cluster specification",
        "Get a cluster's storage",
        "Get a domain",
        "Get GCP cloud account connection status",
        "Get GCP temporary credentials",
        "Get a specific GitHub installation",
        "Get file content",
        "Get Hugging Face integration status",
        "Get machine type details",
        "Get specific notification integration",
        "Get specific notification subscription",
        "Get the API document",
        "Get organization by ID",
        "Get organization plan",
        "Read the organization's plan limits and usage",
        "Get complete pricing data",
        "Get the self-hosted AWS setup template",
        "Check a self-hosted cluster's cloud credentials",
        "Get self-hosted credential vault status",
        "Get a self-hosted cluster's setup",
        "Get service account",
        "Get current user profile",
        "Get one credential",
        "Sign a new certificate for a cluster's agent",
        "List access policies",
        "List an access policy's API keys",
        "List API keys for a user",
        "Get application deploy history",
        "List application profiles",
        "List all applications",
        "List audit events for an organization",
        "List supported availability tiers",
        "List the account's capacity reservations and Capacity Blocks",
        "List the organization's cloud accounts",
        "List the organization's cloud connections",
        "Get managed cluster add-on deployment history",
        "List supported versions for a managed cluster add-on",
        "List managed add-ons for a cluster",
        "Get cluster operation history",
        "List cluster progress for all clusters",
        "List all clusters for your organization",
        "List domains",
        "List repositories for a GitHub installation",
        "List GitHub installations",
        "List repository branches",
        "Get supported Kubernetes versions",
        "List available machine types",
        "Get which notification channels this organization's plan includes",
        "Get available channels",
        "List notification integrations",
        "List notification subscriptions",
        "Get available notification topics",
        "Get organization members",
        "Get organization roles",
        "List organizations for the caller",
        "List the plans on offer",
        "List the provisioners each provider offers",
        "List available regions for a provider",
        "List supported providers",
        "List distinct accelerators available in a region",
        "List available zones for a region",
        "List service account keys",
        "List service accounts",
        "List the organization's credentials",
        "Map GitHub installation to organization",
        "Register an agent on a cluster",
        "Remove user from organization",
        "Reopen an application's managed endpoint",
        "Replace a self-hosted cluster's stored key",
        "Request cluster operation approval",
        "Resume a git-pinned application",
        "Resync an application",
        "Resync a managed cluster add-on",
        "Revoke an access policy's API key",
        "Revoke API key",
        "Revoke service account key",
        "Revoke a credential",
        "Roll an application back to a previous version",
        "Roll back a managed cluster add-on",
        "Change a member's role",
        "Start a GitHub App installation",
        "Start a self-hosted cluster's setup",
        "Stream application events via WebSocket",
        "Stream application logs via WebSocket",
        "Stream application status",
        "Stream cluster progress via WebSocket",
        "Switch current organization",
        "Sync cluster authentication configuration",
        "Test a token against an access policy",
        "Send a test notification",
        "Transfer an organization's ownership",
        "Unbind a domain hostname from an app",
        "Unregister an agent from a cluster",
        "Unsubscribe from notifications",
        "Update cluster configuration",
        "Update a managed cluster add-on",
        "Set a cluster's exposure settings",
        "Set a cluster's storage bindings",
        "Update service account",
        "Create or revise an access policy",
        "Create or update application profile",
        "Configure notification integration",
        "Create or update notification subscription",
        "Validate API key",
        "Validate file path in a GitHub repository",
        "Verify domain ownership",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in NoticeOperation],
    [
        "Add a user to an organization with specified role (Viewer, Editor or Admin; default Viewer). Takes the global admin role and ownership of the organization; adding an admin also needs the plan's admin roles.",
        "Archives the service account and disables all its keys. Archiving cannot be undone. Requires a user with admin or owner permissions in the organization.",
        "Binds a hostname to an application. The binding starts pending; the application's endpoint reports when it is live.",
        "Returns file and directory entries for the given path in the repository. Defaults to the repository root if no path is specified.",
        "Removes multiple application profiles in a single request. Profiles in use by deployed applications are skipped; deletable profiles are removed and the in-use ones are reported back as a conflict.",
        "Asks the running update, scale, upgrade or rollback of a cluster to stop, and answers once the request is accepted, naming the node groups it removes. The operation stops its current step and removes any node group it was adding; changes already made to other node groups stay. Follow it with the cluster read: lastCancellation is CANCELLING while that runs, then CANCELLED with what was removed. A create, a delete or a registration can't be cancelled.",
        "Claims a domain and returns the DNS TXT record that proves you own it. It serves nothing until verified.",
        "Links a GitHub App installation to the organization when the given GitHub user token proves its user administers the account the app is installed on: an admin of that GitHub organization, or the personal account's own user. Organization owner only; the token is not stored.",
        "Withdraws the public route; the application keeps running on its internal address. Durable across redeploys, and asynchronous. Send the current generation.",
        "Acknowledges GitHub's redirect after an app install; it links nothing. Link the installation with claimGithubInstallation. Organization owner only, with the state startGithubInstallation issued to the same user.",
        "Connect your AWS account so AstroPulse can provision EKS clusters. Creates an IAM role via CloudFormation.",
        "Connect your Azure subscription so AstroPulse can provision AKS clusters via Workload Identity Federation.",
        "Connect your GCP project so AstroPulse can provision GKE clusters. Sets up Workload Identity Federation.",
        "Stores a read-only Hugging Face token for the organization so gated hf:// models deploy without a per-application Secret. The token is always checked with Hugging Face first and stored only if Hugging Face accepts it: a rejected token is refused (400), and when Hugging Face cannot be reached nothing is stored (503). Replaces any previously connected token; the token is never returned.",
        "Checks AWS or GCP credentials for a self-hosted cluster against the account (identity, state bucket, required roles and APIs), stores them encrypted in AstroPulse only when every check passes, and records both steps on the cluster's setup. A failed check is refused with 400 naming the check, what to fix and the cloud provider's error.",
        "Creates a caller API key for a policy whose keys AstroPulse keeps. The key is returned only in this response; endpoints on the policy accept it within a minute, with no redeploy.",
        "Create an API key for an organization. The API key will be used to authenticate the requests to the AstroPulse API. Requires a signed-in user session.",
        "Deploys a new Kubernetes cluster from a K8sCluster specification, in the manifest envelope or the flat request shape. A dry run (?dryRun=true) and a create run the same checks: the spec, the region's zones, node group bounds, the cloud account connection (connected, setup template current) and the provider preflight. The account connection is the first check. A dry run answers 200 with the checklist whether or not the checks pass: read data.valid and data.checks; data.complete is false when some checks did not finish, named in data.unfinishedChecks. A create whose checks fail answers 400 with reason PreflightFailed and the same checks in details.checks; nothing is created. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.",
        "Returns a short-lived access token for the cluster's API, for as long as the kubeconfig you generated is valid. The kubeconfig from `astroctl infra k8s generate-kubeconfig` or `set-context` requests one automatically and renews it before it expires.",
        "Returns a short-lived GitHub App installation access token scoped to the given installation. Use this token to make authenticated GitHub API calls on behalf of the installation.",
        "Returns a short-lived access token scoped to a single repository. Intended for CI/CD systems that need read access to deploy configuration files.",
        "Create a new organization and provision its associated resources. The authenticated user becomes the organization admin. Organization names must be unique. Beyond your default one it needs the global admin role and room under the plan's organization limit.",
        "Requires a user with admin or owner permissions in the organization.",
        "Issues a new key for the service account. The secret is returned only in this response. Requires a user with admin or owner permissions in the organization.",
        "Creates an AstroPulse profile for the authenticated user if one does not yet exist, or returns the existing profile. Called automatically after first login.",
        "Deletes a policy no endpoint references, with any API keys AstroPulse keeps for it. One still attached to an application is refused.",
        "Delete an API key for an organization by its ID. The API key will no longer be valid for authentication. Requires a signed-in user session.",
        "Permanently removes the application and its associated resources. Organization admins and owners can delete applications.",
        "Permanently removes the application profile. Profiles currently in use by deployed applications cannot be deleted.",
        "Permanently removes the cluster and the cloud resources created for it; disks its volumes use are kept in your cloud account and listed. Registered (agent-based) clusters must use the unregister endpoint instead. With recordOnly=true, removes only AstroPulse's record of a self-hosted cluster whose stored key is gone; nothing in your cloud account is deleted. With dryRun=true, lists the volumes the delete would leave in your cloud account and deletes nothing.",
        "Removes the managed add-on from the cluster. The astro-agent add-on cannot be deleted; it is removed when a registered cluster is unregistered or a provisioned cluster is deleted.",
        "Deletes a domain claim. One with bindings is refused; unbind the hostnames first.",
        "Unlinks the GitHub App installation from the organization and revokes the organization's deployment credentials for it. Other organizations linked to it keep their links and credentials, and it remains installed on GitHub.",
        "Removes the notification delivery integration for the specified channel. Existing subscriptions using this channel will no longer deliver notifications.",
        "Removes the notification subscription for the given topic. The organization will no longer receive alerts for this event type.",
        "Deletes AstroPulse's stored copy of a self-hosted cluster's credentials. The key stays valid in the cloud account; the message names it and how to delete it there.",
        "Deploy an application from an Application specification. Use ?dryRun=true to validate without deploying. A Helm or repository source's values.type is optional; it is inferred from whether object or files is set.",
        "Validates the requested configuration and deploys the managed add-on. Applying the configuration the add-on already runs changes nothing. A configuration whose last deployment failed is refused with 409; fix the cause, then resync the add-on to retry it.",
        "Returns the organization's GitHub App installations with their status on GitHub, as linked; available is always empty. With refresh=true, also re-creates their deployment credentials.",
        "Deletes the organization's stored Hugging Face token. Within about ten minutes the token is withdrawn from your clusters: running model pods keep what they downloaded, and new or restarted model pods read gated models only through a Secret the cluster's model-serving add-on names, if one is set. The token stays valid at Hugging Face until it is revoked there. Repeating the call has no further effect.",
        "Removes AstroPulse's record of a connection whose setup failed or never finished; nothing in the cloud account changes. A connected connection, or one whose setup is still running, is refused with 409.",
        "Downloads every matching event as a file, CSV or JSON: the body is the file itself, not the usual envelope. To read them as data, list them instead. Enterprise plan. Organization admins and owners export every event; other members only their own. Each event names the actor who performed it. At most 50000 events are exported; when more match, the newest 50000 are returned and X-Audit-Export-Truncated is true.",
        "Removes the record of a cluster's self-hosted setup and ends the setup if it is still waiting for credentials. Nothing in your AWS account or GCP project is changed; the message names the cleanup command for what the setup created. Refused while credentials are stored for the cluster: disconnect them first.",
        "Generates your kubeconfig for the cluster, valid for the lifetime you choose. A kubeconfig that signs in through astroctl (every cluster but a self-hosted one) is returned immediately; a self-hosted cluster's carries a client certificate, returns 202 and requires polling via GET. With native, the kubeconfig signs in with your own cloud identity through your cloud provider's tool instead, and the message says what it needs.",
        "One access policy, including the revision an endpoint quotes to prove which version it enforces.",
        "Returns the name, status, expiry, and organization association for a specific API key. Requires a signed-in user session.",
        "Returns how many of the caller's keys in the organization are active, expired and revoked, and the active key that expires first within 7 days. Requires a signed-in user session.",
        "Retrieve details of a specific application within an organization",
        "Returns closed-hour cost and usage buckets for one application; its cluster is resolved from the application record. Missing and gap buckets stay explicit and are never reported as zero spend.",
        "Aggregates closed hourly cost rollups for one application over the window. Coverage says how completely the cluster reported; an application that contributed nothing reports reporting=false, not zero spend.",
        "Where the application is served, and whether it is open. A model's URL lives here; an endpoint still settling reports Pending with no URL, and its message says what it waits for.",
        "Returns stored resource-usage samples for one application at the resolution the agent recorded them. A window with no sample is absent from points rather than a zero, and each point carries its own coverage.",
        "Returns the configuration and tier details for the specified application profile.",
        "Returns the original deployment specification for the application, useful for auditing or re-deploying with modified parameters.",
        "Get one audit event by ID, at any age. Enterprise plan. Below admin, only the caller's own events; anyone else's answers not found.",
        "Get audit statistics and analytics for an organization. Requires enterprise plan and admin role.",
        "Get detailed information about a specific availability tier",
        "Polls an AWS account connection started by POST /api/v1/cloud/aws/connect. Returns nextStep once setup is ready: the CloudFormation console link that creates the role in your account, pre-filled, with what to do. Once ready, if the account's stack is at an older template, nextStep is its update link and command. Then reports a terminal status when setup completes or fails. While a check of the account fails, lastError says why and how long AstroPulse has been retrying.",
        "Get temporary AWS credentials for cluster operations",
        "Polls an Azure subscription connection started by POST /api/v1/cloud/azure/connect. Returns nextStep once setup is ready: the Azure Cloud Shell link, the command to paste there and the setup script it runs. While a check of the subscription fails, lastError says why and how long AstroPulse has been retrying. Then reports a terminal status when setup completes or fails.",
        "Get temporary Azure credentials for cluster operations",
        "Reports whether AstroPulse can reach the account connected for a cluster right now, the same way for every provider: NotConnected, Pending, Connected, OutdatedTemplate (AWS), Failed, or Unknown when it could not be checked just now. It never returns credentials. An OutdatedTemplate answer carries nextStep: the stack's update link and command. For a member who is not an organization admin the answer omits accountId, region, resourceGroup, connectionId, nextStep and the template versions.",
        "Retrieves detailed information about a specific Kubernetes cluster",
        "Returns the GPUs a model replica can ask for on the cluster: those its node groups carry and those its autoscaling pools can launch, with the most one replica can ask for and whether each can be placed now.",
        "Returns one platform-managed add-on and its lifecycle state.",
        "Returns AstroPulse's add-on catalog with compatibility evaluated for this cluster by the same rules that gate deployment.",
        "Returns the add-on's cost over time. Missing intervals are never converted to zero spend; an astro-agent not yet recorded as the cluster's add-on has no points.",
        "Returns the add-on's cost summary. Coverage says how completely the cluster reported; no reported allocation is not zero spend. An astro-agent not yet recorded as the cluster's add-on reports none.",
        "Returns normalized per-vulnerability details for one workload. Detail is read from the cluster on demand and is not persisted by AstroPulse.",
        "Returns the latest per-workload and per-image vulnerability severity counts. Freshness timestamps are included so callers can evaluate the result against the cluster's configured scan frequency. With no results, a 404 says why: its reason is ScannerNotInstalled, NothingToScan, ImagesNotScannable, ScanPending or ScanOverdue, with the title and nextStep that say what to do; its details list any unscannedImages.",
        "Returns CPU, memory, and network usage for the add-on. A window with no reported sample is absent rather than zero; an astro-agent not yet recorded as the cluster's add-on reports none.",
        "Returns the manifest of an installed add-on, its version and configuration, in the shape an add-on apply takes. Credential values are never included.",
        "Returns agent connection status and registration progress. Use operationId during an in-flight registration. Install instructions are returned to organization admins and owners only.",
        "Aggregates provider-neutral, closed hourly metering rollups by namespace, application, or node group.",
        "Returns bounded, closed-hour cost and usage buckets for charts. Missing and gap buckets remain explicit and are never converted to zero spend.",
        "Aggregates provider-neutral, closed hourly metering rollups for a cluster. Missing and gap windows are explicit and are never rendered as zero spend.",
        "Returns how the cluster exposes applications over TLS: the ClusterIssuer in use and whether the agent observed it Ready, who runs cert-manager and external-dns, and whether exposure takes the gateway path.",
        "The charges outside a new cluster's nodes, such as its control plane and NAT gateways, with how many it gets and each one's published hourly price, where it was read and when. Nodes are priced on their machine types.",
        "Returns the kubeconfig for the cluster. Returns 202 Accepted while generation is in progress (self-managed clusters), or 200 with the config when ready.",
        "Lists every platform-managed application on the cluster with its resource usage averaged over the window, so heavy workloads surface without naming one. An application with no stored sample is absent rather than zero.",
        "Cluster-wide totals and coverage: how many applications reported resource usage in the window, how many samples backed that, and whether every sample was complete. An application that reported nothing is not counted.",
        "Returns progress details for the most recent or specified cluster operation. Pass operationId to target a specific operation.",
        "Returns the manifest the cluster was created from, in the shape the create request takes. Credential values are never included.",
        "Returns the storage classes the cluster offers, what each one provides, and the names bound to them. Classes are observed, never set here.",
        "One domain: verification state, the TXT challenge while unverified, and its bindings.",
        "Polls a GCP project connection started by POST /api/v1/cloud/gcp/connect. Returns nextStep once setup is ready: the Cloud Shell link for your project, the command to paste there and the setup script it runs. While a check of the project fails, lastError says why and how long AstroPulse has been retrying. Then reports a terminal status when setup completes or fails.",
        "Get temporary GCP credentials for cluster operations",
        "Returns account details, permissions, and sync status for the specified GitHub App installation.",
        "Returns the decoded content of a file at the specified path and ref. Supports YAML, JSON, and plain text files up to GitHub's API size limit.",
        "Reports whether the organization has connected Hugging Face, when the token was last updated, and the token's last four characters. The token itself is never returned. For a member who is not an organization admin, tokenFingerprint is omitted.",
        "What the provider publishes about one machine type, as AstroPulse sees it, at list price. Whether your own account can launch it is answered by the dry run when you apply.",
        "Returns the configuration for the specified notification delivery channel (email or slack).",
        "Returns the notification subscription configuration for the specified event topic, including its enabled channels.",
        "Returns this API's OpenAPI 3 document: every operation, type and enum value, with each value's display name and meaning. It needs no credentials.",
        "Returns the organization's details, such as its name and plan. Members and the owner's ID are returned only to an admin or owner.",
        "Get the current subscription plan for an organization",
        "The organization's plan and, for each resource the plan limits by number, how many it uses, how many the plan allows and the plan that allows more. These are the figures a PlanLimitReached refusal reports, readable before any request. A resource the plan does not limit is left out.",
        "Returns all active pricing plans and categories. No authentication required.",
        "Returns the CloudFormation template a self-hosted cluster's setup deploys, for review or an IaC pipeline.",
        "Reports whether AstroPulse can reach the cloud account a self-hosted cluster's stored credentials are for, with the same answers as getCloudConnection. It never returns credentials.",
        "Returns the status of stored credentials for a self-hosted cluster",
        "Returns each recorded setup step with its state (pending, running, done, failed, skipped), when it changed, a plain-language reason and, on failure, the cloud provider's own error, plus nextStep: what to do now.",
        "Requires a user with admin or owner permissions in the organization.",
        "Returns the authenticated user's profile, organization memberships, roles, and active organization context.",
        "Returns one of your organization's credentials as a lease: what it is, what it powers, its version, who stored it, and when it was stored, rotated and last checked, with what that check found. The value is never returned. Organization admins only.",
        "Signs a new certificate for a cluster's AstroPulse agent from a certificate signing request for a key you made and keep, to write with that key to the agent's TLS Secret from a machine that can reach the cluster. The certificate carries the cluster's own identity, and once the agent connects with it the agent's previous certificate is no longer accepted. A registered cluster's agent can be issued one while the cluster is being registered or once it is registered; a provisioned cluster's once it is ready.",
        "The organization's access policies: what each accepts, its revision, and the applications attached.",
        "The API keys of a policy whose keys AstroPulse keeps: ID, label, creation and expiry. Key values are never returned.",
        "Returns all active, expired, and revoked API keys owned by the authenticated user across all organizations. Requires a signed-in user session.",
        "Returns the version history (deploys/rollbacks) for an application with rollback eligibility.",
        "Returns all application profiles for the organization, including their deployment tiers and associated resource configuration.",
        "Returns all applications deployed within the authenticated user's organization.",
        "List audit events with filtering and pagination, newest first; dry runs and reads only when asked for. Enterprise plan. Organization admins and owners see every event; other members see only their own. With no dates the last 30 days are listed.",
        "Lists all supported availability tiers for the organization",
        "Lists, through the cluster's AWS connection, the capacity reservations and Capacity Blocks in a region: machine type, zone, free and total instances, start and end, state, and whether a node group (instanceType Reserved or CapacityBlock) or the Karpenter GPU pool could use each in the cluster's zones. No credentials are returned.",
        "One entry per cloud account (and Azure resource group) the organization connected or runs clusters in, with its state, the clusters in it and the connections whose clusters are not in AstroPulse. Connections not checked in the last five minutes are checked again when the list is read; verifiedAt is when a check last got an answer from the account.",
        "Every cloud account connection the organization has set up, newest first, as AstroPulse last recorded it. Failed or unfinished setups older than three days are left out unless includeFailed is true. Connections not checked in the last five minutes are checked again when the list is read; no credentials are returned. For a member who is not an organization admin each connection omits accountId, region, resourceGroup, connectionId, the template versions and createdAt.",
        "Returns the add-on's deployment and update history. An add-on that is not installed on the cluster is not found; an astro-agent not yet recorded as the cluster's add-on has an empty history.",
        "Returns the versions of the add-on that can be applied to this cluster. When none is offered, data is empty and message says why.",
        "Returns the managed add-ons installed on the cluster and their current lifecycle state.",
        "Returns historical operations for the cluster. If the cluster record no longer exists, pass provider, provisionerType, accountId, and region as query parameters to look up by storage location.",
        "Returns paginated progress records across all clusters in the organization, filterable by operation type and status.",
        "Retrieves a list of all Kubernetes clusters managed by AstroPulse",
        "The organization's domains, with their verification state and bound hostnames.",
        "Returns all repositories the GitHub App installation has been granted access to, filtered by the specified installation ID.",
        "Returns all GitHub App installations linked to the organization, including account login, type, and sync status.",
        "Returns all branch names in the specified GitHub repository, useful for populating branch selectors when deploying.",
        "Get the list of supported Kubernetes versions for a specific provisioner and cloud provider. For GKE, you can filter by release channel to see versions available in that channel.",
        "Machine types the provider offers in the region, as AstroPulse sees them, at list price. Whether your own account can launch one — quota, availability, reservations — is answered by the dry run.",
        "For each notification channel, whether the organization's plan includes it and, when it does not, the plan that does. Configuring an integration or subscription on a channel the plan does not include is refused.",
        "Returns the supported notification delivery channels (e.g., email, slack) that can be configured for the organization.",
        "Returns all configured notification delivery integrations (e.g., email, Slack) for the organization.",
        "Returns all configured notification subscriptions for the organization, including topics and delivery channels.",
        "Returns the notification topics an organization can subscribe to.",
        "Get all members of an organization with pagination",
        "Returns every organization role, lowest first. Send a role's key as role to add-member and set-role; they accept only the roles whose assignable is true. The owner role is not assignable: it moves by ownership transfer.",
        "List the organizations the caller's credentials can act in: every organization the caller belongs to, or only its own for an API key scoped to one organization or a service account. Members and the owner's ID are returned only to an admin or owner.",
        "Every plan an organization can be on. For the plan one is actually on, read that organization's plan.",
        "For each cloud AstroPulse supports, the ways it can create a cluster there: display name, a one-line summary of who runs the control plane and what you manage, the documentation page, and whether the account needs a one-time setup first. acceleratorNodeGroups says whether a node group may carry a GPU on that provisioner, and acceleratorMinKubernetesVersion the lowest Kubernetes version such a cluster may run; a create or update outside them is refused.",
        "Regions the provider offers, as AstroPulse sees them. Whether your own account can deploy into one — it may not be opted in — is answered by the dry run when you apply. With provisioner, only the regions that provisioner can create a cluster in: EKS and GKE need a region with at least three zones.",
        "Returns the list of cloud providers available for cluster provisioning on AstroPulse.",
        "Distinct accelerators in the region's catalog as AstroPulse sees it, at list price; read it to learn which filter values exist. Whether your own account can launch one is answered by the dry run. Each row says how old its prices are (scrapedAt, ageSeconds), whether they are stale, and when the provider's latest refresh failed (refreshFailedAt).",
        "Zones the provider offers in the region, as AstroPulse sees them. Whether your own account has capacity and quota in one is answered by the dry run when you apply.",
        "Requires a user with admin or owner permissions in the organization.",
        "Requires a user with admin or owner permissions in the organization.",
        "Lists the credentials your organization has given AstroPulse (a Hugging Face token, a registry login, a self-hosted cluster's cloud keys, ...), one page at a time, oldest first. Each entry says what the credential is, what it powers, who stored it, and when it was stored, rotated and last checked. A credential's value is never returned. Filter by kind, cluster or scope; pass nextPageToken back as pageToken for the next page. Every member may list; for a member who is not an organization admin each entry omits leaseId, path, producer, version, updatedAt, expiresAt, createdBy, lastWrittenBy, fingerprint and last4. A credential AstroPulse cannot read is listed with state Unreadable: revoke it and connect it again.",
        "Re-links a GitHub App installation that is already connected to this organization. A new installation is connected by installing the app from the organization (startGithubInstallation).",
        "Registers a Kubernetes cluster through the AstroPulse agent. Works with any cluster type (EKS, GKE, AKS, on-premises).",
        "Removes the specified user from the organization. The last admin cannot be removed, nor the owner.",
        "Publishes a closed endpoint again, once the cluster re-checks its policy and certificate. A deleted application's endpoint cannot be reopened. Send the current generation.",
        "Checks a new key for the self-hosted cluster a credential belongs to against its cloud account and, only when every check passes, stores it in place of the old one. The old key stays valid in your cloud account; the message names it and how to delete it there. Organization admins only.",
        "Submits an approve or reject decision for a pending cluster operation. Requires a signed-in organization owner.",
        "Clears a rollback's pin so the configured branch deploys again. dryRun=true returns the plan and changes nothing.",
        "Triggers an immediate GitOps resync for the application, reconciling the deployed state with the desired configuration in the repository.",
        "Builds the add-on again from its saved configuration at its installed version and deploys it, even when nothing changed. An astro-agent not yet recorded as the cluster's add-on is refused with the reason.",
        "Deletes the key from AstroPulse first; every endpoint on the policy refuses it within a minute, with no redeploy. A revoked key cannot be restored.",
        "Marks the API key as revoked so it can no longer authenticate requests. The key record is retained for audit purposes. Requires a signed-in user session.",
        "Revokes the key immediately. Requires a user with admin or owner permissions in the organization.",
        "Deletes every stored version of the credential and, for kinds that support it, revokes it at its provider too. The answer says what stops working and how the provider answered: a failed callback means AstroPulse's copy is gone but the credential may still work at the provider, so revoke it there. A credential that was replaced or removed since you read it answers 404 and nothing is deleted. A self-hosted cluster's key is not revoked while the cluster has an operation in progress. Organization admins only.",
        "Redeploys an earlier version and pins it there; a git source stops following its branch until resumed. dryRun=true returns the plan and changes nothing.",
        "Rolls an add-on back to a prior successful version. Manual-only add-ons require explicit approval. Set dryRun to check the rollback without running it.",
        "Sets a member's role to Viewer, Editor or Admin. Takes the global admin role and ownership of the organization; granting admin also needs the plan's admin roles. The owner's role never changes.",
        "Returns a short-lived state to pass to GitHub when installing the app. The installation callback accepts the install only with this state, from the same user and organization. Organization owner only.",
        "Plans the resources a self-hosted cluster needs in your AWS account or GCP project and starts recording the setup. Poll GET on the same path for each step's state and nextStep: the console link and command that create the resources.",
        "Establishes a WebSocket connection for real-time application event streaming. Upgrades HTTP to WebSocket and streams Pulse (CD) service and optionally Kubernetes events.",
        "Establishes a WebSocket connection for real-time application log streaming. Upgrades HTTP to WebSocket and streams logs with optional pod and container targeting.",
        "Opens a WebSocket connection that streams real-time status events for the specified application, including deployment progress, health conditions, and deploy service sync state.",
        "Opens a WebSocket connection and streams live progress events for an in-progress cluster operation. Use operationId to target a specific run.",
        "Sets the user's active organization so subsequent API calls default to that organization's scope. The user must be a member of the target organization.",
        "Re-synchronizes internal authentication configuration for a specific cluster to fix missing certificates or connectivity issues",
        "Whether an endpoint under the policy's latest revision would accept this JWT, and if not exactly why. The token is never stored, logged or audited.",
        "Sends a test message through the saved configuration of the given delivery channel, so the channel can be checked without re-entering its settings. Only the slack channel can be tested.",
        "Makes another member the owner of a team organization; the previous owner stays a member as admin and can then be removed. Takes the current owner, or a super-admin. The new owner must be a member holding the global admin role. A default organization cannot be transferred.",
        "Releases a hostname from its application. The application keeps running on its internal address.",
        "Removes the agent from a registered cluster and the cluster from AstroPulse. With agent-only=true, only the agent is disconnected and the cluster's record is kept.",
        "Processes an unsubscribe link click, disabling the specified notification subscription for the organization associated with the unsubscribe token.",
        "Updates a cluster's Kubernetes version, node groups or tags; AstroPulse picks the update strategy from the provider and the change. Dry-run and report requests return 200 — read validationPassed and preflightChecks; checks that did not finish are named in upgradePlan.unfinishedChecks. The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.",
        "Updates the managed add-on's version or configuration. Applying the configuration the add-on already runs changes nothing. A configuration whose last deployment failed is refused with 409; fix the cause, then resync the add-on to retry it.",
        "Names the ClusterIssuer exposed applications' certificates come from when cert-manager runs outside AstroPulse. An empty name clears it; the resolved exposure is returned.",
        "Replaces every storage binding on the cluster; bindings not listed are removed. Each binding names a storage class the cluster has. Storage classes cannot be created here.",
        "Requires a user with admin or owner permissions in the organization.",
        "Revision must be zero to create, or the current revision to change it; the same policy applied again returns its current revision. A JWT policy's provider is checked first; an issuer alone fills jwksUri from discovery.",
        "Creates or updates an application profile: the deployment resources, tier and environment settings applications in the organization deploy with. Cluster targeting is immutable while the target cluster exists.",
        "Saves the delivery channel configuration (e.g., Slack webhook URL or email recipients) for the organization, replacing any existing settings for that channel type. Leaving the Slack webhook URL out, or sending back the masked one, keeps the saved URL. Slack notifications are delivered through an incoming webhook only; a Slack app installation is refused.",
        "Saves the notification subscription for the given topic, replacing any existing configuration. At least one delivery channel is required.",
        "Returns the current status of the API key (active, expired, or revoked) along with its expiry timestamp and associated organization. For a service account key it also returns the account's id, name and role.",
        "Looks a path up on a branch of a repository and returns what is there. A path the repository does not have answers 404 with reason GitHubPathNotFound.",
        "Checks the DNS TXT record and marks the domain verified when it resolves. Safe to repeat while DNS propagates.",
    ],
))


# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ErrorReason(str, Enum):
    """
    ErrorReason
    """

    """
    allowed enum values
    """
    APIKeyExpired = 'APIKeyExpired'
    APIKeyInvalid = 'APIKeyInvalid'
    APIKeyMissing = 'APIKeyMissing'
    APIKeyNotFound = 'APIKeyNotFound'
    APIKeyQuotaExceeded = 'APIKeyQuotaExceeded'
    APIKeyRevoked = 'APIKeyRevoked'
    AccessDenied = 'AccessDenied'
    AccessPolicyKeysNotManaged = 'AccessPolicyKeysNotManaged'
    AddonClusterManaged = 'AddonClusterManaged'
    AddonConfigurationFailed = 'AddonConfigurationFailed'
    AddonConfigurationRejected = 'AddonConfigurationRejected'
    AddonDeleteBlocked = 'AddonDeleteBlocked'
    AddonDeleteFailed = 'AddonDeleteFailed'
    AddonDependencyMissing = 'AddonDependencyMissing'
    AddonDeploymentFailed = 'AddonDeploymentFailed'
    AddonLookupFailed = 'AddonLookupFailed'
    AddonNotCompatible = 'AddonNotCompatible'
    AddonNotFound = 'AddonNotFound'
    AddonOutOfBand = 'AddonOutOfBand'
    AddonOwnershipMismatch = 'AddonOwnershipMismatch'
    AddonPreflightFailed = 'AddonPreflightFailed'
    AddonReadyTimeout = 'AddonReadyTimeout'
    AddonReleaseUnavailable = 'AddonReleaseUnavailable'
    AddonSizingRejected = 'AddonSizingRejected'
    AddonStatusFailed = 'AddonStatusFailed'
    AddonVersionRetired = 'AddonVersionRetired'
    AgentCapabilityRequired = 'AgentCapabilityRequired'
    AgentCertificateRateLimited = 'AgentCertificateRateLimited'
    AgentCertificateUnreachable = 'AgentCertificateUnreachable'
    AgentCertificateWriteRefused = 'AgentCertificateWriteRefused'
    AgentImageUnreleased = 'AgentImageUnreleased'
    AgentNotConnected = 'AgentNotConnected'
    AgentRegistrationRequired = 'AgentRegistrationRequired'
    AgentsDisabled = 'AgentsDisabled'
    AgentsNotConfigured = 'AgentsNotConfigured'
    AgentsUnreachable = 'AgentsUnreachable'
    AlreadyExists = 'AlreadyExists'
    AlreadyOwner = 'AlreadyOwner'
    AppAlreadyExists = 'AppAlreadyExists'
    AppClusterUnreachableTimeout = 'AppClusterUnreachableTimeout'
    AppDeleteBlocked = 'AppDeleteBlocked'
    AppDeleteFailed = 'AppDeleteFailed'
    AppDeleteValidationError = 'AppDeleteValidationError'
    AppDeploymentFailed = 'AppDeploymentFailed'
    AppLifecycleOwnershipMismatch = 'AppLifecycleOwnershipMismatch'
    AppNotConfigured = 'AppNotConfigured'
    AppNotDeployed = 'AppNotDeployed'
    AppNotFound = 'AppNotFound'
    AppNotServing = 'AppNotServing'
    AppProfileAlreadyExists = 'AppProfileAlreadyExists'
    AppProfileDeleteFailed = 'AppProfileDeleteFailed'
    AppProfileNotFound = 'AppProfileNotFound'
    AppUpdateBlocked = 'AppUpdateBlocked'
    ArchitectureNotFound = 'ArchitectureNotFound'
    ArchitectureNotSupported = 'ArchitectureNotSupported'
    AvailabilityDataNotFound = 'AvailabilityDataNotFound'
    CallerNotAllowed = 'CallerNotAllowed'
    CannotChangeOwnerRole = 'CannotChangeOwnerRole'
    CannotRemoveFromDefaultOrg = 'CannotRemoveFromDefaultOrg'
    CannotRemoveOwner = 'CannotRemoveOwner'
    CannotTransferDefaultOrg = 'CannotTransferDefaultOrg'
    CategoryNotSupported = 'CategoryNotSupported'
    ChecksUnfinished = 'ChecksUnfinished'
    CloudCatalogNotLoaded = 'CloudCatalogNotLoaded'
    CloudProviderDataNotFound = 'CloudProviderDataNotFound'
    ClusterAlreadyExists = 'ClusterAlreadyExists'
    ClusterClientUnavailable = 'ClusterClientUnavailable'
    ClusterContextResolutionFailed = 'ClusterContextResolutionFailed'
    ClusterCreatedByAstroPulse = 'ClusterCreatedByAstroPulse'
    ClusterDeleteError = 'ClusterDeleteError'
    ClusterLookupFailed = 'ClusterLookupFailed'
    ClusterNotFound = 'ClusterNotFound'
    ClusterNotReady = 'ClusterNotReady'
    ClusterOperationInProgress = 'ClusterOperationInProgress'
    ClusterUnreachable = 'ClusterUnreachable'
    ConfigError = 'ConfigError'
    ConfigurationMismatch = 'ConfigurationMismatch'
    Conflict = 'Conflict'
    ContainerNotStarted = 'ContainerNotStarted'
    CredentialRefreshBlocked = 'CredentialRefreshBlocked'
    CredentialRefreshFailed = 'CredentialRefreshFailed'
    CredentialUnreadable = 'CredentialUnreadable'
    DatabaseError = 'DatabaseError'
    DependencyCheckFailed = 'DependencyCheckFailed'
    DependencyExists = 'DependencyExists'
    DeployInitError = 'DeployInitError'
    DeploymentClientUnavailable = 'DeploymentClientUnavailable'
    DeploymentEngineError = 'DeploymentEngineError'
    DeploymentEngineMaintenance = 'DeploymentEngineMaintenance'
    DeploymentEngineUnavailable = 'DeploymentEngineUnavailable'
    EventRefreshMissed = 'EventRefreshMissed'
    EventSnapshotIncomplete = 'EventSnapshotIncomplete'
    EventStreamFailed = 'EventStreamFailed'
    ForceResyncRateLimited = 'ForceResyncRateLimited'
    GitHubAuthorizationExpired = 'GitHubAuthorizationExpired'
    GitHubInstallationAlreadyExists = 'GitHubInstallationAlreadyExists'
    GitHubInstallationInvalid = 'GitHubInstallationInvalid'
    GitHubInstallationNotFound = 'GitHubInstallationNotFound'
    GitHubInstallationSuspended = 'GitHubInstallationSuspended'
    GitHubInstallationUnauthorized = 'GitHubInstallationUnauthorized'
    GitHubPathNotFound = 'GitHubPathNotFound'
    GitHubPermissionRequired = 'GitHubPermissionRequired'
    HTTPError = 'HTTPError'
    IdentityAlreadyLinked = 'IdentityAlreadyLinked'
    IdentityProviderUnreachable = 'IdentityProviderUnreachable'
    IdentityResolutionFailed = 'IdentityResolutionFailed'
    ImmutableConfiguration = 'ImmutableConfiguration'
    InternalError = 'InternalError'
    InvalidAddonDependencies = 'InvalidAddonDependencies'
    InvalidArgument = 'InvalidArgument'
    InvalidBulkStrategy = 'InvalidBulkStrategy'
    InvalidClient = 'InvalidClient'
    InvalidConfiguration = 'InvalidConfiguration'
    InvalidContentType = 'InvalidContentType'
    InvalidFormat = 'InvalidFormat'
    InvalidIdentity = 'InvalidIdentity'
    InvalidInternalHelmSourceOverride = 'InvalidInternalHelmSourceOverride'
    InvalidLifecycleMetadata = 'InvalidLifecycleMetadata'
    InvalidPaginationParams = 'InvalidPaginationParams'
    InvalidStoredConfiguration = 'InvalidStoredConfiguration'
    InvalidTargetNamespace = 'InvalidTargetNamespace'
    InvalidTimeout = 'InvalidTimeout'
    InvalidUserID = 'InvalidUserID'
    KubeconfigNotFound = 'KubeconfigNotFound'
    LeaseChanged = 'LeaseChanged'
    LeaseExists = 'LeaseExists'
    LeaseExpired = 'LeaseExpired'
    LeaseNotFound = 'LeaseNotFound'
    LogsStreamError = 'LogsStreamError'
    LogsUnavailable = 'LogsUnavailable'
    MachineNotFound = 'MachineNotFound'
    ManagedEndpoint = 'ManagedEndpoint'
    ManualApprovalRequired = 'ManualApprovalRequired'
    MethodNotAllowed = 'MethodNotAllowed'
    MissingCPURequirement = 'MissingCPURequirement'
    MissingMemoryRequirement = 'MissingMemoryRequirement'
    MissingRequired = 'MissingRequired'
    NamespaceCreationError = 'NamespaceCreationError'
    NoOperationRunning = 'NoOperationRunning'
    NoPodsFound = 'NoPodsFound'
    NodeGroupRemovalBlocked = 'NodeGroupRemovalBlocked'
    NotFound = 'NotFound'
    NotReady = 'NotReady'
    NotificationIntegrationError = 'NotificationIntegrationError'
    NotificationIntegrationNotFound = 'NotificationIntegrationNotFound'
    NotificationIntegrationsError = 'NotificationIntegrationsError'
    NotificationRequiredTopic = 'NotificationRequiredTopic'
    NotificationSubscriptionError = 'NotificationSubscriptionError'
    NotificationSubscriptionNotFound = 'NotificationSubscriptionNotFound'
    NotificationTopicsError = 'NotificationTopicsError'
    NotificationUnsubscribeError = 'NotificationUnsubscribeError'
    NotificationValidationError = 'NotificationValidationError'
    OperationCancelled = 'OperationCancelled'
    OperationEnded = 'OperationEnded'
    OperationFailed = 'OperationFailed'
    OperationStartFailed = 'OperationStartFailed'
    OrganizationAlreadyExists = 'OrganizationAlreadyExists'
    OrganizationNotFound = 'OrganizationNotFound'
    OwnerChanged = 'OwnerChanged'
    PlatformManagedResource = 'PlatformManagedResource'
    PodDiscoveryFailed = 'PodDiscoveryFailed'
    PreflightFailed = 'PreflightFailed'
    PreviousLogsUnavailable = 'PreviousLogsUnavailable'
    PricingDataError = 'PricingDataError'
    PricingDataNotFound = 'PricingDataNotFound'
    PricingVersionNotFound = 'PricingVersionNotFound'
    ProfilesListError = 'ProfilesListError'
    PurchaseOptionNotSupported = 'PurchaseOptionNotSupported'
    RecordOnlyNotAllowed = 'RecordOnlyNotAllowed'
    RedeployTriggerFailed = 'RedeployTriggerFailed'
    RegionNotFound = 'RegionNotFound'
    RegisteredClusterNotManaged = 'RegisteredClusterNotManaged'
    RequestTooLarge = 'RequestTooLarge'
    RollbackNotAllowed = 'RollbackNotAllowed'
    RollbackStartFailed = 'RollbackStartFailed'
    SelfHostedKeyInvalid = 'SelfHostedKeyInvalid'
    SelfHostedKeyRefused = 'SelfHostedKeyRefused'
    SelfHostedKeyUnconfirmed = 'SelfHostedKeyUnconfirmed'
    ServiceAccountArchived = 'ServiceAccountArchived'
    ServiceAccountConflict = 'ServiceAccountConflict'
    ServiceAccountInvalid = 'ServiceAccountInvalid'
    ServiceAccountNotFound = 'ServiceAccountNotFound'
    ServiceAccountUnavailable = 'ServiceAccountUnavailable'
    ServiceNotFound = 'ServiceNotFound'
    ServiceUnavailable = 'ServiceUnavailable'
    ShowingInitContainer = 'ShowingInitContainer'
    StatusServiceUnavailable = 'StatusServiceUnavailable'
    StatusUnavailable = 'StatusUnavailable'
    StuckTerminationError = 'StuckTerminationError'
    SuspendedResumeFailed = 'SuspendedResumeFailed'
    SyncError = 'SyncError'
    TerminationError = 'TerminationError'
    TierDeleteFailed = 'TierDeleteFailed'
    TierNotFound = 'TierNotFound'
    Timeout = 'Timeout'
    TooManyPods = 'TooManyPods'
    TooManyRequests = 'TooManyRequests'
    Unauthorized = 'Unauthorized'
    UnsafeConfiguration = 'UnsafeConfiguration'
    UnsafeDeploymentOption = 'UnsafeDeploymentOption'
    UnsupportedAddon = 'UnsupportedAddon'
    UnsupportedAddonVersion = 'UnsupportedAddonVersion'
    UnsupportedCleanupOption = 'UnsupportedCleanupOption'
    UnsupportedUpdateOption = 'UnsupportedUpdateOption'
    UnsupportedUpdateStrategy = 'UnsupportedUpdateStrategy'
    UserAlreadyExists = 'UserAlreadyExists'
    UserAlreadyMember = 'UserAlreadyMember'
    UserNotFound = 'UserNotFound'
    UserNotMember = 'UserNotMember'
    UserProfileNotFound = 'UserProfileNotFound'
    VaultDelegationDenied = 'VaultDelegationDenied'
    VaultInvalidPath = 'VaultInvalidPath'
    VaultInvalidRequest = 'VaultInvalidRequest'
    VaultPolicyDenied = 'VaultPolicyDenied'
    VaultPurposeRequired = 'VaultPurposeRequired'
    VaultRateLimited = 'VaultRateLimited'
    VaultSchemaViolation = 'VaultSchemaViolation'
    VaultScopeDenied = 'VaultScopeDenied'
    VaultSelectorRequired = 'VaultSelectorRequired'
    VaultTokenInvalid = 'VaultTokenInvalid'
    VaultTokenMissing = 'VaultTokenMissing'
    VaultUnavailable = 'VaultUnavailable'
    VaultUnknownKind = 'VaultUnknownKind'
    VaultValueTooLarge = 'VaultValueTooLarge'
    VersionDestroyed = 'VersionDestroyed'
    VersionNotFound = 'VersionNotFound'
    WaitingForCredentials = 'WaitingForCredentials'
    WatchFailed = 'WatchFailed'
    WatchStreamError = 'WatchStreamError'
    ZoneNotFound = 'ZoneNotFound'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ErrorReason from a JSON string"""
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
    [member._value_ for member in ErrorReason],
    [
        "API key expired",
        "API key invalid",
        "API key missing",
        "API key not found",
        "API key quota exceeded",
        "API key revoked",
        "Access denied",
        "Keys not kept in AstroPulse",
        "Managed with the cluster",
        "This configuration already failed",
        "Configuration refused",
        "Removal blocked",
        "Removal failed",
        "Dependency missing",
        "Add-on deployment failed",
        "Add-ons unavailable",
        "Add-on not compatible",
        "Add-on not found",
        "Already installed outside AstroPulse",
        "Not an add-on",
        "Preflight check failed",
        "Not ready in time",
        "This add-on release isn't available",
        "Sizing refused",
        "Add-on status unavailable",
        "Version retired",
        "Agent upgrade needed",
        "Too many certificates",
        "Cluster API unreachable",
        "Agent certificate write refused",
        "Agent unavailable",
        "The agent isn't connected",
        "Agent required",
        "Agents disabled",
        "Agents not configured",
        "Agents unreachable",
        "Already exists",
        "Already the owner",
        "Application exists",
        "Deployment unconfirmed",
        "Delete blocked",
        "Delete failed",
        "Delete refused",
        "Deployment failed",
        "Ownership cannot change",
        "Not set up for this",
        "Not deployed yet",
        "Application not found",
        "Not serving",
        "Profile exists",
        "Profile not deleted",
        "Profile not found",
        "Change not possible in place",
        "Architecture not found",
        "Architecture not supported",
        "Availability data not found",
        "Caller not allowed",
        "Owner role is fixed",
        "Cannot leave the default organization",
        "Owner cannot be removed",
        "Default organization not transferable",
        "Category not supported",
        "Checks didn't finish",
        "Cloud catalog loading",
        "Cloud data not found",
        "Cluster already exists",
        "Cluster connection unavailable",
        "Cluster not resolved",
        "Cluster created by AstroPulse",
        "Cleanup failed",
        "Cluster unavailable",
        "Cluster not found",
        "The cluster isn't ready",
        "An operation is running on the cluster",
        "Cluster unreachable",
        "Configuration error",
        "Wrong configuration",
        "Conflict",
        "Container not started",
        "Credential refresh blocked",
        "Credential refresh failed",
        "Credential unreadable",
        "Storage error",
        "Dependencies unknown",
        "In use",
        "Deployment did not start",
        "Deployment service unreachable",
        "Deployment service error",
        "Deployment service in maintenance",
        "Deployment service unavailable",
        "Refresh missed",
        "Events incomplete",
        "Events unavailable",
        "Resync limited",
        "GitHub sign-in expired",
        "GitHub installation exists",
        "GitHub installation invalid",
        "GitHub installation not found",
        "GitHub installation suspended",
        "GitHub access denied",
        "GitHub path not found",
        "GitHub permission needed",
        "Request failed",
        "Identity linked elsewhere",
        "Identity provider unreachable",
        "Identity unavailable",
        "Setting cannot change",
        "Internal error",
        "Invalid dependencies",
        "Invalid request",
        "Invalid strategy",
        "Invalid client",
        "Invalid configuration",
        "Unsupported content type",
        "Invalid format",
        "Invalid identity",
        "Invalid package source",
        "Invalid lifecycle settings",
        "Invalid page",
        "Stored configuration invalid",
        "Invalid namespace",
        "Invalid timeout",
        "Invalid user ID",
        "Kubeconfig not found",
        "Credential changed",
        "Credential exists",
        "Credential expired",
        "Credential not found",
        "Log stream interrupted",
        "Logs unavailable",
        "Machine type not found",
        "Endpoint requires authentication",
        "Approval required",
        "Method not allowed",
        "CPU missing",
        "Memory missing",
        "Field missing",
        "Namespace not created",
        "Nothing running",
        "No running pod",
        "Node group removal blocked",
        "Not found",
        "Not ready",
        "Integration failed",
        "Integration not found",
        "Integrations unavailable",
        "Topic not found",
        "Subscription failed",
        "Subscription not found",
        "Topics unavailable",
        "Unsubscribe failed",
        "Invalid notification settings",
        "Cancelled",
        "Operation ended",
        "Operation failed",
        "Could not start",
        "Organization exists",
        "Organization not found",
        "Owner changed",
        "Managed by AstroPulse",
        "Pods not found",
        "Checks failed",
        "Earlier logs gone",
        "Pricing invalid",
        "Pricing not found",
        "Pricing version not found",
        "Profiles unavailable",
        "Purchase option not supported",
        "Record-only removal not allowed",
        "Redeploy did not start",
        "Region not found",
        "Not managed by AstroPulse",
        "Request too large",
        "Rollback not allowed",
        "Rollback did not start",
        "Key not valid",
        "Key refused",
        "Key not confirmed",
        "Service account archived",
        "Service account conflict",
        "Service account invalid",
        "Service account not found",
        "Service accounts unavailable",
        "Service not found",
        "Service unavailable",
        "Init container",
        "Status unavailable",
        "Deployment status unavailable",
        "Stop stuck",
        "Resume failed",
        "Sync failed",
        "Stop failed",
        "Tier not deleted",
        "Tier not found",
        "Timed out",
        "Too many pods",
        "Too many requests",
        "Not authenticated",
        "Unsafe configuration",
        "Unsafe option",
        "Unsupported add-on",
        "Unsupported version",
        "Unsupported cleanup option",
        "Unsupported update option",
        "Unsupported update strategy",
        "User exists",
        "Already a member",
        "User not found",
        "Not a member",
        "User profile not found",
        "Delegation not allowed",
        "Credential path not valid",
        "Request not valid",
        "Not allowed by policy",
        "Purpose required",
        "Too many vault requests",
        "Credential not valid for its kind",
        "Outside your scope",
        "Credential not named",
        "Vault sign-in not valid",
        "Not signed in to the vault",
        "Credential storage unavailable",
        "Unknown credential kind",
        "Credential too large",
        "Credential version destroyed",
        "Credential version not found",
        "Waiting for credentials",
        "Watch failed",
        "Watch interrupted",
        "Zone not found",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in ErrorReason],
    [
        "The API key has expired.",
        "The API key is not valid.",
        "The request carries no API key.",
        "No API key matches the one sent.",
        "The organization already has as many API keys as its plan allows; revoke one before creating another.",
        "The API key has been revoked.",
        "The caller may not do this.",
        "The access policy does not keep its API keys in AstroPulse.",
        "The add-on is installed and removed with the cluster, so it cannot be removed on its own.",
        "This configuration's last deployment failed, so it was not started again.",
        "The add-on's configuration is not valid; the message says why.",
        "The add-on was not removed, because an object it manages still has to be released.",
        "Removing the add-on failed.",
        "An add-on this one needs is not on the cluster and was not applied first.",
        "Installing or changing the add-on did not complete.",
        "The cluster's add-ons could not be read.",
        "The add-on cannot run on this cluster.",
        "The add-on is not installed on the cluster.",
        "The cluster already runs this add-on's software, installed another way.",
        "The application named is not a managed add-on.",
        "Cloud access or infrastructure the add-on needs could not be confirmed, so nothing was changed.",
        "The add-on did not become ready in time.",
        "The add-on release asked for or recorded is not available; update the add-on to its recommended release.",
        "A component's sizing is not valid; the message names the field and why.",
        "The add-on's status could not be read.",
        "This version of the add-on is past its end of support.",
        "The cluster's agent does not offer a feature the request needs.",
        "Agent certificates for this cluster were issued too often; try again later.",
        "A new agent certificate could not be written because AstroPulse can't reach the cluster's API; apply it from a machine that can.",
        "The cluster's API refused writing the agent's new certificate.",
        "No release of the AstroPulse agent is published yet.",
        "The cluster's agent is not connected to AstroPulse.",
        "The request needs the AstroPulse agent, and the cluster has none.",
        "Cluster agents are not enabled on this AstroPulse installation.",
        "The connection to cluster agents is not configured.",
        "Cluster agents cannot be reached right now; try again shortly.",
        "A resource with that name already exists.",
        "The user named already owns the organization.",
        "An application with that name already exists.",
        "The deployment could not be confirmed because the cluster stayed unreachable too long.",
        "Something still holds the application, so it was not deleted.",
        "Deleting the application failed.",
        "The delete request is not valid.",
        "The application's deployment failed.",
        "An application cannot move between user-managed and AstroPulse-managed.",
        "The application or its cluster is not set up for what the request asks.",
        "The application exists but has not been deployed to its cluster yet.",
        "The application does not exist.",
        "The deployment succeeded, but the application's workloads are now unhealthy.",
        "An application profile with that name already exists.",
        "Deleting the application profile failed.",
        "The application profile does not exist.",
        "The change cannot be applied to the running application, because a field cannot change or the change is impossible.",
        "The architecture does not exist.",
        "The architecture is not supported.",
        "No availability data exists for the request.",
        "The AstroPulse service that made the request may not make it.",
        "The organization owner's role cannot be changed.",
        "A user cannot be removed from their default organization.",
        "The organization's owner cannot be removed.",
        "A default organization's ownership cannot be transferred.",
        "The machine category is not supported.",
        "Some of the checks a cluster create runs first didn't finish; nothing was changed, so try again.",
        "The cloud's regions and prices are not loaded yet; try again shortly.",
        "AstroPulse holds no data for the cloud provider.",
        "A cluster with that name already exists.",
        "AstroPulse could not connect to the cluster for this stream.",
        "The application's cluster could not be resolved.",
        "A cluster AstroPulse created is deleted, not unregistered.",
        "Removing the application from its cluster failed.",
        "The cluster could not be read.",
        "The cluster does not exist.",
        "The cluster is not in a state that accepts this request.",
        "Another operation on the cluster must finish first.",
        "AstroPulse could not reach the cluster.",
        "AstroPulse is not configured for this request.",
        "The configuration is not for this add-on.",
        "The request conflicts with the resource's current state.",
        "The container has not started, so it has no logs yet.",
        "The cluster's credentials cannot be refreshed right now.",
        "Refreshing the cluster's credentials failed.",
        "A credential AstroPulse keeps can't be read; revoke it, then create or connect it again.",
        "AstroPulse could not read or write its records.",
        "What depends on the resource could not be checked.",
        "Something else depends on the resource, so the request was refused.",
        "The deployment could not be prepared.",
        "AstroPulse could not reach its deployment service for this stream.",
        "AstroPulse's deployment service could not report the application.",
        "Deployments resume on their own once it is back.",
        "AstroPulse's deployment service could not be reached.",
        "The latest events could not be read; the ones shown may be out of date.",
        "Not every event could be read; retry.",
        "The application's events could not be streamed.",
        "Forced resyncs are limited; try again later.",
        "GitHub no longer accepts your GitHub authorization; sign in to GitHub again.",
        "The GitHub App is already installed.",
        "The GitHub App installation is not valid.",
        "The GitHub App installation does not exist.",
        "The GitHub App installation is suspended.",
        "Access to the GitHub App installation was denied.",
        "The repository has no file or directory at that path.",
        "An owner of the GitHub account must approve a permission the GitHub App needs.",
        "The server answered with an error status.",
        "The identity is already linked to another user.",
        "The access policy's identity provider could not be reached.",
        "The identity could not be resolved.",
        "A setting of the installed add-on cannot be changed after install.",
        "AstroPulse failed to handle the request; try again, and quote the trace ID if it persists.",
        "The add-ons requested together depend on each other in a way that cannot be installed.",
        "A field of the request is missing or not valid; `details.fields` lists each one.",
        "The strategy for applying several add-ons is not supported.",
        "The client named in the request is not recognized.",
        "The configuration is not valid.",
        "The request body must be JSON.",
        "A value is not in the expected format.",
        "The identity is missing required fields.",
        "The package source override is not valid.",
        "The application's lifecycle settings are not valid.",
        "The page size or offset is not valid.",
        "The add-on's saved configuration could not be read.",
        "The add-on cannot be installed in that namespace.",
        "The timeout is not valid.",
        "The user ID is not valid.",
        "No kubeconfig is available for the cluster.",
        "The credential changed since it was read; read it again and retry.",
        "A credential by that name already exists.",
        "The credential's lease has ended.",
        "The organization holds no such credential.",
        "Reading the logs stopped with an error.",
        "The container's logs could not be read.",
        "The machine type does not exist.",
        "The rollback deploys the earlier version with the endpoint's current access policy; run it again.",
        "The operation needs to be approved before it runs.",
        "The route does not accept this HTTP method.",
        "The tier names no CPU requirement.",
        "The tier names no memory requirement.",
        "A required field is missing.",
        "The application's namespace could not be created.",
        "No operation was running on the cluster when the stream opened.",
        "The application has no running pod to read logs from.",
        "The cloud account stops the node group from being removed.",
        "The resource does not exist.",
        "The resource is not ready for this request yet.",
        "The notification integration could not be changed.",
        "The notification integration does not exist.",
        "The notification integrations could not be read.",
        "A required notification topic does not exist.",
        "The notification subscription could not be changed.",
        "The notification subscription does not exist.",
        "The notification topics could not be read.",
        "Unsubscribing from notifications failed.",
        "The notification settings are not valid.",
        "The operation was cancelled.",
        "The operation the stream followed has ended.",
        "The operation failed; the message says why.",
        "The operation could not be started.",
        "An organization with that name already exists.",
        "The organization does not exist.",
        "The organization's owner changed during the transfer.",
        "The resource is managed by AstroPulse and cannot be changed this way.",
        "The application's pods could not be listed.",
        "A check the cluster create runs first failed, so nothing was created.",
        "The logs of the container's previous run are no longer kept.",
        "The pricing data is not valid.",
        "No pricing data exists.",
        "The pricing version does not exist.",
        "The application profiles could not be read.",
        "The purchase option is not supported.",
        "Only a self-hosted cluster whose stored key is gone can be removed from AstroPulse without deleting it.",
        "The redeploy could not be started.",
        "The region does not exist.",
        "AstroPulse doesn't create or change a registered cluster; make the change with the cluster's own tools.",
        "The request body is too large.",
        "This add-on cannot be rolled back.",
        "The rollback could not be started.",
        "The key sent is not a valid key for the cloud; download it again, then connect again.",
        "The key cannot be stored for this cluster; the message says why.",
        "AstroPulse couldn't confirm which account the key belongs to; try again in a minute.",
        "The service account is archived.",
        "A service account with that name already exists.",
        "The service account request is not valid.",
        "The service account does not exist.",
        "The service accounts could not be read or written.",
        "The service does not exist.",
        "An AstroPulse service could not be reached; try again shortly.",
        "The logs shown are an init container's, because the pod's containers start only after it finishes.",
        "AstroPulse could not read the status right now; retry shortly.",
        "The current deployment status could not be read; retry shortly.",
        "The running operation did not stop.",
        "The suspended operation could not be resumed.",
        "The application could not be synced.",
        "Stopping the running operation failed.",
        "Deleting the tier failed.",
        "The tier does not exist.",
        "The request did not finish in time.",
        "The application has more pods than one log stream reads; name a pod.",
        "The rate limit was reached; try again later.",
        "The request carries no valid credential.",
        "The configuration was refused because it is unsafe.",
        "A deployment option was refused because it is unsafe.",
        "AstroPulse does not offer this add-on.",
        "AstroPulse does not offer this version of the add-on.",
        "The cleanup option is not supported.",
        "The update option is not supported.",
        "The update strategy is not supported.",
        "The user already exists.",
        "The user is already a member of the organization.",
        "The user does not exist.",
        "The user is not a member of the organization.",
        "The user profile does not exist.",
        "The caller may not act for the account it named.",
        "The credential's path is not a valid one.",
        "A field of the request breaks its own rules, such as a length or range.",
        "The vault's policy does not allow this request.",
        "The request must say why it reads the credential.",
        "The credential vault had too many requests; try again shortly.",
        "The credential's fields don't match what its kind requires.",
        "The credential is outside what the caller may reach.",
        "The request must name which credentials it means.",
        "The token the credential vault was sent is not valid.",
        "The request reached the credential vault without a token.",
        "AstroPulse's credential storage can't be reached right now; try again in a minute.",
        "The vault has no credential kind of that name.",
        "The credential is larger than the vault stores.",
        "That version of the credential was destroyed and can't be read.",
        "The credential has no version by that number.",
        "The cluster's credentials are being refreshed; the stream resumes once they are.",
        "AstroPulse could not start watching for changes.",
        "The stream of changes stopped with an error.",
        "The zone does not exist.",
    ],
))


# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class NoticeCode(str, Enum):
    """
    NoticeCode
    """

    """
    allowed enum values
    """
    HostnameTaken = 'HostnameTaken'
    ScalingUnconfirmed = 'ScalingUnconfirmed'
    NoIngressController = 'NoIngressController'
    EndpointTLSMode = 'EndpointTLSMode'
    ScalingFixed = 'ScalingFixed'
    ScalingCPUOnGPU = 'ScalingCPUOnGPU'
    ScalingQueueKept = 'ScalingQueueKept'
    ScalingQueueChosen = 'ScalingQueueChosen'
    ModelMemoryBelowDefault = 'ModelMemoryBelowDefault'
    ModelKVCacheSize = 'ModelKVCacheSize'
    ModelMultimodalLimitHigh = 'ModelMultimodalLimitHigh'
    ModelContextAboveModel = 'ModelContextAboveModel'
    ModelCacheBelowArtifact = 'ModelCacheBelowArtifact'
    ClusterOperationRunning = 'ClusterOperationRunning'
    GPUQuotaInsufficient = 'GPUQuotaInsufficient'
    GPUQuotaShort = 'GPUQuotaShort'
    GPUQuotaUnverified = 'GPUQuotaUnverified'
    GPUQuotaNodeGroupLimited = 'GPUQuotaNodeGroupLimited'
    GPUCapacityUnverified = 'GPUCapacityUnverified'
    ClusterOperationInProgress = 'ClusterOperationInProgress'
    ClusterNotReady = 'ClusterNotReady'
    KubeconfigExpired = 'KubeconfigExpired'
    ClusterAlreadyExists = 'ClusterAlreadyExists'
    ClusterDeleteFailed = 'ClusterDeleteFailed'
    ClusterDeleteApplicationsRemain = 'ClusterDeleteApplicationsRemain'
    ClusterDeleteDNSUnconfirmed = 'ClusterDeleteDNSUnconfirmed'
    ClusterDeleteVolumesKept = 'ClusterDeleteVolumesKept'
    ClusterDeleteVolumesUnlisted = 'ClusterDeleteVolumesUnlisted'
    ClusterDeleteAgentOutdated = 'ClusterDeleteAgentOutdated'
    ClusterRegistrationUnfinished = 'ClusterRegistrationUnfinished'
    ClusterUpdateFailed = 'ClusterUpdateFailed'
    ClusterOperationNotCancellable = 'ClusterOperationNotCancellable'
    ClusterCancelAccepted = 'ClusterCancelAccepted'
    ClusterCancelPreview = 'ClusterCancelPreview'
    ClusterUpdateReplacing = 'ClusterUpdateReplacing'
    ClusterUpdateReplacePreview = 'ClusterUpdateReplacePreview'
    CancelNodeGroupRemoved = 'CancelNodeGroupRemoved'
    CancelNodeGroupNotCreated = 'CancelNodeGroupNotCreated'
    CancelNodeGroupRemovalFailed = 'CancelNodeGroupRemovalFailed'
    CancelNodeGroupRemovalRefused = 'CancelNodeGroupRemovalRefused'
    CancelNodeGroupRemovalTimedOut = 'CancelNodeGroupRemovalTimedOut'
    ClusterAmiFamilyUnavailable = 'ClusterAmiFamilyUnavailable'
    AmiFamiliesUnverified = 'AmiFamiliesUnverified'
    EndpointChanged = 'EndpointChanged'
    EndpointNoAPIKeys = 'EndpointNoAPIKeys'
    TokenIssuerMismatch = 'TokenIssuerMismatch'
    TokenClaimTypeMismatch = 'TokenClaimTypeMismatch'
    CloudAccountConnected = 'CloudAccountConnected'
    CloudConnectFailed = 'CloudConnectFailed'
    CloudConnectPreparing = 'CloudConnectPreparing'
    CloudConnectRestart = 'CloudConnectRestart'
    CloudConnectCreateStack = 'CloudConnectCreateStack'
    CloudConnectRunSetupScript = 'CloudConnectRunSetupScript'
    CloudConnectUpdateStack = 'CloudConnectUpdateStack'
    SelfHostedSetupNotStarted = 'SelfHostedSetupNotStarted'
    SelfHostedSetupReady = 'SelfHostedSetupReady'
    SelfHostedSetupFailed = 'SelfHostedSetupFailed'
    SelfHostedSetupPreparing = 'SelfHostedSetupPreparing'
    SelfHostedSetupCreateKey = 'SelfHostedSetupCreateKey'
    SelfHostedSetupCreateStack = 'SelfHostedSetupCreateStack'
    NodeGroupRemovalProviderCompute = 'NodeGroupRemovalProviderCompute'
    NodeGroupRemovalNotSupported = 'NodeGroupRemovalNotSupported'
    NodeGroupRemovalLastSystemGroup = 'NodeGroupRemovalLastSystemGroup'
    AddonUnchanged = 'AddonUnchanged'
    AddonNotInstalled = 'AddonNotInstalled'
    AddonNotRecorded = 'AddonNotRecorded'
    ClusterUpdateUnchanged = 'ClusterUpdateUnchanged'
    ClusterUpdateReapplies = 'ClusterUpdateReapplies'
    AddonDeployInProgress = 'AddonDeployInProgress'
    AddonConfigurationFailed = 'AddonConfigurationFailed'
    CostSpotGPUNotPriced = 'CostSpotGPUNotPriced'
    CostGPUNotPriced = 'CostGPUNotPriced'
    CostAttributionInconsistent = 'CostAttributionInconsistent'
    CostAgentUpgradeRequired = 'CostAgentUpgradeRequired'
    CostManagementNoRate = 'CostManagementNoRate'
    CostNotMetered = 'CostNotMetered'
    CostNoPriceSource = 'CostNoPriceSource'
    CostCountNotRecorded = 'CostCountNotRecorded'
    CostPriceStale = 'CostPriceStale'
    CostPriceUnavailable = 'CostPriceUnavailable'
    CostSpotPriceUnavailable = 'CostSpotPriceUnavailable'
    CostListPriceUnavailable = 'CostListPriceUnavailable'
    AgentCertificateExpiring = 'AgentCertificateExpiring'
    AgentCertificateExpired = 'AgentCertificateExpired'
    AgentCertificateUnreachable = 'AgentCertificateUnreachable'
    AgentCertificateWriteRefused = 'AgentCertificateWriteRefused'
    AgentUpgradeRequired = 'AgentUpgradeRequired'
    TLSAcmeEmailMissing = 'TLSAcmeEmailMissing'
    TLSNoChallengeAvailable = 'TLSNoChallengeAvailable'
    TLSGatewayNeedsDNSZone = 'TLSGatewayNeedsDNSZone'
    TLSStagingCertificates = 'TLSStagingCertificates'
    TLSSelfSignedCertificates = 'TLSSelfSignedCertificates'
    TLSIssuerTurnedOff = 'TLSIssuerTurnedOff'
    TLSLetsEncryptIssuersCreated = 'TLSLetsEncryptIssuersCreated'
    TLSDNSRoleRestart = 'TLSDNSRoleRestart'
    LoadBalancerReplaced = 'LoadBalancerReplaced'
    LoadBalancerLeftRunning = 'LoadBalancerLeftRunning'
    EndpointRemoved = 'EndpointRemoved'
    ScannerNotInstalled = 'ScannerNotInstalled'
    NothingToScan = 'NothingToScan'
    ImagesNotScannable = 'ImagesNotScannable'
    ScanPending = 'ScanPending'
    ScanOverdue = 'ScanOverdue'
    ScanRegistryDenied = 'ScanRegistryDenied'
    ScanTimedOut = 'ScanTimedOut'
    ScanResultNotStored = 'ScanResultNotStored'
    ScanNoteUnreadable = 'ScanNoteUnreadable'
    ClusterDeleteApplicationsNotStarted = 'ClusterDeleteApplicationsNotStarted'
    ClusterVersionUnconfirmed = 'ClusterVersionUnconfirmed'
    ClusterMajorUpgrade = 'ClusterMajorUpgrade'
    ClusterUpgradePathNote = 'ClusterUpgradePathNote'
    ClusterNodeGroupRecreated = 'ClusterNodeGroupRecreated'
    ClusterNodeGroupTaintsChange = 'ClusterNodeGroupTaintsChange'
    ClusterAmiFamilyChange = 'ClusterAmiFamilyChange'
    ClusterImageTypeChange = 'ClusterImageTypeChange'
    ClusterUpgradeChannelChange = 'ClusterUpgradeChannelChange'
    ClusterControlPlaneResize = 'ClusterControlPlaneResize'
    ClusterGPUPoolBuysSpot = 'ClusterGPUPoolBuysSpot'
    ClusterGPUPoolDropsSpot = 'ClusterGPUPoolDropsSpot'
    AddonSettingsUnsupported = 'AddonSettingsUnsupported'
    AddonVersionChange = 'AddonVersionChange'
    AddonConfigurationAdvice = 'AddonConfigurationAdvice'
    AddonModelsRedeploy = 'AddonModelsRedeploy'
    AddonModelReplicasRestart = 'AddonModelReplicasRestart'
    AddonQueueCapacityChange = 'AddonQueueCapacityChange'
    AddonCostSettingKept = 'AddonCostSettingKept'
    AddonModelMetricsChange = 'AddonModelMetricsChange'
    AddonFollowUp = 'AddonFollowUp'
    AddonDependencies = 'AddonDependencies'
    ScannerRestart = 'ScannerRestart'
    KarpenterDisruptionChange = 'KarpenterDisruptionChange'
    KarpenterIdleCost = 'KarpenterIdleCost'
    KarpenterLimitChange = 'KarpenterLimitChange'
    KarpenterNodesReplaced = 'KarpenterNodesReplaced'
    KarpenterGPUNodesReplaced = 'KarpenterGPUNodesReplaced'
    KarpenterGPUSpot = 'KarpenterGPUSpot'
    KarpenterGPUExpiry = 'KarpenterGPUExpiry'
    KarpenterGPUCostCeiling = 'KarpenterGPUCostCeiling'
    KarpenterGPUCostUnknown = 'KarpenterGPUCostUnknown'
    KarpenterGPUIdleWait = 'KarpenterGPUIdleWait'
    KarpenterInterruptionQueueOn = 'KarpenterInterruptionQueueOn'
    ClusterNodeGroupShrinks = 'ClusterNodeGroupShrinks'
    ClusterUpdateReadinessNotAssessed = 'ClusterUpdateReadinessNotAssessed'
    AcceleratorNoGPUNodes = 'AcceleratorNoGPUNodes'
    WorkloadQueueJobsBlocked = 'WorkloadQueueJobsBlocked'
    ClusterSystemPodsOnSpot = 'ClusterSystemPodsOnSpot'
    ResourceNotFound = 'ResourceNotFound'
    ClusterCreateFailed = 'ClusterCreateFailed'
    ClusterOperationFailed = 'ClusterOperationFailed'
    ClusterApprovalDeclined = 'ClusterApprovalDeclined'
    ClusterNotCreatedYet = 'ClusterNotCreatedYet'
    ClusterNeverCreated = 'ClusterNeverCreated'
    ClusterDeleted = 'ClusterDeleted'
    AgentConnectionUnusable = 'AgentConnectionUnusable'
    AgentNotConnected = 'AgentNotConnected'
    AgentNotReporting = 'AgentNotReporting'
    AgentConnectionUnchecked = 'AgentConnectionUnchecked'
    AgentNotConnectedYet = 'AgentNotConnectedYet'
    SelfHostedKeyMissing = 'SelfHostedKeyMissing'
    SelfHostedKeyUnreadable = 'SelfHostedKeyUnreadable'
    AddonFailed = 'AddonFailed'
    AddonUnhealthy = 'AddonUnhealthy'
    AddonRollbackUnfinished = 'AddonRollbackUnfinished'
    AddonReleaseUnavailable = 'AddonReleaseUnavailable'
    AddonReleaseNotOffered = 'AddonReleaseNotOffered'
    AddonQueueNamespacesStale = 'AddonQueueNamespacesStale'
    ApplicationDeployFailed = 'ApplicationDeployFailed'
    ApplicationUpdateNotApplied = 'ApplicationUpdateNotApplied'
    ApplicationNotServing = 'ApplicationNotServing'
    ApplicationUpdateNotRollingOut = 'ApplicationUpdateNotRollingOut'
    ApplicationLiveStateUnread = 'ApplicationLiveStateUnread'
    ApplicationCannotScale = 'ApplicationCannotScale'
    ApplicationRollbackWindowUnconfirmed = 'ApplicationRollbackWindowUnconfirmed'
    ApplicationDeleteFailed = 'ApplicationDeleteFailed'
    ClientOutdated = 'ClientOutdated'
    NotificationChannelNotInPlan = 'NotificationChannelNotInPlan'
    FeatureNotInPlan = 'FeatureNotInPlan'
    PlanLimitReached = 'PlanLimitReached'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NoticeCode from a JSON string"""
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
    [member._value_ for member in NoticeCode],
    [
        "Hostname already taken",
        "Scaling signal may not be collected",
        "Nothing may serve this hostname",
        "Where your app will be served",
        "Model runs at a fixed replica count",
        "CPU scaling doesn't follow GPU load",
        "Model keeps scaling on waiting requests",
        "Model moves to scaling on waiting requests",
        "Memory is below the default",
        "Check the KV cache size",
        "Media limit reserves a lot of memory",
        "Context is longer than the model's",
        "Cache size is smaller than the model",
        "Waiting for a cluster operation",
        "GPU quota too low",
        "GPU quota may be too low",
        "GPU quota not checked",
        "Node group cannot add GPU nodes",
        "GPU capacity not checked",
        "An operation is running on the cluster",
        "The cluster isn't ready",
        "Kubeconfig expired",
        "Cluster already exists",
        "Last delete failed",
        "Applications were still being removed",
        "DNS records may still be in your zone",
        "Volumes kept in your cloud account",
        "Some volumes are not accounted for",
        "The cluster's agent needs an update",
        "Registration did not finish",
        "Last update failed",
        "This operation can't be cancelled",
        "Cancelling the running update",
        "Cancelling would stop the running update",
        "Replacing the running update",
        "This change replaces the running update",
        "Node group removed",
        "Node group was not created",
        "Node group left in the cluster",
        "Node group kept in the cluster",
        "Node group removal did not finish",
        "AMI family not offered for this version",
        "AMI families not checked",
        "The endpoint changed meanwhile",
        "The access policy has no API keys",
        "Token from another issuer",
        "Claim is not the type the policy reads",
        "Cloud account connected",
        "Connecting the cloud account did not finish",
        "Preparing your cloud connection",
        "This connection has no setup link",
        "Create the AstroPulse role in AWS",
        "Run the setup script in Cloud Shell",
        "Update the AstroPulse stack in AWS",
        "No self-hosted setup recorded",
        "Self-hosted setup complete",
        "Self-hosted setup failed",
        "Preparing your cluster setup",
        "Create the service account key",
        "Create the setup stack in AWS",
        "No node groups to remove",
        "Node group removal isn't available yet",
        "Last node group that can run system pods",
        "Add-on unchanged",
        "Add-on isn't installed",
        "Add-on has no deployment yet",
        "Cluster unchanged",
        "Unchanged node groups are applied again",
        "Already being deployed",
        "This configuration already failed",
        "Spot GPU usage isn't priced",
        "GPU usage isn't priced",
        "Some hours can't be split by application",
        "Agent too old to price management",
        "No cluster management rate",
        "Some charges aren't measured",
        "No published price for some charges",
        "Some charges aren't counted",
        "Some charges use the last prices read",
        "Some charges couldn't be priced",
        "Spot nodes are priced at On-Demand rates",
        "This cluster's costs aren't priced",
        "Agent certificate expires soon",
        "Agent certificate expired",
        "Cluster API unreachable",
        "Agent certificate write refused",
        "Agent update required",
        "Let's Encrypt needs a contact email",
        "Certificates cannot be issued yet",
        "Gateway endpoints need a DNS zone",
        "Endpoints use Let's Encrypt staging",
        "Endpoints use self-signed certificates",
        "AstroPulse creates no certificate issuer",
        "Let's Encrypt issuers will be created",
        "cert-manager restarts to use the DNS role",
        "Load balancer is replaced",
        "An earlier load balancer is still running",
        "Endpoint is removed",
        "Vulnerability scanner isn't installed",
        "Nothing to scan",
        "No image could be scanned",
        "No scan result yet",
        "Scan results are overdue",
        "A registry refused the scanner",
        "Scan timed out",
        "Scan result wasn't stored",
        "Some images couldn't be scanned",
        "Applications could not be removed",
        "Target version support is unconfirmed",
        "Major Kubernetes version upgrade",
        "Note on this upgrade path",
        "A node group is recreated",
        "Node group taints change",
        "Nodes are replaced for the AMI family",
        "Nodes are recreated for the image type",
        "Nodes roll for the upgrade channel",
        "The control plane is resized",
        "GPU nodes on Spot may be reclaimed",
        "The GPU pool stops buying Spot",
        "Some settings are not supported",
        "The add-on version changes",
        "Check this add-on configuration",
        "Model applications redeploy",
        "Model replicas restart",
        "The workload queue is resized",
        "A cost setting is kept",
        "Model metrics collection changes",
        "A follow-up step needs attention",
        "What this add-on needs",
        "The vulnerability scanner restarts once",
        "Node removal settings change",
        "Idle nodes stay billed",
        "A node pool limit changes",
        "Nodes will be replaced",
        "GPU nodes will be replaced",
        "GPU pool may buy Spot",
        "GPU nodes expire",
        "GPU pool cost ceiling",
        "GPU pool cost unknown",
        "Empty GPU nodes are billed until removed",
        "The interruption queue is always on",
        "Pods move off the nodes given up",
        "Readiness not assessed",
        "Nothing to check yet: no GPU nodes",
        "Jobs can't be admitted",
        "System pods run only on Spot nodes",
        "Not found in this organization",
        "Creating the cluster failed",
        "The last cluster operation failed",
        "Creation was not approved",
        "The cluster isn't created yet",
        "The cluster was never created",
        "The cluster has been deleted",
        "The agent's connection isn't working",
        "The agent isn't connected",
        "The agent hasn't reported recently",
        "Agent connection not checked",
        "The agent hasn't connected yet",
        "No stored key for this cluster",
        "The stored key can't be read",
        "The add-on's last change failed",
        "The add-on isn't healthy",
        "The last rollback did not finish",
        "This add-on release isn't available",
        "Update this add-on",
        "The add-on gives a queue to namespaces nothing uses",
        "Deployment failed",
        "The last update was not applied",
        "The application isn't serving",
        "The update isn't rolling out",
        "Showing the last recorded status",
        "The application can't scale",
        "Rollback eligibility not confirmed",
        "Deleting the application failed",
        "This CLI is too old",
        "Not included in your plan",
        "Not available on your plan",
        "Plan limit reached",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in NoticeCode],
    [
        "The application's name is taken under the domain, so the application is served at its generated name.",
        "The cluster's metrics may not collect the signal the model scales on.",
        "The application is exposed through Ingress on a cluster with no Ingress add-on, so nothing may serve its hostname.",
        "Where an application exposed through Ingress will be served, and which certificate it presents.",
        "The model runs at a fixed replica count because the cluster cannot scale it on waiting requests.",
        "A GPU model scales on CPU, which does not follow the load on its GPU.",
        "A running model narrowed to one replica count keeps scaling on waiting requests.",
        "A running model that leaves a fixed replica count without naming a signal scales on waiting requests from now on.",
        "The model's memory is below the default for its runtime, so a larger model may run out of it.",
        "The KV cache size has no effect on the model's runtime, or cannot be checked against its GPU.",
        "A media limit is high enough that a replica's memory may not hold what the runtime reserves for it.",
        "The context length asked for is longer than the one the model's own files declare, so the model won't start.",
        "The model cache size is smaller than the model's files, so the cache holds more than its size counts.",
        "An operation runs on the cluster, and the application deploys once it finishes.",
        "The cloud account's quota cannot launch the node a GPU replica needs.",
        "The cloud account's quota looks too low for a GPU node, but the request goes ahead, for example on capacity reservations.",
        "The cloud account's GPU quota could not be checked; the request goes ahead.",
        "A GPU node group runs, but the quota cannot launch another of its nodes.",
        "Whether the cluster has the GPU the model asks for could not be checked; the request goes ahead.",
        "Another operation on the cluster must finish first.",
        "The cluster is not in a state that accepts this request.",
        "The kubeconfig's lifetime has ended, so it gets no more access tokens.",
        "A cluster with that name already exists.",
        "A create names a cluster whose last delete failed.",
        "A cluster delete went on while applications on the cluster were still being removed.",
        "A cluster delete went on before the DNS records of its applications were confirmed removed.",
        "A cluster delete leaves the cluster's volumes in the cloud account.",
        "A cluster delete could not list the cluster's volumes, or cannot say whether some were removed.",
        "A cluster delete stopped because the cluster's agent is too old to report what the delete waits for.",
        "A create names a registered cluster whose registration did not finish.",
        "A create names a cluster whose last update failed.",
        "A create, a delete or a registration runs to its end once started.",
        "The running operation was asked to stop and cleans up on its way out.",
        "What cancelling the running update would do, before it is sent.",
        "The running update was asked to stop, and the change sent to replace it starts once it has.",
        "What sending a change that replaces the running update would do, before it is sent.",
        "A node group the cancelled operation was adding was removed.",
        "The operation stopped before the node group existed.",
        "The cloud failed or refused to remove the node group.",
        "Removing the node group would break a rule the cluster keeps.",
        "The node group's removal did not finish in time.",
        "The node groups' AMI family has no image for the cluster's Kubernetes version in its region.",
        "The AMI families each Kubernetes version offers are listed once a cloud account is chosen.",
        "Another change to the endpoint happened first, so closing or reopening it did not.",
        "The endpoint is not serving because its access policy holds no API keys.",
        "A token was issued by another provider than the one the access policy accepts.",
        "A required claim in a token is a list where the access policy reads a string, or the reverse.",
        "The cloud account is connected, and clusters can be created in it.",
        "Connecting the cloud account stopped before AstroPulse could confirm access.",
        "AstroPulse is preparing the setup step for the cloud account.",
        "The connection started before setup links were available, so it has to be started again.",
        "The next step is creating the AstroPulse role in the AWS account from the setup link.",
        "The next step is running the setup script in the cloud's shell.",
        "The AstroPulse stack in the AWS account is out of date and needs an update.",
        "No setup is recorded for the self-hosted cluster.",
        "The self-hosted cluster's setup is complete and its credentials are stored in AstroPulse.",
        "A step of the self-hosted cluster's setup failed.",
        "AstroPulse is preparing the self-hosted cluster's setup step.",
        "The next step is creating the service account key the self-hosted cluster uses.",
        "The next step is creating the self-hosted cluster's setup stack in the AWS account.",
        "The cloud provider runs the cluster's compute, so it has no node groups to remove.",
        "Removing node groups isn't available for this kind of cluster yet.",
        "No other node group could run the cluster's system pods.",
        "The add-on already runs the applied configuration, so nothing was started.",
        "The add-on the request names is not installed on the cluster.",
        "The add-on is listed on the cluster but has no deployment yet, so there is nothing to stream.",
        "The cluster already is as the update asks, so nothing was started.",
        "The update applies node groups it does not change, as asked, to label their nodes and create what the cluster is missing.",
        "The add-on is already being deployed with the applied configuration.",
        "This configuration's last deployment failed, so it was not started again.",
        "Usage on Spot GPU nodes isn't priced because the price sheet has no Spot GPU rate.",
        "Usage on GPU nodes isn't priced because the price sheet sets no rate for them.",
        "For some hours, applications were charged more than the namespaces they run in, so workloads outside applications aren't priced.",
        "Cluster management isn't priced because the cluster's agent is too old for the price sheet's management rate.",
        "Cluster management isn't priced because the price sheet sets no cluster management rate.",
        "Some charges are billed by a volume that isn't measured, such as the data a NAT gateway processes, so they aren't priced.",
        "Some charges outside the cluster have no published price in the cluster's region, so they aren't priced.",
        "Some charges outside the cluster aren't priced because how many the cluster has isn't recorded.",
        "Some charges are priced at the last published prices read, because the latest couldn't be read.",
        "Some charges aren't priced for some hours because the region's published prices couldn't be read yet.",
        "Spot prices can't be read on the cluster, so its Spot nodes are priced at On-Demand rates.",
        "The cloud's list prices can't be read on the cluster, so its costs aren't priced until a price sheet is set.",
        "The agent's certificate expires within 14 days and was not renewed.",
        "The agent's certificate expired, so the agent can't connect.",
        "A new agent certificate could not be written because AstroPulse can't reach the cluster's API; apply it from a machine that can.",
        "The cluster's API refused writing the agent's new certificate.",
        "The agent is too old to renew its certificate, so the certificate expires unless the agent is updated.",
        "Let's Encrypt is the issuer, and no contact email is set.",
        "Let's Encrypt can verify no hostname on the cluster, so it can issue no certificate.",
        "Endpoints behind the gateway get Let's Encrypt certificates only through a DNS zone.",
        "Endpoints get certificates from Let's Encrypt staging, which browsers do not trust.",
        "Endpoints get self-signed certificates, which clients must be told to trust.",
        "The add-on creates no certificate issuer.",
        "The apply creates the Let's Encrypt issuers.",
        "The apply connects the cluster's DNS role, which restarts cert-manager.",
        "The deploy replaces the endpoint's load balancer, so its address changes and DNS follows.",
        "A deploy AstroPulse started on its own replaced the application's load balancer and left the earlier one running.",
        "The apply takes away the endpoint the application has now.",
        "The Vulnerability Scanning add-on is not installed on the cluster.",
        "No workload runs in the namespaces the scanner covers.",
        "No image on the cluster could be scanned.",
        "The scanner has not finished its first scan.",
        "No scan report has arrived for longer than one scan interval.",
        "A registry refused the scanner some images.",
        "Some scans did not finish within their time limit.",
        "Some scans finished but their results could not be stored.",
        "The scanner could not scan some images, for a reason it did not name.",
        "A cluster delete stopped because removing its applications could not start; nothing was removed.",
        "The supported Kubernetes versions could not be read, so the target version was checked against the upgrade rules alone.",
        "The update moves the cluster to a new major Kubernetes version.",
        "Something to know about upgrading between these Kubernetes versions.",
        "A node group is recreated for the change, which disrupts its workloads for a while.",
        "A node group's taints change, which may change where pods are scheduled.",
        "Changing the AMI family replaces the nodes one by one.",
        "Changing the image type recreates the nodes.",
        "Changing the AKS upgrade channel rolls the nodes.",
        "The control plane changes its node count.",
        "The GPU pool buys Spot capacity, which costs less but can be reclaimed at short notice.",
        "The GPU pool stops buying Spot, so its Spot GPU nodes are replaced by On-Demand ones.",
        "Some of the applied settings are not supported on this cluster.",
        "The apply changes the version the add-on runs.",
        "Advice on the applied configuration.",
        "The apply redeploys the cluster's model applications.",
        "The apply restarts the replicas of the cluster's models.",
        "The apply changes how much the workload queue admits.",
        "A cost setting the apply leaves out keeps its current value.",
        "The apply changes which model metrics are collected.",
        "A step that follows the apply needs attention.",
        "What the add-on needs on the cluster to work.",
        "The apply restarts the vulnerability scanner once.",
        "The apply changes when Node Autoscaling removes or replaces nodes.",
        "Idle nodes are kept, and billed, for longer before Node Autoscaling removes them.",
        "The apply changes how much Node Autoscaling may launch in a node pool.",
        "The apply changes node settings, so Node Autoscaling replaces the nodes it runs.",
        "The apply changes GPU node settings, so Node Autoscaling replaces the GPU nodes it runs.",
        "The GPU pool may buy Spot capacity, which costs less but can be reclaimed at short notice.",
        "Each GPU node is replaced after a set time, even while it serves.",
        "The most the GPU pool can cost per hour at its limit.",
        "The GPU pool's cost at its limit could not be worked out.",
        "How long an empty GPU node is kept before it is removed, and what it bills meanwhile.",
        "The interruption queue is always on for a cluster AstroPulse created, so the setting changes nothing.",
        "A node group gives up nodes or is removed, so the pods on those nodes move, and nothing checked that they fit.",
        "The check read neither the cluster's nodes nor its workloads, so its report has no readiness score.",
        "The cluster runs no GPU node yet, so accelerator metrics have nothing to measure.",
        "The workload queue is not running, so Jobs are refused.",
        "Only Spot node groups can run the cluster's system pods, so the cloud can reclaim all of them at once.",
        "The request names a resource the organization does not have.",
        "The cluster's create stopped before the cluster was ready.",
        "The last operation on the cluster failed.",
        "The cluster's creation was not approved, so it was never created.",
        "The cluster is still being created or waits for approval, so there is nothing to connect to.",
        "The cluster's create failed, so there is nothing to connect to.",
        "The cluster was deleted.",
        "The agent reports, but its connection to AstroPulse cannot carry requests.",
        "The cluster's agent is not connected to AstroPulse.",
        "The agent reported before and has not since; it reconnects on its own.",
        "AstroPulse could not check whether the agent is connected.",
        "The agent has not connected for the first time yet; nothing needs doing.",
        "AstroPulse has no stored key for the self-hosted cluster, so it can't change the cluster.",
        "The self-hosted cluster's stored key can't be read.",
        "The add-on's last change failed.",
        "The add-on is installed, but a health check fails.",
        "The add-on's last rollback did not finish.",
        "The add-on release asked for or recorded is not available; update the add-on to its recommended release.",
        "The add-on keeps running on a release no longer offered, but it can't be resynced or rolled back until it is updated to its recommended release.",
        "The workload-queueing add-on gives a queue to a namespace no queued application uses.",
        "The application did not reach a running state.",
        "The application serves its previous version because its last update failed.",
        "The application is held back while it deploys, or one of its resources is not healthy.",
        "A container of the new version cannot start or keeps exiting, so the update cannot roll out; the previous version still serves.",
        "The application's live state could not be read in time, so its last recorded status is shown.",
        "The application serves, but its autoscaler cannot read the cluster's metrics.",
        "Which versions can still be rolled back to could not be read, so each version shows its recorded eligibility.",
        "The application's delete stopped before it finished, so parts of it may still run.",
        "The request was sent by a CLI too old to be understood; installing the latest one resolves it.",
        "The organization's plan does not include the notification channel.",
        "The organization's plan does not include this feature.",
        "The organization has used all of this resource its plan allows.",
    ],
))


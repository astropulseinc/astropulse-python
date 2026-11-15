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



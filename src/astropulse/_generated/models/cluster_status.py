# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ClusterStatus(str, Enum):
    """
    ClusterStatus
    """

    """
    allowed enum values
    """
    Provisioning = 'Provisioning'
    InProgress = 'InProgress'
    Deployed = 'Deployed'
    Ready = 'Ready'
    Updating = 'Updating'
    ProvisionFailed = 'ProvisionFailed'
    DeleteFailed = 'DeleteFailed'
    Failed = 'Failed'
    Deleting = 'Deleting'
    Deleted = 'Deleted'
    Terminated = 'Terminated'
    Registering = 'Registering'
    Registered = 'Registered'
    Unregistered = 'Unregistered'
    RegisterFailed = 'RegisterFailed'
    ServicesDeploying = 'ServicesDeploying'
    ServicesDeployed = 'ServicesDeployed'
    ApprovalPending = 'ApprovalPending'
    ApprovalFailed = 'ApprovalFailed'
    AlreadyExists = 'AlreadyExists'
    ControlPlaneCreating = 'ControlPlaneCreating'
    ControlPlaneReady = 'ControlPlaneReady'
    NodeGroupsCreating = 'NodeGroupsCreating'
    NodeGroupsReady = 'NodeGroupsReady'
    AddonsInstalling = 'AddonsInstalling'
    AddonsReady = 'AddonsReady'
    KarpenterInstalling = 'KarpenterInstalling'
    KarpenterReady = 'KarpenterReady'
    ControlPlaneUpdateFailed = 'ControlPlaneUpdateFailed'
    NodeGroupsUpdateFailed = 'NodeGroupsUpdateFailed'
    AddonsUpdateFailed = 'AddonsUpdateFailed'
    KarpenterFailed = 'KarpenterFailed'
    Finalizing = 'Finalizing'
    PreflightValidating = 'PreflightValidating'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterStatus from a JSON string"""
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
    [member._value_ for member in ClusterStatus],
    [
        "Provisioning",
        "In progress",
        "Deployed",
        "Ready",
        "Updating",
        "Provision failed",
        "Delete failed",
        "Failed",
        "Deleting",
        "Deleted",
        "Terminated",
        "Registering",
        "Registered",
        "Unregistered",
        "Register failed",
        "Deploying services",
        "Services deployed",
        "Pending approval",
        "Approval failed",
        "Already exists",
        "Creating control plane",
        "Control plane ready",
        "Creating node groups",
        "Node groups ready",
        "Installing add-ons",
        "Add-ons ready",
        "Installing node autoscaling",
        "Node autoscaling ready",
        "Control plane update failed",
        "Node groups update failed",
        "Add-ons update failed",
        "Node autoscaling failed",
        "Finalizing",
        "Validating",
    ],
))
_DESCRIPTIONS: dict[str, str] = dict(zip(
    [member._value_ for member in ClusterStatus],
    [
        "AstroPulse is creating the cluster.",
        "The cluster's create or change has started.",
        "The cluster was created.",
        "The cluster is running and nothing is in progress.",
        "AstroPulse is changing the cluster.",
        "Creating the cluster failed.",
        "Deleting the cluster failed; it may still exist.",
        "The cluster's last operation failed.",
        "AstroPulse is deleting the cluster.",
        "The cluster was deleted.",
        "The cluster's operation was stopped before it finished.",
        "The cluster's agent is connecting to AstroPulse.",
        "The cluster's agent is connected to AstroPulse.",
        "The cluster was removed from AstroPulse; the cluster itself is untouched.",
        "Registering the cluster failed.",
        "AstroPulse is installing its services on the cluster.",
        "AstroPulse's services are installed on the cluster.",
        "The cluster waits for an organization owner to approve its create.",
        "The cluster's create was not approved.",
        "A cluster with this name already exists.",
        "AstroPulse is creating the cluster's control plane.",
        "The control plane is running; the nodes come next.",
        "AstroPulse is creating the cluster's node groups.",
        "The node groups are running.",
        "AstroPulse is installing the cluster's add-ons.",
        "The cluster's add-ons are installed.",
        "AstroPulse is installing node autoscaling.",
        "Node autoscaling is installed.",
        "Changing the control plane failed.",
        "Changing the node groups failed.",
        "Changing the cluster's add-ons failed.",
        "Installing or changing node autoscaling failed.",
        "AstroPulse is finishing the cluster's operation.",
        "AstroPulse is checking the request before it changes anything.",
    ],
))


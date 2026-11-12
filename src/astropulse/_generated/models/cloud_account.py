# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cloud_account_cluster import CloudAccountCluster
from astropulse._generated.models.cloud_account_pending_connection import CloudAccountPendingConnection
from astropulse._generated.models.cloud_account_state import CloudAccountState
from astropulse._generated.models.provider import Provider
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CloudAccount(BaseModel):
    """
    CloudAccount
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, description="The AWS account ID, GCP project ID or Azure subscription ID; omitted for callers who are not organization admins.", alias="accountId", json_schema_extra={"examples": ["123456789012"]})
    account_number: Optional[StrictStr] = Field(default=None, description="The GCP project number; omitted for other clouds and for callers who are not organization admins.", alias="accountNumber", json_schema_extra={"examples": ["785715412961"]})
    can_disconnect: Optional[StrictBool] = Field(default=None, description="True when the account has a connection, no cluster uses it and no setup is running.", alias="canDisconnect")
    clusters: Optional[List[CloudAccountCluster]] = Field(default=None, description="The organization's clusters in the account.")
    connected_at: Optional[StrictStr] = Field(default=None, description="When a connection to the account first finished its setup.", alias="connectedAt")
    disconnect_blocked_reason: Optional[StrictStr] = Field(default=None, description="Says why the account cannot be disconnected; empty when it can.", alias="disconnectBlockedReason")
    pending_connections: Optional[List[CloudAccountPendingConnection]] = Field(default=None, description="Connections to the account made for clusters that do not exist yet.", alias="pendingConnections")
    provider: Optional[Provider] = Field(default=None, description="The cloud the account is in.")
    regions: Optional[List[StrictStr]] = Field(default=None, description="The regions the account's connections and clusters are in; omitted for callers who are not organization admins.")
    resource_group: Optional[StrictStr] = Field(default=None, description="The Azure resource group the account's connections were made for; omitted for callers who are not organization admins.", alias="resourceGroup")
    state: Optional[CloudAccountState] = Field(default=None, description="How the account stands now.")
    status_message: Optional[StrictStr] = Field(default=None, description="Says in one sentence how the account stands now.", alias="statusMessage")
    verified_at: Optional[StrictStr] = Field(default=None, description="When a connection check last reached the account and got an answer.", alias="verifiedAt")
    __properties: ClassVar[List[str]] = ["accountId", "accountNumber", "canDisconnect", "clusters", "connectedAt", "disconnectBlockedReason", "pendingConnections", "provider", "regions", "resourceGroup", "state", "statusMessage", "verifiedAt"]

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
        """Create an instance of CloudAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item_clusters in self.clusters:
                if _item_clusters:
                    _items.append(_item_clusters.to_dict())
            _dict['clusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pending_connections (list)
        _items = []
        if self.pending_connections:
            for _item_pending_connections in self.pending_connections:
                if _item_pending_connections:
                    _items.append(_item_pending_connections.to_dict())
            _dict['pendingConnections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "accountNumber": obj.get("accountNumber"),
            "canDisconnect": obj.get("canDisconnect"),
            "clusters": [CloudAccountCluster.from_dict(_item) for _item in obj["clusters"]] if obj.get("clusters") is not None else None,
            "connectedAt": obj.get("connectedAt"),
            "disconnectBlockedReason": obj.get("disconnectBlockedReason"),
            "pendingConnections": [CloudAccountPendingConnection.from_dict(_item) for _item in obj["pendingConnections"]] if obj.get("pendingConnections") is not None else None,
            "provider": obj.get("provider"),
            "regions": obj.get("regions"),
            "resourceGroup": obj.get("resourceGroup"),
            "state": obj.get("state"),
            "statusMessage": obj.get("statusMessage"),
            "verifiedAt": obj.get("verifiedAt")
        })
        return _obj



# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cloud_connection_state import CloudConnectionState
from astropulse._generated.models.provisioner_type import ProvisionerType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CloudAccountPendingConnection(BaseModel):
    """
    CloudAccountPendingConnection
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster the connection was made for.", alias="clusterName")
    connection_id: Optional[StrictStr] = Field(default=None, description="The ID the connect endpoint returned; omitted for callers who are not organization admins.", alias="connectionId")
    last_error: Optional[StrictStr] = Field(default=None, description="Why the latest setup did not finish; omitted for callers who are not organization admins.", alias="lastError")
    message: Optional[StrictStr] = Field(default=None, description="Says in one sentence how the connection stands and that its cluster does not exist yet.", json_schema_extra={"examples": ["Connected for Amazon EKS. No cluster named prod exists yet."]})
    provisioner: Optional[ProvisionerType] = Field(default=None, description="The kind of cluster the connection was made for; omitted when unknown.")
    provisioner_name: Optional[StrictStr] = Field(default=None, description="The provisioner's name for people, such as Amazon EKS; omitted when unknown.", alias="provisionerName", json_schema_extra={"examples": ["Amazon EKS"]})
    started_at: Optional[StrictStr] = Field(default=None, description="When the connection's latest setup started.", alias="startedAt")
    state: Optional[CloudConnectionState] = Field(default=None, description="How the connection stands now.")
    __properties: ClassVar[List[str]] = ["clusterName", "connectionId", "lastError", "message", "provisioner", "provisionerName", "startedAt", "state"]

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
        """Create an instance of CloudAccountPendingConnection from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudAccountPendingConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "connectionId": obj.get("connectionId"),
            "lastError": obj.get("lastError"),
            "message": obj.get("message"),
            "provisioner": obj.get("provisioner"),
            "provisionerName": obj.get("provisionerName"),
            "startedAt": obj.get("startedAt"),
            "state": obj.get("state")
        })
        return _obj



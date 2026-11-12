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
from astropulse._generated.models.cluster_connectivity import ClusterConnectivity
from astropulse._generated.models.cluster_status import ClusterStatus
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.registration_instructions import RegistrationInstructions
from astropulse._generated.models.state_tone import StateTone
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterRegistrationStatus(BaseModel):
    """
    ClusterRegistrationStatus
    """ # noqa: E501
    connection_notice: Optional[Notice] = Field(default=None, description="ConnectionReason as a notice; absent when connectionReason is empty.", alias="connectionNotice")
    connection_reason: Optional[StrictStr] = Field(default=None, description="Says why connectionStatus is not Connected when the agent is still reporting, or that the agent has not connected yet; empty otherwise.", alias="connectionReason")
    connection_status: Optional[ClusterConnectivity] = Field(default=None, description="The agent's live connection state; omitted until the agent first connects.", alias="connectionStatus")
    error: Optional[Failure] = Field(default=None, description="Contains failure details when registration fails.")
    instructions: Optional[RegistrationInstructions] = Field(default=None, description="Contains setup instructions when status is ApprovalPending.")
    last_health_check: Optional[StrictStr] = Field(default=None, description="The timestamp of the last successful heartbeat from the agent (RFC 3339). Empty when agent has never connected.", alias="lastHealthCheck")
    message: Optional[StrictStr] = Field(default=None, description="Provides human-readable status details.")
    operation_id: Optional[StrictStr] = Field(default=None, description="The unique identifier for tracking this registration operation.", alias="operationId")
    status: Optional[ClusterStatus] = Field(default=None, description="The registration's status, such as Registering, ApprovalPending, Registered or RegisterFailed.")
    status_tone: Optional[StateTone] = Field(default=None, description="How status reads at a glance.", alias="statusTone")
    __properties: ClassVar[List[str]] = ["connectionNotice", "connectionReason", "connectionStatus", "error", "instructions", "lastHealthCheck", "message", "operationId", "status", "statusTone"]

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
        """Create an instance of ClusterRegistrationStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of connection_notice
        if self.connection_notice:
            _dict['connectionNotice'] = self.connection_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of instructions
        if self.instructions:
            _dict['instructions'] = self.instructions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterRegistrationStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectionNotice": Notice.from_dict(obj["connectionNotice"]) if obj.get("connectionNotice") is not None else None,
            "connectionReason": obj.get("connectionReason"),
            "connectionStatus": obj.get("connectionStatus"),
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "instructions": RegistrationInstructions.from_dict(obj["instructions"]) if obj.get("instructions") is not None else None,
            "lastHealthCheck": obj.get("lastHealthCheck"),
            "message": obj.get("message"),
            "operationId": obj.get("operationId"),
            "status": obj.get("status"),
            "statusTone": obj.get("statusTone")
        })
        return _obj



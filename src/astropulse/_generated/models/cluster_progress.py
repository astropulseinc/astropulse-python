# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.cluster_operation_step import ClusterOperationStep
from astropulse._generated.models.operation_status import OperationStatus
from astropulse._generated.models.operation_type import OperationType
from astropulse._generated.models.progress_event import ProgressEvent
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterProgress(BaseModel):
    """
    ClusterProgress
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="The cluster's identifier.", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster this operation runs against.", alias="clusterName")
    completed_at: Optional[datetime] = Field(default=None, description="When it finished, absent while it runs.", alias="completedAt")
    current_phase: Optional[ClusterOperationStep] = Field(default=None, description="The step the operation is on. Omitted when it is on no step, such as while it runs its preflight checks or once it has ended.", alias="currentPhase")
    last_update: Optional[datetime] = Field(default=None, description="When this record last changed.", alias="lastUpdate")
    message: Optional[StrictStr] = Field(default=None, description="The latest human-readable line.")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Carries operation-specific values.")
    operation_id: Optional[StrictStr] = Field(default=None, description="Identifies this operation; pass it to the progress endpoints to follow it.", alias="operationId")
    operation_type: Optional[OperationType] = Field(default=None, description="What the operation does.", alias="operationType")
    organization_id: Optional[StrictStr] = Field(default=None, description="Owns the cluster.", alias="organizationId")
    progress_percentage: Optional[StrictInt] = Field(default=None, description="How far through it is, 0 to 100.", alias="progressPercentage")
    recent_events: Optional[List[ProgressEvent]] = Field(default=None, description="The tail of the event stream, newest last.", alias="recentEvents")
    started_at: Optional[datetime] = Field(default=None, description="When the operation began.", alias="startedAt")
    status: Optional[OperationStatus] = Field(default=None, description="Where it has got to.")
    superseded_by: Optional[StrictStr] = Field(default=None, description="Set in the operation history on a failed create, delete or add-on apply once a later one of the same kind has completed, and holds that operation's ID.", alias="supersededBy")
    user_id: Optional[StrictStr] = Field(default=None, description="Who asked for the operation.", alias="userId")
    __properties: ClassVar[List[str]] = ["clusterId", "clusterName", "completedAt", "currentPhase", "lastUpdate", "message", "metadata", "operationId", "operationType", "organizationId", "progressPercentage", "recentEvents", "startedAt", "status", "supersededBy", "userId"]

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
        """Create an instance of ClusterProgress from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recent_events (list)
        _items = []
        if self.recent_events:
            for _item_recent_events in self.recent_events:
                if _item_recent_events:
                    _items.append(_item_recent_events.to_dict())
            _dict['recentEvents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterProgress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "completedAt": obj.get("completedAt"),
            "currentPhase": obj.get("currentPhase"),
            "lastUpdate": obj.get("lastUpdate"),
            "message": obj.get("message"),
            "metadata": obj.get("metadata"),
            "operationId": obj.get("operationId"),
            "operationType": obj.get("operationType"),
            "organizationId": obj.get("organizationId"),
            "progressPercentage": obj.get("progressPercentage"),
            "recentEvents": [ProgressEvent.from_dict(_item) for _item in obj["recentEvents"]] if obj.get("recentEvents") is not None else None,
            "startedAt": obj.get("startedAt"),
            "status": obj.get("status"),
            "supersededBy": obj.get("supersededBy"),
            "userId": obj.get("userId")
        })
        return _obj



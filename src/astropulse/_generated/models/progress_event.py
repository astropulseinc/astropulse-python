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
from astropulse._generated.models.progress_event_level import ProgressEventLevel
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProgressEvent(BaseModel):
    """
    ProgressEvent
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="The cluster's identifier.", alias="clusterId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster this happened on.", alias="clusterName")
    labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Carry extra context.")
    level: Optional[ProgressEventLevel] = Field(default=None, description="How severe the event is.")
    message: Optional[StrictStr] = Field(default=None, description="What happened.")
    operation_id: Optional[StrictStr] = Field(default=None, description="The operation this belongs to.", alias="operationId")
    operation_status: Optional[OperationStatus] = Field(default=None, description="How the operation ended, on the event that ended it. Omitted on every other event.", alias="operationStatus")
    operation_type: Optional[OperationType] = Field(default=None, description="What the operation does.", alias="operationType")
    phase: Optional[ClusterOperationStep] = Field(default=None, description="The step of the operation the event happened in. Omitted when it belongs to no step, such as a preflight check.")
    phase_label: Optional[StrictStr] = Field(default=None, description="The step it happened in, in words, such as Creating node groups. Omitted when it belongs to no step.", alias="phaseLabel")
    progress_percentage: Optional[StrictInt] = Field(default=None, description="How far through the operation was, 0 to 100.", alias="progressPercentage")
    raw_output: Optional[StrictStr] = Field(default=None, description="The provisioner's own output, when there was any.", alias="rawOutput")
    timestamp: Optional[datetime] = Field(default=None, description="When it happened.")
    __properties: ClassVar[List[str]] = ["clusterId", "clusterName", "labels", "level", "message", "operationId", "operationStatus", "operationType", "phase", "phaseLabel", "progressPercentage", "rawOutput", "timestamp"]

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
        """Create an instance of ProgressEvent from a JSON string"""
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
        """Create an instance of ProgressEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterName": obj.get("clusterName"),
            "labels": obj.get("labels"),
            "level": obj.get("level"),
            "message": obj.get("message"),
            "operationId": obj.get("operationId"),
            "operationStatus": obj.get("operationStatus"),
            "operationType": obj.get("operationType"),
            "phase": obj.get("phase"),
            "phaseLabel": obj.get("phaseLabel"),
            "progressPercentage": obj.get("progressPercentage"),
            "rawOutput": obj.get("rawOutput"),
            "timestamp": obj.get("timestamp")
        })
        return _obj



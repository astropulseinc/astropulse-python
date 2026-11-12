# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.capacity_block_phase import CapacityBlockPhase
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CapacityBlockStatus(BaseModel):
    """
    CapacityBlockStatus
    """ # noqa: E501
    availability_zone: Optional[StrictStr] = Field(default=None, description="The zone the block reserves capacity in.", alias="availabilityZone")
    end_time: Optional[StrictStr] = Field(default=None, description="When the block ends, RFC 3339. The group's nodes are terminated when the block ends.", alias="endTime")
    instance_count: Optional[StrictInt] = Field(default=None, description="How many instances the block reserves.", alias="instanceCount")
    instance_type: Optional[StrictStr] = Field(default=None, description="The instance type the block reserves.", alias="instanceType")
    phase: Optional[CapacityBlockPhase] = Field(default=None, description="Where the block stands now. An ended block's node group runs no nodes; delete it, or create a new CapacityBlock node group on a new block.")
    reservation_id: Optional[StrictStr] = Field(default=None, description="The block's capacity reservation id.", alias="reservationId")
    start_time: Optional[StrictStr] = Field(default=None, description="When the block starts, RFC 3339.", alias="startTime")
    __properties: ClassVar[List[str]] = ["availabilityZone", "endTime", "instanceCount", "instanceType", "phase", "reservationId", "startTime"]

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
        """Create an instance of CapacityBlockStatus from a JSON string"""
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
        """Create an instance of CapacityBlockStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availabilityZone": obj.get("availabilityZone"),
            "endTime": obj.get("endTime"),
            "instanceCount": obj.get("instanceCount"),
            "instanceType": obj.get("instanceType"),
            "phase": obj.get("phase"),
            "reservationId": obj.get("reservationId"),
            "startTime": obj.get("startTime")
        })
        return _obj



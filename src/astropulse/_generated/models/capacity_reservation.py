# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.capacity_reservation_kind import CapacityReservationKind
from astropulse._generated.models.instance_type import InstanceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CapacityReservation(BaseModel):
    """
    CapacityReservation
    """ # noqa: E501
    available_count: Optional[StrictInt] = Field(default=None, description="How many instances are free now.", alias="availableCount")
    end_date: Optional[StrictStr] = Field(default=None, description="When the reservation ends, when it has one.", alias="endDate")
    gpu_pool_reason: Optional[StrictStr] = Field(default=None, description="Says why the GPU pool could not, when it cannot.", alias="gpuPoolReason")
    gpu_pool_usable: Optional[StrictBool] = Field(default=None, description="True when the Karpenter GPU pool could launch into it.", alias="gpuPoolUsable")
    id: Optional[StrictStr] = Field(default=None, description="The reservation ID.")
    kind: Optional[CapacityReservationKind] = Field(default=None, description="Whether the capacity is an On-Demand Capacity Reservation or a Capacity Block for ML.")
    machine_type: Optional[StrictStr] = Field(default=None, description="The instance type reserved.", alias="machineType")
    node_group_instance_type: Optional[InstanceType] = Field(default=None, description="The instanceType a node group sets to run on it.", alias="nodeGroupInstanceType")
    node_group_reason: Optional[StrictStr] = Field(default=None, description="Says why no node group could, when one cannot.", alias="nodeGroupReason")
    node_group_usable: Optional[StrictBool] = Field(default=None, description="True when a node group in the cluster's zones could run on it.", alias="nodeGroupUsable")
    start_date: Optional[StrictStr] = Field(default=None, description="When the reservation starts, when it has one.", alias="startDate")
    state: Optional[StrictStr] = Field(default=None, description="The cloud's state for the reservation (active, scheduled, ...).")
    total_count: Optional[StrictInt] = Field(default=None, description="How many instances are reserved.", alias="totalCount")
    zone: Optional[StrictStr] = Field(default=None, description="The availability zone.")
    __properties: ClassVar[List[str]] = ["availableCount", "endDate", "gpuPoolReason", "gpuPoolUsable", "id", "kind", "machineType", "nodeGroupInstanceType", "nodeGroupReason", "nodeGroupUsable", "startDate", "state", "totalCount", "zone"]

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
        """Create an instance of CapacityReservation from a JSON string"""
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
        """Create an instance of CapacityReservation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableCount": obj.get("availableCount"),
            "endDate": obj.get("endDate"),
            "gpuPoolReason": obj.get("gpuPoolReason"),
            "gpuPoolUsable": obj.get("gpuPoolUsable"),
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "machineType": obj.get("machineType"),
            "nodeGroupInstanceType": obj.get("nodeGroupInstanceType"),
            "nodeGroupReason": obj.get("nodeGroupReason"),
            "nodeGroupUsable": obj.get("nodeGroupUsable"),
            "startDate": obj.get("startDate"),
            "state": obj.get("state"),
            "totalCount": obj.get("totalCount"),
            "zone": obj.get("zone")
        })
        return _obj



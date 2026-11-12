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
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.observed_node_gpu import ObservedNodeGPU
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ObservedNodeSet(BaseModel):
    """
    ObservedNodeSet
    """ # noqa: E501
    capacity_type: Optional[InstanceType] = Field(default=None, description="How the nodes are bought. Omitted when the provider does not state it.", alias="capacityType")
    cordoned: Optional[StrictInt] = Field(default=None, description="How many of them take no new workloads while nothing says they are being removed. Omitted when none.")
    count: Optional[StrictInt] = Field(default=None, description="How many nodes are in the set.")
    draining: Optional[StrictInt] = Field(default=None, description="How many of them are being drained to leave the cluster: the cloud is reclaiming or stopping them, an autoscaler is removing them, or they are being deleted. Omitted when none.")
    gpus: Optional[List[ObservedNodeGPU]] = Field(default=None, description="The accelerators on each node of the set.")
    machine_type: Optional[StrictStr] = Field(default=None, description="The nodes' machine type, for example g6.xlarge. Omitted when the nodes do not say.", alias="machineType")
    ready: Optional[StrictInt] = Field(default=None, description="How many of them are ready. Omitted when not reported.")
    zone: Optional[StrictStr] = Field(default=None, description="The nodes' availability zone. Omitted when the nodes do not say.")
    __properties: ClassVar[List[str]] = ["capacityType", "cordoned", "count", "draining", "gpus", "machineType", "ready", "zone"]

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
        """Create an instance of ObservedNodeSet from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in gpus (list)
        _items = []
        if self.gpus:
            for _item_gpus in self.gpus:
                if _item_gpus:
                    _items.append(_item_gpus.to_dict())
            _dict['gpus'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObservedNodeSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capacityType": obj.get("capacityType"),
            "cordoned": obj.get("cordoned"),
            "count": obj.get("count"),
            "draining": obj.get("draining"),
            "gpus": [ObservedNodeGPU.from_dict(_item) for _item in obj["gpus"]] if obj.get("gpus") is not None else None,
            "machineType": obj.get("machineType"),
            "ready": obj.get("ready"),
            "zone": obj.get("zone")
        })
        return _obj



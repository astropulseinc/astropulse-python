# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MetricsDimensions(BaseModel):
    """
    MetricsDimensions
    """ # noqa: E501
    average_cpu_cores_used: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The CPU used across the reading.", alias="averageCpuCoresUsed")
    memory_working_set_bytes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The memory held across it.", alias="memoryWorkingSetBytes")
    network_receive_bytes_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The network receive and transmit rates are absent (not zero) unless every sample contributing to this reading carried a network measurement — never present when any contributor's source was metrics-api, and never present at cluster scope unless every reporting application observed network. A zero here would read as \"no traffic,\" which looks exactly like an outage.", alias="networkReceiveBytesPerSecond")
    network_transmit_bytes_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="networkTransmitBytesPerSecond")
    __properties: ClassVar[List[str]] = ["averageCpuCoresUsed", "memoryWorkingSetBytes", "networkReceiveBytesPerSecond", "networkTransmitBytesPerSecond"]

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
        """Create an instance of MetricsDimensions from a JSON string"""
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
        """Create an instance of MetricsDimensions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "averageCpuCoresUsed": obj.get("averageCpuCoresUsed"),
            "memoryWorkingSetBytes": obj.get("memoryWorkingSetBytes"),
            "networkReceiveBytesPerSecond": obj.get("networkReceiveBytesPerSecond"),
            "networkTransmitBytesPerSecond": obj.get("networkTransmitBytesPerSecond")
        })
        return _obj



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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CostPriceSheet(BaseModel):
    """
    CostPriceSheet
    """ # noqa: E501
    cluster_management_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The hourly fee for managing the cluster, such as a managed control plane's. Left out, the fee shows as unpriced; 0 means there is none.", alias="clusterManagementHour")
    cpu_core_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one CPU core for an hour.", alias="cpuCoreHour")
    currency: Optional[StrictStr] = Field(default='USD', description="The currency of these prices, as a three-letter ISO 4217 code. Left out, it is USD.")
    gpu_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one GPU for an hour.", alias="gpuHour")
    gpu_node_label: Optional[Annotated[str, Field(strict=True, max_length=253)]] = Field(default=None, description="The node label that marks GPU nodes, for a cluster whose GPU nodes can't be told apart otherwise.", alias="gpuNodeLabel")
    gpu_node_label_value: Optional[Annotated[str, Field(strict=True, max_length=253)]] = Field(default=None, description="The value `gpuNodeLabel` must have for a node to count as a GPU node.", alias="gpuNodeLabelValue")
    ram_gb_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one gigabyte of memory for an hour.", alias="ramGbHour")
    spot_cpu_core_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one CPU core for an hour on a Spot node, one carrying `spotNodeLabel`.", alias="spotCpuCoreHour")
    spot_gpu_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one GPU for an hour on a Spot node.", alias="spotGpuHour")
    spot_node_label: Optional[Annotated[str, Field(strict=True, max_length=253)]] = Field(default=None, description="The node label that marks Spot nodes on your cloud, such as `eks.amazonaws.com/capacityType=SPOT`. Required when Spot prices are set.", alias="spotNodeLabel")
    spot_node_label_value: Optional[Annotated[str, Field(strict=True, max_length=253)]] = Field(default=None, description="The value `spotNodeLabel` must have for a node to count as Spot.", alias="spotNodeLabelValue")
    spot_ram_gb_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one gigabyte of memory for an hour on a Spot node; set it with `spotCpuCoreHour`.", alias="spotRamGbHour")
    storage_gb_hour: Optional[Annotated[str, Field(strict=True, max_length=26)]] = Field(default=None, description="The price of one gigabyte of storage for an hour.", alias="storageGbHour")
    __properties: ClassVar[List[str]] = ["clusterManagementHour", "cpuCoreHour", "currency", "gpuHour", "gpuNodeLabel", "gpuNodeLabelValue", "ramGbHour", "spotCpuCoreHour", "spotGpuHour", "spotNodeLabel", "spotNodeLabelValue", "spotRamGbHour", "storageGbHour"]

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
        """Create an instance of CostPriceSheet from a JSON string"""
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
        """Create an instance of CostPriceSheet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterManagementHour": obj.get("clusterManagementHour"),
            "cpuCoreHour": obj.get("cpuCoreHour"),
            "currency": obj.get("currency") if obj.get("currency") is not None else 'USD',
            "gpuHour": obj.get("gpuHour"),
            "gpuNodeLabel": obj.get("gpuNodeLabel"),
            "gpuNodeLabelValue": obj.get("gpuNodeLabelValue"),
            "ramGbHour": obj.get("ramGbHour"),
            "spotCpuCoreHour": obj.get("spotCpuCoreHour"),
            "spotGpuHour": obj.get("spotGpuHour"),
            "spotNodeLabel": obj.get("spotNodeLabel"),
            "spotNodeLabelValue": obj.get("spotNodeLabelValue"),
            "spotRamGbHour": obj.get("spotRamGbHour"),
            "storageGbHour": obj.get("storageGbHour")
        })
        return _obj



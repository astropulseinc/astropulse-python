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
from astropulse._generated.models.model_placement_instance import ModelPlacementInstance
from astropulse._generated.models.model_placement_quota import ModelPlacementQuota
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelPlacement(BaseModel):
    """
    ModelPlacement
    """ # noqa: E501
    accelerator: Optional[StrictStr] = Field(default=None, description="The GPU model each replica asks for; empty when it names none.")
    capacity_types: Optional[List[StrictStr]] = Field(default=None, description="The purchase options the pool launches, in the order it prefers them: reserved, spot, on-demand.", alias="capacityTypes")
    gpu_limit: Optional[StrictInt] = Field(default=None, description="The most GPUs the pool may run at once across its nodes.", alias="gpuLimit")
    gpus_at_max_replicas: Optional[StrictInt] = Field(default=None, description="How many GPUs the model's maximum replica count would take of that limit.", alias="gpusAtMaxReplicas")
    gpus_at_min_replicas: Optional[StrictInt] = Field(default=None, description="How many GPUs the model's minimum replica count takes of that limit.", alias="gpusAtMinReplicas")
    gpus_per_replica: Optional[StrictInt] = Field(default=None, description="How many GPUs one replica takes.", alias="gpusPerReplica")
    instance_types: Optional[List[ModelPlacementInstance]] = Field(default=None, description="The instance types that can hold one replica, the one most likely to launch listed first.", alias="instanceTypes")
    node_pool: Optional[StrictStr] = Field(default=None, description="The GPU node pool that launches the replicas' nodes.", alias="nodePool")
    notes: Optional[List[StrictStr]] = Field(default=None, description="Say the placement in sentences, for display.")
    quota: Optional[ModelPlacementQuota] = Field(default=None, description="The cloud account quota one replica's node draws on.")
    __properties: ClassVar[List[str]] = ["accelerator", "capacityTypes", "gpuLimit", "gpusAtMaxReplicas", "gpusAtMinReplicas", "gpusPerReplica", "instanceTypes", "nodePool", "notes", "quota"]

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
        """Create an instance of ModelPlacement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in instance_types (list)
        _items = []
        if self.instance_types:
            for _item_instance_types in self.instance_types:
                if _item_instance_types:
                    _items.append(_item_instance_types.to_dict())
            _dict['instanceTypes'] = _items
        # override the default output from pydantic by calling `to_dict()` of quota
        if self.quota:
            _dict['quota'] = self.quota.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelPlacement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": obj.get("accelerator"),
            "capacityTypes": obj.get("capacityTypes"),
            "gpuLimit": obj.get("gpuLimit"),
            "gpusAtMaxReplicas": obj.get("gpusAtMaxReplicas"),
            "gpusAtMinReplicas": obj.get("gpusAtMinReplicas"),
            "gpusPerReplica": obj.get("gpusPerReplica"),
            "instanceTypes": [ModelPlacementInstance.from_dict(_item) for _item in obj["instanceTypes"]] if obj.get("instanceTypes") is not None else None,
            "nodePool": obj.get("nodePool"),
            "notes": obj.get("notes"),
            "quota": ModelPlacementQuota.from_dict(obj["quota"]) if obj.get("quota") is not None else None
        })
        return _obj



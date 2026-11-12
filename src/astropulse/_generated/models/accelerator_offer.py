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
from astropulse._generated.models.accelerator_offer_availability import AcceleratorOfferAvailability
from astropulse._generated.models.accelerator_offer_instance import AcceleratorOfferInstance
from astropulse._generated.models.accelerator_offer_quota import AcceleratorOfferQuota
from astropulse._generated.models.accelerator_offer_reason_code import AcceleratorOfferReasonCode
from astropulse._generated.models.accelerator_offer_source import AcceleratorOfferSource
from astropulse._generated.models.instance_type import InstanceType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AcceleratorOffer(BaseModel):
    """
    AcceleratorOffer
    """ # noqa: E501
    availability: Optional[AcceleratorOfferAvailability] = Field(default=None, description="Whether a replica asking for this offer can be placed.")
    cache_node_group: Optional[StrictStr] = Field(default=None, description="The name to set as source.model.cache.nodeGroup to keep the model's weights on these nodes. Empty when these nodes hold no weight cache.", alias="cacheNodeGroup")
    capacity_types: Optional[List[InstanceType]] = Field(default=None, description="How the nodes are bought, in order of preference. Empty when AstroPulse does not know how they are bought.", alias="capacityTypes")
    instance_types: Optional[List[AcceleratorOfferInstance]] = Field(default=None, description="The machine types that provide this GPU, in the order they are chosen, with the GPUs each carries.", alias="instanceTypes")
    limit: Optional[StrictInt] = Field(default=None, description="The most GPUs the autoscaling pool runs at once, shared by every workload on it.")
    max_per_replica: Optional[StrictInt] = Field(default=None, description="The most GPUs of this model one replica can ask for: the largest node within the pool's GPU limit, lowered when the cloud account's quota cannot launch a larger node. Zero when availability is Unavailable.", alias="maxPerReplica")
    model: Optional[StrictStr] = Field(default=None, description="The GPU model in lower case, for example l4. Empty when the pool's GPU models are not known yet; any GPU of the vendor is then accepted.")
    node_group: Optional[StrictStr] = Field(default=None, description="The node group in workerNodes, when source is NodeGroup.", alias="nodeGroup")
    pool: Optional[StrictStr] = Field(default=None, description="The autoscaling node pool's name, when source is AutoscalingPool.")
    quota: Optional[AcceleratorOfferQuota] = Field(default=None, description="The cloud account quota a replica's node draws on: for an autoscaling pool, the node maxPerReplica needs; for a node group, one more of its nodes.")
    reason: Optional[StrictStr] = Field(default=None, description="Says reasonCode in a sentence, with what to change.")
    reason_code: Optional[AcceleratorOfferReasonCode] = Field(default=None, description="Why availability is not Available, or why maxPerReplica is lower than the largest node allows.", alias="reasonCode")
    source: Optional[AcceleratorOfferSource] = Field(default=None, description="Where the GPUs come from.")
    vendor: Optional[StrictStr] = Field(default=None, description="The GPU maker, for example nvidia.")
    __properties: ClassVar[List[str]] = ["availability", "cacheNodeGroup", "capacityTypes", "instanceTypes", "limit", "maxPerReplica", "model", "nodeGroup", "pool", "quota", "reason", "reasonCode", "source", "vendor"]

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
        """Create an instance of AcceleratorOffer from a JSON string"""
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
        """Create an instance of AcceleratorOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability": obj.get("availability"),
            "cacheNodeGroup": obj.get("cacheNodeGroup"),
            "capacityTypes": obj.get("capacityTypes"),
            "instanceTypes": [AcceleratorOfferInstance.from_dict(_item) for _item in obj["instanceTypes"]] if obj.get("instanceTypes") is not None else None,
            "limit": obj.get("limit"),
            "maxPerReplica": obj.get("maxPerReplica"),
            "model": obj.get("model"),
            "nodeGroup": obj.get("nodeGroup"),
            "pool": obj.get("pool"),
            "quota": AcceleratorOfferQuota.from_dict(obj["quota"]) if obj.get("quota") is not None else None,
            "reason": obj.get("reason"),
            "reasonCode": obj.get("reasonCode"),
            "source": obj.get("source"),
            "vendor": obj.get("vendor")
        })
        return _obj



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
from astropulse._generated.models.accelerator_offer import AcceleratorOffer
from astropulse._generated.models.accelerator_offers_incomplete_reason import AcceleratorOffersIncompleteReason
from astropulse._generated.models.accelerator_offers_unavailable_reason import AcceleratorOffersUnavailableReason
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAccelerators(BaseModel):
    """
    ClusterAccelerators
    """ # noqa: E501
    offers: Optional[List[AcceleratorOffer]] = Field(default=None, description="The GPUs the cluster's node groups carry and the GPUs its autoscaling pools can launch.")
    offers_incomplete: Optional[AcceleratorOffersIncompleteReason] = Field(default=None, description="Why the autoscaling pools' offers are missing. Empty when offers are complete.", alias="offersIncomplete")
    offers_incomplete_message: Optional[StrictStr] = Field(default=None, description="Says offersIncomplete in a sentence, with what to do next. Empty when offersIncomplete is empty.", alias="offersIncompleteMessage")
    offers_unavailable: Optional[AcceleratorOffersUnavailableReason] = Field(default=None, description="Why no offers are listed. Empty when there are offers.", alias="offersUnavailable")
    offers_unavailable_message: Optional[StrictStr] = Field(default=None, description="Says offersUnavailable in a sentence, with what a model can still ask for. Empty when offersUnavailable is empty.", alias="offersUnavailableMessage")
    region: Optional[StrictStr] = Field(default=None, description="The region the autoscaling pools' instance types are listed for.")
    __properties: ClassVar[List[str]] = ["offers", "offersIncomplete", "offersIncompleteMessage", "offersUnavailable", "offersUnavailableMessage", "region"]

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
        """Create an instance of ClusterAccelerators from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in offers (list)
        _items = []
        if self.offers:
            for _item_offers in self.offers:
                if _item_offers:
                    _items.append(_item_offers.to_dict())
            _dict['offers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAccelerators from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offers": [AcceleratorOffer.from_dict(_item) for _item in obj["offers"]] if obj.get("offers") is not None else None,
            "offersIncomplete": obj.get("offersIncomplete"),
            "offersIncompleteMessage": obj.get("offersIncompleteMessage"),
            "offersUnavailable": obj.get("offersUnavailable"),
            "offersUnavailableMessage": obj.get("offersUnavailableMessage"),
            "region": obj.get("region")
        })
        return _obj



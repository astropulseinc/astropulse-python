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
from astropulse._generated.models.cost_pricing_source import CostPricingSource
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CostTotal(BaseModel):
    """
    CostTotal
    """ # noqa: E501
    amount: Optional[StrictStr] = Field(default=None, description="The amount of the priced usage, a decimal in `currency`; an entry whose `pricingSource` is `Unpriced` marks the usage left out.")
    currency: Optional[StrictStr] = None
    pricing_source: Optional[CostPricingSource] = Field(default=None, description="Where the prices came from.", alias="pricingSource")
    unpriced_reasons: Optional[List[Notice]] = Field(default=None, description="Why part of the usage has no price, on the `Unpriced` entry, each with what to do about it.", alias="unpricedReasons")
    __properties: ClassVar[List[str]] = ["amount", "currency", "pricingSource", "unpricedReasons"]

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
        """Create an instance of CostTotal from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in unpriced_reasons (list)
        _items = []
        if self.unpriced_reasons:
            for _item_unpriced_reasons in self.unpriced_reasons:
                if _item_unpriced_reasons:
                    _items.append(_item_unpriced_reasons.to_dict())
            _dict['unpricedReasons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CostTotal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "pricingSource": obj.get("pricingSource"),
            "unpricedReasons": [Notice.from_dict(_item) for _item in obj["unpricedReasons"]] if obj.get("unpricedReasons") is not None else None
        })
        return _obj



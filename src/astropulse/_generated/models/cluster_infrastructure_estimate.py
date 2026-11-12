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
from astropulse._generated.models.cluster_infrastructure_charge import ClusterInfrastructureCharge
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_type import ProvisionerType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterInfrastructureEstimate(BaseModel):
    """
    ClusterInfrastructureEstimate
    """ # noqa: E501
    charges: Optional[List[ClusterInfrastructureCharge]] = Field(default=None, description="The charges outside the cluster's nodes, which are priced on their machine types.")
    provider: Optional[Provider] = Field(default=None, description="The cloud.")
    provisioner: Optional[ProvisionerType] = Field(default=None, description="The provisioner the cluster is created with.")
    region: Optional[StrictStr] = Field(default=None, description="The cloud region.")
    __properties: ClassVar[List[str]] = ["charges", "provider", "provisioner", "region"]

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
        """Create an instance of ClusterInfrastructureEstimate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in charges (list)
        _items = []
        if self.charges:
            for _item_charges in self.charges:
                if _item_charges:
                    _items.append(_item_charges.to_dict())
            _dict['charges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterInfrastructureEstimate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "charges": [ClusterInfrastructureCharge.from_dict(_item) for _item in obj["charges"]] if obj.get("charges") is not None else None,
            "provider": obj.get("provider"),
            "provisioner": obj.get("provisioner"),
            "region": obj.get("region")
        })
        return _obj



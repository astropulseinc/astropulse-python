# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.node_group import NodeGroup
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DataPlane(BaseModel):
    """
    DataPlane
    """ # noqa: E501
    node_groups: Optional[Annotated[List[NodeGroup], Field(min_length=1)]] = Field(default=None, description="A slice of NodeGroup configurations for the data plane. It must contain at least one NodeGroup except when the provider owns worker compute — EKS Auto Mode or GKE Autopilot — where it must be omitted because the cloud provider, not AstroPulse, owns worker compute.", alias="nodeGroups")
    __properties: ClassVar[List[str]] = ["nodeGroups"]

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
        """Create an instance of DataPlane from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in node_groups (list)
        _items = []
        if self.node_groups:
            for _item_node_groups in self.node_groups:
                if _item_node_groups:
                    _items.append(_item_node_groups.to_dict())
            _dict['nodeGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataPlane from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeGroups": [NodeGroup.from_dict(_item) for _item in obj["nodeGroups"]] if obj.get("nodeGroups") is not None else None
        })
        return _obj



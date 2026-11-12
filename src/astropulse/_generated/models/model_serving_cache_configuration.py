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
from astropulse._generated.models.model_cache_backing import ModelCacheBacking
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModelServingCacheConfiguration(BaseModel):
    """
    ModelServingCacheConfiguration
    """ # noqa: E501
    backing: Optional[ModelCacheBacking] = Field(default=None, description="Where the weights are kept; required whenever `modelCache` is set.")
    name: Optional[StrictStr] = Field(default=None, description="The cluster storage that holds the weights, by its binding name; required with `Storage` backing and refused with `Node` backing.")
    node_groups: Optional[List[StrictStr]] = Field(default=None, description="The node groups, CPU or GPU, and the GPU node pool, whose nodes keep the weights; a cached model runs on one of them. Leave out the groups that run the cluster's own components.", alias="nodeGroups")
    size: Optional[StrictStr] = Field(default=None, description="How much space the cache may use, such as 2Ti; required with `Storage` backing and refused with `Node` backing, where the node's own disk sets it.")
    __properties: ClassVar[List[str]] = ["backing", "name", "nodeGroups", "size"]

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
        """Create an instance of ModelServingCacheConfiguration from a JSON string"""
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
        """Create an instance of ModelServingCacheConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backing": obj.get("backing"),
            "name": obj.get("name"),
            "nodeGroups": obj.get("nodeGroups"),
            "size": obj.get("size")
        })
        return _obj



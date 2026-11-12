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
from astropulse._generated.models.cluster_delete_outcome import ClusterDeleteOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterDeleteItem(BaseModel):
    """
    ClusterDeleteItem
    """ # noqa: E501
    detail: Optional[StrictStr] = Field(default=None, description="A short description of the item, such as \"20Gi, gp3\".")
    id: Optional[StrictStr] = Field(default=None, description="Your cloud provider's id for the item, shown when you ask for more detail.")
    name: Optional[StrictStr] = Field(default=None, description="The item's name.")
    namespace: Optional[StrictStr] = Field(default=None, description="The item's namespace, when it has one.")
    outcome: Optional[ClusterDeleteOutcome] = Field(default=None, description="What the delete does with the item.")
    reason: Optional[StrictStr] = Field(default=None, description="Says why the item is kept or what to do about it.")
    __properties: ClassVar[List[str]] = ["detail", "id", "name", "namespace", "outcome", "reason"]

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
        """Create an instance of ClusterDeleteItem from a JSON string"""
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
        """Create an instance of ClusterDeleteItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "detail": obj.get("detail"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "outcome": obj.get("outcome"),
            "reason": obj.get("reason")
        })
        return _obj



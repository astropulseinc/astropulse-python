# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.git_hub_detected_installation import GitHubDetectedInstallation
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GitHubDetectedInstallations(BaseModel):
    """
    GitHubDetectedInstallations
    """ # noqa: E501
    available: Optional[List[GitHubDetectedInstallation]] = None
    linked: Optional[List[GitHubDetectedInstallation]] = None
    __properties: ClassVar[List[str]] = ["available", "linked"]

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
        """Create an instance of GitHubDetectedInstallations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available (list)
        _items = []
        if self.available:
            for _item_available in self.available:
                if _item_available:
                    _items.append(_item_available.to_dict())
            _dict['available'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in linked (list)
        _items = []
        if self.linked:
            for _item_linked in self.linked:
                if _item_linked:
                    _items.append(_item_linked.to_dict())
            _dict['linked'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GitHubDetectedInstallations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available": [GitHubDetectedInstallation.from_dict(_item) for _item in obj["available"]] if obj.get("available") is not None else None,
            "linked": [GitHubDetectedInstallation.from_dict(_item) for _item in obj["linked"]] if obj.get("linked") is not None else None
        })
        return _obj



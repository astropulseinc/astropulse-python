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
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScanFindingsUnscannedImages(BaseModel):
    """
    ScanFindingsUnscannedImages
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="How many images could not be scanned for this reason; 0 when not known.")
    images: Optional[List[StrictStr]] = Field(default=None, description="Names up to three of them; Count includes the rest.")
    notice: Optional[Notice] = Field(default=None, description="Says why these images have no findings and what to do; its code is `ScanRegistryDenied`, `ScanTimedOut`, `ScanResultNotStored` or `ScanNoteUnreadable`.")
    __properties: ClassVar[List[str]] = ["count", "images", "notice"]

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
        """Create an instance of ScanFindingsUnscannedImages from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notice
        if self.notice:
            _dict['notice'] = self.notice.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScanFindingsUnscannedImages from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "images": obj.get("images"),
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None
        })
        return _obj



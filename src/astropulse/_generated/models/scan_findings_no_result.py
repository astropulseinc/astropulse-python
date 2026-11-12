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
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.scan_finding_owner import ScanFindingOwner
from astropulse._generated.models.scan_findings_no_result_reason import ScanFindingsNoResultReason
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScanFindingsNoResult(BaseModel):
    """
    ScanFindingsNoResult
    """ # noqa: E501
    label: Optional[StrictStr] = Field(default=None, description="A few words for a table cell or a badge.")
    message: Optional[StrictStr] = Field(default=None, description="One or two sentences saying why there is no result and what to change.")
    notice: Optional[Notice] = Field(default=None, description="Set when a result is overdue (`ScanOverdue`), with the step that gets it scanned.")
    owner: Optional[ScanFindingOwner] = Field(default=None, description="The application or add-on.")
    reason: Optional[ScanFindingsNoResultReason] = Field(default=None, description="Why there is no result.")
    __properties: ClassVar[List[str]] = ["label", "message", "notice", "owner", "reason"]

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
        """Create an instance of ScanFindingsNoResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScanFindingsNoResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "message": obj.get("message"),
            "notice": Notice.from_dict(obj["notice"]) if obj.get("notice") is not None else None,
            "owner": ScanFindingOwner.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "reason": obj.get("reason")
        })
        return _obj



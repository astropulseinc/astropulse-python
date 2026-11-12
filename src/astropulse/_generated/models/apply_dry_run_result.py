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
from astropulse._generated.models.apply_dry_run_action import ApplyDryRunAction
from astropulse._generated.models.dry_run_verdict import DryRunVerdict
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplyDryRunResult(BaseModel):
    """
    ApplyDryRunResult
    """ # noqa: E501
    action: Optional[ApplyDryRunAction] = Field(default=None, description="What applying would do: Create when the resource does not exist yet, Update when it does.")
    message: Optional[StrictStr] = Field(default=None, description="What applying the request would do, in one sentence.")
    title: Optional[StrictStr] = Field(default=None, description="The verdict as a headline to show.")
    verdict: Optional[DryRunVerdict] = Field(default=None, description="How the dry run ended: always Passed, since a request that fails a check is refused with the error an apply would return.")
    __properties: ClassVar[List[str]] = ["action", "message", "title", "verdict"]

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
        """Create an instance of ApplyDryRunResult from a JSON string"""
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
        """Create an instance of ApplyDryRunResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "message": obj.get("message"),
            "title": obj.get("title"),
            "verdict": obj.get("verdict")
        })
        return _obj



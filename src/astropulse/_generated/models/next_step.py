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
from astropulse._generated.models.notice_operation import NoticeOperation
from astropulse._generated.models.shell_command import ShellCommand
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class NextStep(BaseModel):
    """
    NextStep
    """ # noqa: E501
    label: Optional[StrictStr] = Field(default=None, description="Says the step in a few words, at most 40 characters.")
    operation: Optional[NoticeOperation] = Field(default=None, description="The operationId of the API operation that takes the step; absent when the step is not an API call.")
    params: Optional[Dict[str, StrictStr]] = Field(default=None, description="The operation's path and query parameters, by name.")
    request: Optional[Dict[str, Any]] = Field(default=None, description="The operation's request body, or the part of it already known.")
    shell: Optional[ShellCommand] = Field(default=None, description="The command to run in a cloud shell or terminal, when the step needs one.")
    url: Optional[StrictStr] = Field(default=None, description="The page to open for a step taken outside AstroPulse, such as a cloud console page.")
    __properties: ClassVar[List[str]] = ["label", "operation", "params", "request", "shell", "url"]

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
        """Create an instance of NextStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shell
        if self.shell:
            _dict['shell'] = self.shell.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NextStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "operation": obj.get("operation"),
            "params": obj.get("params"),
            "request": obj.get("request"),
            "shell": ShellCommand.from_dict(obj["shell"]) if obj.get("shell") is not None else None,
            "url": obj.get("url")
        })
        return _obj



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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ShellCommand(BaseModel):
    """
    ShellCommand
    """ # noqa: E501
    command: Optional[StrictStr] = Field(default=None, description="The one line to paste and run.")
    script: Optional[StrictStr] = Field(default=None, description="The setup script the command runs, to read before running it.")
    script_name: Optional[StrictStr] = Field(default=None, description="The file name the command saves the setup script under.", alias="scriptName")
    script_summary: Optional[StrictStr] = Field(default=None, description="Says in one sentence what the setup script creates in your account.", alias="scriptSummary")
    shell: Optional[StrictStr] = Field(default=None, description="Where to run the command, such as Cloud Shell.")
    sign_in: Optional[StrictStr] = Field(default=None, description="Says which account the shell must be signed in to.", alias="signIn")
    __properties: ClassVar[List[str]] = ["command", "script", "scriptName", "scriptSummary", "shell", "signIn"]

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
        """Create an instance of ShellCommand from a JSON string"""
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
        """Create an instance of ShellCommand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "command": obj.get("command"),
            "script": obj.get("script"),
            "scriptName": obj.get("scriptName"),
            "scriptSummary": obj.get("scriptSummary"),
            "shell": obj.get("shell"),
            "signIn": obj.get("signIn")
        })
        return _obj



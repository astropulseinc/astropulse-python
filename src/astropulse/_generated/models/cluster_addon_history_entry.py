# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.application_version_state import ApplicationVersionState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonHistoryEntry(BaseModel):
    """
    ClusterAddonHistoryEntry
    """ # noqa: E501
    created_at: Optional[StrictStr] = Field(default=None, description="When this version was applied, RFC 3339.", alias="createdAt")
    created_by_display: Optional[StrictStr] = Field(default=None, description="Names whoever applied it.", alias="createdByDisplay")
    current: Optional[StrictBool] = Field(default=None, description="Marks the version installed right now.")
    rollback_eligible: Optional[StrictBool] = Field(default=None, description="Marks a version this add-on can be rolled back to.", alias="rollbackEligible")
    state: Optional[ApplicationVersionState] = Field(default=None, description="How this version ended: whether it converged, failed, or is still settling.")
    unavailable_reason: Optional[StrictStr] = Field(default=None, description="Says why this version cannot be rolled back to; set whenever rollbackEligible is false.", alias="unavailableReason")
    version: Optional[StrictStr] = Field(default=None, description="This entry's version as vN; a rollback to it takes N as its target version.")
    __properties: ClassVar[List[str]] = ["createdAt", "createdByDisplay", "current", "rollbackEligible", "state", "unavailableReason", "version"]

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
        """Create an instance of ClusterAddonHistoryEntry from a JSON string"""
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
        """Create an instance of ClusterAddonHistoryEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "createdByDisplay": obj.get("createdByDisplay"),
            "current": obj.get("current"),
            "rollbackEligible": obj.get("rollbackEligible"),
            "state": obj.get("state"),
            "unavailableReason": obj.get("unavailableReason"),
            "version": obj.get("version")
        })
        return _obj



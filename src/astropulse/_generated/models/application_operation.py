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
from astropulse._generated.models.application_rollback_state import ApplicationRollbackState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ApplicationOperation(BaseModel):
    """
    ApplicationOperation
    """ # noqa: E501
    application_name: Optional[StrictStr] = Field(default=None, description="The user-facing application name.", alias="applicationName")
    current_version: Optional[StrictStr] = Field(default=None, description="The version deployed before the operation.", alias="currentVersion")
    message: Optional[StrictStr] = Field(default=None, description="A human-readable status message.")
    next_actions: Optional[List[StrictStr]] = Field(default=None, description="Concrete follow-up commands for humans/automation.", alias="nextActions")
    operation_id: Optional[StrictStr] = Field(default=None, description="The idempotency/correlation id for this operation.", alias="operationId")
    phase: Optional[ApplicationRollbackState] = Field(default=None, description="The current Astro rollback/resume state.")
    progress_url: Optional[StrictStr] = Field(default=None, description="The polling/streaming endpoint for live progress.", alias="progressUrl")
    target_version: Optional[StrictStr] = Field(default=None, description="The version being rolled back/resumed to.", alias="targetVersion")
    workflow_id: Optional[StrictStr] = Field(default=None, description="AstroPulse's execution id for this operation. It is opaque: quote it in a support request, do not parse or store it.", alias="workflowId")
    __properties: ClassVar[List[str]] = ["applicationName", "currentVersion", "message", "nextActions", "operationId", "phase", "progressUrl", "targetVersion", "workflowId"]

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
        """Create an instance of ApplicationOperation from a JSON string"""
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
        """Create an instance of ApplicationOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "applicationName": obj.get("applicationName"),
            "currentVersion": obj.get("currentVersion"),
            "message": obj.get("message"),
            "nextActions": obj.get("nextActions"),
            "operationId": obj.get("operationId"),
            "phase": obj.get("phase"),
            "progressUrl": obj.get("progressUrl"),
            "targetVersion": obj.get("targetVersion"),
            "workflowId": obj.get("workflowId")
        })
        return _obj



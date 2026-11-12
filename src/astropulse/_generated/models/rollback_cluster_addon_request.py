# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class RollbackClusterAddonRequest(BaseModel):
    """
    RollbackClusterAddonRequest
    """ # noqa: E501
    dry_run: Optional[StrictBool] = Field(default=None, description="Checks the rollback and reports what it would do, without changing the add-on.", alias="dryRun")
    manual_approval: Optional[StrictBool] = Field(default=None, description="Confirms a rollback AstroPulse would otherwise hold.", alias="manualApproval")
    operation_id: Optional[StrictStr] = Field(default=None, description="Ties this rollback to an operation already in flight.", alias="operationId")
    reason: Optional[StrictStr] = Field(default=None, description="Recorded with the rollback.")
    target_version: StrictInt = Field(description="The revision number to roll back to, from the add-on's history. A revision number, not a chart version.", alias="targetVersion")
    __properties: ClassVar[List[str]] = ["dryRun", "manualApproval", "operationId", "reason", "targetVersion"]

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
        """Create an instance of RollbackClusterAddonRequest from a JSON string"""
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
        """Create an instance of RollbackClusterAddonRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dryRun": obj.get("dryRun"),
            "manualApproval": obj.get("manualApproval"),
            "operationId": obj.get("operationId"),
            "reason": obj.get("reason"),
            "targetVersion": obj.get("targetVersion")
        })
        return _obj



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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UpdateConfig(BaseModel):
    """
    UpdateConfig
    """ # noqa: E501
    allow_downgrade: Optional[StrictBool] = Field(default=None, description="Permits rollback to an older Kubernetes version. Required when target version is older than current version. Default: false (downgrades rejected for safety).", alias="allowDowngrade")
    dry_run: Optional[StrictBool] = Field(default=None, description="Validates the update without executing it. Returns the execution plan with preflight results, selected strategy, estimated duration, and any blocking issues. Default: false.", alias="dryRun")
    generate_report: Optional[StrictBool] = Field(default=None, description="Produces a comprehensive readiness report including the execution plan, strategy selection rationale, risk assessment, and provider-specific recommendations. Default: false.", alias="generateReport")
    max_surge: Optional[StrictStr] = Field(default=None, description="How many extra nodes may be added above the desired count during the update, as a count (\"1\") or a percentage (\"25%\"). When omitted, each node group keeps its own setting.", alias="maxSurge")
    max_unavailable: Optional[StrictStr] = Field(default=None, description="How many nodes may be unavailable at once during the update, as a count (\"2\") or a percentage (\"25%\"). When omitted, each node group keeps its own setting.", alias="maxUnavailable")
    reapply: Optional[StrictBool] = Field(default=None, description="Applies the named node groups even when they are unchanged, which replaces their nodes on a self-hosted cluster. Default: false.")
    replace_running: Optional[StrictBool] = Field(default=None, description="Cancels the update that is running on the cluster and starts this one once it has stopped. Without it, an update sent while another runs is refused. Default: false.", alias="replaceRunning")
    __properties: ClassVar[List[str]] = ["allowDowngrade", "dryRun", "generateReport", "maxSurge", "maxUnavailable", "reapply", "replaceRunning"]

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
        """Create an instance of UpdateConfig from a JSON string"""
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
        """Create an instance of UpdateConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowDowngrade": obj.get("allowDowngrade"),
            "dryRun": obj.get("dryRun"),
            "generateReport": obj.get("generateReport"),
            "maxSurge": obj.get("maxSurge"),
            "maxUnavailable": obj.get("maxUnavailable"),
            "reapply": obj.get("reapply"),
            "replaceRunning": obj.get("replaceRunning")
        })
        return _obj



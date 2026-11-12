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
from astropulse._generated.models.deployment_diff_item import DeploymentDiffItem
from astropulse._generated.models.dry_run_verdict import DryRunVerdict
from astropulse._generated.models.model_placement import ModelPlacement
from astropulse._generated.models.model_runtime_choice import ModelRuntimeChoice
from astropulse._generated.models.model_scaling_rule import ModelScalingRule
from astropulse._generated.models.notice import Notice
from astropulse._generated.models.outcome import Outcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class DeployValidationResult(BaseModel):
    """
    DeployValidationResult
    """ # noqa: E501
    changes: Optional[List[DeploymentDiffItem]] = Field(default=None, description="The fields an apply would change from the application's newest version; absent for a new application or when nothing changes.")
    message: Optional[StrictStr] = Field(default=None, description="Describes the outcome; it names any check that did not finish.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what the deploy would do differently from what the request asked; absent when there is nothing to say.")
    outcome: Optional[Outcome] = Field(default=None, description="Proceed when the application would deploy as submitted, and Blocked when a notice stops it.")
    placement: Optional[ModelPlacement] = Field(default=None, description="Says where a model's GPU replicas would run when a GPU node pool launches their nodes; absent otherwise.")
    runtime: Optional[ModelRuntimeChoice] = Field(default=None, description="The serving runtime a model would run on and the format it is served as; absent for an application that is not a model or a format no supported runtime serves.")
    scaling: Optional[ModelScalingRule] = Field(default=None, description="How a model's replicas would scale; absent for other source types.")
    title: Optional[StrictStr] = Field(default=None, description="The verdict as a headline to show.")
    unfinished_checks: Optional[List[StrictStr]] = Field(default=None, description="Names the checks that did not finish, so they neither passed nor failed.", alias="unfinishedChecks")
    verdict: Optional[DryRunVerdict] = Field(default=None, description="How the dry run ended: Passed, Failed, or Unfinished when some checks did not finish and none failed.")
    __properties: ClassVar[List[str]] = ["changes", "message", "notices", "outcome", "placement", "runtime", "scaling", "title", "unfinishedChecks", "verdict"]

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
        """Create an instance of DeployValidationResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item_changes in self.changes:
                if _item_changes:
                    _items.append(_item_changes.to_dict())
            _dict['changes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        # override the default output from pydantic by calling `to_dict()` of placement
        if self.placement:
            _dict['placement'] = self.placement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runtime
        if self.runtime:
            _dict['runtime'] = self.runtime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scaling
        if self.scaling:
            _dict['scaling'] = self.scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeployValidationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "changes": [DeploymentDiffItem.from_dict(_item) for _item in obj["changes"]] if obj.get("changes") is not None else None,
            "message": obj.get("message"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "outcome": obj.get("outcome"),
            "placement": ModelPlacement.from_dict(obj["placement"]) if obj.get("placement") is not None else None,
            "runtime": ModelRuntimeChoice.from_dict(obj["runtime"]) if obj.get("runtime") is not None else None,
            "scaling": ModelScalingRule.from_dict(obj["scaling"]) if obj.get("scaling") is not None else None,
            "title": obj.get("title"),
            "unfinishedChecks": obj.get("unfinishedChecks"),
            "verdict": obj.get("verdict")
        })
        return _obj



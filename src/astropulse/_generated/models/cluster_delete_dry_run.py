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
from astropulse._generated.models.cluster_delete_group import ClusterDeleteGroup
from astropulse._generated.models.dry_run_verdict import DryRunVerdict
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterDeleteDryRun(BaseModel):
    """
    ClusterDeleteDryRun
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster the delete was asked for.", alias="clusterName")
    groups: Optional[List[ClusterDeleteGroup]] = Field(default=None, description="What the delete would act on, by kind, the groups needing your attention first.")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what the delete would leave and what to do about it.")
    summary: Optional[StrictStr] = Field(default=None, description="One line naming, by kind, what the delete would act on.")
    title: StrictStr = Field(description="The verdict as a headline to show.")
    verdict: DryRunVerdict = Field(description="How the dry run ended: Passed when the delete would go ahead and every group was listed, Unfinished when a group could not be listed.")
    __properties: ClassVar[List[str]] = ["clusterName", "groups", "notices", "summary", "title", "verdict"]

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
        """Create an instance of ClusterDeleteDryRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notices (list)
        _items = []
        if self.notices:
            for _item_notices in self.notices:
                if _item_notices:
                    _items.append(_item_notices.to_dict())
            _dict['notices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterDeleteDryRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "groups": [ClusterDeleteGroup.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "summary": obj.get("summary"),
            "title": obj.get("title"),
            "verdict": obj.get("verdict")
        })
        return _obj



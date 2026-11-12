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
from astropulse._generated.models.cluster_addon_health_check import ClusterAddonHealthCheck
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonHealth(BaseModel):
    """
    ClusterAddonHealth
    """ # noqa: E501
    checks: Optional[List[ClusterAddonHealthCheck]] = Field(default=None, description="The individual results behind Healthy.")
    healthy: Optional[StrictBool] = Field(default=None, description="The single answer: is the add-on's own workload working?")
    last_checked: Optional[StrictStr] = Field(default=None, description="When the cluster last reported, RFC 3339.", alias="lastChecked")
    notices: Optional[List[Notice]] = Field(default=None, description="Say what the add-on's current health stops on the cluster, each with the one step to take.")
    overall_status: Optional[ClusterAddonStatus] = Field(default=None, description="Summarises the checks below in one word.", alias="overallStatus")
    __properties: ClassVar[List[str]] = ["checks", "healthy", "lastChecked", "notices", "overallStatus"]

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
        """Create an instance of ClusterAddonHealth from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item_checks in self.checks:
                if _item_checks:
                    _items.append(_item_checks.to_dict())
            _dict['checks'] = _items
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
        """Create an instance of ClusterAddonHealth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checks": [ClusterAddonHealthCheck.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None,
            "healthy": obj.get("healthy"),
            "lastChecked": obj.get("lastChecked"),
            "notices": [Notice.from_dict(_item) for _item in obj["notices"]] if obj.get("notices") is not None else None,
            "overallStatus": obj.get("overallStatus")
        })
        return _obj



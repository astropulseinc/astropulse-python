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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class GCPConnectRequest(BaseModel):
    """
    GCPConnectRequest
    """ # noqa: E501
    account_hint: Optional[StrictStr] = Field(default=None, description="The email address of the Google account that owns the project. When set, Cloud Shell opens as that account if it is signed in to the browser, and the setup script stops if it runs as another.", alias="accountHint", json_schema_extra={"examples": ["owner@example.com"]})
    cluster_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The name of the cluster", alias="clusterName")
    duration: Optional[StrictStr] = Field(default=None, description="The duration for which the credentials are valid", json_schema_extra={"examples": ["1h"]})
    force_update: Optional[StrictBool] = Field(default=None, description="Bypasses cluster existence checks and forces resource updates", alias="forceUpdate")
    target_project_id: Optional[StrictStr] = Field(default=None, description="The ID of the target GCP project (your project) Optional for credentials - looked up from cluster if not provided Format: 6-30 lowercase letters, digits, hyphens; must start with letter", alias="targetProjectId")
    target_project_number: Optional[StrictStr] = Field(default=None, description="The numeric GCP project number (required for cloud connect) Retrieve via: gcloud projects describe PROJECT_ID --format=\"value(projectNumber)\"", alias="targetProjectNumber")
    target_region: Optional[StrictStr] = Field(default=None, description="The GCP region where resources should be created Optional for credentials - looked up from cluster if not provided Format: location-direction-number (e.g., us-central1)", alias="targetRegion")
    __properties: ClassVar[List[str]] = ["accountHint", "clusterName", "duration", "forceUpdate", "targetProjectId", "targetProjectNumber", "targetRegion"]

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
        """Create an instance of GCPConnectRequest from a JSON string"""
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
        """Create an instance of GCPConnectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountHint": obj.get("accountHint"),
            "clusterName": obj.get("clusterName"),
            "duration": obj.get("duration"),
            "forceUpdate": obj.get("forceUpdate"),
            "targetProjectId": obj.get("targetProjectId"),
            "targetProjectNumber": obj.get("targetProjectNumber"),
            "targetRegion": obj.get("targetRegion")
        })
        return _obj



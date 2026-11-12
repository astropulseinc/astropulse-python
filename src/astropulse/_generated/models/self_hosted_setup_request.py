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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedSetupRequest(BaseModel):
    """
    SelfHostedSetupRequest
    """ # noqa: E501
    account_hint: Optional[StrictStr] = Field(default=None, description="The email address of the Google account that owns the project (GCP only). When set, Cloud Shell opens as that account if it is signed in to the browser, and the setup commands stop if they run as another.", alias="accountHint", json_schema_extra={"examples": ["owner@example.com"]})
    account_id: StrictStr = Field(description="The AWS account ID (12 digits) or GCP project ID (required).", alias="accountId")
    cluster_name: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The cluster the resources are for (required).", alias="clusterName")
    region: StrictStr = Field(description="Where the resources are created (required).")
    __properties: ClassVar[List[str]] = ["accountHint", "accountId", "clusterName", "region"]

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
        """Create an instance of SelfHostedSetupRequest from a JSON string"""
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
        """Create an instance of SelfHostedSetupRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountHint": obj.get("accountHint"),
            "accountId": obj.get("accountId"),
            "clusterName": obj.get("clusterName"),
            "region": obj.get("region")
        })
        return _obj



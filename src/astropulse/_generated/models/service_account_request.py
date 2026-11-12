# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from astropulse._generated.models.organization_role import OrganizationRole
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ServiceAccountRequest(BaseModel):
    """
    ServiceAccountRequest
    """ # noqa: E501
    description: Optional[Annotated[str, Field(strict=True, max_length=1000)]] = Field(default=None, description="Describes the automation, up to 1000 characters.")
    name: Annotated[str, Field(strict=True, max_length=100)] = Field(description="Labels the service account, up to 100 characters. It is unique among the organization's active service accounts; an archived account's name can be used again.")
    role: OrganizationRole = Field(description="The account's organization role: Viewer, Editor or Admin. A service account is never an Owner.")
    __properties: ClassVar[List[str]] = ["description", "name", "role"]

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
        """Create an instance of ServiceAccountRequest from a JSON string"""
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
        """Create an instance of ServiceAccountRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "role": obj.get("role")
        })
        return _obj



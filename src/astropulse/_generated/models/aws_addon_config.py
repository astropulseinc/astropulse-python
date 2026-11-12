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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AWSAddonConfig(BaseModel):
    """
    AWSAddonConfig
    """ # noqa: E501
    iam_role_arn: Optional[StrictStr] = Field(default=None, description="The role Node Autoscaling runs as in your AWS account, from the prerequisites stack AstroPulse generates, for a registered EKS cluster. Leave it empty on a cluster AstroPulse created.", alias="iamRoleArn")
    instance_profile: Optional[StrictStr] = Field(default=None, description="The instance profile given to the nodes Node Autoscaling starts.", alias="instanceProfile")
    security_group_tags: Optional[List[StrictStr]] = Field(default=None, description="Tags, written key=value, that pick the security groups for new nodes.", alias="securityGroupTags")
    subnet_tags: Optional[List[StrictStr]] = Field(default=None, description="Tags, written key=value, that pick the subnets for new nodes.", alias="subnetTags")
    __properties: ClassVar[List[str]] = ["iamRoleArn", "instanceProfile", "securityGroupTags", "subnetTags"]

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
        """Create an instance of AWSAddonConfig from a JSON string"""
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
        """Create an instance of AWSAddonConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iamRoleArn": obj.get("iamRoleArn"),
            "instanceProfile": obj.get("instanceProfile"),
            "securityGroupTags": obj.get("securityGroupTags"),
            "subnetTags": obj.get("subnetTags")
        })
        return _obj



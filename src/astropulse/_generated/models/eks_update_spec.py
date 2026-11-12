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
from astropulse._generated.models.ami_family import AMIFamily
from astropulse._generated.models.credentials import Credentials
from astropulse._generated.models.eks_auto_mode_config import EKSAutoModeConfig
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EKSUpdateSpec(BaseModel):
    """
    EKSUpdateSpec
    """ # noqa: E501
    ami_family: Optional[AMIFamily] = Field(default=None, description="The operating system image of the cluster's nodes. Omitted keeps it; changing it replaces the nodes.", alias="amiFamily")
    auto_mode: Optional[EKSAutoModeConfig] = Field(default=None, description="Updates the EKS Auto Mode GPU NodePool switch (optional). Valid only on clusters provisioned with computeMode `AutoMode`; flipping it renders or removes the pool.", alias="autoMode")
    credentials: Optional[Credentials] = Field(default=None, description="Replaces the cluster's stored static credentials when it carries data; omitted, or with the type and no data, it keeps them.")
    ecr_account_ids: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = Field(default=None, description="Replaces the other AWS accounts whose ECR the nodes pull from (optional, max 20); omit to keep them, send [] to clear them.", alias="ecrAccountIds")
    __properties: ClassVar[List[str]] = ["amiFamily", "autoMode", "credentials", "ecrAccountIds"]

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
        """Create an instance of EKSUpdateSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto_mode
        if self.auto_mode:
            _dict['autoMode'] = self.auto_mode.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EKSUpdateSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amiFamily": obj.get("amiFamily"),
            "autoMode": EKSAutoModeConfig.from_dict(obj["autoMode"]) if obj.get("autoMode") is not None else None,
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "ecrAccountIds": obj.get("ecrAccountIds")
        })
        return _obj



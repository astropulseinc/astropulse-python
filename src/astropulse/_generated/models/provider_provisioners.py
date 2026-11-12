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
from astropulse._generated.models.provider import Provider
from astropulse._generated.models.provisioner_info import ProvisionerInfo
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ProviderProvisioners(BaseModel):
    """
    ProviderProvisioners
    """ # noqa: E501
    account_id_example: Optional[StrictStr] = Field(default=None, description="An example of an account's identifier on this cloud, in its exact format.", alias="accountIdExample")
    account_id_label: Optional[StrictStr] = Field(default=None, description="The name of the field that identifies an account on this cloud, such as AWS account ID.", alias="accountIdLabel")
    account_label: Optional[StrictStr] = Field(default=None, description="What this cloud calls an account: Account, Project or Subscription.", alias="accountLabel")
    command_shell: Optional[StrictStr] = Field(default=None, description="Where this cloud's setup commands run, sent on each command as shell.", alias="commandShell")
    display_name: Optional[StrictStr] = Field(default=None, description="The cloud's name for people.", alias="displayName")
    provider: Optional[Provider] = Field(default=None, description="The cloud.")
    provisioners: Optional[List[ProvisionerInfo]] = Field(default=None, description="Offered in the order a client should list them.")
    __properties: ClassVar[List[str]] = ["accountIdExample", "accountIdLabel", "accountLabel", "commandShell", "displayName", "provider", "provisioners"]

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
        """Create an instance of ProviderProvisioners from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in provisioners (list)
        _items = []
        if self.provisioners:
            for _item_provisioners in self.provisioners:
                if _item_provisioners:
                    _items.append(_item_provisioners.to_dict())
            _dict['provisioners'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProviderProvisioners from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountIdExample": obj.get("accountIdExample"),
            "accountIdLabel": obj.get("accountIdLabel"),
            "accountLabel": obj.get("accountLabel"),
            "commandShell": obj.get("commandShell"),
            "displayName": obj.get("displayName"),
            "provider": obj.get("provider"),
            "provisioners": [ProvisionerInfo.from_dict(_item) for _item in obj["provisioners"]] if obj.get("provisioners") is not None else None
        })
        return _obj



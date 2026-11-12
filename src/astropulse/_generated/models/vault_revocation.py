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
from astropulse._generated.models.vault_lease import VaultLease
from astropulse._generated.models.vault_revocation_callback import VaultRevocationCallback
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class VaultRevocation(BaseModel):
    """
    VaultRevocation
    """ # noqa: E501
    callback: Optional[VaultRevocationCallback] = Field(default=None, description="What happened at the provider, for kinds that revoke the credential there too.")
    lease: Optional[VaultLease] = Field(default=None, description="The credential that was revoked.")
    stops_working: Optional[StrictStr] = Field(default=None, description="Says what no longer works now the credential is gone.", alias="stopsWorking")
    __properties: ClassVar[List[str]] = ["callback", "lease", "stopsWorking"]

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
        """Create an instance of VaultRevocation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of callback
        if self.callback:
            _dict['callback'] = self.callback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lease
        if self.lease:
            _dict['lease'] = self.lease.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VaultRevocation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "callback": VaultRevocationCallback.from_dict(obj["callback"]) if obj.get("callback") is not None else None,
            "lease": VaultLease.from_dict(obj["lease"]) if obj.get("lease") is not None else None,
            "stopsWorking": obj.get("stopsWorking")
        })
        return _obj



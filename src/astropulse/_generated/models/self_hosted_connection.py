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
from astropulse._generated.models.failure import Failure
from astropulse._generated.models.self_hosted_credential_state import SelfHostedCredentialState
from astropulse._generated.models.self_hosted_setup import SelfHostedSetup
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedConnection(BaseModel):
    """
    SelfHostedConnection
    """ # noqa: E501
    cluster_name: Optional[StrictStr] = Field(default=None, description="The cluster name", alias="clusterName")
    error: Optional[Failure] = Field(default=None, description="Contains any error message if the request failed")
    message: Optional[StrictStr] = Field(default=None, description="Says what was stored and, after a replace, which key is still valid in the cloud account and the command that deletes it there.")
    setup: Optional[SelfHostedSetup] = Field(default=None, description="The cluster's recorded setup, with the check and store steps this request ran.")
    status: Optional[SelfHostedCredentialState] = Field(default=None, description="How the stored credentials stand.")
    __properties: ClassVar[List[str]] = ["clusterName", "error", "message", "setup", "status"]

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
        """Create an instance of SelfHostedConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of setup
        if self.setup:
            _dict['setup'] = self.setup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelfHostedConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterName": obj.get("clusterName"),
            "error": Failure.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "message": obj.get("message"),
            "setup": SelfHostedSetup.from_dict(obj["setup"]) if obj.get("setup") is not None else None,
            "status": obj.get("status")
        })
        return _obj



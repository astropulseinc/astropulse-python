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
from astropulse._generated.models.provider import Provider
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedConnectRequest(BaseModel):
    """
    SelfHostedConnectRequest
    """ # noqa: E501
    account_id: StrictStr = Field(description="The cloud account or project ID (required)", alias="accountId")
    bucket_name: Optional[StrictStr] = Field(default=None, description="The state store bucket name. Defaults to the bucket setup creates for the cluster.", alias="bucketName")
    cluster_name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="The cluster name (required, 1-50 characters, valid DNS name)", alias="clusterName")
    credentials: Dict[str, StrictStr] = Field(description="Contains the cloud provider credential key-value pairs (required)")
    force_update: Optional[StrictBool] = Field(default=None, description="Overwrites existing vault credentials if true", alias="forceUpdate")
    provider: Provider = Field(description="The cloud the self-hosted cluster runs in.")
    region: StrictStr = Field(description="The cloud region (required)")
    without_setup: Optional[StrictBool] = Field(default=None, description="Stores credentials you made yourself when no setup was started for the cluster in this organization. Without it, only the credentials the cluster's setup created are stored.", alias="withoutSetup")
    __properties: ClassVar[List[str]] = ["accountId", "bucketName", "clusterName", "credentials", "forceUpdate", "provider", "region", "withoutSetup"]

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
        """Create an instance of SelfHostedConnectRequest from a JSON string"""
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
        """Create an instance of SelfHostedConnectRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "bucketName": obj.get("bucketName"),
            "clusterName": obj.get("clusterName"),
            "credentials": obj.get("credentials"),
            "forceUpdate": obj.get("forceUpdate"),
            "provider": obj.get("provider"),
            "region": obj.get("region"),
            "withoutSetup": obj.get("withoutSetup")
        })
        return _obj



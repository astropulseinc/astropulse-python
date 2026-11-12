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
from astropulse._generated.models.credentials import Credentials
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SelfHostedSpec(BaseModel):
    """
    SelfHostedSpec
    """ # noqa: E501
    account_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The cloud provider account identifier (required, minimum 1 character). For AWS: 12-digit account ID. For GCP: project ID (6-30 lowercase letters/digits/hyphens).", alias="accountId")
    bucket_name: Optional[StrictStr] = Field(default=None, description="The bucket that holds the cluster's state, in the cluster's account and region (S3 on AWS, Cloud Storage on GCP). Required with `Static` or `Dynamic` credentials; with `Vault` credentials it defaults to the bucket setup creates.", alias="bucketName")
    credentials: Credentials = Field(description="The cloud provider authentication credentials (required)")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The target Kubernetes version (optional, format: semver e.g. \"1.30.14\"). Only full semantic version is accepted (major.minor.patch). Major.minor format is not supported. If omitted, AstroPulse uses the default version.", alias="kubernetesVersion")
    network_id: Optional[StrictStr] = Field(default=None, description="The cloud provider network identifier (optional). For AWS: VPC ID. For GCP: VPC network name. If omitted, a new network is created.", alias="networkId")
    __properties: ClassVar[List[str]] = ["accountId", "bucketName", "credentials", "kubernetesVersion", "networkId"]

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
        """Create an instance of SelfHostedSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SelfHostedSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "bucketName": obj.get("bucketName"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "networkId": obj.get("networkId")
        })
        return _obj



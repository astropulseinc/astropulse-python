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
from astropulse._generated.models.workload_identity_cloud import WorkloadIdentityCloud
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AddonWorkloadIdentity(BaseModel):
    """
    AddonWorkloadIdentity
    """ # noqa: E501
    aws_role_arn: Optional[StrictStr] = Field(default=None, description="The AWS IAM role the add-on runs as, such as `arn:aws:iam::123456789012:role/dns`.", alias="awsRoleArn")
    azure_client_id: Optional[StrictStr] = Field(default=None, description="The client ID of the Azure managed identity the add-on runs as.", alias="azureClientId")
    cloud: Optional[WorkloadIdentityCloud] = Field(default=None, description="The cloud the identity belongs to, which decides the field it is set in. Left out, it is the cloud of the field that is set, or `Other` when only annotations or labels are.")
    gcp_service_account: Optional[StrictStr] = Field(default=None, description="The Google service account the add-on runs as, such as `dns@my-project.iam.gserviceaccount.com`.", alias="gcpServiceAccount")
    service_account_annotations: Optional[Dict[str, StrictStr]] = Field(default=None, description="Annotations your cloud needs on the add-on's service account, when `cloud` is `Other`.", alias="serviceAccountAnnotations")
    service_account_labels: Optional[Dict[str, StrictStr]] = Field(default=None, description="Labels your cloud needs on the add-on's workload identity, when `cloud` is `Other`.", alias="serviceAccountLabels")
    __properties: ClassVar[List[str]] = ["awsRoleArn", "azureClientId", "cloud", "gcpServiceAccount", "serviceAccountAnnotations", "serviceAccountLabels"]

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
        """Create an instance of AddonWorkloadIdentity from a JSON string"""
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
        """Create an instance of AddonWorkloadIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsRoleArn": obj.get("awsRoleArn"),
            "azureClientId": obj.get("azureClientId"),
            "cloud": obj.get("cloud"),
            "gcpServiceAccount": obj.get("gcpServiceAccount"),
            "serviceAccountAnnotations": obj.get("serviceAccountAnnotations"),
            "serviceAccountLabels": obj.get("serviceAccountLabels")
        })
        return _obj



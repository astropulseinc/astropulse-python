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
from astropulse._generated.models.eks_compute_mode import EKSComputeMode
from astropulse._generated.models.subnet_spec import SubnetSpec
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class EKSClusterSpec(BaseModel):
    """
    EKSClusterSpec
    """ # noqa: E501
    account_id: StrictStr = Field(description="The AWS account ID (required, 12-digit numeric string, e.g. \"123456789012\")", alias="accountId")
    ami_family: Optional[AMIFamily] = Field(default=None, description="The operating system image of the cluster's nodes. Defaults to `AmazonLinux2023`.", alias="amiFamily")
    auto_mode: Optional[EKSAutoModeConfig] = Field(default=None, description="Configures EKS Auto Mode extensions (optional). Valid only when computeMode is AutoMode; on ManagedNodeGroups, provision GPU capacity through the self-managed Karpenter add-on instead.", alias="autoMode")
    compute_mode: Optional[EKSComputeMode] = Field(default=None, description="Who creates and manages the worker nodes. `AutoMode` cannot be used with the Karpenter add-on.", alias="computeMode")
    credentials: Optional[Credentials] = Field(default=None, description="The AWS credentials the cluster is created and managed with; required for a new cluster. Applying an existing cluster again without them, or with the type and no data, keeps the stored ones.")
    ecr_account_ids: Optional[Annotated[List[StrictStr], Field(max_length=20)]] = Field(default=None, description="Other AWS accounts whose ECR the nodes pull from (optional, max 20). Their repository policies must allow the cluster's node roles, which the cluster reports.", alias="ecrAccountIds")
    kubernetes_version: Optional[StrictStr] = Field(default=None, description="The target Kubernetes version (optional). Accepts major.minor (e.g. \"1.30\") or major.minor.patch (e.g. \"1.30.14\") format. If omitted, AstroPulse uses the latest default version.", alias="kubernetesVersion")
    subnets: Optional[Dict[str, List[SubnetSpec]]] = Field(default=None, description="Maps availability zone names to subnet specifications for BYOVPC (optional). Required when VPCId is provided. Key is the zone name (e.g. \"us-west-2a\"), value is a list of SubnetSpec.")
    tags: Optional[Dict[str, StrictStr]] = Field(default=None, description="AWS tags applied to the cluster's node groups (optional, at most 40). Keys are 1-128 and values at most 256 letters, digits, spaces and _ . : / = + - @; keys may not start with aws:, platform.astropulse.io/, alpha.eksctl.io/, eksctl.cluster.k8s.io/ or karpenter.sh/.")
    vpc_cidr: Optional[StrictStr] = Field(default=None, description="The VPC's IPv4 range: required with vpcId, where it must equal the existing VPC's CIDR, and optional without it, where it sets the new VPC's range (e.g. \"10.0.0.0/16\"). It must be a /16 to /24 inside 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10 or 198.19.0.0/16.", alias="vpcCIDR")
    vpc_id: Optional[StrictStr] = Field(default=None, description="The existing AWS VPC ID (optional, format: vpc-xxxxxxxx). If omitted, a new VPC is created. Provide for BYOVPC deployments.", alias="vpcId")
    __properties: ClassVar[List[str]] = ["accountId", "amiFamily", "autoMode", "computeMode", "credentials", "ecrAccountIds", "kubernetesVersion", "subnets", "tags", "vpcCIDR", "vpcId"]

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
        """Create an instance of EKSClusterSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in subnets (dict of array)
        _field_dict_of_array = {}
        if self.subnets:
            for _key_subnets in self.subnets:
                if self.subnets[_key_subnets] is not None:
                    _field_dict_of_array[_key_subnets] = [
                        _item.to_dict() for _item in self.subnets[_key_subnets]
                    ]
            _dict['subnets'] = _field_dict_of_array
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EKSClusterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "amiFamily": obj.get("amiFamily"),
            "autoMode": EKSAutoModeConfig.from_dict(obj["autoMode"]) if obj.get("autoMode") is not None else None,
            "computeMode": obj.get("computeMode"),
            "credentials": Credentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "ecrAccountIds": obj.get("ecrAccountIds"),
            "kubernetesVersion": obj.get("kubernetesVersion"),
            "subnets": {
                _k: [SubnetSpec.from_dict(_item) for _item in _v] if _v is not None else None
                for _k, _v in obj["subnets"].items()
            }
            if obj.get("subnets") is not None
            else None,
            "tags": obj.get("tags"),
            "vpcCIDR": obj.get("vpcCIDR"),
            "vpcId": obj.get("vpcId")
        })
        return _obj



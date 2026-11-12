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
from astropulse._generated.models.aws_addon_config import AWSAddonConfig
from astropulse._generated.models.instance_type import InstanceType
from astropulse._generated.models.karpenter_capacity_reservations import KarpenterCapacityReservations
from astropulse._generated.models.karpenter_disruption import KarpenterDisruption
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class KarpenterAddonConfiguration(BaseModel):
    """
    KarpenterAddonConfiguration
    """ # noqa: E501
    allowed_accelerators: Optional[List[StrictStr]] = Field(default=None, description="The GPU models GPU nodes may have, as the machine catalog names them, such as l4 or a10g. Left out, every model is allowed.", alias="allowedAccelerators")
    ami_alias: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="The machine image new nodes start from, as family@version such as al2023@v20260818; changing it replaces existing nodes. Left out, AstroPulse's default applies; with the GPU node pool on, pin a version rather than @latest.", alias="amiAlias")
    aws: Optional[AWSAddonConfig] = Field(default=None, description="Node Autoscaling's AWS settings, on EKS only.")
    cpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="How the default pool's nodes may be bought; Spot costs less but needs the interruption queue. Left out, it keeps the last value set, or buys both, Spot first, where the cluster has the queue and `OnDemand` elsewhere.", alias="cpuCapacityTypes")
    cpu_limit: Optional[Annotated[int, Field(le=100000, strict=True, ge=1)]] = Field(default=100, description="The most CPU cores the default node pool may run in total, from 1 to 100000; pods wait once it is reached.", alias="cpuLimit")
    disruption: Optional[KarpenterDisruption] = Field(default=None, description="When nodes in the default pool are removed or replaced to save cost.")
    enable_gpu_node_pool: Optional[StrictBool] = Field(default=None, description="Lets Node Autoscaling start GPU nodes. They take only pods that tolerate nvidia.com/gpu:NoSchedule, and AstroPulse runs the NVIDIA device plugin on them, so remove any you installed yourself.", alias="enableGpuNodePool")
    gpu_capacity_reservations: Optional[KarpenterCapacityReservations] = Field(default=None, description="EC2 capacity reservations, Capacity Blocks included, that GPU nodes use before Spot or On-Demand. On a cluster AstroPulse created, each is checked before install to exist, be active, be a g or p instance type of generation 4 or later, and be in one of the cluster's zones.", alias="gpuCapacityReservations")
    gpu_capacity_types: Optional[List[InstanceType]] = Field(default=None, description="How GPU nodes may be bought; Spot costs less, but a node can be reclaimed at short notice and needs `interruptionQueue` on a registered cluster. Left out, a new pool buys `OnDemand` and an existing one keeps its current value.", alias="gpuCapacityTypes")
    gpu_disruption: Optional[KarpenterDisruption] = Field(default=None, description="When GPU nodes are removed or replaced to save cost; `gpuLimit` still caps GPU spend.", alias="gpuDisruption")
    gpu_instance_families: Optional[List[StrictStr]] = Field(default=None, description="The instance families GPU nodes may use, such as g6 or g5, at most 32.", alias="gpuInstanceFamilies")
    gpu_instance_sizes: Optional[List[StrictStr]] = Field(default=None, description="The instance sizes GPU nodes may use, such as xlarge or 2xlarge, at most 32.", alias="gpuInstanceSizes")
    gpu_limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=10, description="The most GPUs the GPU node pool may run in total, from 1 to 1000.", alias="gpuLimit")
    gpu_max_memory_gi_b_per_node: Optional[Annotated[int, Field(le=32768, strict=True, ge=1)]] = Field(default=None, description="The most memory one GPU node may have, in GiB, from 1 to 32768.", alias="gpuMaxMemoryGiBPerNode")
    gpu_max_vcpu_per_node: Optional[Annotated[int, Field(le=1024, strict=True, ge=1)]] = Field(default=None, description="The most CPU cores one GPU node may have, from 1 to 1024. Left out, the smallest size that fits each workload and your quota is chosen.", alias="gpuMaxVcpuPerNode")
    gpu_node_drain_timeout: Optional[StrictStr] = Field(default=None, description="How long a GPU node being removed waits for its pods to finish, up to 24h, or `None` for no limit. Left out, a new pool uses 1h and an existing one keeps its current value.", alias="gpuNodeDrainTimeout", json_schema_extra={"examples": ["1h"]})
    gpu_node_expiry: Optional[StrictStr] = Field(default=None, description="How long a GPU node runs before it is replaced, even while busy: `Never`, or days or hours such as 30d or 12h. Left out, a new pool uses `Never` and an existing one keeps its current value.", alias="gpuNodeExpiry", json_schema_extra={"examples": ["Never"]})
    interruption_queue: Optional[StrictBool] = Field(default=None, description="Turn on when your registered cluster has Node Autoscaling's interruption queue, from the prerequisites stack AstroPulse generates: Spot nodes are then drained before they are reclaimed, and Spot may be bought. Clusters AstroPulse created always have it.", alias="interruptionQueue")
    memory_limit: Optional[StrictStr] = Field(default='400Gi', description="The most memory the default node pool may run in total, such as 400Gi; the pool stops adding nodes at this or `cpuLimit`, whichever comes first.", alias="memoryLimit", json_schema_extra={"examples": ["400Gi"]})
    service_account_name: Optional[StrictStr] = Field(default=None, description="The Kubernetes service account Node Autoscaling runs as. Left out, AstroPulse's default applies.", alias="serviceAccountName")
    __properties: ClassVar[List[str]] = ["allowedAccelerators", "amiAlias", "aws", "cpuCapacityTypes", "cpuLimit", "disruption", "enableGpuNodePool", "gpuCapacityReservations", "gpuCapacityTypes", "gpuDisruption", "gpuInstanceFamilies", "gpuInstanceSizes", "gpuLimit", "gpuMaxMemoryGiBPerNode", "gpuMaxVcpuPerNode", "gpuNodeDrainTimeout", "gpuNodeExpiry", "interruptionQueue", "memoryLimit", "serviceAccountName"]

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
        """Create an instance of KarpenterAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws
        if self.aws:
            _dict['aws'] = self.aws.to_dict()
        # override the default output from pydantic by calling `to_dict()` of disruption
        if self.disruption:
            _dict['disruption'] = self.disruption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpu_capacity_reservations
        if self.gpu_capacity_reservations:
            _dict['gpuCapacityReservations'] = self.gpu_capacity_reservations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpu_disruption
        if self.gpu_disruption:
            _dict['gpuDisruption'] = self.gpu_disruption.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KarpenterAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedAccelerators": obj.get("allowedAccelerators"),
            "amiAlias": obj.get("amiAlias"),
            "aws": AWSAddonConfig.from_dict(obj["aws"]) if obj.get("aws") is not None else None,
            "cpuCapacityTypes": obj.get("cpuCapacityTypes"),
            "cpuLimit": obj.get("cpuLimit") if obj.get("cpuLimit") is not None else 100,
            "disruption": KarpenterDisruption.from_dict(obj["disruption"]) if obj.get("disruption") is not None else None,
            "enableGpuNodePool": obj.get("enableGpuNodePool"),
            "gpuCapacityReservations": KarpenterCapacityReservations.from_dict(obj["gpuCapacityReservations"]) if obj.get("gpuCapacityReservations") is not None else None,
            "gpuCapacityTypes": obj.get("gpuCapacityTypes"),
            "gpuDisruption": KarpenterDisruption.from_dict(obj["gpuDisruption"]) if obj.get("gpuDisruption") is not None else None,
            "gpuInstanceFamilies": obj.get("gpuInstanceFamilies"),
            "gpuInstanceSizes": obj.get("gpuInstanceSizes"),
            "gpuLimit": obj.get("gpuLimit") if obj.get("gpuLimit") is not None else 10,
            "gpuMaxMemoryGiBPerNode": obj.get("gpuMaxMemoryGiBPerNode"),
            "gpuMaxVcpuPerNode": obj.get("gpuMaxVcpuPerNode"),
            "gpuNodeDrainTimeout": obj.get("gpuNodeDrainTimeout"),
            "gpuNodeExpiry": obj.get("gpuNodeExpiry"),
            "interruptionQueue": obj.get("interruptionQueue"),
            "memoryLimit": obj.get("memoryLimit") if obj.get("memoryLimit") is not None else '400Gi',
            "serviceAccountName": obj.get("serviceAccountName")
        })
        return _obj



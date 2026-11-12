# coding: utf-8

"""
    Generated from the AstroPulse API document by OpenAPI Generator. Do not edit by hand:
    run scripts/generate.sh.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from astropulse._generated.models.addon_availability import AddonAvailability
from astropulse._generated.models.addon_component_sizing import AddonComponentSizing
from astropulse._generated.models.addon_resource_requirements import AddonResourceRequirements
from astropulse._generated.models.cert_manager_addon_configuration import CertManagerAddonConfiguration
from astropulse._generated.models.cost_visibility_addon_configuration import CostVisibilityAddonConfiguration
from astropulse._generated.models.external_dns_addon_configuration import ExternalDNSAddonConfiguration
from astropulse._generated.models.gateway_addon_configuration import GatewayAddonConfiguration
from astropulse._generated.models.karpenter_addon_configuration import KarpenterAddonConfiguration
from astropulse._generated.models.model_serving_addon_configuration import ModelServingAddonConfiguration
from astropulse._generated.models.nginx_addon_configuration import NginxAddonConfiguration
from astropulse._generated.models.vulnerability_scanning_addon_configuration import VulnerabilityScanningAddonConfiguration
from astropulse._generated.models.workload_autoscaling_addon_configuration import WorkloadAutoscalingAddonConfiguration
from astropulse._generated.models.workload_queueing_addon_configuration import WorkloadQueueingAddonConfiguration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddonConfiguration(BaseModel):
    """
    ClusterAddonConfiguration
    """ # noqa: E501
    availability: Optional[AddonAvailability] = Field(default=None, description="How many copies of the add-on's components run; choose `High` to keep it serving when a node fails, where the cluster has the nodes for it. Left out, an update keeps the current value and a new add-on runs `Standard`.")
    cert_manager: Optional[CertManagerAddonConfiguration] = Field(default=None, description="Configures the cert-manager add-on.", alias="certManager")
    components: Optional[Dict[str, AddonComponentSizing]] = Field(default=None, description="CPU and memory for each of the add-on's other components, by component name; change one only if it runs out of memory or the cluster is small. A component left out keeps its sizing, and `{}` returns it to AstroPulse's sizing.")
    cost_visibility: Optional[CostVisibilityAddonConfiguration] = Field(default=None, description="Configures the cost-visibility add-on.", alias="costVisibility")
    external_dns: Optional[ExternalDNSAddonConfiguration] = Field(default=None, description="Configures the external-dns add-on.", alias="externalDns")
    gateway: Optional[GatewayAddonConfiguration] = Field(default=None, description="Configures the gateway add-on.")
    karpenter: Optional[KarpenterAddonConfiguration] = Field(default=None, description="Configures the Node Autoscaling add-on.")
    model_serving: Optional[ModelServingAddonConfiguration] = Field(default=None, description="Configures the model-serving add-on.", alias="modelServing")
    nginx: Optional[NginxAddonConfiguration] = Field(default=None, description="Configures the nginx-ingress add-on.")
    resources: Optional[AddonResourceRequirements] = Field(default=None, description="CPU and memory for the add-on's main component; change them only if it runs out of memory or the cluster is small. Settings left out keep their current value, and `{}` returns to AstroPulse's sizing.")
    vulnerability_scanning: Optional[VulnerabilityScanningAddonConfiguration] = Field(default=None, description="Configures the vulnerability-scanning add-on.", alias="vulnerabilityScanning")
    workload_autoscaling: Optional[WorkloadAutoscalingAddonConfiguration] = Field(default=None, description="Configures the workload-autoscaling add-on.", alias="workloadAutoscaling")
    workload_queueing: Optional[WorkloadQueueingAddonConfiguration] = Field(default=None, description="Configures the workload-queueing add-on.", alias="workloadQueueing")
    __properties: ClassVar[List[str]] = ["availability", "certManager", "components", "costVisibility", "externalDns", "gateway", "karpenter", "modelServing", "nginx", "resources", "vulnerabilityScanning", "workloadAutoscaling", "workloadQueueing"]

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
        """Create an instance of ClusterAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cert_manager
        if self.cert_manager:
            _dict['certManager'] = self.cert_manager.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in components (dict)
        _field_dict = {}
        if self.components:
            for _key_components in self.components:
                if self.components[_key_components]:
                    _field_dict[_key_components] = self.components[_key_components].to_dict()
            _dict['components'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of cost_visibility
        if self.cost_visibility:
            _dict['costVisibility'] = self.cost_visibility.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_dns
        if self.external_dns:
            _dict['externalDns'] = self.external_dns.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gateway
        if self.gateway:
            _dict['gateway'] = self.gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of karpenter
        if self.karpenter:
            _dict['karpenter'] = self.karpenter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_serving
        if self.model_serving:
            _dict['modelServing'] = self.model_serving.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nginx
        if self.nginx:
            _dict['nginx'] = self.nginx.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vulnerability_scanning
        if self.vulnerability_scanning:
            _dict['vulnerabilityScanning'] = self.vulnerability_scanning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workload_autoscaling
        if self.workload_autoscaling:
            _dict['workloadAutoscaling'] = self.workload_autoscaling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workload_queueing
        if self.workload_queueing:
            _dict['workloadQueueing'] = self.workload_queueing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availability": obj.get("availability"),
            "certManager": CertManagerAddonConfiguration.from_dict(obj["certManager"]) if obj.get("certManager") is not None else None,
            "components": dict(
                (_k, AddonComponentSizing.from_dict(_v))
                for _k, _v in obj["components"].items()
            )
            if obj.get("components") is not None
            else None,
            "costVisibility": CostVisibilityAddonConfiguration.from_dict(obj["costVisibility"]) if obj.get("costVisibility") is not None else None,
            "externalDns": ExternalDNSAddonConfiguration.from_dict(obj["externalDns"]) if obj.get("externalDns") is not None else None,
            "gateway": GatewayAddonConfiguration.from_dict(obj["gateway"]) if obj.get("gateway") is not None else None,
            "karpenter": KarpenterAddonConfiguration.from_dict(obj["karpenter"]) if obj.get("karpenter") is not None else None,
            "modelServing": ModelServingAddonConfiguration.from_dict(obj["modelServing"]) if obj.get("modelServing") is not None else None,
            "nginx": NginxAddonConfiguration.from_dict(obj["nginx"]) if obj.get("nginx") is not None else None,
            "resources": AddonResourceRequirements.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "vulnerabilityScanning": VulnerabilityScanningAddonConfiguration.from_dict(obj["vulnerabilityScanning"]) if obj.get("vulnerabilityScanning") is not None else None,
            "workloadAutoscaling": WorkloadAutoscalingAddonConfiguration.from_dict(obj["workloadAutoscaling"]) if obj.get("workloadAutoscaling") is not None else None,
            "workloadQueueing": WorkloadQueueingAddonConfiguration.from_dict(obj["workloadQueueing"]) if obj.get("workloadQueueing") is not None else None
        })
        return _obj



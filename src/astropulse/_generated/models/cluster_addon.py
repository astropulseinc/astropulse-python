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
from astropulse._generated.models.application_status import ApplicationStatus
from astropulse._generated.models.cluster_addon_accelerator_readiness import ClusterAddonAcceleratorReadiness
from astropulse._generated.models.cluster_addon_configuration import ClusterAddonConfiguration
from astropulse._generated.models.cluster_addon_cost_pricing import ClusterAddonCostPricing
from astropulse._generated.models.cluster_addon_exposure import ClusterAddonExposure
from astropulse._generated.models.cluster_addon_health import ClusterAddonHealth
from astropulse._generated.models.cluster_addon_ingress_tls import ClusterAddonIngressTLS
from astropulse._generated.models.cluster_addon_model_cache_readiness import ClusterAddonModelCacheReadiness
from astropulse._generated.models.cluster_addon_queue_namespaces import ClusterAddonQueueNamespaces
from astropulse._generated.models.cluster_addon_resilience import ClusterAddonResilience
from astropulse._generated.models.cluster_addon_status import ClusterAddonStatus
from astropulse._generated.models.cluster_addon_support import ClusterAddonSupport
from astropulse._generated.models.cluster_addon_tls_readiness import ClusterAddonTLSReadiness
from astropulse._generated.models.cluster_addon_type import ClusterAddonType
from astropulse._generated.models.notice import Notice
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ClusterAddon(BaseModel):
    """
    ClusterAddon
    """ # noqa: E501
    accelerator: Optional[ClusterAddonAcceleratorReadiness] = Field(default=None, description="Reported for the accelerator-metrics add-on only: what this cluster has for the exporter to measure. See ClusterAddonAcceleratorReadiness.")
    available_upgrades: Optional[List[StrictStr]] = Field(default=None, description="The versions it can move to, ordered oldest to newest: the last one is the newest release on offer.", alias="availableUpgrades")
    configurable: Optional[StrictBool] = Field(default=None, description="Reports whether this add-on accepts a configuration. False means it installs with no settings of its own.")
    configuration: Optional[ClusterAddonConfiguration] = Field(default=None, description="The settings it is running with, as they were applied.")
    current_version: Optional[StrictStr] = Field(default=None, description="The Astro chart version installed -- what `apply --version` and rollback take. See UpstreamVersion for the release inside.", alias="currentVersion")
    deployed_at: Optional[StrictStr] = Field(default=None, description="When the add-on was first installed, RFC 3339.", alias="deployedAt")
    display_name: Optional[StrictStr] = Field(default=None, description="The add-on's name in front of a person.", alias="displayName")
    display_status: Optional[StrictStr] = Field(default=None, description="The short text to show for this add-on in a list when its notice changes what to show; absent otherwise, when its status's display name applies.", alias="displayStatus")
    endpoint_authentication: Optional[List[StrictStr]] = Field(default=None, description="Lists the access-policy mechanisms (jwt, apiKeys) the installed release enforces on model endpoints. Absent when the add-on cannot enforce any: an exposure add-on that only routes, or a release the catalog does not declare.", alias="endpointAuthentication")
    exposure: Optional[ClusterAddonExposure] = Field(default=None, description="How the add-on can be reached, for the exposure add-ons (gateway, nginx-ingress) only, as the cluster agent last observed it. Absent on every other add-on.")
    findings_policy: Optional[StrictStr] = Field(default=None, description="Says which findings the vulnerability-scanning add-on leaves out of its results. Absent on every other add-on.", alias="findingsPolicy")
    health: Optional[ClusterAddonHealth] = Field(default=None, description="What the cluster reports about the add-on's own workload.")
    ingress_tls: Optional[ClusterAddonIngressTLS] = Field(default=None, description="Reported for the nginx-ingress add-on only: the TLS modes it offers applications.", alias="ingressTls")
    last_updated_at: Optional[StrictStr] = Field(default=None, description="When it was last changed, RFC 3339.", alias="lastUpdatedAt")
    model_cache: Optional[ClusterAddonModelCacheReadiness] = Field(default=None, description="Reported for the model-serving add-on only: what its weight cache holds on this cluster, and how the cluster's models read private artifacts. See ClusterAddonModelCacheReadiness.", alias="modelCache")
    name: Optional[StrictStr] = Field(default=None, description="The name of the Application serving this add-on on the cluster.")
    phase: Optional[ApplicationStatus] = Field(default=None, description="What the add-on's workload is doing now, in the same words as an application's phase. Absent before the add-on has a workload.")
    pricing: Optional[ClusterAddonCostPricing] = Field(default=None, description="Reported for the cost-visibility add-on only: the price-sheet rates its configuration sets that this cluster does not apply yet. Absent when every rate applies.")
    queue_namespaces: Optional[ClusterAddonQueueNamespaces] = Field(default=None, description="Is, for the workload-queueing add-on, where the namespaces it gives a queue differ from those of the queued applications; absent when they agree.", alias="queueNamespaces")
    resilience: Optional[ClusterAddonResilience] = Field(default=None, description="How the add-on runs on this cluster: its effective availability, how many copies run and why, and its main component's sizing.")
    status: Optional[ClusterAddonStatus] = Field(default=None, description="The lifecycle answer: is this add-on installed and working? A resync or upgrade of a working add-on leaves it `Deployed`, because it is still installed and still serving.")
    status_notice: Optional[Notice] = Field(default=None, description="Says what a failed or unhealthy status, or an unfinished rollback, means and the one step that resolves it; absent otherwise.", alias="statusNotice")
    status_reason: Optional[StrictStr] = Field(default=None, description="A sentence explaining the add-on's status, such as why it failed or why no upgrade is offered. Empty when there is nothing to explain.", alias="statusReason")
    support: Optional[ClusterAddonSupport] = Field(default=None, description="Says whether the installed version is supported and until when. Absent when the installed version is not known.")
    syncing: Optional[StrictBool] = Field(default=None, description="The operation answer: is deployment work in flight right now? `status` stays `Deployed` while a working add-on is resynced or upgraded.")
    tls: Optional[ClusterAddonTLSReadiness] = Field(default=None, description="Reported for the cert-manager add-on only: what its configuration can mint on this cluster. See ClusterAddonTLSReadiness.")
    type: Optional[ClusterAddonType] = Field(default=None, description="The add-on's public name, and what every add-on command takes.")
    upstream_version: Optional[StrictStr] = Field(default=None, description="The third-party release the installed version runs, such as \"cert-manager v1.21.2\" or \"KServe v0.20.0\". Empty when there is none.", alias="upstreamVersion")
    __properties: ClassVar[List[str]] = ["accelerator", "availableUpgrades", "configurable", "configuration", "currentVersion", "deployedAt", "displayName", "displayStatus", "endpointAuthentication", "exposure", "findingsPolicy", "health", "ingressTls", "lastUpdatedAt", "modelCache", "name", "phase", "pricing", "queueNamespaces", "resilience", "status", "statusNotice", "statusReason", "support", "syncing", "tls", "type", "upstreamVersion"]

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
        """Create an instance of ClusterAddon from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accelerator
        if self.accelerator:
            _dict['accelerator'] = self.accelerator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exposure
        if self.exposure:
            _dict['exposure'] = self.exposure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of health
        if self.health:
            _dict['health'] = self.health.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ingress_tls
        if self.ingress_tls:
            _dict['ingressTls'] = self.ingress_tls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model_cache
        if self.model_cache:
            _dict['modelCache'] = self.model_cache.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of queue_namespaces
        if self.queue_namespaces:
            _dict['queueNamespaces'] = self.queue_namespaces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resilience
        if self.resilience:
            _dict['resilience'] = self.resilience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_notice
        if self.status_notice:
            _dict['statusNotice'] = self.status_notice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of support
        if self.support:
            _dict['support'] = self.support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls
        if self.tls:
            _dict['tls'] = self.tls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterAddon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accelerator": ClusterAddonAcceleratorReadiness.from_dict(obj["accelerator"]) if obj.get("accelerator") is not None else None,
            "availableUpgrades": obj.get("availableUpgrades"),
            "configurable": obj.get("configurable"),
            "configuration": ClusterAddonConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "currentVersion": obj.get("currentVersion"),
            "deployedAt": obj.get("deployedAt"),
            "displayName": obj.get("displayName"),
            "displayStatus": obj.get("displayStatus"),
            "endpointAuthentication": obj.get("endpointAuthentication"),
            "exposure": ClusterAddonExposure.from_dict(obj["exposure"]) if obj.get("exposure") is not None else None,
            "findingsPolicy": obj.get("findingsPolicy"),
            "health": ClusterAddonHealth.from_dict(obj["health"]) if obj.get("health") is not None else None,
            "ingressTls": ClusterAddonIngressTLS.from_dict(obj["ingressTls"]) if obj.get("ingressTls") is not None else None,
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "modelCache": ClusterAddonModelCacheReadiness.from_dict(obj["modelCache"]) if obj.get("modelCache") is not None else None,
            "name": obj.get("name"),
            "phase": obj.get("phase"),
            "pricing": ClusterAddonCostPricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "queueNamespaces": ClusterAddonQueueNamespaces.from_dict(obj["queueNamespaces"]) if obj.get("queueNamespaces") is not None else None,
            "resilience": ClusterAddonResilience.from_dict(obj["resilience"]) if obj.get("resilience") is not None else None,
            "status": obj.get("status"),
            "statusNotice": Notice.from_dict(obj["statusNotice"]) if obj.get("statusNotice") is not None else None,
            "statusReason": obj.get("statusReason"),
            "support": ClusterAddonSupport.from_dict(obj["support"]) if obj.get("support") is not None else None,
            "syncing": obj.get("syncing"),
            "tls": ClusterAddonTLSReadiness.from_dict(obj["tls"]) if obj.get("tls") is not None else None,
            "type": obj.get("type"),
            "upstreamVersion": obj.get("upstreamVersion")
        })
        return _obj



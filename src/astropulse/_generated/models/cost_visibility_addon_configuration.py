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
from typing_extensions import Annotated
from astropulse._generated.models.cost_metrics_source import CostMetricsSource
from astropulse._generated.models.cost_price_sheet import CostPriceSheet
from astropulse._generated.models.cost_pricing import CostPricing
from astropulse._generated.models.cost_visibility_prometheus_configuration import CostVisibilityPrometheusConfiguration
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class CostVisibilityAddonConfiguration(BaseModel):
    """
    CostVisibilityAddonConfiguration
    """ # noqa: E501
    collection_interval_minutes: Optional[Annotated[int, Field(le=1440, strict=True, ge=1)]] = Field(default=5, description="How often, in minutes, usage is collected, from 1 to 1440; costs are still reported by the hour.", alias="collectionIntervalMinutes")
    metrics_source: Optional[CostMetricsSource] = Field(default=None, description="Where cost reporting reads usage. Left out, it is `Existing` when `prometheusEndpoint` is set and `Managed` otherwise.", alias="metricsSource")
    price_sheet: Optional[CostPriceSheet] = Field(default=None, description="Your own unit prices, used instead of published ones. Usage with no price is reported as unpriced, never as free.", alias="priceSheet")
    pricing: Optional[CostPricing] = Field(default=None, description="How usage is priced. Left out, it is `PriceSheet` when `priceSheet` is set and `Published` otherwise.")
    pricing_role_arn: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = Field(default=None, description="An AWS IAM role allowed `ec2:DescribeSpotPriceHistory`, so Spot nodes are priced at their Spot price on a cluster AstroPulse didn't create.", alias="pricingRoleArn")
    prometheus: Optional[CostVisibilityPrometheusConfiguration] = Field(default=None, description="Settings for the Prometheus AstroPulse installs and runs; not accepted with `prometheusEndpoint`.")
    prometheus_endpoint: Optional[Annotated[str, Field(strict=True, max_length=512)]] = Field(default=None, description="The address of a Prometheus you already run, reachable from the cluster, to read usage from instead of installing one.", alias="prometheusEndpoint")
    __properties: ClassVar[List[str]] = ["collectionIntervalMinutes", "metricsSource", "priceSheet", "pricing", "pricingRoleArn", "prometheus", "prometheusEndpoint"]

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
        """Create an instance of CostVisibilityAddonConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_sheet
        if self.price_sheet:
            _dict['priceSheet'] = self.price_sheet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prometheus
        if self.prometheus:
            _dict['prometheus'] = self.prometheus.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CostVisibilityAddonConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "collectionIntervalMinutes": obj.get("collectionIntervalMinutes") if obj.get("collectionIntervalMinutes") is not None else 5,
            "metricsSource": obj.get("metricsSource"),
            "priceSheet": CostPriceSheet.from_dict(obj["priceSheet"]) if obj.get("priceSheet") is not None else None,
            "pricing": obj.get("pricing"),
            "pricingRoleArn": obj.get("pricingRoleArn"),
            "prometheus": CostVisibilityPrometheusConfiguration.from_dict(obj["prometheus"]) if obj.get("prometheus") is not None else None,
            "prometheusEndpoint": obj.get("prometheusEndpoint")
        })
        return _obj



# PricingFeatureValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_roles** | **List[str]** | For role-based features (e.g. \&quot;admin, developer, platform-admin\&quot;) | [optional] 
**enabled** | **bool** | For boolean features (e.g. \&quot;Premium Support\&quot;) | [optional] 
**limit** | **int** | For numeric limits (e.g. \&quot;10 applications\&quot;) | [optional] 
**tier** | **str** | For tiered features (e.g. \&quot;Basic\&quot; vs \&quot;Advanced\&quot;) | [optional] 

## Example

```python
from astropulse._generated.models.pricing_feature_value import PricingFeatureValue

# TODO update the JSON string below
json = "{}"
# create an instance of PricingFeatureValue from a JSON string
pricing_feature_value_instance = PricingFeatureValue.from_json(json)
# print the JSON string representation of the object
print(PricingFeatureValue.to_json())

# convert the object into a dict
pricing_feature_value_dict = pricing_feature_value_instance.to_dict()
# create an instance of PricingFeatureValue from a dict
pricing_feature_value_from_dict = PricingFeatureValue.from_dict(pricing_feature_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



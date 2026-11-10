# AvailabilityTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | [**TierType**](TierType.md) | The availability tier the application runs at. | [optional] 

## Example

```python
from astropulse._generated.models.availability_tier import AvailabilityTier

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityTier from a JSON string
availability_tier_instance = AvailabilityTier.from_json(json)
# print the JSON string representation of the object
print(AvailabilityTier.to_json())

# convert the object into a dict
availability_tier_dict = availability_tier_instance.to_dict()
# create an instance of AvailabilityTier from a dict
availability_tier_from_dict = AvailabilityTier.from_dict(availability_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



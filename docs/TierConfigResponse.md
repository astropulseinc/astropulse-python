# TierConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TierConfig**](TierConfig.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.tier_config_response import TierConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TierConfigResponse from a JSON string
tier_config_response_instance = TierConfigResponse.from_json(json)
# print the JSON string representation of the object
print(TierConfigResponse.to_json())

# convert the object into a dict
tier_config_response_dict = tier_config_response_instance.to_dict()
# create an instance of TierConfigResponse from a dict
tier_config_response_from_dict = TierConfigResponse.from_dict(tier_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



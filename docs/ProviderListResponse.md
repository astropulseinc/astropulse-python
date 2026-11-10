# ProviderListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Provider]**](Provider.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.provider_list_response import ProviderListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderListResponse from a JSON string
provider_list_response_instance = ProviderListResponse.from_json(json)
# print the JSON string representation of the object
print(ProviderListResponse.to_json())

# convert the object into a dict
provider_list_response_dict = provider_list_response_instance.to_dict()
# create an instance of ProviderListResponse from a dict
provider_list_response_from_dict = ProviderListResponse.from_dict(provider_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



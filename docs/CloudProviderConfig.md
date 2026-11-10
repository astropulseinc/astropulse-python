# CloudProviderConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zones** | **List[str]** |  | [optional] 
**provider** | [**CloudProviderName**](CloudProviderName.md) |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cloud_provider_config import CloudProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProviderConfig from a JSON string
cloud_provider_config_instance = CloudProviderConfig.from_json(json)
# print the JSON string representation of the object
print(CloudProviderConfig.to_json())

# convert the object into a dict
cloud_provider_config_dict = cloud_provider_config_instance.to_dict()
# create an instance of CloudProviderConfig from a dict
cloud_provider_config_from_dict = CloudProviderConfig.from_dict(cloud_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



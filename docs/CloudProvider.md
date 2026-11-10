# CloudProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**CloudProviderName**](CloudProviderName.md) | The cloud provider. | 
**region** | **str** | The cloud provider region (required, minimum 1 character). Provider-specific format: AWS (e.g. \&quot;us-east-1\&quot;), GCP (e.g. \&quot;us-central1\&quot;), Azure (e.g. \&quot;eastus\&quot;). | 

## Example

```python
from astropulse._generated.models.cloud_provider import CloudProvider

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvider from a JSON string
cloud_provider_instance = CloudProvider.from_json(json)
# print the JSON string representation of the object
print(CloudProvider.to_json())

# convert the object into a dict
cloud_provider_dict = cloud_provider_instance.to_dict()
# create an instance of CloudProvider from a dict
cloud_provider_from_dict = CloudProvider.from_dict(cloud_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



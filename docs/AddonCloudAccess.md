# AddonCloudAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_keys** | **Dict[str, str]** | The key the credentials take in the Secret &#x60;secretRef&#x60; names, by the provider the add-on publishes to; absent when the add-on reads no file from it. | [optional] 
**service_account** | [**AddonServiceAccount**](AddonServiceAccount.md) | The Kubernetes service account the add-on runs as, which the cloud identity in &#x60;identity&#x60; must trust; absent when the add-on runs as no one fixed account. | [optional] 

## Example

```python
from astropulse._generated.models.addon_cloud_access import AddonCloudAccess

# TODO update the JSON string below
json = "{}"
# create an instance of AddonCloudAccess from a JSON string
addon_cloud_access_instance = AddonCloudAccess.from_json(json)
# print the JSON string representation of the object
print(AddonCloudAccess.to_json())

# convert the object into a dict
addon_cloud_access_dict = addon_cloud_access_instance.to_dict()
# create an instance of AddonCloudAccess from a dict
addon_cloud_access_from_dict = AddonCloudAccess.from_dict(addon_cloud_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



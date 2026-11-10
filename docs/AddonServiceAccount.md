# AddonServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The service account&#39;s name. | [optional] 
**namespace** | **str** | The namespace the service account is in. | [optional] 

## Example

```python
from astropulse._generated.models.addon_service_account import AddonServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AddonServiceAccount from a JSON string
addon_service_account_instance = AddonServiceAccount.from_json(json)
# print the JSON string representation of the object
print(AddonServiceAccount.to_json())

# convert the object into a dict
addon_service_account_dict = addon_service_account_instance.to_dict()
# create an instance of AddonServiceAccount from a dict
addon_service_account_from_dict = AddonServiceAccount.from_dict(addon_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



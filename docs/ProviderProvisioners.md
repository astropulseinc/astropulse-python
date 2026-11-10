# ProviderProvisioners


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id_example** | **str** | An example of an account&#39;s identifier on this cloud, in its exact format. | [optional] 
**account_id_label** | **str** | The name of the field that identifies an account on this cloud, such as AWS account ID. | [optional] 
**account_label** | **str** | What this cloud calls an account: Account, Project or Subscription. | [optional] 
**command_shell** | **str** | Where this cloud&#39;s setup commands run, sent on each command as shell. | [optional] 
**display_name** | **str** | The cloud&#39;s name for people. | [optional] 
**provider** | [**Provider**](Provider.md) | The cloud. | [optional] 
**provisioners** | [**List[ProvisionerInfo]**](ProvisionerInfo.md) | Offered in the order a client should list them. | [optional] 

## Example

```python
from astropulse._generated.models.provider_provisioners import ProviderProvisioners

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProvisioners from a JSON string
provider_provisioners_instance = ProviderProvisioners.from_json(json)
# print the JSON string representation of the object
print(ProviderProvisioners.to_json())

# convert the object into a dict
provider_provisioners_dict = provider_provisioners_instance.to_dict()
# create an instance of ProviderProvisioners from a dict
provider_provisioners_from_dict = ProviderProvisioners.from_dict(provider_provisioners_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



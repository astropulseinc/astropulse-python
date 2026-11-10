# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | [**List[DomainBinding]**](DomainBinding.md) | The hostnames under the domain bound to applications. | [optional] 
**created_at** | **datetime** | When the domain was claimed. | [optional] 
**failure_reason** | **str** | Why verification failed; absent unless it did. | [optional] 
**id** | **str** | The domain&#39;s identifier. | [optional] 
**name** | **str** | The domain name, such as example.com. | [optional] 
**org_id** | **str** | The organization that claims the domain. | [optional] 
**status** | [**DomainStatus**](DomainStatus.md) | How far the domain&#39;s verification has got. | [optional] 
**updated_at** | **datetime** | When the domain last changed. | [optional] 
**verification_expires_at** | **datetime** | When the verification challenge expires. | [optional] 
**verification_record_name** | **str** | The DNS name to publish the verification TXT record at. | [optional] 
**verification_record_value** | **str** | The value the verification TXT record must hold. | [optional] 
**verification_token** | **str** | The token inside the verification value. | [optional] 
**verified_at** | **datetime** | When the domain was verified; absent until it is. | [optional] 

## Example

```python
from astropulse._generated.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



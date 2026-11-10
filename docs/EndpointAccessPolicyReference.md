# EndpointAccessPolicyReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Of the organization&#39;s access policy to enforce on the endpoint. | [optional] 
**var_none** | [**EndpointAccessPolicyNone**](EndpointAccessPolicyNone.md) | Opts the endpoint out of caller authentication: anyone who reaches the hostname can call it. Compared exactly; applying it needs organization owner authority and is audited. | [optional] 
**revision** | **int** | Of the named policy this deployment is bound to. Resolved by the API at apply (omit it to take the latest) and preserved in deployment and rollback snapshots, so a policy update reaches an application on its next deploy, never silently. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_access_policy_reference import EndpointAccessPolicyReference

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAccessPolicyReference from a JSON string
endpoint_access_policy_reference_instance = EndpointAccessPolicyReference.from_json(json)
# print the JSON string representation of the object
print(EndpointAccessPolicyReference.to_json())

# convert the object into a dict
endpoint_access_policy_reference_dict = endpoint_access_policy_reference_instance.to_dict()
# create an instance of EndpointAccessPolicyReference from a dict
endpoint_access_policy_reference_from_dict = EndpointAccessPolicyReference.from_dict(endpoint_access_policy_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



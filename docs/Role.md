# Role


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignable** | **bool** | True for the roles add-member and set-role accept. The owner role is false: it moves only by ownership transfer. | [optional] 
**id** | **str** | Identifies the role; the same value as &#x60;key&#x60;. | [optional] 
**key** | [**OrganizationRole**](OrganizationRole.md) | The value add-member and set-role take as &#x60;role&#x60;. | [optional] 
**name** | **str** | The role&#39;s display name. | [optional] 
**permissions** | [**List[Permission]**](Permission.md) | What a holder of the role may do. | [optional] 

## Example

```python
from astropulse._generated.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



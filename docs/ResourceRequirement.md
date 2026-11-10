# ResourceRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | [**MemResources**](MemResources.md) | The memory the application may use, as a minimum and a maximum. Default unit is Gi. | 

## Example

```python
from astropulse._generated.models.resource_requirement import ResourceRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceRequirement from a JSON string
resource_requirement_instance = ResourceRequirement.from_json(json)
# print the JSON string representation of the object
print(ResourceRequirement.to_json())

# convert the object into a dict
resource_requirement_dict = resource_requirement_instance.to_dict()
# create an instance of ResourceRequirement from a dict
resource_requirement_from_dict = ResourceRequirement.from_dict(resource_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



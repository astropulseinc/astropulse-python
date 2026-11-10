# ResolvedNodeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator_type** | **str** | The provider&#39;s own name for the accelerator, where the provider attaches it by name (GCP, for example nvidia-l4); empty otherwise. | [optional] 
**machine_types** | **List[str]** | The machine types the node group will run, first choice first. | [optional] 
**name** | **str** | The node group&#39;s name. | [optional] 

## Example

```python
from astropulse._generated.models.resolved_node_group import ResolvedNodeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedNodeGroup from a JSON string
resolved_node_group_instance = ResolvedNodeGroup.from_json(json)
# print the JSON string representation of the object
print(ResolvedNodeGroup.to_json())

# convert the object into a dict
resolved_node_group_dict = resolved_node_group_instance.to_dict()
# create an instance of ResolvedNodeGroup from a dict
resolved_node_group_from_dict = ResolvedNodeGroup.from_dict(resolved_node_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



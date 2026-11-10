# ControlPlaneNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_group** | [**ControlPlaneNodeGroup**](ControlPlaneNodeGroup.md) |  | 

## Example

```python
from astropulse._generated.models.control_plane_node import ControlPlaneNode

# TODO update the JSON string below
json = "{}"
# create an instance of ControlPlaneNode from a JSON string
control_plane_node_instance = ControlPlaneNode.from_json(json)
# print the JSON string representation of the object
print(ControlPlaneNode.to_json())

# convert the object into a dict
control_plane_node_dict = control_plane_node_instance.to_dict()
# create an instance of ControlPlaneNode from a dict
control_plane_node_from_dict = ControlPlaneNode.from_dict(control_plane_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



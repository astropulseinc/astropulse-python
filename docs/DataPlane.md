# DataPlane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_groups** | [**List[NodeGroup]**](NodeGroup.md) | A slice of NodeGroup configurations for the data plane. It must contain at least one NodeGroup except when the provider owns worker compute — EKS Auto Mode or GKE Autopilot — where it must be omitted because the cloud provider, not AstroPulse, owns worker compute. | [optional] 

## Example

```python
from astropulse._generated.models.data_plane import DataPlane

# TODO update the JSON string below
json = "{}"
# create an instance of DataPlane from a JSON string
data_plane_instance = DataPlane.from_json(json)
# print the JSON string representation of the object
print(DataPlane.to_json())

# convert the object into a dict
data_plane_dict = data_plane_instance.to_dict()
# create an instance of DataPlane from a dict
data_plane_from_dict = DataPlane.from_dict(data_plane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



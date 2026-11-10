# ClusterAcceleratorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAccelerators**](ClusterAccelerators.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_accelerators_response import ClusterAcceleratorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAcceleratorsResponse from a JSON string
cluster_accelerators_response_instance = ClusterAcceleratorsResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterAcceleratorsResponse.to_json())

# convert the object into a dict
cluster_accelerators_response_dict = cluster_accelerators_response_instance.to_dict()
# create an instance of ClusterAcceleratorsResponse from a dict
cluster_accelerators_response_from_dict = ClusterAcceleratorsResponse.from_dict(cluster_accelerators_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



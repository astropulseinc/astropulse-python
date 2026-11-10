# ClusterCreationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterCreation**](ClusterCreation.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_creation_response import ClusterCreationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreationResponse from a JSON string
cluster_creation_response_instance = ClusterCreationResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterCreationResponse.to_json())

# convert the object into a dict
cluster_creation_response_dict = cluster_creation_response_instance.to_dict()
# create an instance of ClusterCreationResponse from a dict
cluster_creation_response_from_dict = ClusterCreationResponse.from_dict(cluster_creation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



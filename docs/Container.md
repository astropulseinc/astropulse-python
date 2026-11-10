# Container


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_size** | **int** | The maximum number of container replicas (required, minimum: 1, must be &gt;&#x3D; MinSize) | 
**min_size** | **int** | The minimum number of container replicas (required, minimum: 1) | 

## Example

```python
from astropulse._generated.models.container import Container

# TODO update the JSON string below
json = "{}"
# create an instance of Container from a JSON string
container_instance = Container.from_json(json)
# print the JSON string representation of the object
print(Container.to_json())

# convert the object into a dict
container_dict = container_instance.to_dict()
# create an instance of Container from a dict
container_from_dict = Container.from_dict(container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



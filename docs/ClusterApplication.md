# ClusterApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_timestamp** | **datetime** | The timestamp when the application was created | [optional] 
**dns_endpoint** | **str** | The DNS endpoint for accessing the application | [optional] 
**last_updated_timestamp** | **datetime** | The timestamp of the last update to the application | [optional] 
**name** | **str** | The name of the application | [optional] 
**namespace** | **str** | The namespace where the application is running in the cluster | [optional] 
**resource_name** | **str** | The resource name within the cluster | [optional] 
**source_type** | [**SourceType**](SourceType.md) | The kind of source the application is deployed from. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_application import ClusterApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterApplication from a JSON string
cluster_application_instance = ClusterApplication.from_json(json)
# print the JSON string representation of the object
print(ClusterApplication.to_json())

# convert the object into a dict
cluster_application_dict = cluster_application_instance.to_dict()
# create an instance of ClusterApplication from a dict
cluster_application_from_dict = ClusterApplication.from_dict(cluster_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ClusterDryRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterDryRun**](ClusterDryRun.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_dry_run_response import ClusterDryRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDryRunResponse from a JSON string
cluster_dry_run_response_instance = ClusterDryRunResponse.from_json(json)
# print the JSON string representation of the object
print(ClusterDryRunResponse.to_json())

# convert the object into a dict
cluster_dry_run_response_dict = cluster_dry_run_response_instance.to_dict()
# create an instance of ClusterDryRunResponse from a dict
cluster_dry_run_response_from_dict = ClusterDryRunResponse.from_dict(cluster_dry_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



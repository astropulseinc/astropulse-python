# ClusterAddonResyncResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonResyncResponse**](ClusterAddonResyncResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_resync_response_envelope import ClusterAddonResyncResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonResyncResponseEnvelope from a JSON string
cluster_addon_resync_response_envelope_instance = ClusterAddonResyncResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonResyncResponseEnvelope.to_json())

# convert the object into a dict
cluster_addon_resync_response_envelope_dict = cluster_addon_resync_response_envelope_instance.to_dict()
# create an instance of ClusterAddonResyncResponseEnvelope from a dict
cluster_addon_resync_response_envelope_from_dict = ClusterAddonResyncResponseEnvelope.from_dict(cluster_addon_resync_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



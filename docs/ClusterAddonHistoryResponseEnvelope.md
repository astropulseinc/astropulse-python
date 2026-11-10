# ClusterAddonHistoryResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClusterAddonHistoryResponse**](ClusterAddonHistoryResponse.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_history_response_envelope import ClusterAddonHistoryResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonHistoryResponseEnvelope from a JSON string
cluster_addon_history_response_envelope_instance = ClusterAddonHistoryResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonHistoryResponseEnvelope.to_json())

# convert the object into a dict
cluster_addon_history_response_envelope_dict = cluster_addon_history_response_envelope_instance.to_dict()
# create an instance of ClusterAddonHistoryResponseEnvelope from a dict
cluster_addon_history_response_envelope_from_dict = ClusterAddonHistoryResponseEnvelope.from_dict(cluster_addon_history_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



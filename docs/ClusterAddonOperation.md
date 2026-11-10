# ClusterAddonOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**ClusterAddonAcceleratorReadiness**](ClusterAddonAcceleratorReadiness.md) | Accompanies an accelerator-metrics apply: what this cluster has for the exporter to measure. See ClusterAddonAcceleratorReadiness. | [optional] 
**message** | **str** | Says what happened, in words to show a person. | [optional] 
**metadata** | [**ClusterAddonOperationMetadata**](ClusterAddonOperationMetadata.md) | Carries anything the operation wants to say beyond its status. | [optional] 
**notices** | [**List[Notice]**](Notice.md) | What an apply, or its dry run, tells you about it, including why it started nothing. | [optional] 
**outcome** | [**Outcome**](Outcome.md) | The decision on the apply: proceed, or blocked when a notice blocks it. | [optional] 
**status** | [**ClusterAddonStatus**](ClusterAddonStatus.md) | Where the operation got to. | [optional] 
**title** | **str** | The result as a headline to show; for a dry run, whether it passed. | [optional] 
**tls** | [**ClusterAddonTLSReadiness**](ClusterAddonTLSReadiness.md) | Accompanies a cert-manager apply: what the applied configuration can mint on this cluster. See ClusterAddonTLSReadiness. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_addon_operation import ClusterAddonOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAddonOperation from a JSON string
cluster_addon_operation_instance = ClusterAddonOperation.from_json(json)
# print the JSON string representation of the object
print(ClusterAddonOperation.to_json())

# convert the object into a dict
cluster_addon_operation_dict = cluster_addon_operation_instance.to_dict()
# create an instance of ClusterAddonOperation from a dict
cluster_addon_operation_from_dict = ClusterAddonOperation.from_dict(cluster_addon_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ClusterAccelerators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[AcceleratorOffer]**](AcceleratorOffer.md) | The GPUs the cluster&#39;s node groups carry and the GPUs its autoscaling pools can launch. | [optional] 
**offers_incomplete** | [**AcceleratorOffersIncompleteReason**](AcceleratorOffersIncompleteReason.md) | Why the autoscaling pools&#39; offers are missing. Empty when offers are complete. | [optional] 
**offers_incomplete_message** | **str** | Says offersIncomplete in a sentence, with what to do next. Empty when offersIncomplete is empty. | [optional] 
**offers_unavailable** | [**AcceleratorOffersUnavailableReason**](AcceleratorOffersUnavailableReason.md) | Why no offers are listed. Empty when there are offers. | [optional] 
**offers_unavailable_message** | **str** | Says offersUnavailable in a sentence, with what a model can still ask for. Empty when offersUnavailable is empty. | [optional] 
**region** | **str** | The region the autoscaling pools&#39; instance types are listed for. | [optional] 

## Example

```python
from astropulse._generated.models.cluster_accelerators import ClusterAccelerators

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAccelerators from a JSON string
cluster_accelerators_instance = ClusterAccelerators.from_json(json)
# print the JSON string representation of the object
print(ClusterAccelerators.to_json())

# convert the object into a dict
cluster_accelerators_dict = cluster_accelerators_instance.to_dict()
# create an instance of ClusterAccelerators from a dict
cluster_accelerators_from_dict = ClusterAccelerators.from_dict(cluster_accelerators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



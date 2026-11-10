# AcceleratorOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**AcceleratorOfferAvailability**](AcceleratorOfferAvailability.md) | Whether a replica asking for this offer can be placed. | [optional] 
**cache_node_group** | **str** | The name to set as source.model.cache.nodeGroup to keep the model&#39;s weights on these nodes. Empty when these nodes hold no weight cache. | [optional] 
**capacity_types** | [**List[InstanceType]**](InstanceType.md) | How the nodes are bought, in order of preference. Empty when AstroPulse does not know how they are bought. | [optional] 
**instance_types** | [**List[AcceleratorOfferInstance]**](AcceleratorOfferInstance.md) | The machine types that provide this GPU, in the order they are chosen, with the GPUs each carries. | [optional] 
**limit** | **int** | The most GPUs the autoscaling pool runs at once, shared by every workload on it. | [optional] 
**max_per_replica** | **int** | The most GPUs of this model one replica can ask for: the largest node within the pool&#39;s GPU limit, lowered when the cloud account&#39;s quota cannot launch a larger node. Zero when availability is Unavailable. | [optional] 
**model** | **str** | The GPU model in lower case, for example l4. Empty when the pool&#39;s GPU models are not known yet; any GPU of the vendor is then accepted. | [optional] 
**node_group** | **str** | The node group in workerNodes, when source is NodeGroup. | [optional] 
**pool** | **str** | The autoscaling node pool&#39;s name, when source is AutoscalingPool. | [optional] 
**quota** | [**AcceleratorOfferQuota**](AcceleratorOfferQuota.md) | The cloud account quota a replica&#39;s node draws on: for an autoscaling pool, the node maxPerReplica needs; for a node group, one more of its nodes. | [optional] 
**reason** | **str** | Says reasonCode in a sentence, with what to change. | [optional] 
**reason_code** | [**AcceleratorOfferReasonCode**](AcceleratorOfferReasonCode.md) | Why availability is not Available, or why maxPerReplica is lower than the largest node allows. | [optional] 
**source** | [**AcceleratorOfferSource**](AcceleratorOfferSource.md) | Where the GPUs come from. | [optional] 
**vendor** | **str** | The GPU maker, for example nvidia. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_offer import AcceleratorOffer

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorOffer from a JSON string
accelerator_offer_instance = AcceleratorOffer.from_json(json)
# print the JSON string representation of the object
print(AcceleratorOffer.to_json())

# convert the object into a dict
accelerator_offer_dict = accelerator_offer_instance.to_dict()
# create an instance of AcceleratorOffer from a dict
accelerator_offer_from_dict = AcceleratorOffer.from_dict(accelerator_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



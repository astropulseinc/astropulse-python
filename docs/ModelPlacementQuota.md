# ModelPlacementQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_capacity_type** | [**List[GPUQuotaHeadroom]**](GPUQuotaHeadroom.md) | Each purchase option&#39;s own quota for the node, in the order the pool prefers them, when it buys more than one. | [optional] 
**code** | **str** | The quota&#39;s code, for example L-DB2E81BA. | [optional] 
**in_use** | **float** | How much of the quota is already in use; absent when unverified. | [optional] 
**limit** | **float** | The quota&#39;s current value; absent when unverified. | [optional] 
**message** | **str** | Says the verdict in a sentence. | [optional] 
**name** | **str** | The quota&#39;s name, for example Running On-Demand G and VT instances. | [optional] 
**required** | **float** | How much of the quota one replica&#39;s node needs; absent when unverified. | [optional] 
**status** | [**GPUQuotaState**](GPUQuotaState.md) | Whether the quota has room for the node; Unverified, when it could not be read, never means zero. | [optional] 
**unit** | **str** | What the quota counts, for example vCPU. | [optional] 
**unverified_reason** | [**GPUQuotaUnverifiedReason**](GPUQuotaUnverifiedReason.md) | Why the quota was not read, when status is Unverified. | [optional] 

## Example

```python
from astropulse._generated.models.model_placement_quota import ModelPlacementQuota

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPlacementQuota from a JSON string
model_placement_quota_instance = ModelPlacementQuota.from_json(json)
# print the JSON string representation of the object
print(ModelPlacementQuota.to_json())

# convert the object into a dict
model_placement_quota_dict = model_placement_quota_instance.to_dict()
# create an instance of ModelPlacementQuota from a dict
model_placement_quota_from_dict = ModelPlacementQuota.from_dict(model_placement_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



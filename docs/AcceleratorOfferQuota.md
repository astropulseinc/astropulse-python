# AcceleratorOfferQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **float** | How much of the quota is free now; absent when unverified. | [optional] 
**by_capacity_type** | [**List[GPUQuotaHeadroom]**](GPUQuotaHeadroom.md) | Each purchase option&#39;s own quota for the node, in the order the pool prefers them, when it buys more than one. | [optional] 
**code** | **str** | The quota&#39;s code, for example L-DB2E81BA. | [optional] 
**name** | **str** | The quota&#39;s name, for example Running On-Demand G and VT instances. | [optional] 
**needed** | **float** | How much of the quota one node needs; absent when unverified. | [optional] 
**reason** | [**Notice**](Notice.md) | Says why the quota is insufficient or unverified, or that a preferred purchase option&#39;s quota is short, and the next step. | [optional] 
**state** | [**GPUQuotaState**](GPUQuotaState.md) | Whether the quota has room for the node; Unverified never means zero. | [optional] 
**unit** | **str** | What the quota counts: vCPU or GPU. | [optional] 
**unverified_reason** | [**GPUQuotaUnverifiedReason**](GPUQuotaUnverifiedReason.md) | Why the quota was not read, when state is Unverified. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_offer_quota import AcceleratorOfferQuota

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorOfferQuota from a JSON string
accelerator_offer_quota_instance = AcceleratorOfferQuota.from_json(json)
# print the JSON string representation of the object
print(AcceleratorOfferQuota.to_json())

# convert the object into a dict
accelerator_offer_quota_dict = accelerator_offer_quota_instance.to_dict()
# create an instance of AcceleratorOfferQuota from a dict
accelerator_offer_quota_from_dict = AcceleratorOfferQuota.from_dict(accelerator_offer_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



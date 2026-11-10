# GPUQuotaHeadroom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **float** | How much of the quota is free now; absent when unverified. | [optional] 
**capacity_type** | [**InstanceType**](InstanceType.md) | The purchase option: OnDemand or Spot. | [optional] 
**code** | **str** | The quota&#39;s code, for example L-3819A6DF. | [optional] 
**in_use** | **float** | How much of the quota is already in use; absent when unverified. | [optional] 
**limit** | **float** | The quota&#39;s current value; absent when unverified. | [optional] 
**name** | **str** | The quota&#39;s name, for example All G and VT Spot Instance Requests. | [optional] 
**needed** | **float** | How much of the quota one node needs; absent when unverified. | [optional] 
**state** | [**GPUQuotaState**](GPUQuotaState.md) | Whether the quota has room for the node. | [optional] 
**unit** | **str** | What the quota counts: vCPU or GPU. | [optional] 
**unverified_reason** | [**GPUQuotaUnverifiedReason**](GPUQuotaUnverifiedReason.md) | Why the quota was not read, when state is Unverified. | [optional] 

## Example

```python
from astropulse._generated.models.gpu_quota_headroom import GPUQuotaHeadroom

# TODO update the JSON string below
json = "{}"
# create an instance of GPUQuotaHeadroom from a JSON string
gpu_quota_headroom_instance = GPUQuotaHeadroom.from_json(json)
# print the JSON string representation of the object
print(GPUQuotaHeadroom.to_json())

# convert the object into a dict
gpu_quota_headroom_dict = gpu_quota_headroom_instance.to_dict()
# create an instance of GPUQuotaHeadroom from a dict
gpu_quota_headroom_from_dict = GPUQuotaHeadroom.from_dict(gpu_quota_headroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



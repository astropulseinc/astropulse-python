# AcceleratorOfferInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpus** | **int** | How many of the offer&#39;s GPUs one node of this type carries. | [optional] 
**name** | **str** | The machine type, for example g6.xlarge. | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_offer_instance import AcceleratorOfferInstance

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorOfferInstance from a JSON string
accelerator_offer_instance_instance = AcceleratorOfferInstance.from_json(json)
# print the JSON string representation of the object
print(AcceleratorOfferInstance.to_json())

# convert the object into a dict
accelerator_offer_instance_dict = accelerator_offer_instance_instance.to_dict()
# create an instance of AcceleratorOfferInstance from a dict
accelerator_offer_instance_from_dict = AcceleratorOfferInstance.from_dict(accelerator_offer_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AMIFamilyOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu** | **bool** | True when the family has an NVIDIA image for GPU node groups at this version. | [optional] 
**name** | [**AMIFamily**](AMIFamily.md) | The AMI family, as amiFamily takes it. | [optional] 

## Example

```python
from astropulse._generated.models.ami_family_offer import AMIFamilyOffer

# TODO update the JSON string below
json = "{}"
# create an instance of AMIFamilyOffer from a JSON string
ami_family_offer_instance = AMIFamilyOffer.from_json(json)
# print the JSON string representation of the object
print(AMIFamilyOffer.to_json())

# convert the object into a dict
ami_family_offer_dict = ami_family_offer_instance.to_dict()
# create an instance of AMIFamilyOffer from a dict
ami_family_offer_from_dict = AMIFamilyOffer.from_dict(ami_family_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



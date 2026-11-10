# AcceleratorOfferingListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AcceleratorOffering]**](AcceleratorOffering.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.accelerator_offering_list_response import AcceleratorOfferingListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcceleratorOfferingListResponse from a JSON string
accelerator_offering_list_response_instance = AcceleratorOfferingListResponse.from_json(json)
# print the JSON string representation of the object
print(AcceleratorOfferingListResponse.to_json())

# convert the object into a dict
accelerator_offering_list_response_dict = accelerator_offering_list_response_instance.to_dict()
# create an instance of AcceleratorOfferingListResponse from a dict
accelerator_offering_list_response_from_dict = AcceleratorOfferingListResponse.from_dict(accelerator_offering_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



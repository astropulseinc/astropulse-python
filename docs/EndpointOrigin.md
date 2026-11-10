# EndpointOrigin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** | The site, such as https://app.example.com. | [optional] 
**source** | [**EndpointOriginSource**](EndpointOriginSource.md) | Why the site may call the endpoint. | [optional] 

## Example

```python
from astropulse._generated.models.endpoint_origin import EndpointOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointOrigin from a JSON string
endpoint_origin_instance = EndpointOrigin.from_json(json)
# print the JSON string representation of the object
print(EndpointOrigin.to_json())

# convert the object into a dict
endpoint_origin_dict = endpoint_origin_instance.to_dict()
# create an instance of EndpointOrigin from a dict
endpoint_origin_from_dict = EndpointOrigin.from_dict(endpoint_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



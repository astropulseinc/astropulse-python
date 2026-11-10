# AWSConnectStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AWSConnectStatus**](AWSConnectStatus.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.aws_connect_status_response import AWSConnectStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSConnectStatusResponse from a JSON string
aws_connect_status_response_instance = AWSConnectStatusResponse.from_json(json)
# print the JSON string representation of the object
print(AWSConnectStatusResponse.to_json())

# convert the object into a dict
aws_connect_status_response_dict = aws_connect_status_response_instance.to_dict()
# create an instance of AWSConnectStatusResponse from a dict
aws_connect_status_response_from_dict = AWSConnectStatusResponse.from_dict(aws_connect_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



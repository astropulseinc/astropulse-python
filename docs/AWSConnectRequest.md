# AWSConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster name (required, 1-50 characters, valid DNS name) | 
**destination_account_id** | **str** | The target AWS account ID (optional, 12-digit numeric string). Auto-detected from cluster metadata if not provided. | [optional] 
**duration** | **str** | The validity period for credentials (optional, Go duration format e.g. \&quot;1h\&quot;, \&quot;30m\&quot;) | [optional] 
**force_update** | **bool** | Bypasses cluster existence checks and forces resource updates (optional, default: false) | [optional] 
**target_region** | **str** | The AWS region for resource creation (optional, e.g. \&quot;us-west-2\&quot;). Auto-detected from cluster metadata if not provided. | [optional] 

## Example

```python
from astropulse._generated.models.aws_connect_request import AWSConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AWSConnectRequest from a JSON string
aws_connect_request_instance = AWSConnectRequest.from_json(json)
# print the JSON string representation of the object
print(AWSConnectRequest.to_json())

# convert the object into a dict
aws_connect_request_dict = aws_connect_request_instance.to_dict()
# create an instance of AWSConnectRequest from a dict
aws_connect_request_from_dict = AWSConnectRequest.from_dict(aws_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



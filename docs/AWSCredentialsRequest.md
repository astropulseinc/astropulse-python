# AWSCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | The cluster name (required, 1-50 characters, valid DNS name) | 
**destination_account_id** | **str** | The target AWS account ID (optional, 12-digit numeric string). Auto-detected from cluster metadata if not provided. | [optional] 
**duration** | **str** | The validity period for credentials (optional, Go duration format e.g. \&quot;1h\&quot;, \&quot;30m\&quot;) | [optional] 
**target_region** | **str** | The AWS region (optional). Auto-detected from cluster metadata if not provided. | [optional] 

## Example

```python
from astropulse._generated.models.aws_credentials_request import AWSCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AWSCredentialsRequest from a JSON string
aws_credentials_request_instance = AWSCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(AWSCredentialsRequest.to_json())

# convert the object into a dict
aws_credentials_request_dict = aws_credentials_request_instance.to_dict()
# create an instance of AWSCredentialsRequest from a dict
aws_credentials_request_from_dict = AWSCredentialsRequest.from_dict(aws_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



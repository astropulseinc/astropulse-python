# AWSTemporaryCredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AWSTemporaryCredential**](AWSTemporaryCredential.md) |  | [optional] 
**id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from astropulse._generated.models.aws_temporary_credential_response import AWSTemporaryCredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AWSTemporaryCredentialResponse from a JSON string
aws_temporary_credential_response_instance = AWSTemporaryCredentialResponse.from_json(json)
# print the JSON string representation of the object
print(AWSTemporaryCredentialResponse.to_json())

# convert the object into a dict
aws_temporary_credential_response_dict = aws_temporary_credential_response_instance.to_dict()
# create an instance of AWSTemporaryCredentialResponse from a dict
aws_temporary_credential_response_from_dict = AWSTemporaryCredentialResponse.from_dict(aws_temporary_credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



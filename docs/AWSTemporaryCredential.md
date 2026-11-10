# AWSTemporaryCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The access key ID for the AWS credentials | [optional] 
**expiration** | **str** | The expiration time for the AWS credentials | [optional] 
**secret_access_key** | **str** | The secret access key for the AWS credentials | [optional] 
**session_token** | **str** | The session token for the AWS credentials | [optional] 

## Example

```python
from astropulse._generated.models.aws_temporary_credential import AWSTemporaryCredential

# TODO update the JSON string below
json = "{}"
# create an instance of AWSTemporaryCredential from a JSON string
aws_temporary_credential_instance = AWSTemporaryCredential.from_json(json)
# print the JSON string representation of the object
print(AWSTemporaryCredential.to_json())

# convert the object into a dict
aws_temporary_credential_dict = aws_temporary_credential_instance.to_dict()
# create an instance of AWSTemporaryCredential from a dict
aws_temporary_credential_from_dict = AWSTemporaryCredential.from_dict(aws_temporary_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



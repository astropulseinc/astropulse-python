# ErrorResponse

Standard error response format for API errors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**ErrorCode**](ErrorCode.md) | The kind of failure, one of a few values shared by every route. Match on it. | [optional] 
**details** | **object** | Carries structured context for the code. For an Invalid request, details.fields lists every refused field as {field, rule, reason}: its path in the request body (such as dataPlane.nodeGroups[0].labels[\&quot;team.example.com/owner\&quot;], empty for the body as a whole), the rule it broke and what that rule requires. | [optional] 
**message** | **str** | What went wrong, in human-readable form. Do not match on it; match on code. | [optional] 
**next_step** | [**NextStep**](NextStep.md) | The one thing to do about the error, when there is one. | [optional] 
**reason** | **str** | Which failure it was, such as ClusterNotFound: an error reason, or on an error that says what to do next, its notice code. | [optional] 
**severity** | [**NoticeSeverity**](NoticeSeverity.md) | How much the error matters: the severity of the notice it carries; Blocking for an error that names a next step without a notice, and absent for one with neither. | [optional] 
**status** | **int** | The HTTP status code, repeated here for clients that keep only the body. | [optional] 
**title** | **str** | A short headline for the error, when it says what to do next. | [optional] 
**trace_id** | **str** | Identifies this request and is also returned in the X-Trace-ID header. Quote it in a bug report. | [optional] 

## Example

```python
from astropulse._generated.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



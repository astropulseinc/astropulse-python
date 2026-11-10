# NextStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Says the step in a few words, at most 40 characters. | [optional] 
**operation** | [**NoticeOperation**](NoticeOperation.md) | The operationId of the API operation that takes the step; absent when the step is not an API call. | [optional] 
**params** | **Dict[str, str]** | The operation&#39;s path and query parameters, by name. | [optional] 
**request** | **object** | The operation&#39;s request body, or the part of it already known. | [optional] 
**shell** | [**ShellCommand**](ShellCommand.md) | The command to run in a cloud shell or terminal, when the step needs one. | [optional] 
**url** | **str** | The page to open for a step taken outside AstroPulse, such as a cloud console page. | [optional] 

## Example

```python
from astropulse._generated.models.next_step import NextStep

# TODO update the JSON string below
json = "{}"
# create an instance of NextStep from a JSON string
next_step_instance = NextStep.from_json(json)
# print the JSON string representation of the object
print(NextStep.to_json())

# convert the object into a dict
next_step_dict = next_step_instance.to_dict()
# create an instance of NextStep from a dict
next_step_from_dict = NextStep.from_dict(next_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



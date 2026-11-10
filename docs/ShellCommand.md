# ShellCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | The one line to paste and run. | [optional] 
**script** | **str** | The setup script the command runs, to read before running it. | [optional] 
**script_name** | **str** | The file name the command saves the setup script under. | [optional] 
**script_summary** | **str** | Says in one sentence what the setup script creates in your account. | [optional] 
**shell** | **str** | Where to run the command, such as Cloud Shell. | [optional] 
**sign_in** | **str** | Says which account the shell must be signed in to. | [optional] 

## Example

```python
from astropulse._generated.models.shell_command import ShellCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ShellCommand from a JSON string
shell_command_instance = ShellCommand.from_json(json)
# print the JSON string representation of the object
print(ShellCommand.to_json())

# convert the object into a dict
shell_command_dict = shell_command_instance.to_dict()
# create an instance of ShellCommand from a dict
shell_command_from_dict = ShellCommand.from_dict(shell_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



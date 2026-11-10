# RegistrationInstructions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A human-readable instruction for the user. | [optional] 
**script_content** | **str** | The setup script content. | [optional] 
**url** | **str** | The setup URL for completing registration. | [optional] 

## Example

```python
from astropulse._generated.models.registration_instructions import RegistrationInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationInstructions from a JSON string
registration_instructions_instance = RegistrationInstructions.from_json(json)
# print the JSON string representation of the object
print(RegistrationInstructions.to_json())

# convert the object into a dict
registration_instructions_dict = registration_instructions_instance.to_dict()
# create an instance of RegistrationInstructions from a dict
registration_instructions_from_dict = RegistrationInstructions.from_dict(registration_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



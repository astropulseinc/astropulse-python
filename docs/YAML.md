# YAML


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **str** | Specifies the files to exclude | [optional] 
**include** | **str** | Specifies the files to include | [optional] 
**recursive** | **bool** | Specifies whether to search directories recursively If not specified, the default value is true | [optional] [default to True]
**repo** | [**Repo**](Repo.md) | Contains repository details for the YAML files | [optional] 

## Example

```python
from astropulse._generated.models.yaml import YAML

# TODO update the JSON string below
json = "{}"
# create an instance of YAML from a JSON string
yaml_instance = YAML.from_json(json)
# print the JSON string representation of the object
print(YAML.to_json())

# convert the object into a dict
yaml_dict = yaml_instance.to_dict()
# create an instance of YAML from a dict
yaml_from_dict = YAML.from_dict(yaml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApplicationSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helm** | [**Helm**](Helm.md) | Configuration, used when type is Helm | [optional] 
**image** | [**Image**](Image.md) | Configuration, used when type is Image | [optional] 
**model** | [**Model**](Model.md) | Configuration, used when type is Model | [optional] 
**repository** | [**Repository**](Repository.md) | Configuration, used when type is Repository | [optional] 
**type** | [**SourceType**](SourceType.md) | Specifies the type of source (Image, Helm, YAML, Repository, Model) | [optional] 
**yaml** | [**YAML**](YAML.md) | Configuration, used when type is YAML | [optional] 

## Example

```python
from astropulse._generated.models.application_source import ApplicationSource

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSource from a JSON string
application_source_instance = ApplicationSource.from_json(json)
# print the JSON string representation of the object
print(ApplicationSource.to_json())

# convert the object into a dict
application_source_dict = application_source_instance.to_dict()
# create an instance of ApplicationSource from a dict
application_source_from_dict = ApplicationSource.from_dict(application_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



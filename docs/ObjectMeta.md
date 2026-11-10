# ObjectMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | An optional set of key/value annotations. On an Application, org.opencontainers.image.revision (a commit SHA) and org.opencontainers.image.source (a repository URL) record where the version was built from, and are shown in its history. | [optional] 
**name** | **str** | The resource name. Optional. When set and the spec does not set a name, this value is used (manifest semantics: metadata.name is the name). | [optional] 

## Example

```python
from astropulse._generated.models.object_meta import ObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMeta from a JSON string
object_meta_instance = ObjectMeta.from_json(json)
# print the JSON string representation of the object
print(ObjectMeta.to_json())

# convert the object into a dict
object_meta_dict = object_meta_instance.to_dict()
# create an instance of ObjectMeta from a dict
object_meta_from_dict = ObjectMeta.from_dict(object_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



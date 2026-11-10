# ApplicationVersionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | The RFC3339 creation timestamp of the version. | [optional] 
**created_by** | **str** | The actor (user id) who created the version. | [optional] 
**created_by_display** | **str** | The human-readable actor (name, falling back to email) resolved from CreatedBy, so the whole team can see WHO deployed/rolled back rather than a raw id. Best-effort: empty when the actor cannot be resolved. Org-scoped (the actor is an org member), so this does not leak identities across organizations. | [optional] 
**current** | **bool** | Indicates this version is the currently deployed desired state. | [optional] 
**rollback_eligible** | **bool** | Indicates whether this version can be rolled back to today. | [optional] 
**rollback_pinned** | **bool** | Indicates the current version is held by a rollback pin (git moving-ref case). | [optional] 
**source_identity** | [**SourceIdentity**](SourceIdentity.md) | The immutable artifact identity for this version. | [optional] 
**source_summary** | **str** | A short human-readable summary of the source. | [optional] 
**source_type** | [**SourceType**](SourceType.md) | The source type for this version. | [optional] 
**state** | [**ApplicationVersionState**](ApplicationVersionState.md) | The version lifecycle state. | [optional] 
**unavailable_reason** | **str** | Explains why a non-eligible version cannot be rolled back to; set whenever rollbackEligible is false. | [optional] 
**version** | **str** | The Astro version label, e.g. \&quot;v7\&quot;. | [optional] 

## Example

```python
from astropulse._generated.models.application_version_entry import ApplicationVersionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVersionEntry from a JSON string
application_version_entry_instance = ApplicationVersionEntry.from_json(json)
# print the JSON string representation of the object
print(ApplicationVersionEntry.to_json())

# convert the object into a dict
application_version_entry_dict = application_version_entry_instance.to_dict()
# create an instance of ApplicationVersionEntry from a dict
application_version_entry_from_dict = ApplicationVersionEntry.from_dict(application_version_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



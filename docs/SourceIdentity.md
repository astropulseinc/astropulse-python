# SourceIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_digest** | **str** | The resolved Helm chart digest for helm sources, when available. | [optional] 
**chart_provenance** | **str** | The Helm chart provenance reference for helm sources, when available. | [optional] 
**configured_ref** | **str** | The user-configured branch/tag for git sources (e.g. \&quot;main\&quot;), or the artifact URI for model sources. | [optional] 
**display** | **str** | The one user-facing identity string: an image reference, a chart&#39;s name@version, or a repository source&#39;s repository//path@revision. | [optional] 
**effective_revision** | **str** | The immutable revision actually deployed (the pinned SHA after rollback). | [optional] 
**git_commit_sha** | **str** | The source commit this version came from. | [optional] 
**image_digest** | **str** | The resolved image digest (repository@sha256:...) for image sources. | [optional] 
**path** | **str** | The directory within the repository the application is deployed from, for repository and yaml sources. | [optional] 
**source_repository** | **str** | The URL of the repository that commit belongs to. | [optional] 
**type** | [**SourceType**](SourceType.md) | The kind of source. | [optional] 

## Example

```python
from astropulse._generated.models.source_identity import SourceIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of SourceIdentity from a JSON string
source_identity_instance = SourceIdentity.from_json(json)
# print the JSON string representation of the object
print(SourceIdentity.to_json())

# convert the object into a dict
source_identity_dict = source_identity_instance.to_dict()
# create an instance of SourceIdentity from a dict
source_identity_from_dict = SourceIdentity.from_dict(source_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



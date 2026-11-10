# ApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_access** | [**ExternalAccess**](ExternalAccess.md) | How the application is reached from outside the cluster (optional). For image and model applications, omit it for an internal-only app, or set domain to a verified domain (served at &lt;app&gt;.&lt;domain&gt;) or hostname to an exact hostname under one. | [optional] 
**name** | **str** | The application name (required, 1-50 characters, valid DNS name). Must be unique within the organization. Format: lowercase alphanumeric and hyphens. | 
**namespace** | **str** | The Kubernetes namespace for deployment (optional, max 63 characters). Must be a valid Kubernetes namespace name. If omitted, a namespace named after the application instance is generated and belongs to that one application. A namespace you name here is yours: AstroPulse creates it if it does not exist, deploys into it beside whatever else lives there, and never deletes it or labels it with one application&#39;s identity -- several applications may share it. Immutable once set. | [optional] 
**profile_name** | **str** | The application profile name (required, 1-50 characters, valid DNS name). Immutable once set — cannot be changed after application creation. | 
**source** | [**ApplicationSource**](ApplicationSource.md) | Defines where the application artifact is fetched from (required, immutable once set). Must include a valid source type (Image, Helm, Repository, YAML or Model). The source.type presence invariant is enforced by the struct-level validateApplicationRequest in pkg/validator. | 
**sync_type** | [**SyncType**](SyncType.md) | How the application is kept in sync with its spec. Use Manual only for testing on a live cluster. | [optional] 

## Example

```python
from astropulse._generated.models.application_request import ApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRequest from a JSON string
application_request_instance = ApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRequest.to_json())

# convert the object into a dict
application_request_dict = application_request_instance.to_dict()
# create an instance of ApplicationRequest from a dict
application_request_from_dict = ApplicationRequest.from_dict(application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



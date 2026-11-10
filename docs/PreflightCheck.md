# PreflightCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**PreflightCategory**](PreflightCategory.md) | Classifies the check type | [optional] 
**description** | **str** | Explains what was checked and the result | [optional] 
**development_credentials** | **bool** | True on the Account Connection check when a local development platform creates the cluster with its own credentials instead of a connection. | [optional] 
**name** | **str** | The check name (e.g. \&quot;Version Compatibility\&quot;, \&quot;Cloud Provider Capacity\&quot;) | [optional] 
**reason_code** | [**PreflightReasonCode**](PreflightReasonCode.md) | Why the check did not pass. Empty when the check has none. | [optional] 
**remediation** | **str** | Provides actionable steps when status is &#x60;Fail&#x60; | [optional] 
**requires_connection** | **bool** | True when the check is answered by reaching the cluster&#39;s connected cloud account, so it cannot pass until a real account is connected. | [optional] 
**status** | [**PreflightStatus**](PreflightStatus.md) | The check result | [optional] 

## Example

```python
from astropulse._generated.models.preflight_check import PreflightCheck

# TODO update the JSON string below
json = "{}"
# create an instance of PreflightCheck from a JSON string
preflight_check_instance = PreflightCheck.from_json(json)
# print the JSON string representation of the object
print(PreflightCheck.to_json())

# convert the object into a dict
preflight_check_dict = preflight_check_instance.to_dict()
# create an instance of PreflightCheck from a dict
preflight_check_from_dict = PreflightCheck.from_dict(preflight_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



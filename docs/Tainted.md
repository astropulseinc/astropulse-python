# Tainted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | [**TaintEffect**](TaintEffect.md) | The taint effect (optional). One of: NoSchedule, PreferNoSchedule, NoExecute. NoSchedule: pods won&#39;t be scheduled. PreferNoSchedule: best-effort avoidance. NoExecute: evicts existing pods. | [optional] 
**key** | **str** | The taint key that the toleration applies to (required, minimum 1 character) | 
**operator** | [**Operator**](Operator.md) | The key&#39;s relationship to the value (optional, default Equal). One of: Equal, Exists, NotExist, NotEqual. | [optional] 
**value** | **str** | The taint value: required when Operator is Equal, NotEqual or omitted, and empty when it is Exists or NotExist. | [optional] 

## Example

```python
from astropulse._generated.models.tainted import Tainted

# TODO update the JSON string below
json = "{}"
# create an instance of Tainted from a JSON string
tainted_instance = Tainted.from_json(json)
# print the JSON string representation of the object
print(Tainted.to_json())

# convert the object into a dict
tainted_dict = tainted_instance.to_dict()
# create an instance of Tainted from a dict
tainted_from_dict = Tainted.from_dict(tainted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



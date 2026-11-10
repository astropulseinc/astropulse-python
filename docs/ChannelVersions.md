# ChannelVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_version** | **str** | The default version for this channel | [optional] 
**valid_versions** | **List[str]** | The list of all valid versions in this channel | [optional] 

## Example

```python
from astropulse._generated.models.channel_versions import ChannelVersions

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelVersions from a JSON string
channel_versions_instance = ChannelVersions.from_json(json)
# print the JSON string representation of the object
print(ChannelVersions.to_json())

# convert the object into a dict
channel_versions_dict = channel_versions_instance.to_dict()
# create an instance of ChannelVersions from a dict
channel_versions_from_dict = ChannelVersions.from_dict(channel_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



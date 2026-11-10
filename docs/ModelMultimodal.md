# ModelMultimodal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_audio_clips_per_prompt** | **int** | How many audio clips one request may carry. Named for clips rather than for audio because that is what the runtime counts: one item is one attached clip, whatever its length. | [optional] 
**max_images_per_prompt** | **int** | How many images one request may carry. The field most vision models need: document and chart understanding routinely sends several pages in one message, and one image is a common runtime default. | [optional] 
**max_videos_per_prompt** | **int** | How many video clips one request may carry. A clip costs far more than an image -- the runtime samples frames from it and each frame is an image -- so this is the limit to keep small. | [optional] 

## Example

```python
from astropulse._generated.models.model_multimodal import ModelMultimodal

# TODO update the JSON string below
json = "{}"
# create an instance of ModelMultimodal from a JSON string
model_multimodal_instance = ModelMultimodal.from_json(json)
# print the JSON string representation of the object
print(ModelMultimodal.to_json())

# convert the object into a dict
model_multimodal_dict = model_multimodal_instance.to_dict()
# create an instance of ModelMultimodal from a dict
model_multimodal_from_dict = ModelMultimodal.from_dict(model_multimodal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



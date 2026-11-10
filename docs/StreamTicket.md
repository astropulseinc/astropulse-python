# StreamTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | When an unused ticket stops working, at most 30 seconds after it was issued. | [optional] 
**ticket** | **str** | The value to send as the stream URL&#39;s ticket query parameter. It opens only the stream it was issued for. | [optional] 

## Example

```python
from astropulse._generated.models.stream_ticket import StreamTicket

# TODO update the JSON string below
json = "{}"
# create an instance of StreamTicket from a JSON string
stream_ticket_instance = StreamTicket.from_json(json)
# print the JSON string representation of the object
print(StreamTicket.to_json())

# convert the object into a dict
stream_ticket_dict = stream_ticket_instance.to_dict()
# create an instance of StreamTicket from a dict
stream_ticket_from_dict = StreamTicket.from_dict(stream_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



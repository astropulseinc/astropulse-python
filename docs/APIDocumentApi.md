# astropulse._generated.APIDocumentApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api_document**](APIDocumentApi.md#get_open_api_document) | **GET** /api/v1/openapi | Get the API document


# **get_open_api_document**
> Dict[str, object] get_open_api_document()

Get the API document

Returns this API's OpenAPI 3 document: every operation, type and enum value, with each value's display name and meaning. It needs no credentials.

### Example


```python
import astropulse._generated
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)


# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIDocumentApi(api_client)

    try:
        # Get the API document
        api_response = api_instance.get_open_api_document()
        print("The response of APIDocumentApi->get_open_api_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentApi->get_open_api_document: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OpenAPI 3 document |  -  |
**304** | The document is unchanged since the ETag sent in If-None-Match |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


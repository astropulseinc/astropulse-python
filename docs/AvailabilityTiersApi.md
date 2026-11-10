# astropulse._generated.AvailabilityTiersApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_availability_tier**](AvailabilityTiersApi.md#get_availability_tier) | **GET** /api/v1/availability/tiers/{tierId} | Get availability tier information
[**list_availability_tiers**](AvailabilityTiersApi.md#list_availability_tiers) | **GET** /api/v1/availability/tiers | List supported availability tiers


# **get_availability_tier**
> TierConfigResponse get_availability_tier(tier_id)

Get availability tier information

Get detailed information about a specific availability tier

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.tier_config_response import TierConfigResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.AvailabilityTiersApi(api_client)
    tier_id = 'tier_id_example' # str | Availability tier ID

    try:
        # Get availability tier information
        api_response = api_instance.get_availability_tier(tier_id)
        print("The response of AvailabilityTiersApi->get_availability_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityTiersApi->get_availability_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_id** | **str**| Availability tier ID | 

### Return type

[**TierConfigResponse**](TierConfigResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Availability tier information retrieved successfully |  -  |
**400** | Invalid tier ID provided |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view tier information |  -  |
**404** | Tier not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_availability_tiers**
> StringListResponse list_availability_tiers()

List supported availability tiers

Lists all supported availability tiers for the organization

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.string_list_response import StringListResponse
from astropulse._generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.astropulse.io
# See configuration.py for a list of all supported configuration parameters.
configuration = astropulse._generated.Configuration(
    host = "https://api.astropulse.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.AvailabilityTiersApi(api_client)

    try:
        # List supported availability tiers
        api_response = api_instance.list_availability_tiers()
        print("The response of AvailabilityTiersApi->list_availability_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvailabilityTiersApi->list_availability_tiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StringListResponse**](StringListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported availability tiers |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view availability tiers |  -  |
**404** | No supported tiers found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


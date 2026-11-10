# astropulse._generated.APIKeysApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](APIKeysApi.md#create_api_key) | **POST** /api/v1/apikeys | Create API key for an organization
[**delete_api_key**](APIKeysApi.md#delete_api_key) | **POST** /api/v1/apikeys/{orgId}/delete | Delete API key for an organization
[**get_api_key**](APIKeysApi.md#get_api_key) | **GET** /api/v1/apikeys/{orgId}/key/{keyId} | Get API key by ID
[**get_api_key_summary**](APIKeysApi.md#get_api_key_summary) | **GET** /api/v1/apikeys/{orgId}/summary | Get API key summary
[**list_api_keys**](APIKeysApi.md#list_api_keys) | **GET** /api/v1/apikeys | List API keys for a user
[**revoke_api_key**](APIKeysApi.md#revoke_api_key) | **POST** /api/v1/apikeys/{orgId}/revoke | Revoke API key
[**validate_api_key**](APIKeysApi.md#validate_api_key) | **GET** /api/v1/apikeys/validate | Validate API key


# **create_api_key**
> APIKeyCreatedResponse create_api_key(api_key_request)

Create API key for an organization

Create an API key for an organization. The API key will be used to authenticate the requests to the AstroPulse API. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.api_key_created_response import APIKeyCreatedResponse
from astropulse._generated.models.api_key_request import APIKeyRequest
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)
    api_key_request = astropulse._generated.APIKeyRequest() # APIKeyRequest | API Key creation request

    try:
        # Create API key for an organization
        api_response = api_instance.create_api_key(api_key_request)
        print("The response of APIKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_request** | [**APIKeyRequest**](APIKeyRequest.md)| API Key creation request | 

### Return type

[**APIKeyCreatedResponse**](APIKeyCreatedResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created API key |  -  |
**400** | Validation error in request parameters |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | User does not have permission to access this resource |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> DeleteAPIKeyResponseEnvelope delete_api_key(org_id, delete_api_key_request)

Delete API key for an organization

Delete an API key for an organization by its ID. The API key will no longer be valid for authentication. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.delete_api_key_request import DeleteAPIKeyRequest
from astropulse._generated.models.delete_api_key_response_envelope import DeleteAPIKeyResponseEnvelope
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization Id
    delete_api_key_request = astropulse._generated.DeleteAPIKeyRequest() # DeleteAPIKeyRequest | API Key deletion request

    try:
        # Delete API key for an organization
        api_response = api_instance.delete_api_key(org_id, delete_api_key_request)
        print("The response of APIKeysApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization Id | 
 **delete_api_key_request** | [**DeleteAPIKeyRequest**](DeleteAPIKeyRequest.md)| API Key deletion request | 

### Return type

[**DeleteAPIKeyResponseEnvelope**](DeleteAPIKeyResponseEnvelope.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key deleted |  -  |
**400** | Validation error in request parameters |  -  |
**401** | Missing or invalid bearer token. |  -  |
**403** | User does not have permission to access this resource |  -  |
**404** | API key not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> APIKeyResponse get_api_key(org_id, key_id)

Get API key by ID

Returns the name, status, expiry, and organization association for a specific API key. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.api_key_response import APIKeyResponse
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization Id
    key_id = 'key_id_example' # str | Key ID

    try:
        # Get API key by ID
        api_response = api_instance.get_api_key(org_id, key_id)
        print("The response of APIKeysApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization Id | 
 **key_id** | **str**| Key ID | 

### Return type

[**APIKeyResponse**](APIKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad request |  -  |
**403** | forbidden, you are not allowed to view this API key |  -  |
**404** | API key not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_summary**
> APIKeySummaryResponse get_api_key_summary(org_id)

Get API key summary

Returns how many of the caller's keys in the organization are active, expired and revoked, and the active key that expires first within 7 days. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.api_key_summary_response import APIKeySummaryResponse
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization the keys belong to

    try:
        # Get API key summary
        api_response = api_instance.get_api_key_summary(org_id)
        print("The response of APIKeysApi->get_api_key_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_api_key_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization the keys belong to | 

### Return type

[**APIKeySummaryResponse**](APIKeySummaryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_keys**
> APIKeyListResponse list_api_keys()

List API keys for a user

Returns all active, expired, and revoked API keys owned by the authenticated user across all organizations. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.api_key_list_response import APIKeyListResponse
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)

    try:
        # List API keys for a user
        api_response = api_instance.list_api_keys()
        print("The response of APIKeysApi->list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->list_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIKeyListResponse**](APIKeyListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of API keys |  -  |
**404** | no API keys found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_key**
> BooleanResponse revoke_api_key(org_id, revoke_api_key_request=revoke_api_key_request)

Revoke API key

Marks the API key as revoked so it can no longer authenticate requests. The key record is retained for audit purposes. Requires a signed-in user session.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
from astropulse._generated.models.revoke_api_key_request import RevokeAPIKeyRequest
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

# Configure Bearer authorization (JWT): BearerAuth
configuration = astropulse._generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with astropulse._generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = astropulse._generated.APIKeysApi(api_client)
    org_id = 'org_id_example' # str | Organization Id
    revoke_api_key_request = astropulse._generated.RevokeAPIKeyRequest() # RevokeAPIKeyRequest | Reason for revocation (optional)

    try:
        # Revoke API key
        api_response = api_instance.revoke_api_key(org_id, revoke_api_key_request=revoke_api_key_request)
        print("The response of APIKeysApi->revoke_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->revoke_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization Id | 
 **revoke_api_key_request** | [**RevokeAPIKeyRequest**](RevokeAPIKeyRequest.md)| Reason for revocation | [optional] 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad request |  -  |
**403** | forbidden, you are not allowed to revoke this API key |  -  |
**404** | API key not found |  -  |
**500** | internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_api_key**
> APIKeyValidationResponse validate_api_key(x_astro_validate_api_key)

Validate API key

Returns the current status of the API key (active, expired, or revoked) along with its expiry timestamp and associated organization. For a service account key it also returns the account's id, name and role.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.api_key_validation_response import APIKeyValidationResponse
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
    api_instance = astropulse._generated.APIKeysApi(api_client)
    x_astro_validate_api_key = 'x_astro_validate_api_key_example' # str | API Key to validate

    try:
        # Validate API key
        api_response = api_instance.validate_api_key(x_astro_validate_api_key)
        print("The response of APIKeysApi->validate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->validate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_astro_validate_api_key** | **str**| API Key to validate | 

### Return type

[**APIKeyValidationResponse**](APIKeyValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | bad request |  -  |
**401** | Missing or invalid credentials, or the API key to validate is not valid, expired or revoked |  -  |
**500** | internal server error |  -  |
**503** | The API key could not be checked right now; retry after the Retry-After header |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


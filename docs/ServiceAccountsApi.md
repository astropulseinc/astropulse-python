# astropulse._generated.ServiceAccountsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_service_account**](ServiceAccountsApi.md#archive_service_account) | **DELETE** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId} | Archive service account
[**create_service_account**](ServiceAccountsApi.md#create_service_account) | **POST** /api/v1/organizations/{orgId}/service-accounts | Create service account
[**create_service_account_key**](ServiceAccountsApi.md#create_service_account_key) | **POST** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId}/keys | Create service account key
[**get_service_account**](ServiceAccountsApi.md#get_service_account) | **GET** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId} | Get service account
[**list_service_account_keys**](ServiceAccountsApi.md#list_service_account_keys) | **GET** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId}/keys | List service account keys
[**list_service_accounts**](ServiceAccountsApi.md#list_service_accounts) | **GET** /api/v1/organizations/{orgId}/service-accounts | List service accounts
[**revoke_service_account_key**](ServiceAccountsApi.md#revoke_service_account_key) | **DELETE** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId}/keys/{keyId} | Revoke service account key
[**update_service_account**](ServiceAccountsApi.md#update_service_account) | **PUT** /api/v1/organizations/{orgId}/service-accounts/{serviceAccountId} | Update service account


# **archive_service_account**
> OrgServiceAccountResponse archive_service_account(org_id, service_account_id)

Archive service account

Archives the service account and disables all its keys. Archiving cannot be undone. Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID

    try:
        # Archive service account
        api_response = api_instance.archive_service_account(org_id, service_account_id)
        print("The response of ServiceAccountsApi->archive_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->archive_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 

### Return type

[**OrgServiceAccountResponse**](OrgServiceAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account**
> OrgServiceAccountResponse create_service_account(org_id, service_account_request)

Create service account

Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse
from astropulse._generated.models.service_account_request import ServiceAccountRequest
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_request = astropulse._generated.ServiceAccountRequest() # ServiceAccountRequest | Service account details

    try:
        # Create service account
        api_response = api_instance.create_service_account(org_id, service_account_request)
        print("The response of ServiceAccountsApi->create_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_request** | [**ServiceAccountRequest**](ServiceAccountRequest.md)| Service account details | 

### Return type

[**OrgServiceAccountResponse**](OrgServiceAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_account_key**
> ServiceAccountKeyCreatedResponse create_service_account_key(org_id, service_account_id, service_account_key_request)

Create service account key

Issues a new key for the service account. The secret is returned only in this response. Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.service_account_key_created_response import ServiceAccountKeyCreatedResponse
from astropulse._generated.models.service_account_key_request import ServiceAccountKeyRequest
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID
    service_account_key_request = astropulse._generated.ServiceAccountKeyRequest() # ServiceAccountKeyRequest | Credential lifetime

    try:
        # Create service account key
        api_response = api_instance.create_service_account_key(org_id, service_account_id, service_account_key_request)
        print("The response of ServiceAccountsApi->create_service_account_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->create_service_account_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 
 **service_account_key_request** | [**ServiceAccountKeyRequest**](ServiceAccountKeyRequest.md)| Credential lifetime | 

### Return type

[**ServiceAccountKeyCreatedResponse**](ServiceAccountKeyCreatedResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_account**
> OrgServiceAccountResponse get_service_account(org_id, service_account_id)

Get service account

Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID

    try:
        # Get service account
        api_response = api_instance.get_service_account(org_id, service_account_id)
        print("The response of ServiceAccountsApi->get_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->get_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 

### Return type

[**OrgServiceAccountResponse**](OrgServiceAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_account_keys**
> APIKeyListResponse list_service_account_keys(org_id, service_account_id)

List service account keys

Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID

    try:
        # List service account keys
        api_response = api_instance.list_service_account_keys(org_id, service_account_id)
        print("The response of ServiceAccountsApi->list_service_account_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->list_service_account_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 

### Return type

[**APIKeyListResponse**](APIKeyListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_accounts**
> OrgServiceAccountListResponse list_service_accounts(org_id)

List service accounts

Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.org_service_account_list_response import OrgServiceAccountListResponse
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID

    try:
        # List service accounts
        api_response = api_instance.list_service_accounts(org_id)
        print("The response of ServiceAccountsApi->list_service_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->list_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 

### Return type

[**OrgServiceAccountListResponse**](OrgServiceAccountListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_service_account_key**
> BooleanResponse revoke_service_account_key(org_id, service_account_id, key_id)

Revoke service account key

Revokes the key immediately. Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.boolean_response import BooleanResponse
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID
    key_id = 'key_id_example' # str | API key ID

    try:
        # Revoke service account key
        api_response = api_instance.revoke_service_account_key(org_id, service_account_id, key_id)
        print("The response of ServiceAccountsApi->revoke_service_account_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->revoke_service_account_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 
 **key_id** | **str**| API key ID | 

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_account**
> OrgServiceAccountResponse update_service_account(org_id, service_account_id, service_account_request)

Update service account

Requires a user with admin or owner permissions in the organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.org_service_account_response import OrgServiceAccountResponse
from astropulse._generated.models.service_account_request import ServiceAccountRequest
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
    api_instance = astropulse._generated.ServiceAccountsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    service_account_id = 'service_account_id_example' # str | Service account ID
    service_account_request = astropulse._generated.ServiceAccountRequest() # ServiceAccountRequest | Service account details

    try:
        # Update service account
        api_response = api_instance.update_service_account(org_id, service_account_id, service_account_request)
        print("The response of ServiceAccountsApi->update_service_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceAccountsApi->update_service_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **service_account_id** | **str**| Service account ID | 
 **service_account_request** | [**ServiceAccountRequest**](ServiceAccountRequest.md)| Service account details | 

### Return type

[**OrgServiceAccountResponse**](OrgServiceAccountResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


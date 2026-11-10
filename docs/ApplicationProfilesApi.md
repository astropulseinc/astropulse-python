# astropulse._generated.ApplicationProfilesApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_application_profiles**](ApplicationProfilesApi.md#bulk_delete_application_profiles) | **POST** /api/v1/applications/profiles/bulk-delete | Bulk delete application profiles
[**delete_application_profile**](ApplicationProfilesApi.md#delete_application_profile) | **DELETE** /api/v1/applications/profiles/{profileId} | Delete application profile
[**get_application_profile**](ApplicationProfilesApi.md#get_application_profile) | **GET** /api/v1/applications/profiles/{profileId} | Get application profile
[**list_application_profiles**](ApplicationProfilesApi.md#list_application_profiles) | **GET** /api/v1/applications/profiles | List application profiles
[**upsert_application_profile**](ApplicationProfilesApi.md#upsert_application_profile) | **POST** /api/v1/applications/profiles | Create or update application profile


# **bulk_delete_application_profiles**
> bulk_delete_application_profiles(application_profile_bulk_delete_request)

Bulk delete application profiles

Removes multiple application profiles in a single request. Profiles in use by deployed applications are skipped; deletable profiles are removed and the in-use ones are reported back as a conflict.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_profile_bulk_delete_request import ApplicationProfileBulkDeleteRequest
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
    api_instance = astropulse._generated.ApplicationProfilesApi(api_client)
    application_profile_bulk_delete_request = astropulse._generated.ApplicationProfileBulkDeleteRequest() # ApplicationProfileBulkDeleteRequest | List of profile names to delete

    try:
        # Bulk delete application profiles
        api_instance.bulk_delete_application_profiles(application_profile_bulk_delete_request)
    except Exception as e:
        print("Exception when calling ApplicationProfilesApi->bulk_delete_application_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_profile_bulk_delete_request** | [**ApplicationProfileBulkDeleteRequest**](ApplicationProfileBulkDeleteRequest.md)| List of profile names to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Application profiles deleted successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to delete application profiles |  -  |
**404** | One or more application profiles not found |  -  |
**409** | One or more profiles are in use by deployed applications |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_profile**
> ApplicationProfileResponse delete_application_profile(profile_id)

Delete application profile

Permanently removes the application profile. Profiles currently in use by deployed applications cannot be deleted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_profile_response import ApplicationProfileResponse
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
    api_instance = astropulse._generated.ApplicationProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | Profile ID

    try:
        # Delete application profile
        api_response = api_instance.delete_application_profile(profile_id)
        print("The response of ApplicationProfilesApi->delete_application_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProfilesApi->delete_application_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Profile ID | 

### Return type

[**ApplicationProfileResponse**](ApplicationProfileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application profile deleted successfully |  -  |
**400** | Invalid profile ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to delete application profile |  -  |
**404** | Application profile not found |  -  |
**409** | Profile is in use and cannot be deleted |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_profile**
> ApplicationProfileResponse get_application_profile(profile_id)

Get application profile

Returns the configuration and tier details for the specified application profile.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_profile_response import ApplicationProfileResponse
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
    api_instance = astropulse._generated.ApplicationProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | Profile ID

    try:
        # Get application profile
        api_response = api_instance.get_application_profile(profile_id)
        print("The response of ApplicationProfilesApi->get_application_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProfilesApi->get_application_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Profile ID | 

### Return type

[**ApplicationProfileResponse**](ApplicationProfileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application profile retrieved successfully |  -  |
**400** | Invalid profile ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view application profile |  -  |
**404** | Application profile not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_profiles**
> ApplicationProfileListResponse list_application_profiles()

List application profiles

Returns all application profiles for the organization, including their deployment tiers and associated resource configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_profile_list_response import ApplicationProfileListResponse
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
    api_instance = astropulse._generated.ApplicationProfilesApi(api_client)

    try:
        # List application profiles
        api_response = api_instance.list_application_profiles()
        print("The response of ApplicationProfilesApi->list_application_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProfilesApi->list_application_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApplicationProfileListResponse**](ApplicationProfileListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of application profiles retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view application profiles |  -  |
**404** | No application profiles found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_application_profile**
> ApplyDryRunResultResponse upsert_application_profile(application_profile_manifest, dry_run=dry_run)

Create or update application profile

Creates or updates an application profile: the deployment resources, tier and environment settings applications in the organization deploy with. Cluster targeting is immutable while the target cluster exists.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.application_profile_manifest import ApplicationProfileManifest
from astropulse._generated.models.apply_dry_run_result_response import ApplyDryRunResultResponse
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
    api_instance = astropulse._generated.ApplicationProfilesApi(api_client)
    application_profile_manifest = astropulse._generated.ApplicationProfileManifest() # ApplicationProfileManifest | Application profile configuration
    dry_run = True # bool | When true, runs every check an apply runs and changes nothing (optional)

    try:
        # Create or update application profile
        api_response = api_instance.upsert_application_profile(application_profile_manifest, dry_run=dry_run)
        print("The response of ApplicationProfilesApi->upsert_application_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationProfilesApi->upsert_application_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_profile_manifest** | [**ApplicationProfileManifest**](ApplicationProfileManifest.md)| Application profile configuration | 
 **dry_run** | **bool**| When true, runs every check an apply runs and changes nothing | [optional] 

### Return type

[**ApplyDryRunResultResponse**](ApplyDryRunResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry run: the profile would be applied as submitted |  -  |
**201** | Application profile created successfully |  -  |
**400** | Invalid profile configuration |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to create application profiles |  -  |
**404** | Organization not found |  -  |
**409** | Cluster targeting cannot be changed while the profile is attached to an existing cluster |  -  |
**422** | Invalid profile parameters |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


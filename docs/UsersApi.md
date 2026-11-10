# astropulse._generated.UsersApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_profile**](UsersApi.md#create_user_profile) | **POST** /api/v1/users/profile | Create a new user profile
[**get_user_profile**](UsersApi.md#get_user_profile) | **GET** /api/v1/users/profile | Get current user profile
[**switch_current_organization**](UsersApi.md#switch_current_organization) | **POST** /api/v1/users/org | Switch current organization


# **create_user_profile**
> UserProfileResponse create_user_profile()

Create a new user profile

Creates an AstroPulse profile for the authenticated user if one does not yet exist, or returns the existing profile. Called automatically after first login.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.user_profile_response import UserProfileResponse
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
    api_instance = astropulse._generated.UsersApi(api_client)

    try:
        # Create a new user profile
        api_response = api_instance.create_user_profile()
        print("The response of UsersApi->create_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User profile created successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid authorization token |  -  |
**403** | User does not have permission to create profile |  -  |
**404** | User not found. |  -  |
**409** | User profile already exists |  -  |
**422** | Invalid user data |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> UserProfileResponse get_user_profile()

Get current user profile

Returns the authenticated user's profile, organization memberships, roles, and active organization context.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.user_profile_response import UserProfileResponse
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
    api_instance = astropulse._generated.UsersApi(api_client)

    try:
        # Get current user profile
        api_response = api_instance.get_user_profile()
        print("The response of UsersApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User profile retrieved successfully |  -  |
**401** | Missing or invalid authorization token |  -  |
**403** | User does not have permission to view profile |  -  |
**404** | User profile not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_current_organization**
> CurrentOrganizationResponse switch_current_organization(switch_org_request)

Switch current organization

Sets the user's active organization so subsequent API calls default to that organization's scope. The user must be a member of the target organization.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.current_organization_response import CurrentOrganizationResponse
from astropulse._generated.models.switch_org_request import SwitchOrgRequest
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
    api_instance = astropulse._generated.UsersApi(api_client)
    switch_org_request = astropulse._generated.SwitchOrgRequest() # SwitchOrgRequest | Organization to switch to

    try:
        # Switch current organization
        api_response = api_instance.switch_current_organization(switch_org_request)
        print("The response of UsersApi->switch_current_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->switch_current_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **switch_org_request** | [**SwitchOrgRequest**](SwitchOrgRequest.md)| Organization to switch to | 

### Return type

[**CurrentOrganizationResponse**](CurrentOrganizationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization switched successfully |  -  |
**400** | Invalid request body |  -  |
**401** | Missing or invalid authorization token |  -  |
**403** | User is not a member of the target organization |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


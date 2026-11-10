# astropulse._generated.OrganizationsApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_member**](OrganizationsApi.md#add_organization_member) | **POST** /api/v1/organizations/addmember | Add user to organization
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /api/v1/organizations | Create an organization
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /api/v1/organizations/{id} | Get organization by ID
[**get_organization_plan**](OrganizationsApi.md#get_organization_plan) | **GET** /api/v1/organizations/plans | Get organization plan
[**list_organization_members**](OrganizationsApi.md#list_organization_members) | **GET** /api/v1/organizations/{id}/members | Get organization members
[**list_organization_roles**](OrganizationsApi.md#list_organization_roles) | **GET** /api/v1/organizations/roles | Get organization roles
[**list_organizations**](OrganizationsApi.md#list_organizations) | **GET** /api/v1/organizations | List organizations for the caller
[**remove_organization_member**](OrganizationsApi.md#remove_organization_member) | **POST** /api/v1/organizations/removemember | Remove user from organization
[**set_organization_member_role**](OrganizationsApi.md#set_organization_member_role) | **PUT** /api/v1/organizations/{orgId}/members/{userId}/role | Change a member&#39;s role
[**transfer_organization_ownership**](OrganizationsApi.md#transfer_organization_ownership) | **POST** /api/v1/organizations/{orgId}/owner/transfer | Transfer an organization&#39;s ownership


# **add_organization_member**
> OrganizationMemberResponse add_organization_member(add_user_to_organization_request)

Add user to organization

Add a user to an organization with specified role (Viewer, Editor or Admin; default Viewer). Takes the global admin role and ownership of the organization; adding an admin also needs the plan's admin roles.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.add_user_to_organization_request import AddUserToOrganizationRequest
from astropulse._generated.models.organization_member_response import OrganizationMemberResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    add_user_to_organization_request = astropulse._generated.AddUserToOrganizationRequest() # AddUserToOrganizationRequest | User details and role

    try:
        # Add user to organization
        api_response = api_instance.add_organization_member(add_user_to_organization_request)
        print("The response of OrganizationsApi->add_organization_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->add_organization_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_to_organization_request** | [**AddUserToOrganizationRequest**](AddUserToOrganizationRequest.md)| User details and role | 

### Return type

[**OrganizationMemberResponse**](OrganizationMemberResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User added to organization successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to add users to this organization |  -  |
**404** | Organization or user not found |  -  |
**409** | User is already a member of this organization |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> OrganizationResponse create_organization(organization_request)

Create an organization

Create a new organization and provision its associated resources. The authenticated user becomes the organization admin. Organization names must be unique. Beyond your default one it needs the global admin role and room under the plan's organization limit.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_request import OrganizationRequest
from astropulse._generated.models.organization_response import OrganizationResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    organization_request = astropulse._generated.OrganizationRequest() # OrganizationRequest | organization request

    try:
        # Create an organization
        api_response = api_instance.create_organization(organization_request)
        print("The response of OrganizationsApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_request** | [**OrganizationRequest**](OrganizationRequest.md)| organization request | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization created successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User is not authorized to create organization |  -  |
**404** | Organization not found |  -  |
**409** | Organization already exists |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> OrganizationResponse get_organization(id)

Get organization by ID

Returns the organization's details, such as its name and plan. Members and the owner's ID are returned only to an admin or owner.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_response import OrganizationResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    id = 'id_example' # str | Organization ID

    try:
        # Get organization by ID
        api_response = api_instance.get_organization(id)
        print("The response of OrganizationsApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization ID | 

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization details retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to access this organization |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_plan**
> StringResponse get_organization_plan(org_id)

Get organization plan

Get the current subscription plan for an organization

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.string_response import StringResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | Organization to read the plan of

    try:
        # Get organization plan
        api_response = api_instance.get_organization_plan(org_id)
        print("The response of OrganizationsApi->get_organization_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization to read the plan of | 

### Return type

[**StringResponse**](StringResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The plan id this organization is on |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view organization plan |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_members**
> OrganizationMembersPageResponse list_organization_members(id, limit=limit, page_token=page_token, page=page, page_size=page_size)

Get organization members

Get all members of an organization with pagination

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_members_page_response import OrganizationMembersPageResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    id = 'id_example' # str | Organization ID
    limit = 10 # int | Page size from 1 through 100; overrides pageSize (optional) (default to 10)
    page_token = 'page_token_example' # str | Opaque continuation token from nextPageToken (optional)
    page = 56 # int | Page number (default: 1). Prefer pageToken. (optional)
    page_size = 56 # int | Items per page (default: 10, at most 100; a larger value is treated as 100). Prefer limit. (optional)

    try:
        # Get organization members
        api_response = api_instance.list_organization_members(id, limit=limit, page_token=page_token, page=page, page_size=page_size)
        print("The response of OrganizationsApi->list_organization_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization ID | 
 **limit** | **int**| Page size from 1 through 100; overrides pageSize | [optional] [default to 10]
 **page_token** | **str**| Opaque continuation token from nextPageToken | [optional] 
 **page** | **int**| Page number (default: 1). Prefer pageToken. | [optional] 
 **page_size** | **int**| Items per page (default: 10, at most 100; a larger value is treated as 100). Prefer limit. | [optional] 

### Return type

[**OrganizationMembersPageResponse**](OrganizationMembersPageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization members retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view organization members |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_roles**
> RoleListResponse list_organization_roles()

Get organization roles

Returns every organization role, lowest first. Send a role's key as role to add-member and set-role;
they accept only the roles whose assignable is true. The owner role is not assignable: it moves by ownership transfer.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.role_list_response import RoleListResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)

    try:
        # Get organization roles
        api_response = api_instance.list_organization_roles()
        print("The response of OrganizationsApi->list_organization_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organization_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RoleListResponse**](RoleListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization roles retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view organization roles |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organizations**
> OrganizationListResponse list_organizations()

List organizations for the caller

List the organizations the caller belongs to. A service account gets its own organization. Members and the owner's ID are returned only to an admin or owner.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_list_response import OrganizationListResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)

    try:
        # List organizations for the caller
        api_response = api_instance.list_organizations()
        print("The response of OrganizationsApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_organizations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrganizationListResponse**](OrganizationListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of organizations retrieved successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_organization_member**
> StringResponse remove_organization_member(remove_user_from_organization_request)

Remove user from organization

Removes the specified user from the organization. The last admin cannot be removed, nor the owner.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.remove_user_from_organization_request import RemoveUserFromOrganizationRequest
from astropulse._generated.models.string_response import StringResponse
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    remove_user_from_organization_request = astropulse._generated.RemoveUserFromOrganizationRequest() # RemoveUserFromOrganizationRequest | User details

    try:
        # Remove user from organization
        api_response = api_instance.remove_organization_member(remove_user_from_organization_request)
        print("The response of OrganizationsApi->remove_organization_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->remove_organization_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_user_from_organization_request** | [**RemoveUserFromOrganizationRequest**](RemoveUserFromOrganizationRequest.md)| User details | 

### Return type

[**StringResponse**](StringResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User removed from organization successfully |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to remove users from this organization |  -  |
**404** | Organization or user not found |  -  |
**409** | Cannot remove the last admin user |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_organization_member_role**
> OrganizationMemberResponse set_organization_member_role(org_id, user_id, set_organization_member_role_request)

Change a member's role

Sets a member's role to Viewer, Editor or Admin. Takes the global admin role and ownership of the organization; granting admin also needs the plan's admin roles. The owner's role never changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_member_response import OrganizationMemberResponse
from astropulse._generated.models.set_organization_member_role_request import SetOrganizationMemberRoleRequest
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    user_id = 'user_id_example' # str | Member's user ID
    set_organization_member_role_request = astropulse._generated.SetOrganizationMemberRoleRequest() # SetOrganizationMemberRoleRequest | The new role

    try:
        # Change a member's role
        api_response = api_instance.set_organization_member_role(org_id, user_id, set_organization_member_role_request)
        print("The response of OrganizationsApi->set_organization_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->set_organization_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **user_id** | **str**| Member&#39;s user ID | 
 **set_organization_member_role_request** | [**SetOrganizationMemberRoleRequest**](SetOrganizationMemberRoleRequest.md)| The new role | 

### Return type

[**OrganizationMemberResponse**](OrganizationMemberResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The member with the new role |  -  |
**400** | Invalid role |  -  |
**401** | Missing or invalid credentials |  -  |
**403** | Not a global admin and owner, plan without the feature, or the owner&#39;s role |  -  |
**404** | Not a member of the organization |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_organization_ownership**
> OrganizationOwnershipTransferResponse transfer_organization_ownership(org_id, transfer_organization_ownership_request)

Transfer an organization's ownership

Makes another member the owner of a team organization; the previous owner stays a member as admin and can then be removed. Takes the current owner, or a super-admin. The new owner must be a member holding the global admin role. A default organization cannot be transferred.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.organization_ownership_transfer_response import OrganizationOwnershipTransferResponse
from astropulse._generated.models.transfer_organization_ownership_request import TransferOrganizationOwnershipRequest
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
    api_instance = astropulse._generated.OrganizationsApi(api_client)
    org_id = 'org_id_example' # str | Organization ID
    transfer_organization_ownership_request = astropulse._generated.TransferOrganizationOwnershipRequest() # TransferOrganizationOwnershipRequest | The new owner

    try:
        # Transfer an organization's ownership
        api_response = api_instance.transfer_organization_ownership(org_id, transfer_organization_ownership_request)
        print("The response of OrganizationsApi->transfer_organization_ownership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->transfer_organization_ownership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID | 
 **transfer_organization_ownership_request** | [**TransferOrganizationOwnershipRequest**](TransferOrganizationOwnershipRequest.md)| The new owner | 

### Return type

[**OrganizationOwnershipTransferResponse**](OrganizationOwnershipTransferResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ownership transferred |  -  |
**400** | Missing new owner, or the new owner already owns the organization |  -  |
**401** | Missing or invalid credentials |  -  |
**403** | Not the owner, a default organization, or the new owner is not a global admin |  -  |
**404** | The organization is not found, or the new owner is not a member of it |  -  |
**409** | The owner changed while this transfer was requested |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


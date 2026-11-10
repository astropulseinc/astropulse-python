# astropulse._generated.CloudCatalogApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_infrastructure_estimate**](CloudCatalogApi.md#get_cluster_infrastructure_estimate) | **GET** /api/v1/providers/{providerId}/regions/{regionId}/infrastructure | Get what a new cluster gets around it, at list price
[**get_machine_type**](CloudCatalogApi.md#get_machine_type) | **GET** /api/v1/providers/{providerId}/regions/{regionId}/machinetypes/{machinetypeId} | Get machine type details
[**list_machine_types**](CloudCatalogApi.md#list_machine_types) | **GET** /api/v1/providers/{providerId}/regions/{regionId}/machinetypes | List available machine types
[**list_provider_provisioners**](CloudCatalogApi.md#list_provider_provisioners) | **GET** /api/v1/providers/provisioners | List the provisioners each provider offers
[**list_provider_regions**](CloudCatalogApi.md#list_provider_regions) | **GET** /api/v1/providers/{providerId}/regions | List available regions for a provider
[**list_providers**](CloudCatalogApi.md#list_providers) | **GET** /api/v1/providers | List supported providers
[**list_region_accelerators**](CloudCatalogApi.md#list_region_accelerators) | **GET** /api/v1/providers/{providerId}/regions/{regionId}/accelerators | List distinct accelerators available in a region
[**list_region_zones**](CloudCatalogApi.md#list_region_zones) | **GET** /api/v1/providers/{providerId}/regions/{regionId}/zones | List available zones for a region


# **get_cluster_infrastructure_estimate**
> ClusterInfrastructureEstimateResponse get_cluster_infrastructure_estimate(provider_id, region_id, provisioner, compute_mode=compute_mode, private_cluster=private_cluster, existing_network=existing_network)

Get what a new cluster gets around it, at list price

The charges outside a new cluster's nodes, such as its control plane and NAT gateways, with how many it gets and each one's published hourly price, where it was read and when. Nodes are priced on their machine types.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_infrastructure_estimate_response import ClusterInfrastructureEstimateResponse
from astropulse._generated.models.eks_compute_mode import EKSComputeMode
from astropulse._generated.models.provisioner_type import ProvisionerType
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    region_id = 'region_id_example' # str | Region ID
    provisioner = astropulse._generated.ProvisionerType() # ProvisionerType | The provisioner the cluster is created with. Takes only `eks`, `gke`, `aks` or `selfHosted`.
    compute_mode = astropulse._generated.EKSComputeMode() # EKSComputeMode | An EKS cluster's compute mode, as eks.computeMode in the create request (optional)
    private_cluster = True # bool | A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it (optional)
    existing_network = True # bool | The cluster is created in a network you name, whose gateways are your own (optional)

    try:
        # Get what a new cluster gets around it, at list price
        api_response = api_instance.get_cluster_infrastructure_estimate(provider_id, region_id, provisioner, compute_mode=compute_mode, private_cluster=private_cluster, existing_network=existing_network)
        print("The response of CloudCatalogApi->get_cluster_infrastructure_estimate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->get_cluster_infrastructure_estimate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **region_id** | **str**| Region ID | 
 **provisioner** | [**ProvisionerType**](.md)| The provisioner the cluster is created with. Takes only &#x60;eks&#x60;, &#x60;gke&#x60;, &#x60;aks&#x60; or &#x60;selfHosted&#x60;. | 
 **compute_mode** | [**EKSComputeMode**](.md)| An EKS cluster&#39;s compute mode, as eks.computeMode in the create request | [optional] 
 **private_cluster** | **bool**| A GKE cluster whose nodes have internal addresses only, as gke.privateCluster; other provisioners ignore it | [optional] 
 **existing_network** | **bool**| The cluster is created in a network you name, whose gateways are your own | [optional] 

### Return type

[**ClusterInfrastructureEstimateResponse**](ClusterInfrastructureEstimateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The charges and their prices |  -  |
**400** | Invalid provider, region, provisioner or choice |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view prices |  -  |
**404** | Provider or region not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_type**
> MachineTypeResponse get_machine_type(provider_id, region_id, machinetype_id, zone_id=zone_id)

Get machine type details

What the provider publishes about one machine type, as AstroPulse sees it, at list price. Whether your own account can launch it is answered by the dry run when you apply.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.machine_type_response import MachineTypeResponse
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    region_id = 'region_id_example' # str | Region name
    machinetype_id = 'machinetype_id_example' # str | Machine type name
    zone_id = 'zone_id_example' # str | Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used (optional)

    try:
        # Get machine type details
        api_response = api_instance.get_machine_type(provider_id, region_id, machinetype_id, zone_id=zone_id)
        print("The response of CloudCatalogApi->get_machine_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->get_machine_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **region_id** | **str**| Region name | 
 **machinetype_id** | **str**| Machine type name | 
 **zone_id** | **str**| Zone ID. Pass &#39;all&#39; for the region-wide view with each machine listed once. If not specified, the first available zone is used | [optional] 

### Return type

[**MachineTypeResponse**](MachineTypeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Machine type details retrieved successfully |  -  |
**400** | Invalid provider ID, region, zone, or machine type |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view machine type |  -  |
**404** | Provider, region, zone, or machine type not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_machine_types**
> MachineTypeListResponse list_machine_types(provider_id, region_id, cpu_min=cpu_min, cpu_max=cpu_max, mem_min=mem_min, mem_max=mem_max, category=category, architecture=architecture, accelerator_kind=accelerator_kind, accelerator_vendor=accelerator_vendor, accelerator_model=accelerator_model, accelerator_count_min=accelerator_count_min, accelerator_count_max=accelerator_count_max, accelerator_memory_mi_b_min=accelerator_memory_mi_b_min, accelerator_memory_mi_b_max=accelerator_memory_mi_b_max, zone_id=zone_id)

List available machine types

Machine types the provider offers in the region, as AstroPulse sees them, at list price. Whether your own account can launch one — quota, availability, reservations — is answered by the dry run.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.accelerator_kind import AcceleratorKind
from astropulse._generated.models.accelerator_vendor import AcceleratorVendor
from astropulse._generated.models.architecture_type import ArchitectureType
from astropulse._generated.models.compute_type import ComputeType
from astropulse._generated.models.machine_type_list_response import MachineTypeListResponse
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    region_id = 'region_id_example' # str | Region ID
    cpu_min = 'cpu_min_example' # str | Minimum CPU requirement (e.g., '1', '500m') (optional)
    cpu_max = 'cpu_max_example' # str | Maximum CPU requirement (e.g., '4', '2000m') (optional)
    mem_min = 'mem_min_example' # str | Minimum memory requirement (e.g., '1Gi', '512Mi') (optional)
    mem_max = 'mem_max_example' # str | Maximum memory requirement (e.g., '8Gi', '4Gi') (optional)
    category = astropulse._generated.ComputeType() # ComputeType | Machine type category (optional)
    architecture = astropulse._generated.ArchitectureType() # ArchitectureType | CPU architecture (optional)
    accelerator_kind = astropulse._generated.AcceleratorKind() # AcceleratorKind | Only machine types with an accelerator of this kind (optional)
    accelerator_vendor = astropulse._generated.AcceleratorVendor() # AcceleratorVendor | Only machine types whose accelerator comes from this vendor (optional)
    accelerator_model = 'accelerator_model_example' # str | Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable (optional)
    accelerator_count_min = 56 # int | Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this (optional)
    accelerator_count_max = 56 # int | Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this (optional)
    accelerator_memory_mi_b_min = 56 # int | Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this (optional)
    accelerator_memory_mi_b_max = 56 # int | Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this (optional)
    zone_id = 'zone_id_example' # str | Zone ID. Pass 'all' for the region-wide view with each machine listed once. If not specified, the first available zone is used (optional)

    try:
        # List available machine types
        api_response = api_instance.list_machine_types(provider_id, region_id, cpu_min=cpu_min, cpu_max=cpu_max, mem_min=mem_min, mem_max=mem_max, category=category, architecture=architecture, accelerator_kind=accelerator_kind, accelerator_vendor=accelerator_vendor, accelerator_model=accelerator_model, accelerator_count_min=accelerator_count_min, accelerator_count_max=accelerator_count_max, accelerator_memory_mi_b_min=accelerator_memory_mi_b_min, accelerator_memory_mi_b_max=accelerator_memory_mi_b_max, zone_id=zone_id)
        print("The response of CloudCatalogApi->list_machine_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_machine_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **region_id** | **str**| Region ID | 
 **cpu_min** | **str**| Minimum CPU requirement (e.g., &#39;1&#39;, &#39;500m&#39;) | [optional] 
 **cpu_max** | **str**| Maximum CPU requirement (e.g., &#39;4&#39;, &#39;2000m&#39;) | [optional] 
 **mem_min** | **str**| Minimum memory requirement (e.g., &#39;1Gi&#39;, &#39;512Mi&#39;) | [optional] 
 **mem_max** | **str**| Maximum memory requirement (e.g., &#39;8Gi&#39;, &#39;4Gi&#39;) | [optional] 
 **category** | [**ComputeType**](.md)| Machine type category | [optional] 
 **architecture** | [**ArchitectureType**](.md)| CPU architecture | [optional] 
 **accelerator_kind** | [**AcceleratorKind**](.md)| Only machine types with an accelerator of this kind | [optional] 
 **accelerator_vendor** | [**AcceleratorVendor**](.md)| Only machine types whose accelerator comes from this vendor | [optional] 
 **accelerator_model** | **str**| Only machine types carrying this normalized accelerator model (a100, l4, h100). Provider-native type names are not filterable | [optional] 
 **accelerator_count_min** | **int**| Minimum accelerators per machine. Machine types whose provider reports no count never satisfy this | [optional] 
 **accelerator_count_max** | **int**| Maximum accelerators per machine. Machine types whose provider reports no count never satisfy this | [optional] 
 **accelerator_memory_mi_b_min** | **int**| Minimum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this | [optional] 
 **accelerator_memory_mi_b_max** | **int**| Maximum memory per accelerator in MiB. Machine types with unavailable accelerator memory never satisfy this | [optional] 
 **zone_id** | **str**| Zone ID. Pass &#39;all&#39; for the region-wide view with each machine listed once. If not specified, the first available zone is used | [optional] 

### Return type

[**MachineTypeListResponse**](MachineTypeListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available machine types |  -  |
**400** | Invalid provider ID, region, or zone |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view machine types |  -  |
**404** | Provider, region, or zone not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provider_provisioners**
> ProviderProvisionersListResponse list_provider_provisioners()

List the provisioners each provider offers

For each cloud AstroPulse supports, the ways it can create a cluster there: display name, a one-line summary of who
runs the control plane and what you manage, the documentation page, and whether the account needs a one-time setup first.
acceleratorNodeGroups says whether a node group may carry a GPU on that provisioner, and acceleratorMinKubernetesVersion
the lowest Kubernetes version such a cluster may run; a create or update outside them is refused.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider_provisioners_list_response import ProviderProvisionersListResponse
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)

    try:
        # List the provisioners each provider offers
        api_response = api_instance.list_provider_provisioners()
        print("The response of CloudCatalogApi->list_provider_provisioners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_provider_provisioners: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProviderProvisionersListResponse**](ProviderProvisionersListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provisioners per provider |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provider_regions**
> StringListResponse list_provider_regions(provider_id, provisioner=provisioner)

List available regions for a provider

Regions the provider offers, as AstroPulse sees them. Whether your own account can deploy into one — it may not be opted in — is answered by the dry run when you apply.
With provisioner, only the regions that provisioner can create a cluster in: EKS and GKE need a region with at least three zones.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provisioner_type import ProvisionerType
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    provisioner = astropulse._generated.ProvisionerType() # ProvisionerType | Only regions this provisioner can create a cluster in. Takes only `eks`, `gke`, `aks` or `selfHosted`. (optional)

    try:
        # List available regions for a provider
        api_response = api_instance.list_provider_regions(provider_id, provisioner=provisioner)
        print("The response of CloudCatalogApi->list_provider_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_provider_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **provisioner** | [**ProvisionerType**](.md)| Only regions this provisioner can create a cluster in. Takes only &#x60;eks&#x60;, &#x60;gke&#x60;, &#x60;aks&#x60; or &#x60;selfHosted&#x60;. | [optional] 

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
**200** | List of available regions for the provider |  -  |
**400** | Invalid provider ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view regions |  -  |
**404** | Provider not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProviderListResponse list_providers()

List supported providers

Returns the list of cloud providers available for cluster provisioning on AstroPulse.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.provider_list_response import ProviderListResponse
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)

    try:
        # List supported providers
        api_response = api_instance.list_providers()
        print("The response of CloudCatalogApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProviderListResponse**](ProviderListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported cloud providers |  -  |
**400** | Invalid request parameters |  -  |
**401** | Missing or invalid API key |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_region_accelerators**
> AcceleratorOfferingListResponse list_region_accelerators(provider_id, region_id, zone_id=zone_id)

List distinct accelerators available in a region

Distinct accelerators in the region's catalog as AstroPulse sees it, at list price; read it to learn which filter values exist. Whether your own account can launch one is answered by the dry run. Each row says how old its prices are (scrapedAt, ageSeconds), whether they are stale, and when the provider's latest refresh failed (refreshFailedAt).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.accelerator_offering_list_response import AcceleratorOfferingListResponse
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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    region_id = 'region_id_example' # str | Region ID
    zone_id = 'zone_id_example' # str | Only accelerators on machine types offered in this zone. Omit it, or pass 'all', for the whole region (optional)

    try:
        # List distinct accelerators available in a region
        api_response = api_instance.list_region_accelerators(provider_id, region_id, zone_id=zone_id)
        print("The response of CloudCatalogApi->list_region_accelerators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_region_accelerators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **region_id** | **str**| Region ID | 
 **zone_id** | **str**| Only accelerators on machine types offered in this zone. Omit it, or pass &#39;all&#39;, for the whole region | [optional] 

### Return type

[**AcceleratorOfferingListResponse**](AcceleratorOfferingListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Distinct accelerators available in the region, cheapest first |  -  |
**400** | Invalid provider ID or region |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view machine types |  -  |
**404** | Provider or region not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_region_zones**
> StringListResponse list_region_zones(provider_id, region_id)

List available zones for a region

Zones the provider offers in the region, as AstroPulse sees them. Whether your own account has capacity and quota in one is answered by the dry run when you apply.

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
    api_instance = astropulse._generated.CloudCatalogApi(api_client)
    provider_id = 'provider_id_example' # str | Provider ID (e.g., aws, gcp, azure)
    region_id = 'region_id_example' # str | Region ID

    try:
        # List available zones for a region
        api_response = api_instance.list_region_zones(provider_id, region_id)
        print("The response of CloudCatalogApi->list_region_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudCatalogApi->list_region_zones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Provider ID (e.g., aws, gcp, azure) | 
 **region_id** | **str**| Region ID | 

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
**200** | List of available zones for the region |  -  |
**400** | Invalid provider ID or region |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view zones |  -  |
**404** | Provider or region not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


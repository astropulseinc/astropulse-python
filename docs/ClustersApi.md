# astropulse._generated.ClustersApi

All URIs are relative to *https://api.astropulse.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_cluster_operation**](ClustersApi.md#cancel_cluster_operation) | **POST** /api/v1/clusters/{clusterName}/cancel | Cancel the running cluster operation
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /api/v1/clusters | Deploy a new Kubernetes cluster
[**create_cluster_access_token**](ClustersApi.md#create_cluster_access_token) | **POST** /api/v1/clusters/{clusterName}/access-token | Get a cluster access token
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /api/v1/clusters/{clusterName} | Delete a Kubernetes cluster
[**generate_cluster_kubeconfig**](ClustersApi.md#generate_cluster_kubeconfig) | **POST** /api/v1/clusters/{clusterName}/kubeconfig | Generate kubeconfig for a cluster
[**get_cluster**](ClustersApi.md#get_cluster) | **GET** /api/v1/clusters/{clusterName} | Get cluster details
[**get_cluster_accelerators**](ClustersApi.md#get_cluster_accelerators) | **GET** /api/v1/clusters/{clusterName}/accelerators | List the GPUs a cluster can provide
[**get_cluster_agent**](ClustersApi.md#get_cluster_agent) | **GET** /api/v1/clusters/{clusterName}/agent | Get agent status for a cluster
[**get_cluster_cost_allocation**](ClustersApi.md#get_cluster_cost_allocation) | **GET** /api/v1/clusters/{clusterName}/cost/allocation | Get cluster cost allocation
[**get_cluster_cost_series**](ClustersApi.md#get_cluster_cost_series) | **GET** /api/v1/clusters/{clusterName}/cost/series | Get cluster cost time series
[**get_cluster_cost_summary**](ClustersApi.md#get_cluster_cost_summary) | **GET** /api/v1/clusters/{clusterName}/cost/summary | Get cluster cost summary
[**get_cluster_kubeconfig**](ClustersApi.md#get_cluster_kubeconfig) | **GET** /api/v1/clusters/{clusterName}/kubeconfig | Get cluster kubeconfig
[**get_cluster_metrics_allocation**](ClustersApi.md#get_cluster_metrics_allocation) | **GET** /api/v1/clusters/{clusterName}/metrics/allocation | Get cluster metrics allocation
[**get_cluster_metrics_summary**](ClustersApi.md#get_cluster_metrics_summary) | **GET** /api/v1/clusters/{clusterName}/metrics/summary | Get cluster metrics summary
[**get_cluster_progress**](ClustersApi.md#get_cluster_progress) | **GET** /api/v1/clusters/{clusterName}/progress | Get cluster progress
[**get_cluster_spec**](ClustersApi.md#get_cluster_spec) | **GET** /api/v1/clusters/{clusterName}/spec | Get cluster specification
[**get_cluster_storage**](ClustersApi.md#get_cluster_storage) | **GET** /api/v1/clusters/{clusterName}/storage | Get a cluster&#39;s storage
[**issue_cluster_agent_certificate**](ClustersApi.md#issue_cluster_agent_certificate) | **POST** /api/v1/clusters/{clusterName}/agent/certificate | Sign a new certificate for a cluster&#39;s agent
[**list_cluster_operations**](ClustersApi.md#list_cluster_operations) | **GET** /api/v1/clusters/{clusterName}/operations | Get cluster operation history
[**list_cluster_progress**](ClustersApi.md#list_cluster_progress) | **GET** /api/v1/clusters/progress | List cluster progress for all clusters
[**list_clusters**](ClustersApi.md#list_clusters) | **GET** /api/v1/clusters | List all clusters for your organization
[**register_cluster_agent**](ClustersApi.md#register_cluster_agent) | **POST** /api/v1/clusters/{clusterName}/agent | Register an agent on a cluster
[**request_cluster_approval**](ClustersApi.md#request_cluster_approval) | **POST** /api/v1/clusters/approval | Request cluster operation approval
[**stream_cluster_progress**](ClustersApi.md#stream_cluster_progress) | **GET** /api/v1/clusters/{clusterName}/progress/stream | Stream cluster progress via WebSocket
[**sync_cluster_auth**](ClustersApi.md#sync_cluster_auth) | **POST** /api/v1/clusters/{clusterName}/auth/sync | Sync cluster authentication configuration
[**unregister_cluster_agent**](ClustersApi.md#unregister_cluster_agent) | **DELETE** /api/v1/clusters/{clusterName}/agent | Unregister an agent from a cluster
[**update_cluster**](ClustersApi.md#update_cluster) | **PATCH** /api/v1/clusters/{clusterName} | Update cluster configuration
[**update_cluster_storage**](ClustersApi.md#update_cluster_storage) | **PUT** /api/v1/clusters/{clusterName}/storage | Set a cluster&#39;s storage bindings


# **cancel_cluster_operation**
> ClusterOperationResultResponse cancel_cluster_operation(cluster_name, dry_run=dry_run, cancel_cluster_operation_request=cancel_cluster_operation_request)

Cancel the running cluster operation

Asks the running update, scale, upgrade or rollback of a cluster to stop, and answers once the request is accepted, naming the node groups it removes. The operation stops its current step and removes any node group it was adding; changes already made to other node groups stay. Follow it with the cluster read: lastCancellation is CANCELLING while that runs, then CANCELLED with what was removed. A create, a delete or a registration can't be cancelled.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cancel_cluster_operation_request import CancelClusterOperationRequest
from astropulse._generated.models.cluster_operation_result_response import ClusterOperationResultResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    dry_run = False # bool | Answer what the cancel would do, naming the node groups it would remove, without sending it (optional) (default to False)
    cancel_cluster_operation_request = astropulse._generated.CancelClusterOperationRequest() # CancelClusterOperationRequest | Why the operation is being cancelled (optional)

    try:
        # Cancel the running cluster operation
        api_response = api_instance.cancel_cluster_operation(cluster_name, dry_run=dry_run, cancel_cluster_operation_request=cancel_cluster_operation_request)
        print("The response of ClustersApi->cancel_cluster_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->cancel_cluster_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **dry_run** | **bool**| Answer what the cancel would do, naming the node groups it would remove, without sending it | [optional] [default to False]
 **cancel_cluster_operation_request** | [**CancelClusterOperationRequest**](CancelClusterOperationRequest.md)| Why the operation is being cancelled | [optional] 

### Return type

[**ClusterOperationResultResponse**](ClusterOperationResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry run: what the cancel would do |  -  |
**202** | Cancel accepted; the operation is stopping |  -  |
**403** | Insufficient permissions |  -  |
**404** | Cluster not found |  -  |
**409** | No running operation to cancel, or one that can&#39;t be cancelled (reason ClusterOperationNotCancellable) |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster**
> ClusterDryRunResponse create_cluster(k8s_cluster_manifest, dry_run=dry_run)

Deploy a new Kubernetes cluster

Deploys a new Kubernetes cluster from a K8sCluster specification, in the manifest envelope or the flat request shape.
A dry run (?dryRun=true) and a create run the same checks: the spec, the region's zones, node group bounds, the cloud
account connection (connected, setup template current) and the provider preflight. The account connection is the first check.
A dry run answers 200 with the checklist whether or not the checks pass: read data.valid and data.checks; data.complete is false when some checks did not finish, named in data.unfinishedChecks.
A create whose checks fail answers 400 with reason PreflightFailed and the same checks in details.checks; nothing is created.
The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_dry_run_response import ClusterDryRunResponse
from astropulse._generated.models.k8s_cluster_manifest import K8sClusterManifest
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    k8s_cluster_manifest = astropulse._generated.K8sClusterManifest() # K8sClusterManifest | Cluster deployment configuration
    dry_run = True # bool | When true, returns the checklist without creating the cluster (optional)

    try:
        # Deploy a new Kubernetes cluster
        api_response = api_instance.create_cluster(k8s_cluster_manifest, dry_run=dry_run)
        print("The response of ClustersApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **k8s_cluster_manifest** | [**K8sClusterManifest**](K8sClusterManifest.md)| Cluster deployment configuration | 
 **dry_run** | **bool**| When true, returns the checklist without creating the cluster | [optional] 

### Return type

[**ClusterDryRunResponse**](ClusterDryRunResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry run: the checklist; data.valid is false when a check failed or did not finish |  -  |
**202** | Cluster creation accepted: started, or waiting for an owner&#39;s approval |  -  |
**400** | A create whose checks failed: reason PreflightFailed, details.checks lists every check (PreflightCheck, as in a dry run) and details.verdict is Failed. A spec error: details.checks holds the failed check and details.verdict is Failed. A malformed body or an unknown field: details.field names it |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to deploy clusters |  -  |
**404** | Organization not found |  -  |
**409** | The name is taken: reason ClusterAlreadyExists, ClusterUpdateFailed, ClusterDeleteFailed or ClusterRegistrationUnfinished; details.title and details.nextStep say what to do. A create that failed or was rejected can be sent again |  -  |
**422** | Invalid cluster parameters |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |
**504** | Some checks did not finish in time and nothing was created: reason ChecksUnfinished, details.unfinishedChecks names them and details.verdict is Unfinished; send it again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_access_token**
> ClusterAccessTokenResponse create_cluster_access_token(cluster_name)

Get a cluster access token

Returns a short-lived access token for the cluster's API, for as long as the kubeconfig you generated is valid. The kubeconfig from `astroctl infra k8s generate-kubeconfig` or `set-context` requests one automatically and renews it before it expires.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_access_token_response import ClusterAccessTokenResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get a cluster access token
        api_response = api_instance.create_cluster_access_token(cluster_name)
        print("The response of ClustersApi->create_cluster_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->create_cluster_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterAccessTokenResponse**](ClusterAccessTokenResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access token and when it expires |  -  |
**400** | The cluster&#39;s kubeconfig carries its own client certificate and needs no access token |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to access the cluster, or the kubeconfig&#39;s lifetime has ended (reason KubeconfigExpired); nextStep generates a new one |  -  |
**404** | Cluster not found |  -  |
**409** | Cluster is not ready yet (reason ClusterNotReady); try again once it reads Ready |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Cluster access is not available right now; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> ClusterDeletionResponse delete_cluster(cluster_name, record_only=record_only, dry_run=dry_run, show_all=show_all, credentials=credentials)

Delete a Kubernetes cluster

Permanently removes the cluster and the cloud resources created for it; disks its volumes use are kept in your cloud account and listed. Registered (agent-based) clusters must use the unregister endpoint instead.
With recordOnly=true, removes only AstroPulse's record of a self-hosted cluster whose stored key is gone; nothing in your cloud account is deleted.
With dryRun=true, lists the volumes the delete would leave in your cloud account and deletes nothing.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_deletion_response import ClusterDeletionResponse
from astropulse._generated.models.credentials import Credentials
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    record_only = False # bool | Remove only AstroPulse's record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is (optional) (default to False)
    dry_run = False # bool | List what the delete would leave in your cloud account, and delete nothing (optional) (default to False)
    show_all = 'show_all_example' # str | On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page (optional)
    credentials = astropulse._generated.Credentials() # Credentials | Optional credentials for cluster deletion (optional)

    try:
        # Delete a Kubernetes cluster
        api_response = api_instance.delete_cluster(cluster_name, record_only=record_only, dry_run=dry_run, show_all=show_all, credentials=credentials)
        print("The response of ClustersApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **record_only** | **bool**| Remove only AstroPulse&#39;s record of a self-hosted cluster whose stored key is gone, leaving your cloud account as it is | [optional] [default to False]
 **dry_run** | **bool**| List what the delete would leave in your cloud account, and delete nothing | [optional] [default to False]
 **show_all** | **str**| On a dry run, a comma-separated list of group kinds (Applications, Addons, Volumes, CloudResources, AccessPolicies) to return uncapped instead of the first page | [optional] 
 **credentials** | [**Credentials**](Credentials.md)| Optional credentials for cluster deletion | [optional] 

### Return type

[**ClusterDeletionResponse**](ClusterDeletionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete started (or was already running); with recordOnly, the record is removed and data.message lists what is left in your cloud account; with dryRun, nothing was deleted and data.dryRun lists the volumes the delete would keep |  -  |
**202** | Cluster deletion accepted |  -  |
**400** | Invalid cluster ID; dryRun and recordOnly together; recordOnly asked for a cluster that is not a self-hosted cluster without its stored key, or while the cluster has an operation in progress |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to delete clusters |  -  |
**404** | Cluster not found |  -  |
**409** | Cluster is not in a valid state for deletion |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_cluster_kubeconfig**
> KubeconfigResponse generate_cluster_kubeconfig(cluster_name, kubeconfig_request)

Generate kubeconfig for a cluster

Generates your kubeconfig for the cluster, valid for the lifetime you choose. A kubeconfig that signs in through astroctl (every cluster but a self-hosted one) is returned immediately; a self-hosted cluster's carries a client certificate, returns 202 and requires polling via GET.
With native, the kubeconfig signs in with your own cloud identity through your cloud provider's tool instead, and the message says what it needs.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.kubeconfig_request import KubeconfigRequest
from astropulse._generated.models.kubeconfig_response import KubeconfigResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    kubeconfig_request = astropulse._generated.KubeconfigRequest() # KubeconfigRequest | Kubeconfig generation request

    try:
        # Generate kubeconfig for a cluster
        api_response = api_instance.generate_cluster_kubeconfig(cluster_name, kubeconfig_request)
        print("The response of ClustersApi->generate_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->generate_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **kubeconfig_request** | [**KubeconfigRequest**](KubeconfigRequest.md)| Kubeconfig generation request | 

### Return type

[**KubeconfigResponse**](KubeconfigResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubeconfig available immediately (EKS, GKE, AKS) |  -  |
**202** | Kubeconfig generation initiated (self-managed clusters) |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to generate kubeconfig |  -  |
**404** | Cluster not found |  -  |
**409** | Cluster is not ready yet (reason ClusterNotReady); try again once it reads Ready |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> K8sClusterResponse get_cluster(cluster_name)

Get cluster details

Retrieves detailed information about a specific Kubernetes cluster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.k8s_cluster_response import K8sClusterResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get cluster details
        api_response = api_instance.get_cluster(cluster_name)
        print("The response of ClustersApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**K8sClusterResponse**](K8sClusterResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster details retrieved successfully |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view cluster details |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_accelerators**
> ClusterAcceleratorsResponse get_cluster_accelerators(cluster_name)

List the GPUs a cluster can provide

Returns the GPUs a model replica can ask for on the cluster: those its node groups carry and those its autoscaling pools can launch, with the most one replica can ask for and whether each can be placed now.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_accelerators_response import ClusterAcceleratorsResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # List the GPUs a cluster can provide
        api_response = api_instance.get_cluster_accelerators(cluster_name)
        print("The response of ClustersApi->get_cluster_accelerators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_accelerators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterAcceleratorsResponse**](ClusterAcceleratorsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cluster name |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view this cluster |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | The cluster is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_agent**
> ClusterRegistrationStatusResponse get_cluster_agent(cluster_name, operation_id=operation_id)

Get agent status for a cluster

Returns agent connection status and registration progress. Use operationId during an in-flight registration. Install instructions are returned to organization admins and owners only.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_registration_status_response import ClusterRegistrationStatusResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    operation_id = 'operation_id_example' # str | Operation ID for in-flight registration polling (optional)

    try:
        # Get agent status for a cluster
        api_response = api_instance.get_cluster_agent(cluster_name, operation_id=operation_id)
        print("The response of ClustersApi->get_cluster_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **operation_id** | **str**| Operation ID for in-flight registration polling | [optional] 

### Return type

[**ClusterRegistrationStatusResponse**](ClusterRegistrationStatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent status |  -  |
**401** | Missing or invalid API key |  -  |
**403** | operationId does not correspond to this cluster |  -  |
**404** | Cluster not found |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_cost_allocation**
> ClusterCostAllocationResponse get_cluster_cost_allocation(cluster_name, group_by, window=window, application=application, search=search, sort_by=sort_by, sort_order=sort_order, currency=currency, limit=limit, page_token=page_token)

Get cluster cost allocation

Aggregates provider-neutral, closed hourly metering rollups by namespace, application, or node group.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_cost_allocation_response import ClusterCostAllocationResponse
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy
from astropulse._generated.models.sort_order import SortOrder
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    group_by = astropulse._generated.CostAllocationGroupBy() # CostAllocationGroupBy | What the allocations are broken down by
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')
    application = 'application_example' # str | Application name; the display name or the managed resource name both work. Valid only with groupBy=Application (optional)
    search = 'search_example' # str | Case-insensitive allocation name search (optional)
    sort_by = astropulse._generated.CostAllocationSortBy() # CostAllocationSortBy | What the allocations are ordered by (optional)
    sort_order = astropulse._generated.SortOrder() # SortOrder | The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise (optional)
    currency = 'currency_example' # str | ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted (optional)
    limit = 50 # int | Page size from 1 through 200 (optional) (default to 50)
    page_token = 'page_token_example' # str | Opaque continuation token; it pins the original window and filters (optional)

    try:
        # Get cluster cost allocation
        api_response = api_instance.get_cluster_cost_allocation(cluster_name, group_by, window=window, application=application, search=search, sort_by=sort_by, sort_order=sort_order, currency=currency, limit=limit, page_token=page_token)
        print("The response of ClustersApi->get_cluster_cost_allocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_cost_allocation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **group_by** | [**CostAllocationGroupBy**](.md)| What the allocations are broken down by | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]
 **application** | **str**| Application name; the display name or the managed resource name both work. Valid only with groupBy&#x3D;Application | [optional] 
 **search** | **str**| Case-insensitive allocation name search | [optional] 
 **sort_by** | [**CostAllocationSortBy**](.md)| What the allocations are ordered by | [optional] 
 **sort_order** | [**SortOrder**](.md)| The direction of the order; rows with no value always come last. Ascending by default for Name, Descending otherwise | [optional] 
 **currency** | **str**| ISO 4217 currency for cost ordering; mixed-currency results fall back to name ordering when omitted | [optional] 
 **limit** | **int**| Page size from 1 through 200 | [optional] [default to 50]
 **page_token** | **str**| Opaque continuation token; it pins the original window and filters | [optional] 

### Return type

[**ClusterCostAllocationResponse**](ClusterCostAllocationResponse.md)

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
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_cost_series**
> ClusterCostSeriesResponse get_cluster_cost_series(cluster_name, window=window, interval=interval, group_by=group_by, name=name, application=application)

Get cluster cost time series

Returns bounded, closed-hour cost and usage buckets for charts. Missing and gap buckets remain explicit and are never converted to zero spend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_cost_series_response import ClusterCostSeriesResponse
from astropulse._generated.models.cost_allocation_group_by import CostAllocationGroupBy
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')
    interval = 'auto' # str | Bucket interval (auto, 1h, 6h, 12h, 1d) (optional) (default to 'auto')
    group_by = astropulse._generated.CostAllocationGroupBy() # CostAllocationGroupBy | The breakdown `name` is a row of (optional)
    name = 'name_example' # str | The row's exact name; requires groupBy (optional)
    application = 'application_example' # str | An application's name, as groupBy=Application with this name; the display name or the managed resource name both work (optional)

    try:
        # Get cluster cost time series
        api_response = api_instance.get_cluster_cost_series(cluster_name, window=window, interval=interval, group_by=group_by, name=name, application=application)
        print("The response of ClustersApi->get_cluster_cost_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_cost_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]
 **interval** | **str**| Bucket interval (auto, 1h, 6h, 12h, 1d) | [optional] [default to &#39;auto&#39;]
 **group_by** | [**CostAllocationGroupBy**](.md)| The breakdown &#x60;name&#x60; is a row of | [optional] 
 **name** | **str**| The row&#39;s exact name; requires groupBy | [optional] 
 **application** | **str**| An application&#39;s name, as groupBy&#x3D;Application with this name; the display name or the managed resource name both work | [optional] 

### Return type

[**ClusterCostSeriesResponse**](ClusterCostSeriesResponse.md)

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
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_cost_summary**
> ClusterCostSummaryResponse get_cluster_cost_summary(cluster_name, window=window)

Get cluster cost summary

Aggregates provider-neutral, closed hourly metering rollups for a cluster. Missing and gap windows are explicit and are never rendered as zero spend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_cost_summary_response import ClusterCostSummaryResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    window = '24h' # str | Window duration (for example 24h, 7d, 30d) (optional) (default to '24h')

    try:
        # Get cluster cost summary
        api_response = api_instance.get_cluster_cost_summary(cluster_name, window=window)
        print("The response of ClustersApi->get_cluster_cost_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_cost_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **window** | **str**| Window duration (for example 24h, 7d, 30d) | [optional] [default to &#39;24h&#39;]

### Return type

[**ClusterCostSummaryResponse**](ClusterCostSummaryResponse.md)

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
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_kubeconfig**
> KubeconfigResponse get_cluster_kubeconfig(cluster_name)

Get cluster kubeconfig

Returns the kubeconfig for the cluster. Returns 202 Accepted while generation is in progress (self-managed clusters), or 200 with the config when ready.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.kubeconfig_response import KubeconfigResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get cluster kubeconfig
        api_response = api_instance.get_cluster_kubeconfig(cluster_name)
        print("The response of ClustersApi->get_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_kubeconfig: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**KubeconfigResponse**](KubeconfigResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubeconfig retrieved successfully |  -  |
**202** | Kubeconfig generation is in progress; poll again |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to access kubeconfig |  -  |
**404** | Cluster not found |  -  |
**409** | Cluster is not ready yet (reason ClusterNotReady); try again once it reads Ready |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metrics_allocation**
> ClusterMetricsAllocationResponse get_cluster_metrics_allocation(cluster_name, window=window, sort_by=sort_by, sort_order=sort_order, search=search, limit=limit, offset=offset)

Get cluster metrics allocation

Lists every platform-managed application on the cluster with its resource usage averaged over the window, so heavy workloads surface without naming one. An application with no stored sample is absent rather than zero.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_metrics_allocation_response import ClusterMetricsAllocationResponse
from astropulse._generated.models.sort_order import SortOrder
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    window = '1h' # str | Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours (optional) (default to '1h')
    sort_by = astropulse._generated.ClusterMetricsSortField() # ClusterMetricsSortField | What the page is ordered by (optional)
    sort_order = astropulse._generated.SortOrder() # SortOrder | Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last (optional)
    search = 'search_example' # str | Case-insensitive application name search (optional)
    limit = 50 # int | Page size from 1 through 200 (optional) (default to 50)
    offset = 0 # int | Page offset (optional) (default to 0)

    try:
        # Get cluster metrics allocation
        api_response = api_instance.get_cluster_metrics_allocation(cluster_name, window=window, sort_by=sort_by, sort_order=sort_order, search=search, limit=limit, offset=offset)
        print("The response of ClustersApi->get_cluster_metrics_allocation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_metrics_allocation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **window** | **str**| Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours | [optional] [default to &#39;1h&#39;]
 **sort_by** | [**ClusterMetricsSortField**](.md)| What the page is ordered by | [optional] 
 **sort_order** | [**SortOrder**](.md)| Sort direction, Ascending by name and Descending otherwise when omitted; missing values always remain last | [optional] 
 **search** | **str**| Case-insensitive application name search | [optional] 
 **limit** | **int**| Page size from 1 through 200 | [optional] [default to 50]
 **offset** | **int**| Page offset | [optional] [default to 0]

### Return type

[**ClusterMetricsAllocationResponse**](ClusterMetricsAllocationResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_metrics_summary**
> ClusterMetricsSummaryResponse get_cluster_metrics_summary(cluster_name, window=window)

Get cluster metrics summary

Cluster-wide totals and coverage: how many applications reported resource usage in the window, how many samples backed that, and whether every sample was complete. An application that reported nothing is not counted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_metrics_summary_response import ClusterMetricsSummaryResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    window = '1h' # str | Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours (optional) (default to '1h')

    try:
        # Get cluster metrics summary
        api_response = api_instance.get_cluster_metrics_summary(cluster_name, window=window)
        print("The response of ClustersApi->get_cluster_metrics_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_metrics_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **window** | **str**| Window duration (for example 15m, 1h, 24h); minutes-scale, not truncated to whole hours | [optional] [default to &#39;1h&#39;]

### Return type

[**ClusterMetricsSummaryResponse**](ClusterMetricsSummaryResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_progress**
> ClusterProgressResponse get_cluster_progress(cluster_name, operation_id=operation_id)

Get cluster progress

Returns progress details for the most recent or specified cluster operation. Pass operationId to target a specific operation.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_progress_response import ClusterProgressResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    operation_id = 'operation_id_example' # str | Operation ID to get progress for (optional) (optional)

    try:
        # Get cluster progress
        api_response = api_instance.get_cluster_progress(cluster_name, operation_id=operation_id)
        print("The response of ClustersApi->get_cluster_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **operation_id** | **str**| Operation ID to get progress for (optional) | [optional] 

### Return type

[**ClusterProgressResponse**](ClusterProgressResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster progress retrieved successfully |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view cluster progress |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_spec**
> K8sClusterManifestResponse get_cluster_spec(cluster_name)

Get cluster specification

Returns the manifest the cluster was created from, in the shape the create request takes. Credential values are never included.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.k8s_cluster_manifest_response import K8sClusterManifestResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get cluster specification
        api_response = api_instance.get_cluster_spec(cluster_name)
        print("The response of ClustersApi->get_cluster_spec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_spec: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**K8sClusterManifestResponse**](K8sClusterManifestResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster specification retrieved successfully |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view cluster specification |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_storage**
> ClusterStorageResponse get_cluster_storage(cluster_name)

Get a cluster's storage

Returns the storage classes the cluster offers, what each one provides, and the names bound to them. Classes are observed, never set here.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_storage_response import ClusterStorageResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Get a cluster's storage
        api_response = api_instance.get_cluster_storage(cluster_name)
        print("The response of ClustersApi->get_cluster_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->get_cluster_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

### Return type

[**ClusterStorageResponse**](ClusterStorageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view this cluster |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Storage state is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_cluster_agent_certificate**
> AgentCertificateBundleResponse issue_cluster_agent_certificate(cluster_name, agent_certificate_signing_request)

Sign a new certificate for a cluster's agent

Signs a new certificate for a cluster's AstroPulse agent from a certificate signing request for a key you made and keep, to write with that key to the agent's TLS Secret from a machine that can reach the cluster. The certificate carries the cluster's own identity, and once the agent connects with it the agent's previous certificate is no longer accepted. A registered cluster's agent can be issued one while the cluster is being registered or once it is registered; a provisioned cluster's once it is ready.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.agent_certificate_bundle_response import AgentCertificateBundleResponse
from astropulse._generated.models.agent_certificate_signing_request import AgentCertificateSigningRequest
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    agent_certificate_signing_request = astropulse._generated.AgentCertificateSigningRequest() # AgentCertificateSigningRequest | Signing request for the agent's key

    try:
        # Sign a new certificate for a cluster's agent
        api_response = api_instance.issue_cluster_agent_certificate(cluster_name, agent_certificate_signing_request)
        print("The response of ClustersApi->issue_cluster_agent_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->issue_cluster_agent_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **agent_certificate_signing_request** | [**AgentCertificateSigningRequest**](AgentCertificateSigningRequest.md)| Signing request for the agent&#39;s key | 

### Return type

[**AgentCertificateBundleResponse**](AgentCertificateBundleResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate signed |  -  |
**400** | Invalid cluster name or certificate signing request |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to manage the cluster&#39;s agent |  -  |
**404** | Cluster not found |  -  |
**409** | The cluster is not being registered, registered or ready |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_operations**
> ClusterProgressPageResponse list_cluster_operations(cluster_name, limit=limit, page_token=page_token, provider=provider, provisioner_type=provisioner_type, account_id=account_id, region=region)

Get cluster operation history

Returns historical operations for the cluster. If the cluster record no longer exists, pass provider, provisionerType, accountId, and region as query parameters to look up by storage location.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_progress_page_response import ClusterProgressPageResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    limit = 100 # int | Maximum number of operations to return (optional) (default to 100)
    page_token = 'page_token_example' # str | Page token for pagination (optional)
    provider = 'provider_example' # str | Cloud provider: aws, gcp, azure (required if cluster not found) (optional)
    provisioner_type = 'provisioner_type_example' # str | Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found) (optional)
    account_id = 'account_id_example' # str | Cloud account ID (required if cluster not found) (optional)
    region = 'region_example' # str | Cloud region (required if cluster not found) (optional)

    try:
        # Get cluster operation history
        api_response = api_instance.list_cluster_operations(cluster_name, limit=limit, page_token=page_token, provider=provider, provisioner_type=provisioner_type, account_id=account_id, region=region)
        print("The response of ClustersApi->list_cluster_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_cluster_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **limit** | **int**| Maximum number of operations to return | [optional] [default to 100]
 **page_token** | **str**| Page token for pagination | [optional] 
 **provider** | **str**| Cloud provider: aws, gcp, azure (required if cluster not found) | [optional] 
 **provisioner_type** | **str**| Provisioner type: selfmanaged, eks, gke, aks (required if cluster not found) | [optional] 
 **account_id** | **str**| Cloud account ID (required if cluster not found) | [optional] 
 **region** | **str**| Cloud region (required if cluster not found) | [optional] 

### Return type

[**ClusterProgressPageResponse**](ClusterProgressPageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation history retrieved successfully |  -  |
**400** | Invalid cluster ID or missing location parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view operation history |  -  |
**404** | Cluster not found and no location parameters provided |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_progress**
> ClusterProgressPageResponse list_cluster_progress(operation_type=operation_type, status=status, limit=limit, page_token=page_token)

List cluster progress for all clusters

Returns paginated progress records across all clusters in the organization, filterable by operation type and status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_progress_page_response import ClusterProgressPageResponse
from astropulse._generated.models.operation_status import OperationStatus
from astropulse._generated.models.operation_type import OperationType
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    operation_type = astropulse._generated.OperationType() # OperationType | Only operations of this type (optional)
    status = astropulse._generated.OperationStatus() # OperationStatus | Only operations with this status (optional)
    limit = 56 # int | Limit number of results (optional)
    page_token = 'page_token_example' # str | Page token for pagination (optional)

    try:
        # List cluster progress for all clusters
        api_response = api_instance.list_cluster_progress(operation_type=operation_type, status=status, limit=limit, page_token=page_token)
        print("The response of ClustersApi->list_cluster_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_cluster_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_type** | [**OperationType**](.md)| Only operations of this type | [optional] 
 **status** | [**OperationStatus**](.md)| Only operations with this status | [optional] 
 **limit** | **int**| Limit number of results | [optional] 
 **page_token** | **str**| Page token for pagination | [optional] 

### Return type

[**ClusterProgressPageResponse**](ClusterProgressPageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster progress list retrieved successfully |  -  |
**400** | An unknown operation type or status |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view cluster progress |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> K8sClusterListResponse list_clusters(provider_id=provider_id)

List all clusters for your organization

Retrieves a list of all Kubernetes clusters managed by AstroPulse

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.k8s_cluster_list_response import K8sClusterListResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    provider_id = 'provider_id_example' # str | Cloud Provider ID (e.g., aws, gcp) (optional)

    try:
        # List all clusters for your organization
        api_response = api_instance.list_clusters(provider_id=provider_id)
        print("The response of ClustersApi->list_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->list_clusters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| Cloud Provider ID (e.g., aws, gcp) | [optional] 

### Return type

[**K8sClusterListResponse**](K8sClusterListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of clusters retrieved successfully |  -  |
**400** | Invalid provider ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to view clusters |  -  |
**404** | Organization not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_cluster_agent**
> ClusterRegistrationResponse register_cluster_agent(cluster_name, k8s_cluster_registration)

Register an agent on a cluster

Registers a Kubernetes cluster through the AstroPulse agent. Works with any cluster type (EKS, GKE, AKS, on-premises).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_registration_response import ClusterRegistrationResponse
from astropulse._generated.models.k8s_cluster_registration import K8sClusterRegistration
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    k8s_cluster_registration = astropulse._generated.K8sClusterRegistration() # K8sClusterRegistration | Cluster registration configuration

    try:
        # Register an agent on a cluster
        api_response = api_instance.register_cluster_agent(cluster_name, k8s_cluster_registration)
        print("The response of ClustersApi->register_cluster_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->register_cluster_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **k8s_cluster_registration** | [**K8sClusterRegistration**](K8sClusterRegistration.md)| Cluster registration configuration | 

### Return type

[**ClusterRegistrationResponse**](ClusterRegistrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Registration initiated |  -  |
**400** | Invalid registration parameters |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to register clusters |  -  |
**409** | Cluster with same name already exists |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_cluster_approval**
> ClusterApprovalResponse request_cluster_approval(cluster_name, org_id, token, action)

Request cluster operation approval

Submits an approve or reject decision for a pending cluster operation. Requires a signed-in organization owner.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_approval_action import ClusterApprovalAction
from astropulse._generated.models.cluster_approval_response import ClusterApprovalResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Name of the cluster
    org_id = 'org_id_example' # str | Organization ID
    token = 'token_example' # str | Approval token
    action = astropulse._generated.ClusterApprovalAction() # ClusterApprovalAction | The decision on the cluster

    try:
        # Request cluster operation approval
        api_response = api_instance.request_cluster_approval(cluster_name, org_id, token, action)
        print("The response of ClustersApi->request_cluster_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->request_cluster_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Name of the cluster | 
 **org_id** | **str**| Organization ID | 
 **token** | **str**| Approval token | 
 **action** | [**ClusterApprovalAction**](.md)| The decision on the cluster | 

### Return type

[**ClusterApprovalResponse**](ClusterApprovalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The decision and what it did |  -  |
**400** | Invalid request parameters |  -  |
**401** | Not authenticated |  -  |
**403** | Caller is not the org owner |  -  |
**404** | Cluster not found |  -  |
**409** | Approval request already processed |  -  |
**422** | Invalid approval parameters |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_cluster_progress**
> StreamTicket stream_cluster_progress(cluster_name, operation_id=operation_id, accept=accept, x_astro_stream_origin=x_astro_stream_origin)

Stream cluster progress via WebSocket

Opens a WebSocket connection and streams live progress events for an in-progress cluster operation. Use operationId to target a specific run.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.stream_ticket import StreamTicket
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    operation_id = 'operation_id_example' # str | Operation ID to stream progress for (optional) (optional)
    accept = 'accept_example' # str | Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it (optional)
    x_astro_stream_origin = 'x_astro_stream_origin_example' # str | With a ticket request: the browser origin the stream will be opened from (optional)

    try:
        # Stream cluster progress via WebSocket
        api_response = api_instance.stream_cluster_progress(cluster_name, operation_id=operation_id, accept=accept, x_astro_stream_origin=x_astro_stream_origin)
        print("The response of ClustersApi->stream_cluster_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->stream_cluster_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **operation_id** | **str**| Operation ID to stream progress for (optional) | [optional] 
 **accept** | **str**| Send application/vnd.astropulse.stream-ticket+json with a bearer token to get a single-use ticket for this stream instead of opening it | [optional] 
 **x_astro_stream_origin** | **str**| With a ticket request: the browser origin the stream will be opened from | [optional] 

### Return type

[**StreamTicket**](StreamTicket.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols - WebSocket connection established |  -  |
**200** | Ticket request: a single-use ticket for this stream, valid for at most 30 seconds |  -  |
**400** | Invalid cluster ID or WebSocket upgrade failed |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to stream cluster progress |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Streams cannot be opened from the console right now; try again |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cluster_auth**
> StringResponse sync_cluster_auth(cluster_name)

Sync cluster authentication configuration

Re-synchronizes internal authentication configuration for a specific cluster to fix missing certificates or connectivity issues

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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name

    try:
        # Sync cluster authentication configuration
        api_response = api_instance.sync_cluster_auth(cluster_name)
        print("The response of ClustersApi->sync_cluster_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->sync_cluster_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 

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
**200** | Cluster authentication sync initiated successfully |  -  |
**400** | Invalid cluster ID |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to sync cluster authentication |  -  |
**404** | Cluster not found |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_cluster_agent**
> ClusterOperationResultResponse unregister_cluster_agent(cluster_name, agent_only=agent_only, delete_apps=delete_apps)

Unregister an agent from a cluster

Removes the agent from a registered cluster and the cluster from AstroPulse. With agent-only=true, only the agent is disconnected and the cluster's record is kept.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_operation_result_response import ClusterOperationResultResponse
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    agent_only = False # bool | Disconnect only the agent and keep the cluster's record (optional) (default to False)
    delete_apps = False # bool | Delete the applications AstroPulse deployed to the cluster (default: keep them running) (optional) (default to False)

    try:
        # Unregister an agent from a cluster
        api_response = api_instance.unregister_cluster_agent(cluster_name, agent_only=agent_only, delete_apps=delete_apps)
        print("The response of ClustersApi->unregister_cluster_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->unregister_cluster_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **agent_only** | **bool**| Disconnect only the agent and keep the cluster&#39;s record | [optional] [default to False]
 **delete_apps** | **bool**| Delete the applications AstroPulse deployed to the cluster (default: keep them running) | [optional] [default to False]

### Return type

[**ClusterOperationResultResponse**](ClusterOperationResultResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agent unregistered |  -  |
**400** | The cluster was created by AstroPulse; delete it instead |  -  |
**401** | Missing or invalid API key |  -  |
**403** | Insufficient permissions |  -  |
**404** | Cluster not found |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> ClusterUpdateDryRun update_cluster(cluster_name, k8s_cluster_update)

Update cluster configuration

Updates a cluster's Kubernetes version, node groups or tags; AstroPulse picks the update strategy from the provider and the change. Dry-run and report requests return 200 — read validationPassed and preflightChecks; checks that did not finish are named in upgradePlan.unfinishedChecks.
The body is decoded strictly: a field the request type does not have is refused with 400, naming it in details.field.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_update_dry_run import ClusterUpdateDryRun
from astropulse._generated.models.k8s_cluster_update import K8sClusterUpdate
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    k8s_cluster_update = astropulse._generated.K8sClusterUpdate() # K8sClusterUpdate | Cluster update configuration

    try:
        # Update cluster configuration
        api_response = api_instance.update_cluster(cluster_name, k8s_cluster_update)
        print("The response of ClustersApi->update_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **k8s_cluster_update** | [**K8sClusterUpdate**](K8sClusterUpdate.md)| Cluster update configuration | 

### Return type

[**ClusterUpdateDryRun**](ClusterUpdateDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dry-run validation completed or readiness report generated. An update that changes nothing, or only stores credentials, also answers 200 with a ClusterUpdate whose result is Unchanged or CredentialsStored |  -  |
**202** | Cluster update initiated successfully |  -  |
**400** | Invalid cluster configuration, a field the request type does not have (named in details.field), or cluster not in ready state |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to update clusters |  -  |
**404** | Cluster not found |  -  |
**409** | Cluster is not in a valid state for updates |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Service temporarily unavailable; retry after the Retry-After interval |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_storage**
> ClusterStorageResponse update_cluster_storage(cluster_name, set_cluster_storage_request)

Set a cluster's storage bindings

Replaces every storage binding on the cluster; bindings not listed are removed. Each binding names a storage class the cluster has. Storage classes cannot be created here.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import astropulse._generated
from astropulse._generated.models.cluster_storage_response import ClusterStorageResponse
from astropulse._generated.models.set_cluster_storage_request import SetClusterStorageRequest
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
    api_instance = astropulse._generated.ClustersApi(api_client)
    cluster_name = 'cluster_name_example' # str | Cluster name
    set_cluster_storage_request = astropulse._generated.SetClusterStorageRequest() # SetClusterStorageRequest | Storage bindings

    try:
        # Set a cluster's storage bindings
        api_response = api_instance.update_cluster_storage(cluster_name, set_cluster_storage_request)
        print("The response of ClustersApi->update_cluster_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClustersApi->update_cluster_storage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_name** | **str**| Cluster name | 
 **set_cluster_storage_request** | [**SetClusterStorageRequest**](SetClusterStorageRequest.md)| Storage bindings | 

### Return type

[**ClusterStorageResponse**](ClusterStorageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request or a binding names a class the cluster does not have |  -  |
**401** | Missing or invalid API key |  -  |
**403** | User does not have permission to change this cluster |  -  |
**404** | Cluster not found |  -  |
**409** | The cluster&#39;s storage has not been observed yet |  -  |
**429** | Rate limit exceeded |  -  |
**500** | Internal server error |  -  |
**503** | Storage state is temporarily unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


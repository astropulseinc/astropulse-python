"""
    AstroPulse Platform API

    The programmable production foundation for applications, AI workloads, and infrastructure products.  AstroPulse provides a unified control plane for composing cloud infrastructure, deploying workloads, and operating their production lifecycle. Provision and manage Kubernetes clusters, deploy applications and AI models, and manage networking, scaling, access, integrations, observability, cost visibility, and governance.  **Keep your product. Skip rebuilding the production layer.** AstroPulse manages the production machinery underneath your application, runtime, scheduler, inference system, or infrastructure product, while you retain ownership of the capabilities that make it different.  ## Base URL All public API endpoints are served over HTTPS at `https://api.astropulse.io` and versioned under `/api/v1`.  ## Working with AstroPulse The API follows the operational lifecycle of your infrastructure and workloads: - **Connect infrastructure:** Configure cloud accounts, discover regions, machine types, and accelerators, and provision or register Kubernetes clusters. - **Configure environments:** Manage cluster add-ons, application profiles, availability tiers, domains, and endpoint access policies. - **Deploy workloads:** Deploy applications and supported AI models, inspect their state, and discover their serving endpoints. - **Operate and recover:** Monitor deployment progress, manage supported lifecycle operations, inspect version history, plan rollbacks, and recover deployments. - **Observe and govern:** Inspect operational metrics, cost and usage data, activity, integrations, identities, permissions, and audit records.  Resources are organized by their role in the platform. Each operation defines its own parameters, request and response schemas, authentication requirements, and failure conditions.  ## Authentication AstroPulse supports API keys and short-lived bearer tokens. Each endpoint declares which authentication methods it accepts.  **API keys — recommended for automation** Send `X-Astro-API-Key: <key>`. For production automation, use an organization-owned service-account key. Service accounts are managed by organization administrators through the Service Accounts API and do not depend on an individual user's session.  Personal API keys are available under Organization settings > API Keys. API keys are scoped to one organization.  **Bearer tokens — interactive sessions** Send `Authorization: Bearer <jwt>`. These credentials are short-lived access tokens issued by the configured authentication provider.  To print an access token for a direct API request, run `astroctl auth login --print-access-token` (`-p`). A standard `astroctl auth login` stores the authenticated session without printing the token.  For unattended integrations, use API keys instead of interactive session tokens. Store all credentials securely and never expose them in repositories, client-side code, or logs.  ## SDKs and API clients The generated OpenAPI 3 specification is the public contract for AstroPulse REST API consumers and generated clients.  AstroPulse provides operation-specific Python and TypeScript SDK examples in this reference. Each generated SDK exposes resources through typed clients, with method names derived from stable API operation IDs.  **Python SDK:** Install using `pip install \"git+https://github.com/astropulseinc/astropulse-python\"`.  Common operations include `client.clusters.list_clusters()` and `client.applications.deploy_application(...)`. Consult the SDK's documentation for client initialization, authentication, and complete examples.  The same platform capabilities can be accessed through the REST API, supported SDKs, astroctl, and the AstroPulse Console. Refer to the documentation for the supported workflows of each interface.  **Application runtime endpoints:** Applications deployed through AstroPulse expose runtime endpoints separate from the platform control-plane API. Model deployments supporting the OpenAI API protocol can be called with an OpenAI-compatible client configured for the deployed endpoint and its access requirements.  ## Lifecycle and asynchronous operations Infrastructure provisioning, deployment, and certain lifecycle changes can execute asynchronously. An accepted request does not necessarily mean the underlying operation has completed.  Use the operation's response, resource status, and available progress streams to determine completion and inspect failures.  Supported application operations include version history, rollback, resume, and GitOps reconciliation. Rollback operations can provide dry-run plans so callers can inspect an eligible change before applying it.  Consult each operation for its specific state transitions, mutation semantics, retry behavior, and concurrency restrictions.  ## Observability and cost Supported resources expose deployment state, application and cluster metrics, cost and usage series, and operational diagnostics.  Metrics and cost data represent collected observations. Missing samples, incomplete coverage, and unavailable reporting intervals must not be interpreted as zero resource consumption or zero spend.  Use the coverage information, time windows, and aggregation intervals documented by each operation when processing telemetry and cost responses.  ## Real-time streaming Supported application endpoints provide real-time status, event, and log streams over WebSocket connections.  Streaming requests have different connection and authentication semantics from ordinary JSON requests. Supported browser workflows can obtain a short-lived, single-use stream ticket before establishing a WebSocket connection.  Stream tickets are valid for at most 30 seconds. Follow the individual endpoint's documented handshake, authentication, and error-handling requirements.  ## Response format Successful JSON API responses use the documented resource schema, commonly wrapped in an envelope with the result under `data` and optional `id`, `status`, and `message` fields.  Consumers must follow each endpoint's declared response type. Streaming connections and other specialized responses may have different transport semantics.  ## Errors and diagnostics API failures use a consistent JSON error structure containing: - `message`: Human-readable explanation. - `code`: Stable, machine-readable error identifier. - `status`: HTTP response status. - `traceId`: Diagnostic request trace identifier. - `details`: Optional structured error details.  **Branch on HTTP status and `code`, never on the wording of `message`.**  The `X-Trace-ID` response header exposes the request's diagnostic trace identifier. Include it when reporting failures. It is not a distributed tracing propagation header.  Common HTTP errors include: - `400 Bad Request`: Invalid input or request. - `401 Unauthorized`: Missing, invalid, expired, or revoked credentials. - `402 Payment Required`: Requested capability is unavailable under the current plan. - `403 Forbidden`: Insufficient permissions. - `404 Not Found`: Resource or route not found. - `405 Method Not Allowed`: Unsupported HTTP method for a route. - `409 Conflict`: Resource state or concurrent operation conflict. - `429 Too Many Requests`: Rate limit exceeded. - `500 Internal Server Error`: Unexpected server failure. - `503 Service Unavailable`: A required service is temporarily unavailable.  The applicable status codes and response schemas are documented for each operation.  ## Versioning and compatibility Public API versions are identified by the URL path, beginning with `/api/v1`. The generated specification's `info.version` identifies the AstroPulse build from which the document was generated.  Within an API version, backward-compatible evolution can introduce new endpoints, optional request fields, response properties, and values in extensible enumerations.  Clients should tolerate unknown response properties and supported enum extensions. Consumers must not depend on undocumented list ordering or human-readable error messages.  Breaking changes, including removing or renaming fields, changing documented field types, or making previously optional request fields mandatory, require compatibility review and an appropriate API version transition.  The generated OpenAPI specification is the authoritative contract for client generation and compatibility validation.  ## Rate limiting and retries AstroPulse applies layered request rate limits: - Global service-wide limits. - Per-IP limits. - Additional per-API-key limits. - Per-authenticated-principal limits where enabled.  Exceeding an applicable limit returns `429 Too Many Requests`. Respect the `Retry-After` response header and implement bounded exponential backoff with jitter.  Temporary service failures may return `503 Service Unavailable` with retry guidance. Retry state-changing operations only when their documented semantics make repetition safe.  Global and per-IP limits remain applicable regardless of the credential used. Rotating credentials does not bypass those limits.  ## Identity, governance, and audit AstroPulse organizes platform resources within organizations. Authentication, authorization, and applicable plan restrictions govern access to resource operations.  Mutating API requests and designated sensitive reads are recorded for auditability. Audit records capture available actor, organization, resource, action, outcome, and request context without storing request bodies or secrets.  Organization-owned service accounts provide dedicated automation identities, while API keys and user sessions retain their associated authentication and authorization boundaries.  ## Developer documentation This API reference defines the public platform contract. The [AstroPulse Documentation](https://astropulse.io/docs) provides guided workflows, platform concepts, SDK integration, CLI usage, and end-to-end examples.  API schemas and operation definitions are the source of truth for clients, developer tools, and authorized automation.

    The version of the OpenAPI document: v0.0.178
    Contact: contact@astropulse.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from astropulse._generated.models.audit_action import AuditAction
from astropulse._generated.models.audit_event_list_response import AuditEventListResponse
from astropulse._generated.models.audit_event_response import AuditEventResponse
from astropulse._generated.models.audit_event_type import AuditEventType
from astropulse._generated.models.audit_stats_response import AuditStatsResponse

from astropulse._generated.api_client import ApiClient, RequestSerialized
from astropulse._generated.api_response import ApiResponse
from astropulse._generated.rest import RESTResponseType


class AuditApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def export_audit_events(
        self,
        format: Annotated[Optional[Any], Field(description="The file format; CSV when omitted")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> str:
        """Download audit events as a file

        Downloads every matching event as a file, CSV or JSON: the body is the file itself, not the usual envelope. To read them as data, list them instead. Enterprise plan. Organization admins and owners export every event; other members only their own. Each event names the actor who performed it. At most 50000 events are exported; when more match, the newest 50000 are returned and X-Audit-Export-Truncated is true.

        :param format: The file format; CSV when omitted
        :type format: AuditExportFormat
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_audit_events_serialize(
            format=format,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def export_audit_events_with_http_info(
        self,
        format: Annotated[Optional[Any], Field(description="The file format; CSV when omitted")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[str]:
        """Download audit events as a file

        Downloads every matching event as a file, CSV or JSON: the body is the file itself, not the usual envelope. To read them as data, list them instead. Enterprise plan. Organization admins and owners export every event; other members only their own. Each event names the actor who performed it. At most 50000 events are exported; when more match, the newest 50000 are returned and X-Audit-Export-Truncated is true.

        :param format: The file format; CSV when omitted
        :type format: AuditExportFormat
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_audit_events_serialize(
            format=format,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def export_audit_events_without_preload_content(
        self,
        format: Annotated[Optional[Any], Field(description="The file format; CSV when omitted")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Download audit events as a file

        Downloads every matching event as a file, CSV or JSON: the body is the file itself, not the usual envelope. To read them as data, list them instead. Enterprise plan. Organization admins and owners export every event; other members only their own. Each event names the actor who performed it. At most 50000 events are exported; when more match, the newest 50000 are returned and X-Audit-Export-Truncated is true.

        :param format: The file format; CSV when omitted
        :type format: AuditExportFormat
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._export_audit_events_serialize(
            format=format,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _export_audit_events_serialize(
        self,
        format,
        event_type,
        action,
        user_id,
        resource_id,
        dry_run,
        include_dry_runs,
        include_reads,
        q,
        start_date,
        end_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if format is not None:
            
            _query_params.append(('format', format.value))
            
        if event_type is not None:
            
            _query_params.append(('eventType', event_type.value))
            
        if action is not None:
            
            _query_params.append(('action', action.value))
            
        if user_id is not None:
            
            _query_params.append(('userId', user_id))
            
        if resource_id is not None:
            
            _query_params.append(('resourceId', resource_id))
            
        if dry_run is not None:
            
            _query_params.append(('dryRun', dry_run))
            
        if include_dry_runs is not None:
            
            _query_params.append(('includeDryRuns', include_dry_runs))
            
        if include_reads is not None:
            
            _query_params.append(('includeReads', include_reads))
            
        if q is not None:
            
            _query_params.append(('q', q))
            
        if start_date is not None:
            
            _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            
            _query_params.append(('endDate', end_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'text/csv'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/audit/events/export',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_audit_event(
        self,
        event_id: Annotated[StrictStr, Field(description="Event ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AuditEventResponse:
        """Get audit event details

        Get one audit event by ID, at any age. Enterprise plan. Below admin, only the caller's own events; anyone else's answers not found.

        :param event_id: Event ID (required)
        :type event_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_event_serialize(
            event_id=event_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_audit_event_with_http_info(
        self,
        event_id: Annotated[StrictStr, Field(description="Event ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AuditEventResponse]:
        """Get audit event details

        Get one audit event by ID, at any age. Enterprise plan. Below admin, only the caller's own events; anyone else's answers not found.

        :param event_id: Event ID (required)
        :type event_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_event_serialize(
            event_id=event_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_audit_event_without_preload_content(
        self,
        event_id: Annotated[StrictStr, Field(description="Event ID")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get audit event details

        Get one audit event by ID, at any age. Enterprise plan. Below admin, only the caller's own events; anyone else's answers not found.

        :param event_id: Event ID (required)
        :type event_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_event_serialize(
            event_id=event_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_audit_event_serialize(
        self,
        event_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if event_id is not None:
            _path_params['eventId'] = event_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/audit/events/{eventId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_audit_stats(
        self,
        period: Annotated[Optional[StrictStr], Field(description="The period the statistics cover: 7d, 30d or 90d")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true also counts dry runs; by default only real changes are counted")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true also counts recorded reads of sensitive data")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AuditStatsResponse:
        """Get audit statistics for an organization

        Get audit statistics and analytics for an organization. Requires enterprise plan and admin role.

        :param period: The period the statistics cover: 7d, 30d or 90d
        :type period: str
        :param include_dry_runs: true also counts dry runs; by default only real changes are counted
        :type include_dry_runs: bool
        :param include_reads: true also counts recorded reads of sensitive data
        :type include_reads: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_stats_serialize(
            period=period,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditStatsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_audit_stats_with_http_info(
        self,
        period: Annotated[Optional[StrictStr], Field(description="The period the statistics cover: 7d, 30d or 90d")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true also counts dry runs; by default only real changes are counted")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true also counts recorded reads of sensitive data")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AuditStatsResponse]:
        """Get audit statistics for an organization

        Get audit statistics and analytics for an organization. Requires enterprise plan and admin role.

        :param period: The period the statistics cover: 7d, 30d or 90d
        :type period: str
        :param include_dry_runs: true also counts dry runs; by default only real changes are counted
        :type include_dry_runs: bool
        :param include_reads: true also counts recorded reads of sensitive data
        :type include_reads: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_stats_serialize(
            period=period,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditStatsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_audit_stats_without_preload_content(
        self,
        period: Annotated[Optional[StrictStr], Field(description="The period the statistics cover: 7d, 30d or 90d")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true also counts dry runs; by default only real changes are counted")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true also counts recorded reads of sensitive data")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get audit statistics for an organization

        Get audit statistics and analytics for an organization. Requires enterprise plan and admin role.

        :param period: The period the statistics cover: 7d, 30d or 90d
        :type period: str
        :param include_dry_runs: true also counts dry runs; by default only real changes are counted
        :type include_dry_runs: bool
        :param include_reads: true also counts recorded reads of sensitive data
        :type include_reads: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_audit_stats_serialize(
            period=period,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditStatsResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_audit_stats_serialize(
        self,
        period,
        include_dry_runs,
        include_reads,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if period is not None:
            
            _query_params.append(('period', period))
            
        if include_dry_runs is not None:
            
            _query_params.append(('includeDryRuns', include_dry_runs))
            
        if include_reads is not None:
            
            _query_params.append(('includeReads', include_reads))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/audit/stats',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_audit_events(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 100; overrides pageSize")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number (default: 1). Prefer pageToken.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page (default: 50, max: 100). Prefer limit.")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> AuditEventListResponse:
        """List audit events for an organization

        List audit events with filtering and pagination, newest first; dry runs and reads only when asked for. Enterprise plan. Organization admins and owners see every event; other members see only their own. With no dates the last 30 days are listed.

        :param limit: Page size from 1 through 100; overrides pageSize
        :type limit: int
        :param page_token: Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored
        :type page_token: str
        :param page: Page number (default: 1). Prefer pageToken.
        :type page: int
        :param page_size: Items per page (default: 50, max: 100). Prefer limit.
        :type page_size: int
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_audit_events_serialize(
            limit=limit,
            page_token=page_token,
            page=page,
            page_size=page_size,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_audit_events_with_http_info(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 100; overrides pageSize")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number (default: 1). Prefer pageToken.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page (default: 50, max: 100). Prefer limit.")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[AuditEventListResponse]:
        """List audit events for an organization

        List audit events with filtering and pagination, newest first; dry runs and reads only when asked for. Enterprise plan. Organization admins and owners see every event; other members see only their own. With no dates the last 30 days are listed.

        :param limit: Page size from 1 through 100; overrides pageSize
        :type limit: int
        :param page_token: Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored
        :type page_token: str
        :param page: Page number (default: 1). Prefer pageToken.
        :type page: int
        :param page_size: Items per page (default: 50, max: 100). Prefer limit.
        :type page_size: int
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_audit_events_serialize(
            limit=limit,
            page_token=page_token,
            page=page,
            page_size=page_size,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_audit_events_without_preload_content(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="Page size from 1 through 100; overrides pageSize")] = None,
        page_token: Annotated[Optional[StrictStr], Field(description="Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Page number (default: 1). Prefer pageToken.")] = None,
        page_size: Annotated[Optional[StrictInt], Field(description="Items per page (default: 50, max: 100). Prefer limit.")] = None,
        event_type: Annotated[Optional[AuditEventType], Field(description="Only events of this type")] = None,
        action: Annotated[Optional[AuditAction], Field(description="Only events with this action")] = None,
        user_id: Annotated[Optional[StrictStr], Field(description="Filter by user ID")] = None,
        resource_id: Annotated[Optional[StrictStr], Field(description="Only events on this resource ID (exact match)")] = None,
        dry_run: Annotated[Optional[StrictBool], Field(description="true lists only dry runs, requests that checked a change and made none")] = None,
        include_dry_runs: Annotated[Optional[StrictBool], Field(description="true lists dry runs alongside real changes; without it or dryRun, only real changes are listed")] = None,
        include_reads: Annotated[Optional[StrictBool], Field(description="true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read")] = None,
        q: Annotated[Optional[StrictStr], Field(description="Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address")] = None,
        start_date: Annotated[Optional[StrictStr], Field(description="Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.")] = None,
        end_date: Annotated[Optional[StrictStr], Field(description="End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List audit events for an organization

        List audit events with filtering and pagination, newest first; dry runs and reads only when asked for. Enterprise plan. Organization admins and owners see every event; other members see only their own. With no dates the last 30 days are listed.

        :param limit: Page size from 1 through 100; overrides pageSize
        :type limit: int
        :param page_token: Opaque continuation token from nextPageToken; it pins the original filters, so filter parameters sent with it are ignored
        :type page_token: str
        :param page: Page number (default: 1). Prefer pageToken.
        :type page: int
        :param page_size: Items per page (default: 50, max: 100). Prefer limit.
        :type page_size: int
        :param event_type: Only events of this type
        :type event_type: AuditEventType
        :param action: Only events with this action
        :type action: AuditAction
        :param user_id: Filter by user ID
        :type user_id: str
        :param resource_id: Only events on this resource ID (exact match)
        :type resource_id: str
        :param dry_run: true lists only dry runs, requests that checked a change and made none
        :type dry_run: bool
        :param include_dry_runs: true lists dry runs alongside real changes; without it or dryRun, only real changes are listed
        :type include_dry_runs: bool
        :param include_reads: true lists recorded reads of sensitive data, such as of this log; without it, reads are listed only when action is Read
        :type include_reads: bool
        :param q: Case-insensitive text search over action, resource, resource ID, actor name and email, source and IP address
        :type q: str
        :param start_date: Start of the range: an instant (2024-01-15T10:30:00Z) or a date (2024-01-15, from its start, UTC). Alone, the range runs to now.
        :type start_date: str
        :param end_date: End of the range: an instant (2024-01-16T23:59:59Z) or a date (2024-01-16, through its end, UTC). Alone, the range reaches back 30 days.
        :type end_date: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_audit_events_serialize(
            limit=limit,
            page_token=page_token,
            page=page,
            page_size=page_size,
            event_type=event_type,
            action=action,
            user_id=user_id,
            resource_id=resource_id,
            dry_run=dry_run,
            include_dry_runs=include_dry_runs,
            include_reads=include_reads,
            q=q,
            start_date=start_date,
            end_date=end_date,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AuditEventListResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '429': "ErrorResponse",
            '500': "ErrorResponse",
            '503': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_audit_events_serialize(
        self,
        limit,
        page_token,
        page,
        page_size,
        event_type,
        action,
        user_id,
        resource_id,
        dry_run,
        include_dry_runs,
        include_reads,
        q,
        start_date,
        end_date,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if page_token is not None:
            
            _query_params.append(('pageToken', page_token))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if event_type is not None:
            
            _query_params.append(('eventType', event_type.value))
            
        if action is not None:
            
            _query_params.append(('action', action.value))
            
        if user_id is not None:
            
            _query_params.append(('userId', user_id))
            
        if resource_id is not None:
            
            _query_params.append(('resourceId', resource_id))
            
        if dry_run is not None:
            
            _query_params.append(('dryRun', dry_run))
            
        if include_dry_runs is not None:
            
            _query_params.append(('includeDryRuns', include_dry_runs))
            
        if include_reads is not None:
            
            _query_params.append(('includeReads', include_reads))
            
        if q is not None:
            
            _query_params.append(('q', q))
            
        if start_date is not None:
            
            _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            
            _query_params.append(('endDate', end_date))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'ApiKeyAuth', 
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/audit/events',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )



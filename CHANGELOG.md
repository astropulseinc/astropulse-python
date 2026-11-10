# Changelog

All notable changes to this package are recorded here. It follows
[semantic versioning](https://semver.org), independently of the API version: an additive API
change is a minor release, and anything that breaks a caller of this package is a major one.

## Unreleased

First release.

- A generated client for the whole AstroPulse Platform API: applications, models, clusters,
  add-ons, domains, cloud accounts, access policies, integrations, API keys, organizations and
  audit.
- `Client`, which reads `ASTROPULSE_API_KEY`, sets a deadline on every request, and retries
  `429` and `5xx` responses (never a `POST`) honouring `Retry-After`.
- Application and cluster methods take the resource's name (`app_name`, `cluster_name`),
  which is what every application and cluster route is keyed by.
- `Client.wait_until_serving`, which blocks until an application's latest revision is serving
  and raises `DeploymentFailed` or `WaitTimeout` otherwise.
- Typed errors: one exception per HTTP status, each carrying the API's error `code` and
  `trace_id`.
- A cluster read lists its installed add-ons with each one's version and status
  (`K8sCluster.addons`).
- Node groups can run on an EC2 Capacity Block for ML (`instanceType: capacityBlock`), and
  report the block's phase and end time.
- Application logs can be read over a bounded window (`since`, `sinceTime`), filtered to errors
  or warnings with context, and include the previous container after a crash.
- Runnable examples for deploying a model, calling it, reading its metrics, connecting Hugging
  Face and listing clusters.
- Every state code a read returns has its display text beside it (`status_label`, `state_label`,
  `phase_label`, `connectivity_label`, `release_channel_label`, `overall_status_label`,
  `rollback_state_label`), so a client shows the platform's words instead of mapping codes itself.
- An add-on read reports how it runs (`resilience`), health checks that are still starting
  (`pending`), and its release and version history.
- A cluster update can apply named node groups again even when they are unchanged
  (`UpdateConfig.reapply`); the answer says so with the notice `CLUSTER_UPDATE_REAPPLIES`.
- An application read names a version that was applied but has not finished deploying
  (`pending_version`).
- An add-on route for an add-on the cluster does not have answers with the notice
  `ADDON_NOT_INSTALLED` and a step that installs it, in place of a bare not-found. Cost reads
  on a cluster without cost visibility carry the same notice.
- Cluster, application and add-on cost reads explain how their figures are priced where they
  are not what they seem (`pricing_notes`).
- An add-on catalog entry lists the versions that can be installed on the cluster
  (`installable_versions`), and each setting says its default, its bounds (`minimum`,
  `maximum`, `max_items`) and the form its value takes (`format`).
- The audit reads document a `503` answer for when audit storage is temporarily unavailable.
- An apply whose value is the `***REDACTED***` placeholder a read returns is refused, naming the
  field.
- An enum value the API adds later no longer breaks a response. A value an enum does not list
  parses to a member whose `value` is the string received, equal to no listed member, and is
  sent back unchanged; a string field documented with a fixed set of values keeps whatever
  string the API returns. Branch on the members you know (`is` or `match`) and treat anything
  else as unrecognised.
- Organization service accounts (`Client.service_accounts`): organization-owned keys for CI and
  long-running integrations.

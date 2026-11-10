# Security

## Reporting a vulnerability

Please report security issues privately to **contact@astropulse.io**, or through this
repository's private vulnerability reporting on GitHub. Do not open a public issue.

Include what you found, how to reproduce it, and the impact you believe it has. We will
acknowledge your report and keep you updated while we work on a fix.

## Handling credentials

This SDK reads your API key from `ASTROPULSE_API_KEY` so it never has to appear in source.
A key carries your organization's access: treat it like a password, keep it out of version
control and CI logs, and revoke it in the console under **Settings → API Keys** if it leaks.

Errors raised by this SDK carry a `trace_id`. It is safe to paste into a bug report — it
identifies the request, not the caller's credentials.

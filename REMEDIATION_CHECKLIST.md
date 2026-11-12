# Secure Web Application Remediation Checklist

## Input and database
- [ ] Use parameterized queries for all database access.
- [ ] Avoid building SQL/OS commands with string concatenation.
- [ ] Validate type, length, range, and format on the server.
- [ ] Use a database account with only required permissions.

## Output and browser protections
- [ ] Use context-aware output encoding.
- [ ] Keep template auto-escaping enabled.
- [ ] Avoid unsafe DOM sinks such as `innerHTML` for untrusted data.
- [ ] Set a restrictive Content Security Policy and test compatibility.
- [ ] Set `X-Content-Type-Options: nosniff`, frame protections, and a suitable Referrer-Policy.

## Authentication and sessions
- [ ] Store passwords with Argon2id, bcrypt, or scrypt using a maintained library.
- [ ] Enable MFA for privileged or sensitive accounts.
- [ ] Rate-limit login and recovery endpoints.
- [ ] Rotate session identifiers after authentication and privilege changes.
- [ ] Set Secure, HttpOnly, and appropriate SameSite cookie attributes.
- [ ] Enforce session expiry and server-side logout.
- [ ] Add CSRF protection to state-changing requests.

## Authorization
- [ ] Deny by default.
- [ ] Check permissions on every request and every object.
- [ ] Test horizontal access (user-to-user) and vertical access (user-to-admin).
- [ ] Never rely on hidden buttons or client-side checks as authorization.

## Deployment and dependencies
- [ ] Disable debug mode and remove demo accounts/routes.
- [ ] Store secrets outside source control.
- [ ] Enforce HTTPS and secure transport configuration.
- [ ] Pin and regularly update supported dependencies.
- [ ] Scan dependencies and build artifacts.
- [ ] Configure secure logging, alerting, backups, and incident response.
- [ ] Review SSRF risks for any server-side URL fetching feature.

## Release gate
- [ ] Automated tests pass.
- [ ] Manual tests are recorded with evidence.
- [ ] Findings are fixed and retested.
- [ ] Scope and authorization are documented.

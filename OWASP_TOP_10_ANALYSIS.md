# OWASP Top 10 Analysis (2021)

The OWASP Top 10 is an awareness document for major web application security risk categories. The lab demonstrates a subset safely on localhost; the remaining categories are explained conceptually and should be assessed only in an authorized environment.

| Rank | Category | Meaning | Example risk | Recommended control |
|---|---|---|---|---|
| A01 | Broken Access Control | Authorization rules are missing or bypassable. | A user changes `/profile/1` to `/profile/2` and reads another account. | Deny by default; check ownership/role on every request; test horizontal and vertical access. |
| A02 | Cryptographic Failures | Sensitive data is exposed due to weak or missing protection. | Passwords stored in plaintext or sensitive traffic sent over HTTP. | TLS; modern password hashing (Argon2id/bcrypt/scrypt); minimize stored sensitive data; manage keys safely. |
| A03 | Injection | Untrusted input changes the meaning of a query or command. | SQL is built by concatenating a search parameter. | Parameterized queries; safe APIs; input validation; least-privileged database account. |
| A04 | Insecure Design | Security is absent from design and threat modeling. | No abuse-case analysis, rate limits, or recovery controls. | Threat modeling; secure defaults; abuse-case requirements; security review. |
| A05 | Security Misconfiguration | Unsafe defaults or exposed configuration. | Debug mode, verbose errors, default credentials, missing headers. | Harden deployment; disable debug; remove defaults; set headers; patch dependencies. |
| A06 | Vulnerable and Outdated Components | Dependencies contain known vulnerabilities or are unsupported. | Old framework/plugin with a public exploit. | Inventory dependencies; pin and update versions; monitor advisories; remove unused packages. |
| A07 | Identification and Authentication Failures | Identity/session controls are weak. | Weak passwords, session fixation, no rate limiting, poor logout. | Secure password hashing; MFA; session rotation; secure cookie flags; rate limiting. |
| A08 | Software and Data Integrity Failures | Updates, builds, or serialized data are trusted without verification. | Untrusted plugin/update or unsafe deserialization. | Signed artifacts; trusted CI/CD; dependency integrity checks; safe serialization. |
| A09 | Security Logging and Monitoring Failures | Attacks are not detected or investigated. | Repeated login failures are not recorded or alerted. | Log security events without secrets; centralize logs; alert on suspicious patterns; protect log integrity. |
| A10 | Server-Side Request Forgery (SSRF) | Server fetches attacker-controlled destinations. | URL fetch feature can reach internal services. | Destination allowlists; block private/link-local ranges; validate redirects and DNS; use egress controls. |

## Lab mapping and observations

### A01 — Broken Access Control
- Vulnerable route: `/lab/vulnerable/profile/<id>` returns any profile based only on the supplied ID.
- Secure route: `/secure/profile/<id>` requires a session and checks owner-or-admin permission.
- Verification: unauthenticated request should return 401; Alice requesting admin's profile should return 403; admin may view Alice's profile.

### A03 — Injection
- Vulnerable route: `/lab/vulnerable/search?q=...` concatenates user input into SQL.
- Secure route: `/secure/search?q=...` uses a parameter placeholder and passes the value separately.
- Verification: compare source code and use harmless test strings in the local dummy database. Do not use payloads against external systems.

### A05 — Security Misconfiguration
- The app adds defensive response headers and disables Flask debug mode.
- The demo secret key and `SESSION_COOKIE_SECURE=False` are explicitly local-only settings. Production must load a strong secret from a secret manager/environment and set Secure cookies behind HTTPS.

### A07 — Identification and Authentication Failures
- The example uses Werkzeug password hashing, clears the session on successful login, and sets HttpOnly/SameSite cookie attributes.
- Production still needs MFA where appropriate, rate limiting, password reset controls, CSRF protection, session expiry, and secure HTTPS deployment.

### A02, A04, A06, A08, A09, A10
- These categories are covered by the controls in the table and the remediation checklist.
- They are not represented by exploit endpoints in this small lab. Do not claim they were dynamically exploited or verified.

## References
- OWASP Top 10: 2021 — https://owasp.org/Top10/
- OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/
- OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/
- PortSwigger Web Security Academy — https://portswigger.net/web-security

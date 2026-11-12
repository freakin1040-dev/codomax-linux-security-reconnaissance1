# Demo Walkthrough (5–8 minutes)

## Before the demo
1. Start the app using the README instructions.
2. Confirm the address is `http://127.0.0.1:5000`.
3. Use only the dummy accounts and local database.
4. Keep screenshots of your actual run; do not fabricate evidence.

## Part 1 — Explain the request/response lifecycle
- Browser sends an HTTP request to Flask.
- Flask route reads the request, applies validation and business rules, queries SQLite, then returns an HTTP response.
- Cookies may carry a session identifier; the server uses it to identify the logged-in user.
- Authentication establishes identity; authorization decides what that identity may access.

## Part 2 — SQL injection and parameterized queries
- Open `/lab/vulnerable/search?q=Pen` and `/secure/search?q=Pen`.
- Explain that the vulnerable route concatenates input into SQL.
- Show the secure route using `?` placeholder and a separate parameter tuple.
- Emphasize that parameterization keeps data separate from SQL instructions.

## Part 3 — XSS and output encoding
- Open `/lab/vulnerable/hello?name=Student` and `/secure/hello?name=Student`.
- Use a harmless HTML marker such as `<b>Student</b>` encoded in the URL to compare behavior.
- Explain that the secure Jinja template escapes user-provided content.
- Do not use real victims, external sites, or credential-stealing payloads.

## Part 4 — Broken access control
- First request `/lab/vulnerable/profile/2` to show that the demo route has no ownership check.
- Log in as `alice` using the demo credentials.
- Request `/secure/profile/2`; it should return 403 because Alice does not own that profile.
- Log in as `admin` and request `/secure/profile/1`; it should return 200.
- Explain the difference between authentication and authorization.

## Part 5 — Headers and tests
- Inspect response headers in browser developer tools or with curl.
- Run `pytest -q` and show the actual output.
- Explain that tests cover the secure examples only and are not a full penetration test.

## Closing
Summarize the three findings, their OWASP mapping, and the main fixes: parameterized SQL, output encoding, and server-side authorization.

# Burp Suite Community Edition — HTTP Inspection

**Purpose:** Burp Suite is an intercepting proxy used to inspect HTTP(S) requests and responses during authorised web testing.

## Install
Download Community Edition from: https://portswigger.net/burp/communitydownload

## Local exercise
1. Start the local app: `bash scripts/start_lab.sh`.
2. Open Burp and launch its built-in browser (recommended for a beginner).
3. Ensure proxy interception is enabled.
4. Visit `http://127.0.0.1:8000/` in the Burp browser.
5. Inspect the request method, path, headers, and response status.
6. Forward the request and confirm the page loads.
7. Repeat with `/hello`.
8. Turn interception off when finished.

Do not publish cookies, authorisation headers, tokens, or personal data in screenshots. The demo app is intentionally local and contains no real accounts.

## Evidence
Save a screenshot of a request/response and record:
- Request method and path
- Response status
- One non-sensitive header
- What the proxy helped you observe

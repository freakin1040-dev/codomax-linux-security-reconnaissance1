# Local Testing Guide

## 1. Browser and curl
Start the app on `127.0.0.1:5000`.

PowerShell examples:
```powershell
curl.exe -i "http://127.0.0.1:5000/secure/search?q=Pen"
curl.exe -i "http://127.0.0.1:5000/secure/hello?name=Student"
curl.exe -i "http://127.0.0.1:5000/secure/profile/1"
```
The final request should be unauthorized when no session is present.

## 2. Automated tests
```powershell
pytest -q
```
Record the actual result and date in `EVIDENCE_LOG.md`.

## 3. Burp Suite Community — local proxy workflow
1. Install Burp Suite Community from PortSwigger's official website.
2. Start Burp's temporary project and built-in browser, or configure a browser proxy to Burp.
3. Keep the target restricted to `http://127.0.0.1:5000`.
4. Browse the secure search and greeting routes.
5. In Proxy > HTTP history, select a request and inspect method, path, query parameters, headers, cookies, and response.
6. Send a request to Repeater and change only harmless values such as `q=Pen` to `q=Notebook`.
7. Capture a screenshot of the request/response and record the finding. Do not scan or attack unrelated hosts.

## 4. OWASP ZAP — local passive inspection
1. Install ZAP from the official OWASP ZAP website.
2. Open the local app in ZAP's browser or configure the browser to proxy through ZAP.
3. Set the context/target to `http://127.0.0.1:5000` only.
4. Browse the home, login, secure search, and secure greeting routes.
5. Review passive alerts and response headers.
6. If using any active scan, use only the intentionally local training application and confirm the scope first. Passive inspection is sufficient for this beginner lab.
7. Export a report and include the date, target, scan mode, and limitations.

## 5. Evidence and reporting
For each check, record:
- Date/time and app version
- Exact localhost URL
- Tool and configuration
- Expected result and actual result
- Screenshot filename
- Whether the issue was fixed and retested

A tool being installed is not evidence that a scan was performed. Do not state that Burp/ZAP found issues unless you actually ran them and retained the output.

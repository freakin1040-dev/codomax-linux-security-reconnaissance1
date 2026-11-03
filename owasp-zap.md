# OWASP ZAP — Local Web App Assessment

**Purpose:** OWASP ZAP is a web application security testing proxy/scanner. Scanner alerts are leads that require manual validation.

## Install
Download from: https://www.zaproxy.org/download/

## Local exercise
1. Start the local app: `bash scripts/start_lab.sh`.
2. Open ZAP.
3. Use Quick Start / Manual Explore and enter `http://127.0.0.1:8000`.
4. Browse the home and hello pages through ZAP.
5. Review the passive scan alerts.
6. If your course requires an active scan, run it only against this local demo target and only after reviewing the scope. Do not use the scan against public websites.
7. Export a report and save a screenshot under `evidence/zap/`.

The demo intentionally sends a basic HTTP response without several common security headers. A scanner may flag missing headers; this is a training observation, not proof of exploitable impact. Record only alerts actually shown by your ZAP version and validate them manually.

## Evidence
- ZAP version
- Target URL (`127.0.0.1:8000`)
- Scan type and date
- Actual alert names/risk levels
- Report file/screenshot
- Manual validation notes

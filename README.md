# Codomax Internship — Module 03: Web Application Security

**Duration:** Days 11–15  
**Level:** Intermediate  
**Lab:** Localhost-only Flask application demonstrating common web vulnerabilities and their mitigations.

## Repository contents
- `app.py` — intentionally vulnerable teaching routes and safer counterparts.
- `requirements.txt` — minimal dependencies.
- `tests/test_security.py` — automated checks for the safer routes.
- `docs/OWASP_TOP_10_ANALYSIS.md` — OWASP Top 10 (2021) analysis and examples.
- `docs/VULNERABILITY_REPORT.md` — findings, risk, evidence to capture, and fixes.
- `docs/REMEDIATION_CHECKLIST.md` — secure coding checklist.
- `docs/DEMO_WALKTHROUGH.md` — safe demo plan for localhost.
- `docs/TESTING_GUIDE.md` — browser, curl, Burp Suite Community, and OWASP ZAP steps.
- `docs/EVIDENCE_LOG.md` — fill-in evidence record; do not claim tests you did not run.

## Safety boundary
Run this lab only on your own computer using `127.0.0.1`. The `/lab/vulnerable/...` routes are deliberately insecure and exist only to teach recognition and remediation. Never deploy this application publicly, expose it to a network, or test systems without written authorization. Use dummy data only.

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

## Run automated tests
In a second terminal, activate the same virtual environment:
```powershell
pytest -q
```
The tests cover safer examples. A passing test suite is not a substitute for manual security testing.

## Lab credentials and sample data
The demo creates a local SQLite database automatically. It seeds two demo users:
- `alice` / `AliceDemo!23` (user)
- `admin` / `AdminDemo!23` (admin)

These are disposable demonstration credentials. Do not reuse them.

## Route map
| Route | Purpose |
|---|---|
| `/` | Home and safety notice |
| `/login` | Safer login example |
| `/logout` | Logout |
| `/lab/vulnerable/search?q=...` | SQL injection demonstration (local dummy DB only) |
| `/secure/search?q=...` | Parameterized SQL query |
| `/lab/vulnerable/hello?name=...` | Reflected XSS demonstration |
| `/secure/hello?name=...` | Context-escaped output |
| `/lab/vulnerable/profile/<id>` | IDOR demonstration |
| `/secure/profile/<id>` | Ownership/admin authorization check |
| `/health` | Local health check |

## Important implementation note
The vulnerable routes intentionally show unsafe patterns. Keep them confined to localhost and remove them before any deployment. The secure routes are teaching examples, not a complete production authentication system. Production applications also need HTTPS, a mature identity provider or hardened authentication, CSRF protection for state-changing requests, rate limiting, monitoring, secret management, and a formal threat model.

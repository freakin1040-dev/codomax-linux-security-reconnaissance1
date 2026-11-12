# Evidence Log — Complete During Actual Execution

> This is a blank evidence template. Fill it with real observations and screenshots after running the lab.

| ID | Date/time | Test | Tool | Expected result | Actual result | Screenshot / file |
|---|---|---|---|---|---|---|
| E-01 | | App starts on localhost | Browser | Home page loads | | |
| E-02 | | Secure SQL search | Browser/curl | Search returns matching dummy rows | | |
| E-03 | | Secure greeting escaping | Browser/pytest | HTML is escaped | | |
| E-04 | | Unauthenticated profile access | Browser | Secure route returns 401 | | |
| E-05 | | Cross-user profile access | Browser | Alice receives 403 for another user's profile | | |
| E-06 | | Automated tests | pytest | All included tests pass | | |
| E-07 | | HTTP headers inspection | Burp/ZAP/browser | Defensive headers visible | | |
| E-08 | | Passive scan | OWASP ZAP | Alerts reviewed and documented | | |
| E-09 | | Request inspection | Burp Suite | Local request/response captured | | |

## Screenshots folder
Save genuine screenshots in `evidence/` and reference them above. Do not include passwords, personal data, tokens, or session cookies in screenshots.

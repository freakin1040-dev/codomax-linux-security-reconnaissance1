#!/usr/bin/env python3
"""Generate harmless HTTP requests to the local training server."""
from urllib.request import urlopen
from urllib.error import URLError

BASE = "http://127.0.0.1:8000"
for path in ("/", "/hello", "/health", "/search?q=packet-analysis"):
    try:
        with urlopen(BASE + path, timeout=3) as response:
            print(f"{path}: HTTP {response.status}; Content-Type={response.headers.get('Content-Type')}")
            response.read()
    except URLError as exc:
        raise SystemExit(f"Could not reach {BASE}. Start the lab first. Details: {exc}")

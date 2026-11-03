# Local HTTP Training App

This tiny Python standard-library HTTP server is a local target for learning how proxies and scanners observe HTTP. It binds only to `127.0.0.1`, so it is not exposed to other devices on the network.

## Requirements
- Python 3 (Ubuntu/WSL)
- No third-party Python packages

## Start
From the repository root:
```bash
bash scripts/start_lab.sh
```
Then visit `http://127.0.0.1:8000`.

## Stop
```bash
bash scripts/stop_lab.sh
```
Or press Ctrl+C in the terminal running the server.

## Routes
- `/` — home page
- `/hello` — simple text response
- `/health` — plain health status
- `/search?q=...` — displays a safely escaped query value

This is intentionally a minimal training app, not a full vulnerable application. It does not implement login, data storage, or real user accounts.

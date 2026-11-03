# Nmap — Local Service Discovery

**Purpose:** Nmap is a network discovery and security auditing tool. It can identify reachable hosts, open ports, and service information.

## Install on Ubuntu/WSL
```bash
sudo apt update
sudo apt install nmap
nmap --version
```

## Start the local lab first
From the repository root:
```bash
bash scripts/start_lab.sh
```
The demo HTTP service listens on `127.0.0.1:8000`.

## Scan only the local lab service
```bash
nmap -sT -sV -p 8000 127.0.0.1
```
- `-sT`: TCP connect scan.
- `-sV`: attempt service/version detection.
- `-p 8000`: limit scan to the demo application's port.
- `127.0.0.1`: loopback address of the same machine.

Save your real output:
```bash
mkdir -p evidence/nmap
nmap -sT -sV -p 8000 127.0.0.1 -oN evidence/nmap/localhost-8000.txt
```

Do not infer a version if Nmap does not identify one. Add the exact output and a screenshot to the report. Never replace `127.0.0.1` with an unrelated/public target.

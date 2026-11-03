#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -f lab/server.pid ]] && kill -0 "$(cat lab/server.pid)" 2>/dev/null; then
  echo "Lab already running (PID $(cat lab/server.pid))."
  exit 0
fi
nohup python3 lab/app.py > lab/server.log 2>&1 &
echo $! > lab/server.pid
sleep 1
if kill -0 "$(cat lab/server.pid)" 2>/dev/null; then
  echo "Lab started at http://127.0.0.1:8000 (PID $(cat lab/server.pid))."
else
  echo "Lab failed to start. Check lab/server.log."
  exit 1
fi

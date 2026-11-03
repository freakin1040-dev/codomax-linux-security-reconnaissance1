#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -f lab/server.pid ]]; then
  pid="$(cat lab/server.pid)"
  if kill -0 "$pid" 2>/dev/null; then
    kill "$pid"
    echo "Stopped lab process $pid."
  else
    echo "Lab process was not running."
  fi
  rm -f lab/server.pid
else
  echo "No PID file found; lab may not be running."
fi

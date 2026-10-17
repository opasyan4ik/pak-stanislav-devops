#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$project_dir/logs" "$project_dir/backup"
chmod 600 "$project_dir/private.txt"
chmod 644 "$project_dir/public.txt"
chmod +x "$project_dir/scripts/Pak_Stanislav_system.sh"

cat > "$project_dir/logs/application.log" <<'LOG'
INFO Application started
INFO User logged in
WARNING Configuration file missing
INFO Database connected
ERROR Database connection failed
INFO Application restarted
WARNING Memory usage is high
INFO Request received
ERROR Request failed
INFO Application stopped
LOG

printf 'Demo files and permissions are ready.\n'

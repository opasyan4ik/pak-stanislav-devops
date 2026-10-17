#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
info_file="$project_dir/Pak_Stanislav_info.txt"

printf '%s\n' '==============================' 'Student Information' '==============================' ''
printf '%s\n' 'Name: Stanislav' 'Surname: Pak' 'Group: IT2-2314' 'Student ID: 37845' ''
printf '%s\n' '==============================' 'System Information' '==============================' ''
printf 'Username: %s\n' "$(whoami)"
printf 'Hostname: %s\n' "$(hostname)"
printf 'Current Date: %s\n' "$(date)"
printf 'Operating System: %s\n' "$(uname -s)"
printf 'Disk Usage:\n'
df -h "$project_dir" | head -n 2
printf 'Memory Usage:\n'
free -h | head -n 2

if [[ -f "$info_file" ]]; then
    printf '%s\n' 'Student information file exists.'
else
    printf '%s\n' 'Student information file does not exist.'
fi

#!/usr/bin/env bash
set -euo pipefail

echo "Deploying with docker-compose..."
docker compose -f config/docker/docker-compose.yml up -d --build 
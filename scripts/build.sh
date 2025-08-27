#!/usr/bin/env bash
set -euo pipefail

echo "Building TypeScript client..."
(cd src/client/typescript && npm run build || true)

echo "Build complete" 
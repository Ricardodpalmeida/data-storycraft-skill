#!/usr/bin/env bash
# Package the skill folder as a zip for upload (SKILL.md at the zip's top-level folder).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_DIR="$ROOT/skill/data-storycraft"
DIST="$ROOT/dist"

[ -f "$SKILL_DIR/SKILL.md" ] || { echo "SKILL.md not found in $SKILL_DIR" >&2; exit 1; }

mkdir -p "$DIST"
rm -f "$DIST/data-storycraft.zip"
(cd "$ROOT/skill" && zip -qr "$DIST/data-storycraft.zip" data-storycraft -x '*.DS_Store')
echo "Wrote $DIST/data-storycraft.zip"

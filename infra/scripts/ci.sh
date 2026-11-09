#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
python3 scripts/validate.py --root .
if command -v mvn >/dev/null 2>&1; then
  mvn -q test
elif command -v javac >/dev/null 2>&1; then
  classes="$(mktemp -d)"
  trap 'rm -rf "$classes"' EXIT
  javac -d "$classes" $(find src/main/java -name '*.java') src/test/java/com/gardusigustavo/packagejava/AnswerCheck.java
  java -ea -cp "$classes" com.gardusigustavo.packagejava.AnswerCheck
else
  echo "java toolchain unavailable; bootstrap validation only"
fi
for f in infra/scripts/*.sh; do bash -n "$f"; done
echo "java checks ok"

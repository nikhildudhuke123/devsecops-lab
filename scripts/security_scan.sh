#!/usr/bin/env bash

set -u

FAILED=0

run_check() {
  local name="$1"
  shift

  echo
  echo "========================================"
  echo "[$name]"
  echo "========================================"

  if "$@"; then
    echo "[PASS] $name"
  else
    echo "[FAIL] $name"
    FAILED=1
  fi
}

run_check "Terraform Validate" terraform -chdir=terraform/aws validate
run_check "Semgrep SAST" semgrep scan --config auto --error .
run_check "Trivy Filesystem Scan" trivy fs --scanners vuln --severity HIGH,CRITICAL .
run_check "Gitleaks Secret Scan" gitleaks detect --no-banner --redact
run_check "Checkov Terraform Scan" checkov -d terraform/aws --framework terraform

echo
echo "========================================"
if [ "$FAILED" -eq 0 ]; then
  echo "SECURITY SCAN RESULT: PASS"
  exit 0
else
  echo "SECURITY SCAN RESULT: FAIL"
  exit 1
fi

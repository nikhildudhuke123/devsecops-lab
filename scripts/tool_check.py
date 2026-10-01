#!/usr/bin/env python3

import shutil
import subprocess

TOOLS = {
    "git": ["--version"],
    "python3": ["--version"],
    "docker": ["--version"],
    "semgrep": ["--version"],
    "trivy": ["--version"],
    "gitleaks": ["version"],
    "checkov": ["--version"],
    "terraform": ["--version"],
    "kubectl": ["version", "--client=true", "--output=yaml"],
    "helm": ["version", "--short"],
    "aws": ["--version"],
    "syft": ["--version"],
}


def get_version(tool: str, args: list[str]) -> tuple[bool, str]:
    path = shutil.which(tool)

    if not path:
        return False, "NOT FOUND"

    try:
        result = subprocess.run(
            [tool, *args],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        output = (result.stdout or result.stderr).strip()

        if result.returncode != 0:
            return False, output or f"command failed with exit code {result.returncode}"

        return True, output.splitlines()[0] if output else "VERSION UNKNOWN"

    except (OSError, subprocess.SubprocessError) as exc:
        return False, f"ERROR: {exc}"


def main() -> None:
    print("DevSecOps Tool Availability Check")
    print("=" * 50)

    failures = 0

    for tool, args in TOOLS.items():
        ok, version = get_version(tool, args)
        status = "OK" if ok else "FAIL"

        print(f"{tool:12} [{status}] {version}")

        if not ok:
            failures += 1

    print("=" * 50)
    print(f"Tools checked: {len(TOOLS)}")
    print(f"Missing/error: {failures}")

    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()

# DevSecOps Lab

A hands-on DevSecOps security engineering lab demonstrating security controls across the application, CI/CD pipeline, container, Kubernetes, runtime, and AWS infrastructure layers.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |
   +--> Semgrep -------- SAST
   +--> Trivy ---------- SCA / Container Security
   +--> Gitleaks ------- Secret Detection
   +--> Syft ----------- SBOM
   +--> OWASP ZAP ------ DAST
   +--> Checkov -------- IaC Security
   |
   v
GHCR
   |
   v
Kubernetes
   |
   +--> RBAC
   +--> NetworkPolicy
   +--> SecurityContext
   +--> Kyverno -------- Admission Control
   +--> Ingress + TLS
   |
   v
Application
   |
   +--> Falco ---------- Runtime Detection
   |
   v
AWS
   |
   +--> S3
         +--> Public Access Block
         +--> KMS Encryption
         +--> Versioning
         +--> Lifecycle Management
```
## Security Coverage

### Application Security

- Parameterized SQL queries
- Security response headers
- Semgrep SAST
- Trivy dependency scanning
- OWASP ZAP DAST

### Container Security

- Multi-stage Docker build
- Non-root container user
- Read-only root filesystem
- Linux capabilities dropped
- Privilege escalation disabled
- Trivy vulnerability scanning
- Syft SBOM generation

### Kubernetes Security

- Dedicated ServiceAccount
- Least-privilege RBAC
- NetworkPolicy
- Kubernetes SecurityContext
- CPU and memory limits
- Readiness and liveness probes
- Digest-pinned container image
- Disabled automatic ServiceAccount token mounting
- NGINX Ingress
- TLS
- Kyverno admission policy
- Falco runtime detection
### AWS / IaC Security

Terraform manages the AWS S3 infrastructure with:

- Public access blocking
- KMS-based default encryption
- Versioning
- Lifecycle configuration
- Incomplete multipart-upload cleanup
- IAM permissions scoped to the DevSecOps lab

Checkov scans the Terraform configuration before deployment.

## CI/CD

GitHub Actions performs:

1. Semgrep SAST
2. Trivy SCA
3. Gitleaks secret scanning
4. Docker image build
5. Syft SBOM generation
6. OWASP ZAP DAST
7. Trivy container scanning
8. GHCR image publishing
9. Checkov Terraform scanning
## Security Automation

Local security automation is available through:

`./scripts/security_scan.sh`

The tool availability checker is:

`./scripts/tool_check.py`

## Purple Team Validation

Controlled validation scenarios include:

- SQL injection resistance
- Interactive container shell detection with Falco
- Kubernetes workload egress restriction

See:

- `docs/threat-model/README.md`
- `docs/red-purple-team/README.md`
- `docs/architecture/README.md`

## Project Structure

```text
.
├── app/
├── k8s/
├── scripts/
├── terraform/
├── docs/
│   ├── architecture/
│   ├── red-purple-team/
│   └── threat-model/
├── .github/workflows/
└── README.md
```

## Tools

Git, GitHub, Linux, Docker, Semgrep, Trivy, Gitleaks, Syft, Checkov, OWASP ZAP, Terraform, Kubernetes, kind, Helm, Kyverno, Falco, AWS CLI, and GitHub Actions.

## Lab Principles

- Shift security left
- Least privilege
- Defense in depth
- Policy as code
- Infrastructure as code
- Automated security gates
- Runtime detection
- Continuous validation

## Important

The local TLS certificate and private key are intentionally excluded from Git.

The AWS Terraform state files are also excluded from Git because Terraform state can contain sensitive infrastructure information.

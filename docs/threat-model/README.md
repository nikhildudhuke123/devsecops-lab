# DevSecOps Lab Threat Model

## 1. Scope

This threat model covers the DevSecOps Lab application and its deployment pipeline:

Developer → GitHub → CI/CD → Docker → Kubernetes → Ingress/TLS → Flask Application → AWS S3

## 2. Assets

- Source code
- CI/CD pipeline
- Container image
- Kubernetes workload
- Kubernetes credentials and secrets
- Application/API data
- AWS S3 bucket and objects
- TLS private key
- GitHub repository and package registry

## 3. Trust Boundaries

### Boundary 1: Developer → GitHub

Code and configuration leave the developer workstation and enter the GitHub repository.

### Boundary 2: GitHub → CI/CD Runner

Repository-controlled code is executed by the GitHub Actions runner.

### Boundary 3: CI/CD → Container Registry

Built container images are pushed to GHCR.

### Boundary 4: Registry → Kubernetes

The Kubernetes cluster pulls the container image using an image-pull secret.

### Boundary 5: Internet → Kubernetes Ingress

External HTTP/HTTPS traffic enters through the NGINX Ingress Controller.

### Boundary 6: Application → AWS

Cloud resources are accessed using AWS IAM credentials.

## 4. STRIDE Analysis

| Threat | Example | Existing Mitigation |
|---|---|---|
| Spoofing | Unauthorized access to application/API | Authentication controls and Kubernetes RBAC |
| Tampering | Malicious code or image modification | GitHub controls, image digest pinning, Semgrep, Trivy |
| Repudiation | Lack of evidence for security events | Git history, CI logs, Falco runtime detection |
| Information Disclosure | Secrets exposed in source or containers | Gitleaks, Kubernetes secret handling, private GHCR |
| Denial of Service | Resource exhaustion in Kubernetes | CPU/memory limits, readiness/liveness probes |
| Elevation of Privilege | Compromised workload gaining Kubernetes privileges | Dedicated ServiceAccount, restricted RBAC, non-root container, Kyverno |

## 5. Security Controls

### Application

- Parameterized SQL queries
- Security response headers
- Gunicorn
- SAST with Semgrep
- SCA with Trivy
- DAST with OWASP ZAP
- Secret scanning with Gitleaks

### Container

- Multi-stage build
- Non-root user
- Read-only root filesystem
- Dropped Linux capabilities
- `allowPrivilegeEscalation: false`
- Vulnerability scanning with Trivy
- SBOM generation with Syft

### Kubernetes

- RBAC
- NetworkPolicy
- SecurityContext
- Resource limits
- Health probes
- Image digest pinning
- `automountServiceAccountToken: false`
- Ingress with TLS
- Kyverno admission policy
- Falco runtime detection

### AWS

- Terraform-managed infrastructure
- S3 public access blocking
- KMS-based encryption
- Versioning
- Lifecycle management
- IAM least-privilege permissions for the lab

## 6. Residual Risks

The current Checkov scan reports three findings:

- S3 access logging
- S3 event notifications
- S3 cross-region replication

These controls are not currently implemented because they depend on the operational requirements and architecture of the lab.

## 7. Security Objective

The objective is to detect and prevent vulnerabilities as early as possible while maintaining runtime visibility after deployment.

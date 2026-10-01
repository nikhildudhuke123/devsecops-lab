# DevSecOps Lab Architecture

## 1. End-to-End Flow

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
   |
   +--> Trivy ---------- SCA
   |
   +--> Gitleaks ------- Secret Detection
   |
   +--> Docker Build
   |       |
   |       +--> Trivy Container Scan
   |       +--> Syft SBOM
   |
   +--> OWASP ZAP ------ DAST
   |
   +--> Checkov -------- Terraform/IaC Security
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
DevSecOps Application
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
## 2. Security Lifecycle

### Prevent

- Secure coding practices
- Parameterized SQL
- Kubernetes SecurityContext
- RBAC
- NetworkPolicy
- Kyverno admission policy
- S3 public-access controls
- Encryption and versioning

### Detect

- Semgrep
- Trivy
- Gitleaks
- Checkov
- OWASP ZAP
- Falco

### Respond / Validate

- Security scan automation
- Red/Purple Team simulations
- Runtime validation
- Threat modeling
- Terraform plan/apply workflow

## 3. Infrastructure

### Local Kubernetes

The lab uses Kubernetes running through kind.

Core workload components:

- DevSecOps application Deployment
- Kubernetes Service
- NetworkPolicy
- Dedicated ServiceAccount
- Restricted Role and RoleBinding
- Ingress
- TLS Secret
- Kyverno policy
- Falco runtime monitoring

### AWS

Terraform manages the S3 portion of the lab.

Current controls include:

- Block public ACLs
- Block public bucket policies
- Restrict public buckets
- KMS-based default encryption
- Bucket versioning
- Lifecycle management
- Aborted multipart-upload cleanup
## 4. CI/CD Security Gates

The GitHub Actions pipeline performs:

1. SAST
2. SCA
3. Secret scanning
4. Container build
5. SBOM generation
6. DAST
7. Container vulnerability scanning
8. Image publishing

A separate Checkov workflow scans Terraform infrastructure code.

## 5. Runtime Security

Falco provides runtime detection for suspicious activity inside Kubernetes workloads.

The lab validated interactive shell detection through `kubectl exec -it`.

## 6. Validation Scenarios

Controlled Purple Team tests have validated:

- SQL injection resistance
- Interactive shell runtime detection
- Kubernetes egress restriction

## 7. Design Principles

The lab follows these principles:

- Shift security left
- Least privilege
- Defense in depth
- Immutable and traceable artifacts
- Policy as code
- Automated security gates
- Runtime detection
- Infrastructure as code
- Continuous validation

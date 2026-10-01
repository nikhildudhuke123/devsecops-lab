# Red / Purple Team Validation

## Purpose

This document records controlled security simulations performed against the DevSecOps Lab.

All tests were executed against the lab's own Kubernetes environment.

## Test 1: SQL Injection

### Objective

Verify that the `/api/user?id=` endpoint is not vulnerable to SQL injection.

### Payload

`1 OR 1=1`

### Result

`{"users":[]}`

The payload was treated as input and did not return all database records.

### Defensive Control

Parameterized SQL query using a bound parameter.

---
## Test 2: Interactive Container Shell

### Objective

Verify runtime detection of an interactive shell inside the application container.

### Action

An interactive shell was opened using `kubectl exec -it`.

### Result

Falco generated a NOTICE event indicating that a shell was spawned in a container with an attached terminal.

### Defensive Control

Falco runtime detection.

---
## Test 3: Workload Egress

### Objective

Verify that the application workload cannot initiate arbitrary outbound network connections.

### Target

`http://1.1.1.1`

### Result

The connection timed out and the request failed.

### Defensive Control

Kubernetes NetworkPolicy with an empty egress rule set.

---
## Security Validation Summary

| Scenario | Expected Control | Result |
|---|---|---|
| SQL injection | Parameterized SQL | Passed |
| Interactive shell | Falco runtime detection | Passed |
| Outbound network access | NetworkPolicy | Passed |

## Scope

These are controlled validation tests for the DevSecOps Lab and are not intended to represent a complete penetration test.

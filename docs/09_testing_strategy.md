# 09 — Testing Strategy

**Project Name:** SupportDesk  
**Document Version:** 1.0

## 1. Introduction

This document defines how SupportDesk will be tested to verify correctness, reliability, security, and performance.

## 2. Testing Objectives

- Verify functional requirements.
- Validate business rules.
- Detect defects early.
- Protect tenant data isolation.
- Verify authorization.
- Maintain database consistency.
- Evaluate API performance.

## 3. Testing Types

### 3.1 Unit Testing

Tests individual functions and business logic in isolation.

Examples:

- Ticket priority validation.
- Ticket status transition rules.
- SLA deadline calculations.
- Permission checks.

### 3.2 Integration Testing

Tests interactions between application components.

Examples:

- API and PostgreSQL integration.
- Authentication and database integration.
- Ticket creation with assignment.
- Conversation creation and retrieval.

### 3.3 API Testing

Tests HTTP endpoints.

Examples:

- Valid requests.
- Invalid request payloads.
- Authentication failures.
- Authorization failures.
- Expected HTTP status codes.
- Response structure validation.

### 3.4 Security Testing

Tests:

- Unauthorized access.
- Role permission enforcement.
- Cross-tenant data access attempts.
- Invalid tokens.
- Unsafe input.
- File upload validation.

### 3.5 Performance Testing

Locust will be used to evaluate API behaviour under concurrent load.

Tests will measure:

- Response time.
- Throughput.
- Error rate.
- Resource usage.
- Database performance.

### 3.6 Regression Testing

Previously working functionality must be tested after changes to ensure existing behaviour is not broken.

## 4. Testing Tools

| Tool | Purpose |
|---|---|
| Pytest | Automated tests |
| HTTPX | API testing |
| PostgreSQL test database | Integration testing |
| Locust | Load and performance testing |
| Coverage | Test coverage measurement |

## 5. Critical Test Scenarios

- Customer creates a ticket successfully.
- Customer cannot access another customer's restricted ticket.
- Agent can access permitted assigned tickets.
- Manager can assign tickets.
- Internal notes are not visible to customers.
- Invalid ticket status transitions are rejected.
- SLA deadlines are calculated correctly.
- Unauthorized users cannot access protected APIs.
- Organization A cannot access Organization B's data.
- Database failures do not leave incomplete transactional operations.

## 6. Test Environment

Separate environments should be maintained for:

- Development
- Testing
- Staging
- Production

Production data should not be casually copied into development or testing environments.

## 7. Quality Criteria

A feature can be considered ready for release when:

- Its functional tests pass.
- Relevant integration tests pass.
- Authorization and tenant isolation tests pass.
- Important edge cases are covered.
- No known critical defects remain.
- Code review is completed.

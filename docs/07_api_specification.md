# 07 — API Specification

**Project Name:** SupportDesk  
**Document Version:** 1.0

## 1. Introduction

This document defines the initial REST API structure for SupportDesk.

The backend will be developed using FastAPI.

## 2. API Standards

- API style: REST
- Communication format: JSON
- Authentication: Bearer token
- API versioning: `/api/v1`
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- Documentation: OpenAPI / Swagger

## 3. Base URL

Development:

`http://localhost:8000/api/v1`

Production URL will be configured during deployment.

## 4. Authentication APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /auth/register | Register user |
| POST | /auth/login | Authenticate user |
| POST | /auth/refresh | Refresh access token |
| POST | /auth/logout | Logout / revoke session where supported |
| GET | /auth/me | Get current user |

## 5. Organization APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /organizations | Create organization |
| GET | /organizations | List organizations |
| GET | /organizations/{id} | Get organization |
| PATCH | /organizations/{id} | Update organization |

## 6. User APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /users | Create user |
| GET | /users | List users |
| GET | /users/{id} | Get user |
| PATCH | /users/{id} | Update user |
| PATCH | /users/{id}/status | Activate or deactivate user |

## 7. Department APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /departments | Create department |
| GET | /departments | List departments |
| GET | /departments/{id} | Get department |
| PATCH | /departments/{id} | Update department |
| DELETE | /departments/{id} | Delete department where permitted |

## 8. Ticket APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /tickets | Create ticket |
| GET | /tickets | List tickets |
| GET | /tickets/{id} | Get ticket details |
| PATCH | /tickets/{id} | Update ticket |
| PATCH | /tickets/{id}/status | Change ticket status |
| PATCH | /tickets/{id}/priority | Change ticket priority |

## 9. Assignment APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /tickets/{id}/assign | Assign ticket |
| POST | /tickets/{id}/reassign | Reassign ticket |
| GET | /tickets/{id}/assignments | View assignment history |

## 10. Conversation APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /tickets/{id}/messages | Add message |
| GET | /tickets/{id}/messages | Get conversation |
| POST | /tickets/{id}/notes | Add internal note |

## 11. SLA and Escalation APIs

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /sla-policies | Create SLA policy |
| GET | /sla-policies | List SLA policies |
| GET | /tickets/{id}/sla | Get ticket SLA details |
| GET | /escalations | List escalations |
| POST | /tickets/{id}/escalate | Escalate ticket |

## 12. Reporting APIs

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /reports/tickets | Ticket statistics |
| GET | /reports/agents | Agent performance |
| GET | /reports/sla | SLA performance |

## 13. Standard Response Format

Successful responses should use consistent JSON structures.

Example:

```json
{
  "success": true,
  "message": "Ticket created successfully",
  "data": {
    "id": 101,
    "subject": "Unable to access account",
    "status": "open"
  }
}
```

Error response example:

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": []
}
```

Actual response schemas and error formats will be finalized during API implementation.

## 14. HTTP Status Codes

- 200 — OK
- 201 — Created
- 204 — No Content
- 400 — Bad Request
- 401 — Unauthorized
- 403 — Forbidden
- 404 — Not Found
- 409 — Conflict
- 422 — Validation Error
- 500 — Internal Server Error

## 15. API Security

- Protected APIs must require authentication.
- Authorization must be checked for every protected operation.
- Tenant ownership must be validated.
- Sensitive information must not be returned in API responses.
- Input validation must be performed.

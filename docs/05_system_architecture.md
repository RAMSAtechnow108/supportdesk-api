# 05 — High-Level Design (HLD)

**Project Name:** SupportDesk  
**Document Version:** 1.0

## 1. Introduction

This document describes the high-level architecture of SupportDesk, including major components, their responsibilities, and communication between them.

## 2. Architecture Style

SupportDesk will initially use a **Modular Monolith with Layered Architecture**.

A modular monolith keeps the application in one deployable unit while organizing business functionality into independent modules.

This approach is suitable for the initial project because it provides clear boundaries without introducing the operational complexity of microservices.

## 3. Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python 3.13 |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Migrations | Alembic |
| Validation | Pydantic |
| Authentication | JWT-based authentication |
| Cache / Message Broker | Redis |
| Background Jobs | Celery |
| Testing | Pytest |
| Load Testing | Locust |
| Containerization | Docker |
| Reverse Proxy | Nginx |
| CI/CD | GitHub Actions |

## 4. High-Level Components

### 4.1 API Layer

Responsible for:

- Receiving HTTP requests.
- Validating request data.
- Authentication and authorization dependencies.
- Returning HTTP responses.

### 4.2 Service Layer

Responsible for:

- Business logic.
- Workflow execution.
- Business rule validation.
- Transaction coordination.

### 4.3 Repository / Data Access Layer

Responsible for:

- Database queries.
- Creating, updating, and retrieving records.
- Encapsulating data access operations.

### 4.4 Database Layer

PostgreSQL will store application data, including users, organizations, tickets, conversations, and audit records.

### 4.5 Background Processing Layer

Redis and Celery will support asynchronous operations such as notifications, SLA checks, and scheduled tasks.

### 4.6 Monitoring and Logging

The system will maintain application logs, error information, and operational metrics.

## 5. Major Business Modules

- Authentication Module
- Organization Module
- User Management Module
- Department Module
- Ticket Management Module
- Assignment Module
- Conversation Module
- Attachment Module
- SLA Module
- Escalation Module
- Notification Module
- Reporting Module
- Audit Module

## 6. High-Level Request Flow

1. Client sends an HTTP request.
2. FastAPI receives the request.
3. Request validation is performed.
4. Authentication and authorization are checked.
5. API layer calls the appropriate service.
6. Service executes business rules.
7. Repository performs database operations.
8. Database returns the result.
9. Service prepares the result.
10. API returns the HTTP response.

## 7. Multi-Tenant Architecture

The initial design will use a shared PostgreSQL database with a shared schema.

Organization-owned records will be associated with an organization identifier.

Every organization-scoped query must enforce tenant isolation.

Platform-level operations will have separate authorization rules.

## 8. Deployment Architecture

The planned deployment environment includes:

- Nginx as reverse proxy.
- FastAPI application.
- PostgreSQL database.
- Redis.
- Celery workers.
- Docker containers.

The exact production hosting provider and infrastructure configuration will be finalized later.

## 9. Architecture Principles

- Separation of concerns.
- Single responsibility.
- Explicit module boundaries.
- Secure data access.
- Transactional consistency.
- Reusable business services.
- Testable components.
- Maintainable code.

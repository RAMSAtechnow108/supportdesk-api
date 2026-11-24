# 06 — Database Design

**Project Name:** SupportDesk  
**Document Version:** 1.0

## 1. Introduction

This document describes the initial logical database design of SupportDesk.

PostgreSQL will be used as the primary relational database.

SQLAlchemy will be used for ORM-based database interactions, and Alembic will manage schema migrations.

## 2. Database Design Principles

- Use primary keys to identify records.
- Use foreign keys to maintain relationships.
- Apply unique constraints where required.
- Use appropriate indexes for frequently queried fields.
- Store timestamps for important records.
- Maintain organization ownership for tenant-specific data.
- Use transactions for related database operations.
- Avoid unnecessary duplication of data.

## 3. Initial Entities

### 3.1 organizations

Stores organization information.

Expected fields:

- id
- name
- slug
- status
- created_at
- updated_at

### 3.2 users

Stores platform users.

Expected fields:

- id
- organization_id
- full_name
- email
- password_hash
- status
- created_at
- updated_at

### 3.3 roles

Stores system roles.

Expected fields:

- id
- name
- description

### 3.4 user_roles

Associates users with roles.

Expected fields:

- id
- user_id
- role_id

### 3.5 departments

Stores support departments.

Expected fields:

- id
- organization_id
- name
- description
- status
- created_at

### 3.6 tickets

Stores customer support tickets.

Expected fields:

- id
- organization_id
- customer_id
- department_id
- subject
- description
- status
- priority
- created_at
- updated_at
- resolved_at
- closed_at

### 3.7 ticket_assignments

Stores ticket assignment history.

Expected fields:

- id
- ticket_id
- agent_id
- assigned_by
- assigned_at
- unassigned_at

### 3.8 conversations

Stores ticket messages and internal notes.

Expected fields:

- id
- ticket_id
- sender_id
- message
- message_type
- created_at

### 3.9 attachments

Stores attachment metadata.

Expected fields:

- id
- conversation_id
- file_name
- file_path
- content_type
- file_size
- uploaded_by
- created_at

### 3.10 sla_policies

Stores SLA configurations.

Expected fields:

- id
- organization_id
- name
- priority
- response_time_minutes
- resolution_time_minutes
- status

### 3.11 ticket_sla_records

Stores SLA deadlines and tracking information for tickets.

Expected fields:

- id
- ticket_id
- sla_policy_id
- response_due_at
- resolution_due_at
- response_met_at
- resolution_met_at
- status

### 3.12 escalations

Stores ticket escalation history.

Expected fields:

- id
- ticket_id
- escalated_to
- reason
- escalated_at
- status

### 3.13 notifications

Stores user notifications.

Expected fields:

- id
- user_id
- title
- message
- notification_type
- read_at
- created_at

### 3.14 audit_logs

Stores important system activities.

Expected fields:

- id
- organization_id
- actor_id
- action
- entity_type
- entity_id
- metadata
- created_at

## 4. Initial Relationships

- One organization can have many users.
- One organization can have many departments.
- One organization can have many tickets.
- One customer can create many tickets.
- One department can handle many tickets.
- One ticket can have multiple assignment records.
- One ticket can have multiple conversations.
- One conversation can have multiple attachments.
- One ticket can have one or more SLA tracking records over its lifecycle, depending on policy design.
- One ticket can have multiple escalation records.
- One user can receive multiple notifications.
- One organization can have multiple audit records.

## 5. Data Integrity

- Foreign keys must enforce valid relationships.
- Email uniqueness rules must be defined at the appropriate tenant or platform scope.
- Required fields must not accept NULL values.
- Status and priority values must be validated.
- Organization-owned data must maintain tenant ownership.
- Important updates must preserve audit history.

## 6. Indexing Strategy

Potential indexes:

- users.email
- users.organization_id
- tickets.organization_id
- tickets.customer_id
- tickets.status
- tickets.priority
- tickets assigned department and assignment lookup fields
- conversations.ticket_id
- notifications.user_id
- audit_logs.organization_id

Final indexes will be decided after query patterns are defined and tested.

## 7. Database Migration Strategy

Alembic will be used to manage database schema changes.

Every important schema change must be represented by a migration.

Migrations must be reviewed and tested before being applied to production.

The detailed ER diagram, column data types, constraints, and migration history will be developed during implementation.

# 03 — Software Requirements Specification (SRS)

**Project Name:** SupportDesk  
**Document Version:** 1.0  
**Status:** Initial Draft

## 1. Introduction

The Software Requirements Specification defines the functional and technical behaviour expected from the SupportDesk platform.

It describes what the software must do, how users interact with it, and what constraints the system must follow.

## 2. Product Overview

SupportDesk is a multi-tenant customer support management platform.

It allows multiple organizations to manage their customer support operations independently while using the same application.

Each organization will have its own users, departments, tickets, and support workflows.

## 3. User Roles

### 3.1 Customer

- Register or access an account.
- Create support tickets.
- View submitted tickets.
- Reply to support conversations.
- Upload relevant attachments.
- View ticket status.

### 3.2 Support Agent

- View assigned tickets.
- Accept and manage tickets.
- Reply to customers.
- Add internal notes.
- Change ticket status according to permissions.
- Resolve assigned tickets.

### 3.3 Support Manager

- Monitor team tickets.
- Assign or reassign tickets.
- Monitor agent workload.
- Review SLA performance.
- Handle escalated tickets.
- Access team reports.

### 3.4 Organization Admin

- Manage organization users.
- Manage departments.
- Configure organization-level settings.
- Manage role permissions.

### 3.5 Platform Admin

- Manage organizations.
- Monitor platform-level operations.
- Manage platform configuration.
- Access platform-level audit information.

## 4. Functional Requirements

### FR-01: Authentication

- Users must be able to authenticate securely.
- The system must validate user credentials.
- The system must support secure session or token-based authentication.
- The system must provide logout functionality.
- Protected endpoints must require authentication.

### FR-02: User Management

- Authorized administrators must be able to create users.
- Users must belong to an organization, except platform-level users.
- Users must have assigned roles.
- Administrators must be able to activate or deactivate users.

### FR-03: Organization Management

- The platform must support multiple organizations.
- Each organization must have its own users and business data.
- Organization-level data must remain isolated.

### FR-04: Department Management

- Organizations must be able to create departments.
- Departments must represent different support teams.
- Agents may be assigned to appropriate departments.
- Ticket routing must respect department configuration.

### FR-05: Ticket Management

- Customers must be able to create tickets.
- Each ticket must have a unique identifier.
- Tickets must contain a subject and description.
- Tickets must support status and priority.
- Authorized users must be able to view ticket details.
- Tickets must maintain their activity history.

### FR-06: Ticket Assignment

- Tickets must be assignable to support agents.
- Authorized managers must be able to reassign tickets.
- The system must record assignment history.
- Automatic assignment rules may be configured in a later phase.

### FR-07: Ticket Workflow

The initial ticket lifecycle will support:

- Open
- In Progress
- Pending
- Resolved
- Closed

The allowed status transitions and reopening rules will be finalized during workflow design.

### FR-08: Conversations and Internal Notes

- Customers and agents must be able to exchange messages.
- Agents must be able to add internal notes.
- Internal notes must not be visible to customers.
- Conversations must maintain timestamps and authorship.

### FR-09: Attachments

- Authorized users must be able to attach files to conversations.
- The system must validate file types and sizes.
- Attachment access must follow ticket permissions.

### FR-10: SLA Management

- The system must support configurable SLA policies.
- SLA targets may differ based on priority or organization policy.
- The system must track response and resolution deadlines.
- SLA breaches must be identifiable.

### FR-11: Escalation Management

- Tickets approaching or exceeding SLA limits must be identifiable.
- The system must support escalation to appropriate managers.
- Escalation events must be recorded.

### FR-12: Notifications

- The system must notify relevant users about important ticket events.
- Events may include ticket creation, assignment, replies, status changes, and escalation.
- Notification channels and delivery rules will be finalized during design.

### FR-13: Reporting and Dashboard

- Managers must be able to view ticket statistics.
- Reports must include ticket counts by status and priority.
- Reports should provide agent workload and performance information.
- SLA compliance must be measurable.

### FR-14: Audit Logging

- Important system activities must be recorded.
- Audit records must include the actor, action, target, and timestamp where applicable.
- Audit records must be accessible only to authorized users.

## 5. Main Use Cases

| Use Case | Actor | Description |
|---|---|---|
| Create Ticket | Customer | Submit a support request |
| View Ticket | Customer/Agent | View ticket details |
| Assign Ticket | Manager | Assign ticket to an agent |
| Reply to Ticket | Customer/Agent | Exchange messages |
| Add Internal Note | Agent | Add private team information |
| Resolve Ticket | Agent | Mark an issue as resolved |
| Monitor SLA | Manager | Track SLA performance |
| Manage Users | Organization Admin | Manage organization users |

## 6. External Interface Requirements

- RESTful HTTP APIs.
- JSON request and response formats.
- API documentation through OpenAPI/Swagger.
- Authentication through secure tokens.
- Database communication through SQLAlchemy.

## 7. Data Requirements

The system is expected to manage:

- Organizations
- Users
- Roles and permissions
- Departments
- Tickets
- Ticket assignments
- Conversations
- Attachments
- SLA policies
- Escalation records
- Notifications
- Audit logs

Detailed database relationships will be defined in the Database Design document.

## 8. Business Rules

- A customer can access only their permitted tickets.
- An agent can access tickets permitted by their organization and role.
- Internal notes must never be exposed to customers.
- Organization data must remain isolated.
- Only authorized users can assign or reassign tickets.
- Ticket status changes must follow configured workflow rules.

Detailed permission and workflow rules will be finalized during implementation planning.

## 9. Acceptance Criteria

The system must satisfy the functional requirements, enforce access restrictions, maintain data consistency, and pass the defined testing strategy before release.

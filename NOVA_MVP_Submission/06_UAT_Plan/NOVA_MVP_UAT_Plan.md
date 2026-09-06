# Deliverable 6: Master User Acceptance Testing (UAT) Plan

**Product:** NOVA — AI-Powered Team Productivity Platform  
**Testing Window:** Week 9 (Sprint 5)  
**Author:** Project Management Intern & QA Lead  
**Target Release Gate:** Production Launch Gate (Week 10)  

---

## 1. UAT Objectives & Governance Strategy

The primary objective of the **NOVA MVP User Acceptance Testing (UAT)** plan is to validate that the software satisfies all business requirements, user stories, and acceptance criteria from an end-user perspective prior to production deployment.

### UAT Governance Scope
* **Testing Duration**: 5 Days (Sprint 5, Week 9 Monday - Friday).
* **Test Environment**: Isolated AWS Staging Environment (`https://staging.nova-app.io`).
* **Test Dataset**: Pre-populated database with 10 dummy project workspaces, 50 task items, and 8 active user accounts.

---

## 2. Participant Personas & Tester Allocation

UAT will be conducted by a 6-member external beta tester panel representing NOVA's core target personas:

1. **Persona 1: Engineering Team Lead (2 Testers)** — Validates task assignment, priority workflows, and Kanban interaction.
2. **Persona 2: Project Manager (2 Testers)** — Validates project dashboard KPIs, member RBAC roles, and status reports.
3. **Persona 3: Executive Leader (1 Tester)** — Validates high-level analytics charts and productivity overview.
4. **Persona 4: Cross-Functional Contributor (1 Tester)** — Validates task comments, profile settings, and notifications.

---

## 3. Defect Classification & Resolution SLAs

During UAT, any identified issues must be logged in the UAT Defect Tracker and classified according to the following severity matrix:

| Severity Level | Definition | Resolution SLA | Launch Blocker? |
| :--- | :--- | :---: | :---: |
| **P0 — Blocker** | System crash, data loss, login failure, security vulnerability. | **$< 4$ Hours** | **YES (Must be 0)** |
| **P1 — Critical** | Primary feature broken (e.g. task creation fails), no workaround. | **$< 12$ Hours** | **YES (Must be 0)** |
| **P2 — Major** | Feature partially broken, functional workaround exists. | **$< 24$ Hours** | No ($\le 3$ allowed) |
| **P3 — Minor** | Cosmetic UI misalignment, typo, minor visual glitch. | Post-Launch V1.1 | No (Allowed) |

---

## 4. Detailed UAT Test Suite (10 Comprehensive Test Scenarios)

```
========================================================================================
NOVA MVP UAT SCENARIO SUITE (SC-01 THROUGH SC-10)
========================================================================================
```

### Scenario SC-01: New User Registration & Account Verification
* **Target Feature**: User Authentication (US-01)
* **Tester Persona**: New Team Contributor
* **Preconditions**: Staging environment accessible; user has a valid un-registered email address.
* **Test Steps**:
  1. Navigate to `https://staging.nova-app.io/signup`.
  2. Enter Full Name ("Jane Doe"), Email (`jane.doe@example.com`), and Password (`SecureP@ss2026`).
  3. Click "Create Account" button.
  4. Check email inbox for verification link and click verification link.
* **Expected Result**: Account successfully created; verification email received within 30 seconds; user redirected to workspace creation screen upon clicking verification link.
* **Pass / Fail Criteria**: **PASS** if login token generated and user lands on dashboard.

---

### Scenario SC-02: User Login & JWT Session Management
* **Target Feature**: User Authentication (US-02)
* **Tester Persona**: Existing Project Member
* **Preconditions**: User account verified.
* **Test Steps**:
  1. Navigate to `https://staging.nova-app.io/login`.
  2. Enter valid credentials and click "Log In".
  3. Verify JWT token stored in browser session.
  4. Refresh page and verify session remains active without re-login prompt.
* **Expected Result**: Login succeeds instantaneously ($< 500\text{ms}$); user session persists across browser refresh.
* **Pass / Fail Criteria**: **PASS** if user directed to workspace homepage.

---

### Scenario SC-03: Create New Project Workspace
* **Target Feature**: Project Management (US-05)
* **Tester Persona**: Project Manager
* **Preconditions**: User logged in as Project Manager / Admin.
* **Test Steps**:
  1. Click "+ New Project" button on navigation sidebar.
  2. Enter Project Name ("Alpha Software Launch"), Project Key ("ALPHA"), and Description.
  3. Select Start Date (Current Date) and Target Launch Date (+6 Weeks).
  4. Click "Create Workspace".
* **Expected Result**: Project successfully created; added to active project list; workspace dashboard initialized.
* **Pass / Fail Criteria**: **PASS** if project details match user input exactly.

---

### Scenario SC-04: Project Member Invite & RBAC Permission Enforcement
* **Target Feature**: Team Management & RBAC (US-14, US-15)
* **Tester Persona**: Workspace Admin
* **Preconditions**: Project "Alpha" exists.
* **Test Steps**:
  1. Open Project Settings $\rightarrow$ Team Members tab.
  2. Click "Invite Member".
  3. Enter email (`developer1@example.com`) and assign role "Contributor".
  4. Log in as `developer1@example.com` and attempt to access Admin-only Project Delete button.
* **Expected Result**: Invitation email dispatched; developer joins project; Admin-only "Delete Project" button is hidden/disabled for Contributor role.
* **Pass / Fail Criteria**: **PASS** if RBAC permissions strictly enforced.

---

### Scenario SC-05: Create Task with Priority & Due Date
* **Target Feature**: Task Management (US-09, US-11)
* **Tester Persona**: Project Lead
* **Preconditions**: User inside Project "Alpha".
* **Test Steps**:
  1. Click "+ Add Task" button on Kanban board.
  2. Enter Task Title ("Implement Auth Middleware"), Description, Priority ("Urgent"), Assignee ("Alex Backend"), and Due Date (Tomorrow).
  3. Click "Save Task".
* **Expected Result**: Task card immediately renders in "To Do" column; displays red "Urgent" priority badge and due date label.
* **Pass / Fail Criteria**: **PASS** if task saved in database and visible on board.

---

### Scenario SC-06: Drag-and-Drop Kanban Status Transition
* **Target Feature**: Task Status Workflow (US-12)
* **Tester Persona**: Software Developer
* **Preconditions**: Task "Implement Auth Middleware" exists in "To Do" column.
* **Test Steps**:
  1. Click and drag task card from "To Do" column.
  2. Drop task card into "In Progress" column.
  3. Refresh web page to verify persistence.
* **Expected Result**: Card smoothly transitions column; database status updates to `IN_PROGRESS`; state persists after refresh.
* **Pass / Fail Criteria**: **PASS** if status update logged in activity feed.

---

### Scenario SC-07: Add Rich Text Task Comments
* **Target Feature**: Collaboration & Task Comments (US-13)
* **Tester Persona**: QA Engineer
* **Preconditions**: Open existing task card modal.
* **Test Steps**:
  1. Click on task card to open detailed drawer modal.
  2. Scroll to Comments section.
  3. Type comment: `"API endpoint tested successfully on Staging."`
  4. Click "Post Comment".
* **Expected Result**: Comment instantly posted with user avatar, name, and current timestamp.
* **Pass / Fail Criteria**: **PASS** if comment persists in thread.

---

### Scenario SC-08: Executive Dashboard KPI & Progress Bar Rendering
* **Target Feature**: Executive Dashboard (US-16)
* **Tester Persona**: Executive Leader
* **Preconditions**: Project contains 10 completed tasks and 5 open tasks.
* **Test Steps**:
  1. Navigate to Executive Dashboard tab.
  2. Inspect KPI summary cards: Active Projects, Open Tasks, Completed Tasks, Overdue Tasks.
  3. Verify Progress Bar completion percentage calculation ($\frac{10}{15} = 67\%$).
* **Expected Result**: KPI numbers update dynamically and match backend task counts accurately.
* **Pass / Fail Criteria**: **PASS** if progress bar calculates percentage accurately.

---

### Scenario SC-09: AI Smart Task Recommendation Engine
* **Target Feature**: AI Task Insights (US-19 / CR-001)
* **Tester Persona**: Engineering Team Lead
* **Preconditions**: Workspace contains tasks with impending due dates within 24 hours.
* **Test Steps**:
  1. Open Dashboard homepage.
  2. Inspect "NOVA AI Recommendation Banner".
  3. Verify top-recommended task matches the item with nearest SLA due date and highest priority tag.
  4. Click "Accept Recommendation" button.
* **Expected Result**: AI banner displays accurate priority suggestion; accepting recommendation elevates task focus.
* **Pass / Fail Criteria**: **PASS** if recommendation algorithm evaluates SLA correctly.

---

### Scenario SC-10: End-to-End System Performance & Mobile Responsiveness
* **Target Feature**: System Reliability & Mobile Compatibility
* **Tester Persona**: Mobile Flutter Tester / QA Lead
* **Preconditions**: Access Staging environment via mobile viewport ($375\times 812\text{px}$).
* **Test Steps**:
  1. Open NOVA app on mobile browser / Flutter build.
  2. Execute navigation across Dashboard, Kanban Board, and Task Drawer.
  3. Measure visual rendering time and UI scaling.
* **Expected Result**: UI layout scales fluidly; zero horizontal scrolling glitch; page load time $< 1.5\text{s}$.
* **Pass / Fail Criteria**: **PASS** if mobile viewport fully functional.

---

## 5. UAT Exit Criteria & Formal Sign-Off

UAT will be declared complete and approved for production release when all the following conditions are satisfied:

1. **Scenario Pass Rate**: 100% pass rate achieved across all 10 UAT scenarios (SC-01 to SC-10).
2. **Defect Status**: Zero open P0 (Blocker) defects and zero open P1 (Critical) defects.
3. **Sign-off Approval**: Formal signatures obtained from Product Manager, Lead QA Engineer, and PM Intern.

### Formal Sign-Off Form

`[SIGNED & APPROVED]`  
**Lead Product Manager Signature:** Date: Week 9, Friday  

`[SIGNED & APPROVED]`  
**Lead QA Engineer Signature:** Date: Week 9, Friday  

`[SIGNED & APPROVED]`  
**Project Management Intern Signature:** Date: Week 9, Friday  

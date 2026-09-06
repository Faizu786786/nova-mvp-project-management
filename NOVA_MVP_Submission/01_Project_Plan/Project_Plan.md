# Deliverable 1: Master Project Plan & Execution Strategy

**Product:** NOVA — AI-Powered Team Productivity Platform  
**Target Timeline:** 10 Weeks (5 Two-Week Agile Sprints)  
**Author:** Project Management Intern  
**Associated Artifact:** [`NOVA_MVP_Master_Project_Plan.xlsx`](file:///d:/PROJECTS/NOVA-MVP/NOVA_MVP_Submission/01_Project_Plan/NOVA_MVP_Master_Project_Plan.xlsx)  

---

## 1. Executive Summary & Project Goal

NOVA is a cloud-native SaaS product designed to help high-performing teams streamline project management, task assignment, real-time collaboration, workflow automation, team productivity tracking, and AI-driven task recommendations. 

The primary objective of this project is to take NOVA from concept to production launch within a strict **10-week execution window**, utilizing a 10-person cross-functional team.

---

## 2. Product Backlog & Prioritization Framework

### Prioritization Methodology: MoSCoW + RICE Scoring

To maximize ROI and guarantee on-time delivery within the 10-week constraint, we combined **MoSCoW Prioritization** (P0-P3) with **RICE Scoring**:

$$\text{RICE Score} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$$

* **Reach**: Estimated active users impacted per sprint (100 - 1,000 users).
* **Impact**: Value contribution to MVP success ($3 = \text{Massive}$, $2 = \text{High}$, $1 = \text{Medium}$, $0.5 = \text{Low}$).
* **Confidence**: Percentage certainty in estimates ($100\% = 1.0$, $90\% = 0.9$, $80\% = 0.8$, $70\% = 0.7$).
* **Effort**: Developer person-sprints required ($1$ to $3$).

---

### Detailed Product Backlog (19 User Stories across 6 Epics)

| Story ID | Epic | Feature | User Story Description | Acceptance Criteria | MoSCoW | RICE Score | Est (Pts) | Target Sprint | Owner |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **US-01** | Auth | Sign Up | As a user, I want to create an account so I can access NOVA. | Validates email format, password strength ($\ge 8$ chars), sends verification link. | **P0 (Must)** | **1350.0** | 3 | Sprint 1 | Backend Dev 1 |
| **US-02** | Auth | Login | As a user, I want to log in securely so I can access my workspace. | Issues JWT bearer token, enforces rate limiting, clear error messages. | **P0 (Must)** | **1350.0** | 3 | Sprint 1 | Backend Dev 1 |
| **US-03** | Auth | Forgot Password | As a user, I want to reset my password if forgotten. | Sends single-use secure reset link via email, expires in 15 mins. | **P1 (Should)** | **400.0** | 3 | Sprint 1 | Backend Dev 2 |
| **US-04** | Auth | User Profile | As a user, I want to update my avatar and profile details. | Allows updating full name, job title, profile picture upload ($< 2\text{MB}$). | **P1 (Should)** | **1440.0** | 2 | Sprint 1 | Front-End Dev 1 |
| **US-05** | Project Mgmt | Create Project | As a lead, I want to create a new project workspace. | Input title, key, description, start/target end dates. | **P0 (Must)** | **900.0** | 5 | Sprint 2 | Backend Dev 2 |
| **US-06** | Project Mgmt | Edit Project | As a lead, I want to modify project details and settings. | Updates metadata; enforces owner/admin permission checks. | **P0 (Must)** | **720.0** | 3 | Sprint 2 | Front-End Dev 2 |
| **US-07** | Project Mgmt | Delete Project | As an admin, I want to archive or soft-delete a project. | Displays confirmation prompt; soft deletes with 30-day restore option. | **P1 (Should)** | **400.0** | 2 | Sprint 2 | Backend Dev 1 |
| **US-08** | Project Mgmt | Project Dashboard | As a manager, I want a high-level project view. | Displays project completion %, active member avatars, task counts. | **P0 (Must)** | **900.0** | 5 | Sprint 2 | Flutter Dev 1 |
| **US-09** | Task Mgmt | Create Task | As a member, I want to create tasks within a project. | Fields: title, description, priority, assignee, due date, tags. | **P0 (Must)** | **900.0** | 5 | Sprint 3 | Backend Dev 1 |
| **US-10** | Task Mgmt | Assign Task | As a lead, I want to assign tasks to team members. | Assignee receives task, activity feed logs assignment event. | **P0 (Must)** | **1350.0** | 3 | Sprint 3 | Front-End Dev 1 |
| **US-11** | Task Mgmt | Priority & Due Date | As a user, I want to set task priority and target due date. | Badges for Low/Med/High/Urgent; due date picker with overdue warning. | **P0 (Must)** | **1800.0** | 2 | Sprint 3 | Flutter Dev 2 |
| **US-12** | Task Mgmt | Status Workflow | As a user, I want to move tasks across status stages. | Statuses: To Do $\rightarrow$ In Progress $\rightarrow$ In Review $\rightarrow$ Done. Drag-and-drop support. | **P0 (Must)** | **900.0** | 5 | Sprint 3 | Front-End Dev 2 |
| **US-13** | Task Mgmt | Task Comments | As a member, I want to comment on tasks. | Rich text comments, timestamped author tags, mention system. | **P1 (Should)** | **640.0** | 3 | Sprint 3 | Backend Dev 2 |
| **US-14** | Team Mgmt | Add/Remove Members| As an admin, I want to invite team members. | Sends email invitation link; revokes access instantly on removal. | **P0 (Must)** | **1215.0** | 3 | Sprint 2 | Backend Dev 1 |
| **US-15** | Team Mgmt | Member Roles | As an admin, I want role-based access control (RBAC). | Roles: Workspace Admin, Project Manager, Contributor, Viewer. | **P0 (Must)** | **810.0** | 5 | Sprint 2 | Backend Dev 2 |
| **US-16** | Dashboard | Executive KPIs | As an executive, I want summary KPI counts. | Cards: Active Projects, Open Tasks, Completed Tasks, Overdue Tasks. | **P0 (Must)** | **900.0** | 5 | Sprint 4 | Front-End Dev 1 |
| **US-17** | Dashboard | Team Productivity | As a manager, I want productivity charts. | Completion trend charts, story points completed vs committed per developer. | **P1 (Should)** | **373.3** | 5 | Sprint 4 | Front-End Dev 2 |
| **US-18** | Notifications | Alerts Engine | As a user, I want in-app and email alerts. | Alerts generated on task assignment, status change, and upcoming due date. | **P1 (Should)** | **640.0** | 3 | Sprint 4 | Backend Dev 1 |
| **US-19** | AI Insights | AI Task Recommender| As a user, I want smart task recommendations. | AI engine recommends top 3 prioritized tasks based on SLA & urgency. | **P1 (Should)** | **420.0** | 5 | Sprint 4 | Backend Dev 2 |

---

## 3. Master 10-Week Project Timeline & Work Breakdown Structure (WBS)

```
========================================================================================
NOVA MVP 10-WEEK MASTER ROADMAP & GANTT CHART
========================================================================================
Phase / Workstream          W1  W2  W3  W4  W5  W6  W7  W8  W9  W10   Owner
----------------------------------------------------------------------------------------
1. Requirements & Design    [========]                                 UI/UX & PM
2. Architecture & Auth      [========]                                 Backend & DevOps
3. Project Mgmt Engine              [========]                         Backend & Mobile
4. Team Mgmt & RBAC                 [========]                         Backend & Web
5. Task Mgmt Engine                         [========]                 Full-Stack Team
6. Dashboard & Analytics                             [========]        Frontend Team
7. AI Task Rules Engine                              [========]        Backend Lead
8. End-to-End QA & Hardening                                  [========] QA Lead & Devs
9. UAT & Client Sign-off                                      [====]    PM & Exec Team
10. Production Deployment                                        [==]   DevOps Lead
========================================================================================
MILESTONES:
M1: Sprint 1 Review & Auth Sign-off (End of Week 2)
M2: Sprint 2 Review & Core Workspace Engine Ready (End of Week 4)
M3: Sprint 3 Review & Task Engine Feature Complete (End of Week 6)
M4: Code Freeze & UAT Environment Ready (End of Week 8)
M5: Production Launch & Post-Launch Retrospective (End of Week 10)
```

---

## 4. Sprint Schedule & Capacity Breakdown

### Capacity Formula
$$\text{Sprint Capacity} = 10 \text{ Team Members} \times 80 \text{ Hours/Sprint} \times 80\% \text{ Focal Factor} = 640 \text{ Engineering Hours}$$
At an average velocity of **12-15 engineering hours per Story Point**, total targeted capacity is **40-45 Story Points per Sprint**.

### Sprint Details

#### Sprint 1 (Weeks 1-2): Foundation, Authentication & Design
* **Sprint Goal**: Establish project infrastructure, finalized UI/UX design tokens, and user authentication APIs.
* **Committed Points**: 38 Points
* **Key Tasks**:
  1. Set up Dockerized Postgres DB & Redis caching layer.
  2. Implement OpenAPI specs & JWT Authentication backend APIs.
  3. Create Flutter mobile & Web React component scaffolding.
  4. Finalize Figma design system & wireframes for all 5 core modules.
* **Definition of Done (DoD)**: Auth APIs passed unit tests ($>85\%$ coverage), UI kit approved, CI/CD pipeline active.

#### Sprint 2 (Weeks 3-4): Project Management & Team RBAC
* **Sprint Goal**: Build core workspace project management engine and user role management.
* **Committed Points**: 42 Points
* **Key Tasks**:
  1. Implement Project CRUD APIs and database relational models.
  2. Implement Workspace Member Invite flow & RBAC middleware.
  3. Build Mobile Flutter & Web Project list and dashboard UI.
* **Definition of Done (DoD)**: Projects created/edited with full permission enforcement, integration tests passing.

#### Sprint 3 (Weeks 5-6): Task Management Engine & Collaboration
* **Sprint Goal**: Deliver core task management, priority assignment, status transitions, and comments.
* **Committed Points**: 45 Points
* **Key Tasks**:
  1. Implement Task CRUD backend endpoints and database schemas.
  2. Build Drag-and-Drop Kanban Board for Web and Swipe-to-Status for Mobile.
  3. Implement Task Comment thread backend and frontend UI.
* **Definition of Done (DoD)**: Tasks editable in real time, zero P0 bugs, performance response time $< 200\text{ms}$.

#### Sprint 4 (Weeks 7-8): Executive Dashboard, Notifications & AI Recommender
* **Sprint Goal**: Implement analytics dashboard, notification engine, and AI-powered task recommendation engine.
* **Committed Points**: 41 Points
* **Key Tasks**:
  1. Build Executive KPI summary cards and team productivity charts.
  2. Implement Background Notification Worker (In-app alerts + Email delivery).
  3. Implement Phase 1 Rule-Based AI Task Recommendation API.
* **Definition of Done (DoD)**: Code freeze achieved, test coverage $>80\%$, staging environment deployed.

#### Sprint 5 (Weeks 9-10): QA Hardening, UAT Execution & Production Launch
* **Sprint Goal**: Execute comprehensive UAT, patch all identified defects, perform security audit, and launch to production.
* **Committed Points**: 25 Points (Testing & Fixes)
* **Key Tasks**:
  1. Run 10 formal UAT test scenarios with client/stakeholder group.
  2. Patch P1/P2 defects identified during testing.
  3. Execute security vulnerability audit and load performance testing (1,000 concurrent users).
  4. Deploy production infrastructure on AWS/GCP, run smoke tests, and hand off to operations.
* **Definition of Done (DoD)**: UAT sign-off received, zero critical/high defects open, production environment active.

---

## 5. RACI Resource Allocation Matrix

| Workstream / Phase | Product Manager | Project Manager | UI/UX Designer | Flutter Devs (2) | Front-End Devs (2) | Backend Devs (2) | QA Lead | DevOps Eng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Requirements & Scope** | **Accountable (A)** | **Responsible (R)** | Consulted (C) | Informed (I) | Informed (I) | Consulted (C) | Informed (I) | Informed (I) |
| **2. UI/UX Wireframes** | Consulted (C) | **Accountable (A)** | **Responsible (R)** | Consulted (C) | Consulted (C) | Informed (I) | Informed (I) | Informed (I) |
| **3. API & Database Dev** | Informed (I) | **Accountable (A)** | Informed (I) | Consulted (C) | Consulted (C) | **Responsible (R)** | Consulted (C) | Consulted (C) |
| **4. Mobile & Web Frontend** | Informed (I) | **Accountable (A)** | Consulted (C) | **Responsible (R)** | **Responsible (R)** | Consulted (C) | Informed (I) | Informed (I) |
| **5. Testing & Quality** | Informed (I) | **Accountable (A)** | Informed (I) | Consulted (C) | Consulted (C) | Consulted (C) | **Responsible (R)** | Informed (I) |
| **6. DevOps & Deployment** | Informed (I) | **Accountable (A)** | Informed (I) | Informed (I) | Informed (I) | Consulted (C) | Consulted (C) | **Responsible (R)** |
| **7. UAT & Release** | **Accountable (A)** | **Responsible (R)** | Consulted (C) | Support (S) | Support (S) | Support (S) | **Responsible (R)** | Informed (I) |

---

## 6. Dependency Tracker (12 Critical Dependencies)

| Dep ID | Dependency Description | Predecessor | Owner | Risk Level | Mitigation Strategy | Status |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| **DEP-01** | UI Component Library required before Frontend implementation. | Figma Design System | UI/UX Designer | **High** | Front-load design system in Sprint 1; freeze tokens by Day 7. | Closed |
| **DEP-02** | Auth API endpoints required before Web/Mobile Login integration. | DB Schema & Auth API | Backend Dev 1 | **Critical** | Pair backend devs to ship JWT Auth by Sprint 1 Day 8. | Closed |
| **DEP-03** | Project Schema required before Task DB relation creation. | Project CRUD API | Backend Dev 2 | **Medium** | Define unified relational schema in Sprint 1. | Closed |
| **DEP-04** | Backend Task API required before Kanban Board integration. | Task Endpoints | Backend Dev 1 | **High** | Provide mock JSON responses by Sprint 3 Day 2 for frontend devs. | Open |
| **DEP-05** | Real-time WebSocket setup required for instant in-app alerts. | Infrastructure | DevOps Eng | **Medium** | Fall back to HTTP polling if WebSocket latency spikes $>300\text{ms}$. | Open |
| **DEP-06** | Task Priority API required before AI Recommendation Engine. | Task CRUD Engine | Backend Lead | **High** | Build rule-based heuristic fallback in parallel during Sprint 4. | Open |
| **DEP-07** | QA Test Suite creation requires stable API build. | Sprint 3 Code Freeze | QA Lead | **High** | QA engineer writes API automation tests during Sprint 3 development. | Open |
| **DEP-08** | Staging environment required before UAT execution. | CI/CD Pipeline | DevOps Eng | **Critical** | Deploy staging infrastructure on AWS by end of Sprint 3. | Open |
| **DEP-09** | SMTP Gateway authorization required for Email Notifications. | AWS SES Account | DevOps Eng | **Low** | Request production SES quota early in Sprint 2. | Closed |
| **DEP-10** | Third-party analytics service setup (PostHog/Mixpanel). | Analytics SDK | Front-End Dev 1 | **Low** | Integrate SDK wrapper early; toggle via feature flag. | Open |
| **DEP-11** | Apple App Store & Google Play Developer Accounts approval. | Store Accounts | PM Intern | **Medium** | Submit store developer verifications in Week 2. | Closed |
| **DEP-12** | Final Security Penetration Test sign-off before Production launch.| Production Build | QA & DevOps | **High** | Run OWASP automated ZAP security scan on Staging build in Week 8. | Open |

---

## 7. Risk Register (10 Project Risks Scored & Managed)

| Risk ID | Category | Risk Description | Likelihood (1-5) | Impact (1-5) | Severity Score | Severity Level | Proactive Mitigation Strategy | Contingency Plan | Owner |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| **R-01** | Technical | Backend API delivery delayed due to complex DB schema. | 4 | 4 | **16** | **CRITICAL** | Start API contract design in Sprint 1; pair backend devs. | Provide mock JSON stubs to frontend devs. | Backend Lead |
| **R-02** | Scope | Scope creep: Unplanned AI feature requested in Week 6. | 4 | 3 | **12** | **HIGH** | Establish Change Control Board (CCB); use Phase 1 heuristic scope swap. | Defer full ML model to V1.1 backlog. | PM Intern |
| **R-03** | Resource | QA bottleneck during Sprint 5 testing window. | 3 | 4 | **12** | **HIGH** | Mandate developer unit testing and automated integration tests in Sprints 2-4. | Reallocate 1 Frontend Dev to QA testing. | QA Lead |
| **R-04** | Design | UI/UX wireframe delays block front-end implementation. | 3 | 3 | **9** | **MEDIUM** | Front-load design reviews; complete component library by end of Sprint 1. | Use pre-styled Tailwind/Chakra UI fallback components. | UI/UX Designer |
| **R-05** | DevOps | Production environment configuration failure on launch day. | 2 | 4 | **8** | **MEDIUM** | Deploy staging environment in Sprint 2; run full dry-run deployment in Sprint 4. | Rollback to previous stable staging tag via Terraform script. | DevOps Engineer |
| **R-06** | Security | Authentication vulnerability or unencrypted token leak. | 2 | 5 | **10** | **HIGH** | Implement JWT standard with HTTPS, bcrypt password hashing, and security audit. | Revoke all active tokens and force password reset. | Backend Dev 1 |
| **R-07** | Integration| Flutter mobile app and Web frontend UI state mismatch. | 3 | 3 | **9** | **MEDIUM** | Share unified OpenAPI/Swagger specification across mobile and web teams. | Align payload schema in daily standups. | Engineering Lead |
| **R-08** | Dependency | Third-party email notification service downtime. | 2 | 3 | **6** | **MEDIUM** | Abstract notification handler with fallback queuing (Redis/Celery). | Retry queue with exponential backoff. | Backend Dev 2 |
| **R-09** | Performance| Dashboard slow response time under heavy task load. | 2 | 4 | **8** | **MEDIUM** | Add DB indexing on task status and project IDs; implement caching. | Implement paginated loading ($25\text{ items/page}$). | Backend Lead |
| **R-10** | Stakeholder| Delayed UAT sign-off from executive management. | 3 | 3 | **9** | **MEDIUM** | Conduct weekly demo showcases; align UAT criteria at start of Sprint 4. | Schedule formal async review session. | Product Manager |

---

## 8. Summary of Alignment with Evaluation Rubric

* **Project Planning (15 Marks)**: Complete project goal, business context, WBS, and governance framework established.
* **Requirements / Backlog (10 Marks)**: 19 user stories prioritized via MoSCoW and RICE scoring.
* **Sprint Planning (10 Marks)**: 5 two-week Agile sprints defined with goals, capacity, tasks, and DoD.
* **Timeline / Gantt (10 Marks)**: 10-week visual roadmap and milestone schedule mapped.
* **Dependency & Risk Management (20 Marks)**: 12 dependencies and 10 risks scored with proactive mitigations.

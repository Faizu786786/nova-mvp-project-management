# Deliverable 9: Project Retrospective & Recruiter Interview Master Preparation Guide

**Product:** NOVA — AI-Powered Team Productivity Platform  
**Author:** Project Management Intern  
**Target Purpose:** Post-Launch Retrospective & 100% Recruiter Interview Readiness  

---

## PART I: Sprint & Project Retrospective

Following the fictional production launch of NOVA MVP in Week 10, the team conducted a formal Project Retrospective to evaluate performance, document lessons learned, and establish continuous improvement actions.

### 1. What Went Well? (3 Key Successes)
1. **Disciplined Scope & Prioritization**: Combining MoSCoW prioritization with RICE scoring allowed the team to deliver 100% of P0 core MVP user stories without incurring scope creep.
2. **Proactive Blocker & Dependency Mitigation**: Deploying mock JSON API stubs during Sprint 3 allowed front-end web and mobile developers to build UI components uninterrupted while backend developers resolved DB migrations.
3. **Seamless Cross-Functional Collaboration**: Daily standups, shared OpenAPI Swagger contracts, and joint UAT execution fostered high team morale and zero communication silos across all 10 team members.

### 2. What Did Not Go Well? (3 Key Challenges)
1. **Initial Database Schema Complexity**: Backend DB migration scripts in Sprint 1 and Sprint 3 took longer than estimated, causing temporary backend bottlenecks.
2. **Testing Bottleneck Risk in Sprint 4**: Mid-sprint code drops created a temporary QA backlog due to heavy manual regression testing before automated API testing scripts were finalized.
3. **Mid-Project Change Request Friction**: The introduction of AI Task Recommendations in Week 6 caused initial uncertainty until the Change Control Board approved the Option D Scope Swap strategy.

### 3. What Should We Improve? (Actionable Matrix)

| What Happened | Impact | Action Item | Owner | Target SLA |
| :--- | :--- | :--- | :--- | :--- |
| **API Delivery Was Late** | QA testing was delayed by 1.5 days in Sprint 3. | **Freeze OpenAPI Contracts on Day 3** of every sprint; require mock payload stubs before coding begins. | Tech Lead | Next Sprint |
| **Requirements Changed in W6** | Sprint 4 planning was disrupted for 48 hours. | **Establish Formal CCB Intake Form**; mandate a 5-day impact review window for all new scope requests. | PM Intern | Immediate |
| **QA Test Backlog in Mid-Sprint**| QA Engineer overwhelmed during code drops. | **Mandate Unit Test Coverage $\ge 80\%$** by developers before PR merge; expand automated API test suite. | QA Lead | Next Sprint |

---

## PART II: Recruiter Interview Master Q&A Guide

Below are executive-level, structured answers for all 12 interview review questions listed on Page 17 of the assignment PDF. Memorizing and utilizing these responses will demonstrate senior-level project management maturity to recruiters.

---

### Question 1: What would you do if a developer misses a critical deadline?
**Recruiter-Grade Answer:**
> *"When a developer misses a critical deadline, I follow a proactive, empathetic, and solution-oriented 4-step protocol:*
> 1. **Assess Root Cause Immediately**: I have a private 1-on-1 with the developer to understand if the delay stems from technical complexity, unclear requirements, external dependencies, or personal bandwidth.
> 2. **Protect the Critical Path**: I look for immediate unblocking actions. For example, if a backend API is delayed, I request static mock JSON stubs so frontend developers are not idled.
> 3. **Rebalance Workload**: I evaluate if another developer with available capacity can pair-program or offload non-critical subtasks.
> 4. **Update the Schedule & Communicate**: If the delay impacts a sprint milestone, I adjust task allocations in Jira, update our burndown chart, and inform the Product Manager with revised SLA target dates."*

---

### Question 2: How would you handle scope creep?
**Recruiter-Grade Answer:**
> *"I manage scope creep through a formal Change Control Board (CCB) governance framework:*
> 1. **Log & Acknowledge**: I never outright reject stakeholder ideas. Instead, I log the request in our Change Request backlog.
> 2. **Multi-Dimensional Impact Analysis**: I evaluate the impact across 6 dimensions: Scope, Timeline, Cost, Resources, Quality, and Existing Features.
> 3. **Present Strategic Trade-Off Options**: I present the stakeholder with 3-4 viable options (e.g. Scope Swap, Schedule Extension, or Phased Rollout in V1.1).
> 4. **Require Formal CCB Sign-Off**: No unplanned story points enter an active sprint without an approved Scope Swap (exchanging an equivalent point value feature) or explicit timeline adjustment."*

---

### Question 3: How do you prioritize conflicting requirements?
**Recruiter-Grade Answer:**
> *"I resolve requirement conflicts objectively using a data-driven prioritization framework combining **MoSCoW** and **RICE Scoring** ($\text{Reach} \times \text{Impact} \times \text{Confidence} / \text{Effort}$):*
> 1. **Align on Business Objectives**: I tie every requirement back to our primary project goals and OKRs (e.g. 10-week MVP launch date and user onboarding friction).
> 2. **Calculate RICE Scores**: Requirements are quantitatively scored. Higher RICE scores represent greater ROI per engineering hour.
> 3. **Facilitate Alignment Workshop**: If two executive stakeholders disagree, I present the RICE scoring matrix and cost-benefit trade-offs to facilitate a consensus decision anchored in data rather than subjective opinion."*

---

### Question 4: What is the difference between a risk and an issue?
**Recruiter-Grade Answer:**
> *"The key distinction lies in probability and timing:*
> * **A Risk** is a potential future event that has not yet occurred, but if it does, it will impact project objectives (e.g. *'Backend API delivery might be delayed due to complex DB migrations'*). Risks are tracked in the Risk Register with Likelihood $\times$ Impact scores and proactive mitigations.
> * **An Issue** is a current, active problem that is happening right now and directly blocking project execution (e.g. *'The staging server database crashed this morning'*). Issues are tracked in the Blocker Log with immediate SLA resolution actions."*

---

### Question 5: What would you escalate to management?
**Recruiter-Grade Answer:**
> *"I escalate issues to executive management selectively based on impact thresholds:*
> 1. **Timeline Deviations**: Any unmitigated risk that threatens to breach our fixed launch milestone by more than 3 business days.
> 2. **Unresolved Resource Conflicts**: Severe resource bottlenecks or inter-departmental dependencies that cannot be resolved at the team lead level.
> 3. **Critical Scope Changes**: Unplanned executive scope requests (like CR-001) that require formal CCB approval for scope swaps or budget changes.
> 4. **Budget / Vendor Failures**: High-cost third-party vendor outages or contract breaches.
> *Before escalating, I always prepare an Impact Brief with at least 2 recommended decision options so management can make a fast, informed decision."*

---

### Question 6: How would you handle a stakeholder who keeps changing requirements?
**Recruiter-Grade Answer:**
> *"I handle frequent requirement changes by establishing clear Agile sprint boundaries and empathetic education:*
> 1. **Enforce Sprint Lock Window**: I educate stakeholders on Agile principles—once a 2-week sprint begins, the sprint scope is locked to protect developer flow state.
> 2. **Establish a Backlog Grooming Intake**: New ideas are directed to the Product Backlog for evaluation during the next Sprint Planning meeting.
> 3. **Demonstrate Trade-Off Costs**: I visually demonstrate the cost of late changes using a Scope Swap matrix (e.g. *'We can add Feature X in Sprint 4, but we will need to move Feature Y to Sprint 5'*).
> 4. **Implement Regular Demo Reviews**: Weekly sprint demos give stakeholders early visibility, reducing late-stage surprises."*

---

### Question 7: How would you decide what goes into an MVP?
**Recruiter-Grade Answer:**
> *"I define MVP scope using the **Lean Product Process** and **MoSCoW Prioritization**:*
> 1. **Identify Core User Value Proposition**: What is the single primary problem NOVA solves? (Streamlining team task assignment and project tracking).
> 2. **Map User Journeys**: I break down the end-to-end user path from Sign-up $\rightarrow$ Project Creation $\rightarrow$ Task Assignment $\rightarrow$ Dashboard Analytics.
> 3. **Filter P0 Must-Haves**: Only features essential to completing the core user journey make the P0 MVP cut. Non-essential enhancements (like complex custom themes or advanced email digests) are placed in the V1.1 backlog.
> 4. **Validate Against Constraints**: I verify that total P0 story points fit within our 10-week engineering capacity buffer."*

---

### Question 8: How do you know whether a project is actually on track?
**Recruiter-Grade Answer:**
> *"I rely on objective quantitative metrics rather than subjective team status reports:*
> 1. **Earned Value Management (EVM)**: I track **Schedule Performance Index (SPI = EV / PV)** and **Cost Performance Index (CPI = EV / AC)**. An SPI $\ge 1.0$ proves we are physically delivering planned work on schedule.
> 2. **Sprint Velocity & Burndown**: I monitor daily sprint burndown charts to ensure velocity is linear and not back-loaded to the final day.
> 3. **Working Software Milestone Gates**: I verify that features pass Definition of Done (DoD) and automated unit tests, rather than trusting '90% done' verbal claims.
> 4. **Blocker & Risk Trends**: A low number of open P0 blockers ($<2$) indicates high delivery health."*

---

### Question 9: What would you do if the launch date cannot move?
**Recruiter-Grade Answer:**
> *"If the launch date is fixed and non-negotiable (Triple Constraint restriction), I manage project flexibility through **Scope Flexing** (reducing feature depth) rather than sacrificing quality or burning out the team:*
> 1. **Trim P1/P2 Features**: I move non-essential P1 features to the post-launch V1.1 roadmap.
> 2. **Simplify Feature Implementation**: For example, instead of building a complex ML recommendation model, I deploy a lightweight rule-based heuristic algorithm.
> 3. **Optimize Resource Efficiency**: I pair developers on complex tasks and deploy mock API stubs to remove cross-team wait times.
> 4. **Protect Testing Window**: I ensure QA testing and UAT windows remain untouched so launch quality is never compromised."*

---

### Question 10: How would you manage a dependency between two teams?
**Recruiter-Grade Answer:**
> *"I manage cross-team dependencies proactively using a 4-step framework:*
> 1. **Map Predecessor Contracts Early**: In Sprint 1 planning, I identify all cross-team handoffs and document them in our Dependency Tracker with explicit SLA target dates.
> 2. **Establish Standard API Contracts**: I require backend and frontend leads to agree on OpenAPI / Swagger specs before coding begins.
> 3. **Deploy Mock JSON Endpoints**: Backend teams deploy static mock APIs early so frontend teams can build and test UI components in parallel without waiting for live DB integrations.
> 4. **Track Handoffs in Standups**: Cross-team dependency status is reviewed daily during standup blockers."*

---

### Question 11: What metrics would you report to management?
**Recruiter-Grade Answer:**
> *"I tailor metrics for executive management to provide a clear, high-level picture of health and ROI:*
> 1. **Overall Project RAG Health**: Green / Yellow / Red indicator backed by Earned Value SPI ($1.05$) and CPI ($1.00$).
> 2. **Milestone & Release Readiness**: % overall completion (e.g. 42% at Week 4), target launch date adherence, and Sprint Velocity trends.
> 3. **Quality & Defect Metrics**: Number of open P0/P1 bugs, UAT test scenario pass rate ($100\%$), and automated test coverage ($>80\%$).
> 4. **Key Risks & CCB Decisions Required**: Top 3 active risks with mitigations and any pending scope change decisions."*

---

### Question 12: How would you run a sprint retrospective?
**Recruiter-Grade Answer:**
> *"I facilitate engaging, psychological-safe Sprint Retrospectives using a structured 5-stage format:*
> 1. **Set the Stage (5 mins)**: Establish an open, blame-free environment focused on team continuous improvement.
> 2. **Gather Data (15 mins)**: Use a collaborative board (e.g. Miro/Mural) organized into 3 columns: *'What Went Well'*, *'What Didn't Go Well'*, and *'Ideas for Improvement'*.
> 3. **Generate Insights & Vote (10 mins)**: The team groups duplicate items and dot-votes on the top 2-3 critical operational challenges.
> 4. **Formulate Action Items (10 mins)**: For each voted item, we define a clear **SMART Action Item** structured as: *What Happened $\rightarrow$ Impact $\rightarrow$ Action Item $\rightarrow$ Owner $\rightarrow$ Due Date*.
> 5. **Close & Track (5 mins)**: Action items are entered directly into Jira as sprint tasks for the next sprint."*

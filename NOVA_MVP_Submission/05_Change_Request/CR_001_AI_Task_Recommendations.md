# Deliverable 5: Change Request Document (CR-001)

**Change Request ID:** CR-001  
**Project:** NOVA MVP — AI-Powered Team Productivity Platform  
**Date Submitted:** Week 6, Day 1  
**Sponsor / Requester:** Executive Management & Product Lead  
**Title:** Inclusion of AI-Powered Task Recommendations in MVP Release  
**Status:** Under Change Control Board (CCB) Evaluation  

---

## 1. Requirement Description

### What is being requested?
During Week 6 of the 10-week execution plan, executive management submitted a high-priority product enhancement request:

> *"We want AI-powered task recommendations included in the MVP before launch."*

The proposed feature requires NOVA to dynamically analyze a user's open tasks, due dates, priority tags, and historical completion velocity to generate a top-3 recommended task list ("Smart Priority Focus") on the user's daily dashboard.

---

## 2. Multi-Dimensional Impact Analysis

Adding an unplanned feature at Week 6 (60% through the project timeline) introduces significant systemic impacts across 6 core project dimensions:

```
+-----------------------------------------------------------------------------------+
| IMPACT EVALUATION SUMMARY MATRIX                                                  |
+-------------------+---------------------------------------------------------------+
| Dimension         | Detailed Impact & Severity Assessment                         |
+-------------------+---------------------------------------------------------------+
| 1. Scope          | +5 Story Points (~60 engineering hours) added to Sprint 4.    |
| 2. Timeline       | Pushes code freeze into Week 9; risks delaying launch by 2 wks|
| 3. Cost           | $0 added dev cost, but +$4,000 staging cloud infrastructure.  |
| 4. Resources      | Diverts Backend Dev 2 & Frontend Dev 1 from Sprint 4 tasks.   |
| 5. Quality        | Reduces Sprint 5 QA test buffer from 10 days to 4 days.       |
| 6. Existing Feat. | Risks destabilizing Task Engine APIs and Dashboard UI.        |
+-------------------+---------------------------------------------------------------+
```

### Detailed Breakdown:
1. **Scope Impact**: Developing a machine-learning task recommendation engine requires custom data ingestion pipelines, model scoring logic, and UI badge integration (+5 Story Points).
2. **Timeline Impact**: Unmitigated absorption will consume 60 hours in Sprint 4, compressing QA regression testing in Sprint 5 and risking a 2-week launch delay (shifting release from Week 10 to Week 12).
3. **Cost Impact**: Direct labor cost remains unchanged ($0 additional headcount), but staging cloud infrastructure expenses increase by ~$4,000 if timeline extends.
4. **Resource Impact**: Reallocates Backend Dev 2 (API logic) and Front-End Dev 1 (UI integration), reducing capacity for Sprint 4 notifications.
5. **Quality Impact**: Severely compresses Sprint 5 QA testing window from 10 full days down to 4 days, elevating risk of undetected P1 production defects.
6. **Existing Feature Impact**: Requires schema modifications on the Task table to expose priority metadata for recommendation scoring.

---

## 3. Trade-Off Options Analysis

The Project Management team evaluated 4 potential strategies for handling CR-001:

### Option A: Absorb Feature Without Changing Launch Date
* **Description**: Force team to work overtime in Sprint 4 and Sprint 5 to build full ML recommendation engine while keeping Week 10 release date fixed.
* **Pros**: Delivers requested AI feature on original target date.
* **Cons**: Extreme team burnout; severe drop in QA test coverage; high probability of critical bugs at launch.
* **Risk Rating**: **CRITICAL (High Risk of Project Failure)**

### Option B: Pure Feature Scope Swap
* **Description**: Include AI task recommendations in Sprint 4, but defer non-essential Sprint 4 features (In-App & Email Notification Digest - US-18) to the V1.1 post-launch backlog.
* **Pros**: Maintains strict 10-week launch date; zero budget increase; keeps team workload balanced.
* **Cons**: Email notifications delayed to post-launch release.
* **Risk Rating**: **LOW (Controlled Scope Trade-Off)**

### Option C: Schedule Extension (Extend Launch by 2 Weeks)
* **Description**: Extend project timeline from 10 weeks to 12 weeks, adding an extra 2-week Sprint 6 dedicated to AI model development and testing.
* **Pros**: Delivers 100% of original scope plus full ML AI feature with complete QA coverage.
* **Cons**: Misses planned Q3 market launch window; increases cloud staging costs by $4,000; disappoints early access beta customers.
* **Risk Rating**: **MEDIUM (Schedule Variance)**

### Option D (RECOMMENDED HYBRID): Phased Rule-Based AI Engine Scope Swap
* **Description**: Build a lightweight, high-performance **Rule-Based Heuristic AI Task Recommendation Algorithm** in Sprint 4 (calculating task priority based on SLA due dates, priority weighting, and dependency block status) while swapping out non-essential email digest notifications to V1.1. Complex ML model training is deferred to V1.1 roadmap.
* **Pros**: Delivers immediate AI-driven task recommendation value to users in MVP; fits within 2 Story Points; maintains 10-week release date; keeps QA buffer 100% intact.
* **Cons**: Initial AI recommendations use deterministic heuristic algorithms rather than neural net ML models.
* **Risk Rating**: **VERY LOW (Optimal Value & Safety)**

---

## 4. Quantitative Trade-Off Decision Matrix

To ensure an objective, data-driven decision, options were evaluated using a weighted multi-criteria matrix ($1 = \text{Poor}$, $5 = \text{Excellent}$):

| Evaluation Criteria | Weight | Option A (Absorb) | Option B (Scope Swap) | Option C (Extend W12) | Option D (Hybrid Rec.) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Schedule Integrity (Week 10 Launch)** | 30% | 2.0 | 5.0 | 1.0 | **5.0** |
| **Product Quality & QA Coverage** | 25% | 1.0 | 4.0 | 5.0 | **5.0** |
| **Customer Value / AI Feature Match** | 20% | 4.0 | 4.0 | 5.0 | **4.5** |
| **Team Morale & Capacity Risk** | 15% | 1.0 | 4.5 | 4.0 | **5.0** |
| **Budget & Cost Control** | 10% | 3.0 | 5.0 | 2.0 | **5.0** |
| **WEIGHTED TOTAL SCORE** | **100%** | **1.95** | **4.55** | **3.30** | **4.90 (WINNER)** |

---

## 5. Final Strategic Recommendation & CCB Governance

### Final Recommendation
The Project Manager strongly recommends **Option D (Phased Rule-Based AI Scope Swap)**.

### Rationale
Option D allows NOVA to proudly market *"AI-Powered Smart Task Recommendations"* in its MVP launch campaign without incurring schedule delays, budget overruns, or software quality degradation. By delivering a fast, deterministic rule-based priority engine in Sprint 4 and swapping out non-critical email digests to V1.1, NOVA satisfies executive requirements while protecting the critical path to a successful Week 10 release.

### CCB Approval Section

`[APPROVED]` **Option D Selected**  
**Executive Sponsor Signature:** VP of Product & Engineering — Date: Week 6, Day 3  
**Project Manager Signature:** PM Intern — Date: Week 6, Day 3  

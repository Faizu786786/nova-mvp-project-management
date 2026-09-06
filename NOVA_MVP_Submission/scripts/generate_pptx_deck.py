import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # Set to widescreen 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Colors
    c_navy = RGBColor(15, 23, 42)      # #0F172A
    c_blue = RGBColor(30, 78, 120)     # #1F4E78
    c_cyan = RGBColor(6, 182, 212)     # #06B6D4
    c_white = RGBColor(255, 255, 255)
    c_gray = RGBColor(100, 116, 139)   # #64748B
    c_light_bg = RGBColor(248, 250, 252) # #F8FAFC
    c_card_bg = RGBColor(241, 245, 249)  # #F1F5F9

    blank_slide_layout = prs.slide_layouts[6]
    
    slides_data = [
        {
            "type": "title",
            "title": "NOVA MVP — Software Launch Plan",
            "subtitle": "End-to-End Project Management Strategy & Execution Framework\nPrepared by: Project Management Intern | Target Release: 10 Weeks"
        },
        {
            "type": "content",
            "title": "1. Executive Summary & Business Objective",
            "bullets": [
                "Product: NOVA — AI-Powered Team Productivity Platform (B2B SaaS).",
                "Business Need: High-performing teams lack consolidated task tracking, velocity analytics, and automated AI priorities.",
                "Target Objective: Plan, execute, and launch NOVA MVP within a strict 10-week execution window (5 Agile Sprints).",
                "Team Allocation: 10 Cross-Functional Headcount (1 PM, 1 Prod Mgr, 1 UI/UX, 2 Flutter, 2 Frontend, 2 Backend, 1 QA, 1 DevOps).",
                "Key Milestone: 100% on-time release with zero P0 critical bugs and >90% feature delivery."
            ]
        },
        {
            "type": "content",
            "title": "2. Product Backlog & Prioritization (MoSCoW + RICE)",
            "bullets": [
                "Structured Backlog: 19 User Stories organized across 6 Core Epics (Auth, Project Mgmt, Task Engine, Team RBAC, Dashboard, AI Insights).",
                "RICE Scoring Formula: (Reach x Impact x Confidence) / Effort evaluated for data-driven prioritization.",
                "P0 Must-Haves (12 Stories): Core Auth, Project CRUD, Drag-and-Drop Task Kanban, Member Roles, Executive KPI cards.",
                "P1 Should-Haves (6 Stories): Forgot password, Task comments, Alerts engine, AI task recommendation MVP.",
                "P2 Could-Haves (1 Story): Advanced custom dashboard theme settings (deferred to V1.1)."
            ]
        },
        {
            "type": "content",
            "title": "3. 10-Week Master Roadmap & Agile Sprints",
            "bullets": [
                "Sprint 1 (Weeks 1-2): Requirements, Auth APIs, DB Schemas, Figma UI Design Kit.",
                "Sprint 2 (Weeks 3-4): Workspace Engine, Project CRUD, Team Invites & Member RBAC.",
                "Sprint 3 (Weeks 5-6): Task Management Engine, Drag-and-Drop Kanban, Task Comments.",
                "Sprint 4 (Weeks 7-8): Executive KPI Dashboard, Alerts Worker, Rule-Based AI Engine.",
                "Sprint 5 (Weeks 9-10): QA Hardening, 10 UAT Scenarios, Security Audit, AWS Cloud Launch."
            ]
        },
        {
            "type": "content",
            "title": "4. Resource Planning & RACI Governance Matrix",
            "bullets": [
                "Accountable (A): Product Manager owns feature scope; PM Intern owns schedule, RACI & risks.",
                "Responsible (R): Engineering Lead (Architecture), Backend/Frontend Devs (Code), QA Lead (Testing), DevOps (Infra).",
                "Capacity Formula: 10 Headcount x 80 hrs/sprint x 80% Focal Factor = 640 Gross Hours (~40 Story Points/Sprint).",
                "Workload Balancing: Front-loaded UI/UX in Sprint 1; QA testing automated continuously across Sprints 2-5."
            ]
        },
        {
            "type": "content",
            "title": "5. Risk Management & Dependency Tracking",
            "bullets": [
                "Risk Management: 10 risks scored on Likelihood (1-5) x Impact (1-5); proactive mitigations assigned.",
                "Critical Risk R-01 (Backend API Delay): Mitigated by pairing backend devs & providing mock JSON stubs to frontend.",
                "High Risk R-03 (Sprint 5 QA Bottleneck): Mitigated by mandating developer unit tests & automated API regression.",
                "Dependency Tracker: 12 technical dependencies tracked across DB schemas, UI kits, AWS infrastructure, and store approvals."
            ]
        },
        {
            "type": "content",
            "title": "6. Case Study: Change Request CR-001 (Week 6 AI Feature)",
            "bullets": [
                "Request: Management requested 'AI Task Recommendations' in MVP during Week 6.",
                "Impact Analysis: Analyzed across Scope (+5 Pts), Timeline (+2 wks risk), Cost, Quality, and Resources.",
                "Trade-Off Evaluation: Evaluated 4 Options using a Weighted Decision Matrix (Schedule 30%, Quality 25%, Value 20%).",
                "Recommended Solution (Option D): Phased Rule-Based AI Engine Scope Swap (swapping out non-critical email digest to V1.1).",
                "Outcome: Delivered AI feature in MVP while keeping Week 10 release date 100% intact!"
            ]
        },
        {
            "type": "content",
            "title": "7. Executive Project Health Dashboard (Week 4 Snapshot)",
            "bullets": [
                "Overall RAG Status: ON TRACK 🟢 (Schedule Performance Index SPI = 1.05, Cost CPI = 1.00).",
                "Progress Metrics: 42% overall completion (53 / 110 Story Points delivered; 86 tasks completed).",
                "Interactive Web Dashboard: Produced 'dashboard.html' featuring dynamic filters, KPI cards, and risk heatmaps.",
                "Live Product Mockup: Developed 'nova_app_demo.html' interactive dark-mode SaaS web prototype."
            ]
        },
        {
            "type": "content",
            "title": "8. User Acceptance Testing (UAT) & Sign-Off",
            "bullets": [
                "UAT Strategy: 5-Day testing window in Week 9 on AWS Staging environment with 6 external beta testers.",
                "Test Suite: 10 detailed step-by-step test scenarios covering Auth, Project CRUD, Kanban, Comments, KPIs, AI, and Mobile.",
                "Defect SLAs: P0 Blocker (<4 hrs), P1 Critical (<12 hrs), P2 Major (<24 hrs).",
                "Exit Benchmark: 100% scenario pass rate, 0 P0/P1 defects open, formal PM & QA sign-off."
            ]
        },
        {
            "type": "content",
            "title": "9. 5-Pillar Launch Checklist & War-Room Runbook",
            "bullets": [
                "Product: 100% P0 features ready, zero blocker bugs, scope freeze enforced.",
                "Technical: AWS ECS multi-AZ container cluster live, DB automated backups active, Sentry monitoring enabled.",
                "Marketing & Support: Landing page live, docs published, press release scheduled, SendGrid email drip active.",
                "War-Room Execution: T-0 hour-by-hour runbook (06:00 AM DB Migration -> 07:30 AM DNS Flip -> 08:15 AM Smoke Tests -> GO LIVE)."
            ]
        },
        {
            "type": "content",
            "title": "10. Sprint Retrospective & Continuous Improvement",
            "bullets": [
                "What Went Well: Cross-functional collaboration, MoSCoW prioritization, proactive scope management, fast API mock deployment.",
                "What Needed Improvement: Initial DB schema complexity, QA bottleneck risk during mid-sprint code drops.",
                "Action Items: Establish Swagger API contract freeze by Day 3 of each sprint; increase automated test coverage to 85%."
            ]
        },
        {
            "type": "content",
            "title": "11. Summary & Candidate Portfolio Conclusion",
            "bullets": [
                "Proven PM Competencies: Requirements breakdown, Agile sprint planning, EVM metrics, risk management, stakeholder comms.",
                "Complete Deliverable Package: Excel Workbook, Interactive Web Dashboard, Product Mockup, 12-Slide Deck, 9 Reports.",
                "Final Outcome: NOVA MVP launched on time, within budget, with high quality and recruiter-grade execution excellence!"
            ]
        }
    ]
    
    for slide_info in slides_data:
        slide = prs.slides.add_slide(blank_slide_layout)
        
        if slide_info["type"] == "title":
            # Dark Background
            bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
            bg.fill.solid()
            bg.fill.fore_color.rgb = c_navy
            bg.line.fill.background()
            
            # Title box
            tx_box = slide.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.333), Inches(3.5))
            tf = tx_box.text_frame
            tf.word_wrap = True
            
            p = tf.paragraphs[0]
            p.text = slide_info["title"]
            p.font.size = Pt(40)
            p.font.bold = True
            p.font.color.rgb = c_cyan
            p.alignment = PP_ALIGN.CENTER
            
            p2 = tf.add_paragraph()
            p2.text = slide_info["subtitle"]
            p2.font.size = Pt(20)
            p2.font.color.rgb = c_white
            p2.alignment = PP_ALIGN.CENTER
            
        else:
            # Header Bar
            header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.2))
            header.fill.solid()
            header.fill.fore_color.rgb = c_blue
            header.line.fill.background()
            
            tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.2), Inches(11.5), Inches(0.8))
            tf = tx_box.text_frame
            p = tf.paragraphs[0]
            p.text = slide_info["title"]
            p.font.size = Pt(26)
            p.font.bold = True
            p.font.color.rgb = c_white
            
            # Card Container
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(5.3))
            card.fill.solid()
            card.fill.fore_color.rgb = c_card_bg
            card.line.color.rgb = c_gray
            
            # Bullets
            tx_box2 = slide.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(11.133), Inches(4.9))
            tf2 = tx_box2.text_frame
            tf2.word_wrap = True
            
            for idx, bullet in enumerate(slide_info["bullets"]):
                p = tf2.paragraphs[0] if idx == 0 else tf2.add_paragraph()
                p.text = "• " + bullet
                p.font.size = Pt(18)
                p.font.color.rgb = c_navy
                p.space_after = Pt(14)
                
    output_path = r"d:\PROJECTS\NOVA-MVP\NOVA_MVP_Submission\08_Final_Presentation\NOVA_MVP_Project_Management_Presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated PowerPoint Presentation Deck at: {output_path}")

if __name__ == "__main__":
    create_presentation()

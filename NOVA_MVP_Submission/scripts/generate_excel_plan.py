import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_master_project_plan():
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    
    # Styles
    font_family = "Segoe UI"
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid") # Dark Navy Blue
    header_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")
    title_font = Font(name=font_family, size=16, bold=True, color="1F4E78")
    subtitle_font = Font(name=font_family, size=11, italic=True, color="595959")
    bold_font = Font(name=font_family, size=10, bold=True)
    regular_font = Font(name=font_family, size=10)
    
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    
    p0_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid") # Light Red/Orange
    p1_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid") # Light Yellow
    p2_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid") # Light Green
    
    # -------------------------------------------------------------
    # TAB 1: Executive Overview
    # -------------------------------------------------------------
    ws1 = wb.create_sheet(title="Overview & Governance")
    ws1.views.sheetView[0].showGridLines = True
    
    ws1['A1'] = "NOVA MVP — Master Project Overview"
    ws1['A1'].font = title_font
    ws1['A2'] = "AI-Powered Team Productivity Platform (10-Week Agile Launch Plan)"
    ws1['A2'].font = subtitle_font
    
    overview_data = [
        ["Project Parameter", "Details"],
        ["Product Name", "NOVA (SaaS Team Productivity Platform)"],
        ["Project Duration", "10 Weeks (5 Agile Sprints x 2 Weeks)"],
        ["Target Launch Date", "Week 10 (Friday Release)"],
        ["Total Team Size", "10 Headcount (1 PM, 1 Prod Mgr, 1 UI/UX, 2 Flutter, 2 Front-End, 2 Backend, 1 QA, 1 DevOps)"],
        ["Primary PM Methodology", "Agile Scrum + MoSCoW & RICE Prioritization"],
        ["Overall Project Status", "ON TRACK (Week 4 Snapshot: 42% Complete, SPI = 1.05, CPI = 1.00)"],
        ["Key Business Goal", "Launch robust MVP to enable team task mgmt, collaboration, dashboard, and AI insights."]
    ]
    
    for r_idx, row in enumerate(overview_data, start=4):
        for c_idx, val in enumerate(row, start=1):
            cell = ws1.cell(row=r_idx, column=c_idx, value=val)
            cell.font = bold_font if c_idx == 1 or r_idx == 4 else regular_font
            cell.border = thin_border
            if r_idx == 4:
                cell.fill = header_fill
                cell.font = header_font
                
    # -------------------------------------------------------------
    # TAB 2: Product Backlog
    # -------------------------------------------------------------
    ws2 = wb.create_sheet(title="Product Backlog")
    ws2.views.sheetView[0].showGridLines = True
    
    backlog_headers = [
        "Story ID", "Epic", "Feature", "User Story Description", "Acceptance Criteria", 
        "MoSCoW", "Reach", "Impact", "Confidence", "Effort", "RICE Score", "Story Points", "Sprint", "Owner"
    ]
    
    ws2.append(backlog_headers)
    for col in range(1, len(backlog_headers) + 1):
        cell = ws2.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        
    backlog_rows = [
        # Epic 1: Auth
        ["US-01", "Authentication", "Sign Up", "As a user, I want to create an account so I can access NOVA.", "Validates email, password strength, sends verification link.", "P0 (Must)", 1000, 3, 0.9, 2, "=ROUND((F2*G2*H2)/I2, 1)", 3, "Sprint 1", "Backend Dev 1"],
        ["US-02", "Authentication", "Login", "As a user, I want to log in securely so I can access my workspace.", "JWT token issued, error message on invalid credentials.", "P0 (Must)", 1000, 3, 0.9, 2, "=ROUND((F3*G3*H3)/I3, 1)", 3, "Backend Dev 1"],
        ["US-03", "Authentication", "Forgot Password", "As a user, I want to reset my password if forgotten.", "Generates secure reset token via email.", "P1 (Should)", 500, 2, 0.8, 2, "=ROUND((F4*G4*H4)/I4, 1)", 3, "Backend Dev 2"],
        ["US-04", "Authentication", "User Profile", "As a user, I want to update my avatar and profile details.", "Allows updating name, title, profile picture.", "P1 (Should)", 800, 2, 0.9, 1, "=ROUND((F5*G5*H5)/I5, 1)", 2, "Front-End Dev 1"],
        
        # Epic 2: Project Mgmt
        ["US-05", "Project Management", "Create Project", "As a team lead, I want to create a new project workspace.", "Project title, key, description, start/end dates.", "P0 (Must)", 1000, 3, 0.9, 3, "=ROUND((F6*G6*H6)/I6, 1)", 5, "Backend Dev 2"],
        ["US-06", "Project Management", "Edit Project", "As a project owner, I want to modify project details.", "Updates project settings, owner permissions enforced.", "P0 (Must)", 800, 2, 0.9, 2, "=ROUND((F7*G7*H7)/I7, 1)", 3, "Front-End Dev 2"],
        ["US-07", "Project Management", "Delete Project", "As an admin, I want to archive or delete a project.", "Soft delete with confirmation modal.", "P1 (Should)", 500, 2, 0.8, 1, "=ROUND((F8*G8*H8)/I8, 1)", 2, "Backend Dev 1"],
        ["US-08", "Project Management", "Project Dashboard", "As a manager, I want a high-level project view.", "Shows project status, task counts, timeline progress.", "P0 (Must)", 1000, 3, 0.9, 3, "=ROUND((F9*G9*H9)/I9, 1)", 5, "Flutter Dev 1"],
        
        # Epic 3: Task Mgmt
        ["US-09", "Task Management", "Create Task", "As a team member, I want to create tasks within a project.", "Inputs title, description, priority, assignee, due date.", "P0 (Must)", 1000, 3, 0.9, 3, "=ROUND((F10*G10*H10)/I10, 1)", 5, "Backend Dev 1"],
        ["US-10", "Task Management", "Assign Task", "As a lead, I want to assign tasks to team members.", "Assignee receives task, update logged in activity history.", "P0 (Must)", 1000, 3, 0.9, 2, "=ROUND((F11*G11*H11)/I11, 1)", 3, "Front-End Dev 1"],
        ["US-11", "Task Management", "Task Priority & Due Date", "As a user, I want to set task priority (Low, Med, High, Urgent).", "Visual priority badges and due date picker.", "P0 (Must)", 1000, 2, 0.9, 1, "=ROUND((F12*G12*H12)/I12, 1)", 2, "Flutter Dev 2"],
        ["US-12", "Task Management", "Task Status Workflow", "As a user, I want to move tasks (To Do, In Progress, Review, Done).", "Kanban drag-and-drop or status dropdown.", "P0 (Must)", 1000, 3, 0.9, 3, "=ROUND((F13*G13*H13)/I13, 1)", 5, "Front-End Dev 2"],
        ["US-13", "Task Management", "Task Comments", "As a member, I want to comment on tasks to collaborate.", "Rich text comments with timestamps.", "P1 (Should)", 800, 2, 0.8, 2, "=ROUND((F14*G14*H14)/I14, 1)", 3, "Backend Dev 2"],
        
        # Epic 4: Team Mgmt
        ["US-14", "Team Management", "Add/Remove Members", "As an admin, I want to manage project members.", "Invite via email, role assignment (Admin, Member, Viewer).", "P0 (Must)", 900, 3, 0.9, 2, "=ROUND((F15*G15*H15)/I15, 1)", 3, "Backend Dev 1"],
        ["US-15", "Team Management", "Member Roles", "As an admin, I want role-based access control (RBAC).", "Enforces view/edit/delete permissions across objects.", "P0 (Must)", 900, 3, 0.9, 3, "=ROUND((F16*G16*H16)/I16, 1)", 5, "Backend Dev 2"],
        
        # Epic 5: Dashboard & Analytics
        ["US-16", "Dashboard", "Executive KPIs", "As an executive, I want to view active/completed/overdue tasks.", "Displays numerical KPI cards and completion progress bars.", "P0 (Must)", 1000, 3, 0.9, 3, "=ROUND((F17*G17*H17)/I17, 1)", 5, "Front-End Dev 1"],
        ["US-17", "Dashboard", "Team Productivity", "As a manager, I want to track team velocity and workload.", "Generates completion breakdown by team member.", "P1 (Should)", 700, 2, 0.8, 3, "=ROUND((F18*G18*H18)/I18, 1)", 5, "Front-End Dev 2"],
        
        # Epic 6: Notifications & AI
        ["US-18", "Notifications", "In-App & Email Alerts", "As a user, I want notifications when assigned tasks or due dates change.", "Triggers real-time alerts and daily digest email.", "P1 (Should)", 800, 2, 0.8, 2, "=ROUND((F19*G19*H19)/I19, 1)", 3, "Backend Dev 1"],
        ["US-19", "AI Insights", "AI Task Recommendations", "As a user, I want smart task priority suggestions based on deadlines.", "Heuristic recommendation engine suggests next priority task.", "P1 (Should)", 600, 3, 0.7, 3, "=ROUND((F20*G20*H20)/I20, 1)", 5, "Backend Dev 2"]
    ]
    
    for r_idx, row in enumerate(backlog_rows, start=2):
        for c_idx, val in enumerate(row, start=1):
            cell = ws2.cell(row=r_idx, column=c_idx, value=val)
            cell.font = regular_font
            cell.border = thin_border
            if c_idx in [1, 6, 11, 12, 13]:
                cell.alignment = Alignment(horizontal="center")
            if "P0" in str(val):
                cell.fill = p0_fill
            elif "P1" in str(val):
                cell.fill = p1_fill
                
    # -------------------------------------------------------------
    # TAB 3: Sprint Planning
    # -------------------------------------------------------------
    ws3 = wb.create_sheet(title="Sprint Schedule")
    ws3.views.sheetView[0].showGridLines = True
    
    sprint_headers = ["Sprint", "Weeks", "Sprint Goal", "Key Deliverables", "Target Points", "Velocity Target", "Status"]
    ws3.append(sprint_headers)
    for col in range(1, len(sprint_headers) + 1):
        cell = ws3.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    sprints = [
        ["Sprint 1", "Weeks 1-2", "Foundation, Auth & Architecture Setup", "Auth APIs, User DB Schema, Flutter/Web scaffolding, CI/CD", 25, "25 pts", "COMPLETED"],
        ["Sprint 2", "Weeks 3-4", "Core Project Management & RBAC Engine", "Project CRUD, Workspace Dashboard, Member Invites & Roles", 28, "28 pts", "COMPLETED"],
        ["Sprint 3", "Weeks 5-6", "Core Task Management & Collaboration Engine", "Task CRUD, Priority/Due dates, Kanban Workflow, Task Comments", 30, "30 pts", "IN PROGRESS"],
        ["Sprint 4", "Weeks 7-8", "Executive Dashboard, Notifications & AI MVP", "Metrics Dashboard, Team Productivity, In-App Alerts, AI Rules Engine", 26, "26 pts", "PLANNED"],
        ["Sprint 5", "Weeks 9-10", "QA Hardening, UAT Execution & Production Launch", "Full E2E Testing, Bug Fixes, Security Audit, Cloud Deployment", 20, "20 pts", "PLANNED"]
    ]
    
    for r_idx, row in enumerate(sprints, start=2):
        for c_idx, val in enumerate(row, start=1):
            cell = ws3.cell(row=r_idx, column=c_idx, value=val)
            cell.font = regular_font
            cell.border = thin_border
            if c_idx in [1, 2, 5, 6, 7]:
                cell.alignment = Alignment(horizontal="center")
                
    # -------------------------------------------------------------
    # TAB 4: RACI Resource Allocation
    # -------------------------------------------------------------
    ws4 = wb.create_sheet(title="RACI Resource Matrix")
    ws4.views.sheetView[0].showGridLines = True
    
    raci_headers = ["Workstream / Phase", "Product Mgr", "Project Mgr", "UI/UX Designer", "Flutter Devs", "Frontend Devs", "Backend Devs", "QA Engineer", "DevOps Eng"]
    ws4.append(raci_headers)
    for col in range(1, len(raci_headers) + 1):
        cell = ws4.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    raci_rows = [
        ["Requirements & Scope Definition", "Accountable (A)", "Responsible (R)", "Consulted (C)", "Informed (I)", "Informed (I)", "Consulted (C)", "Informed (I)", "Informed (I)"],
        ["UI/UX Design & Wireframing", "Consulted (C)", "Accountable (A)", "Responsible (R)", "Consulted (C)", "Consulted (C)", "Informed (I)", "Informed (I)", "Informed (I)"],
        ["Database & API Development", "Informed (I)", "Accountable (A)", "Informed (I)", "Consulted (C)", "Consulted (C)", "Responsible (R)", "Consulted (C)", "Consulted (C)"],
        ["Mobile & Web Frontend Dev", "Informed (I)", "Accountable (A)", "Consulted (C)", "Responsible (R)", "Responsible (R)", "Consulted (C)", "Informed (I)", "Informed (I)"],
        ["Quality Assurance & Bug Tracking", "Informed (I)", "Accountable (A)", "Informed (I)", "Consulted (C)", "Consulted (C)", "Consulted (C)", "Responsible (R)", "Informed (I)"],
        ["DevOps & Production Deployment", "Informed (I)", "Accountable (A)", "Informed (I)", "Informed (I)", "Informed (I)", "Consulted (C)", "Consulted (C)", "Responsible (R)"],
        ["UAT Execution & Client Sign-off", "Accountable (A)", "Responsible (R)", "Consulted (C)", "Support (S)", "Support (S)", "Support (S)", "Responsible (R)", "Informed (I)"]
    ]
    
    for r_idx, row in enumerate(raci_rows, start=2):
        for c_idx, val in enumerate(row, start=1):
            cell = ws4.cell(row=r_idx, column=c_idx, value=val)
            cell.font = regular_font
            cell.border = thin_border
            if c_idx > 1:
                cell.alignment = Alignment(horizontal="center")
                
    # -------------------------------------------------------------
    # TAB 5: Risk Register
    # -------------------------------------------------------------
    ws5 = wb.create_sheet(title="Risk Register")
    ws5.views.sheetView[0].showGridLines = True
    
    risk_headers = ["Risk ID", "Category", "Risk Description", "Likelihood (1-5)", "Impact (1-5)", "Severity (L x I)", "Severity Level", "Mitigation Strategy", "Owner"]
    ws5.append(risk_headers)
    for col in range(1, len(risk_headers) + 1):
        cell = ws5.cell(row=1, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        
    risks = [
        ["R-01", "Technical", "Backend API delivery delayed due to complex DB schema.", 4, 4, "=D2*E2", "CRITICAL (16)", "Start API contract design in Sprint 1; pair backend devs.", "Backend Lead"],
        ["R-02", "Scope", "Scope creep: Unplanned AI feature requested in Week 6.", 4, 3, "=D3*E3", "HIGH (12)", "Establish Change Control Board (CCB); use Phase 1 heuristic scope swap.", "Project Manager"],
        ["R-03", "Resource", "QA bottleneck during Sprint 5 testing window.", 3, 4, "=D4*E4", "HIGH (12)", "Implement developer unit testing and automated integration tests in Sprints 2-4.", "QA Lead"],
        ["R-04", "Design", "UI/UX wireframe delays block front-end implementation.", 3, 3, "=D5*E5", "MEDIUM (9)", "Front-load design reviews; complete component library by end of Sprint 1.", "UI/UX Designer"],
        ["R-05", "DevOps", "Production environment configuration failure on launch day.", 2, 4, "=D6*E6", "MEDIUM (8)", "Deploy staging environment in Sprint 2; run full dry-run deployment in Sprint 4.", "DevOps Engineer"],
        ["R-06", "Security", "Authentication vulnerability or unencrypted token leak.", 2, 5, "=D7*E7", "HIGH (10)", "Implement JWT standard with HTTPS, bcrypt password hashing, and security audit.", "Backend Dev 1"],
        ["R-07", "Integration", "Flutter mobile app and Web frontend UI state mismatch.", 3, 3, "=D8*E8", "MEDIUM (9)", "Share unified OpenAPI/Swagger specification across mobile and web teams.", "Engineering Lead"],
        ["R-08", "Dependency", "Third-party email notification service downtime.", 2, 3, "=D9*E9", "MEDIUM (6)", "Abstract notification handler with fallback queuing (Redis/Celery).", "Backend Dev 2"],
        ["R-09", "Performance", "Dashboard slow response time under heavy task load.", 2, 4, "=D10*E10", "MEDIUM (8)", "Add DB indexing on task status and project IDs; implement caching.", "Backend Lead"],
        ["R-10", "Stakeholder", "Delayed UAT sign-off from executive management.", 3, 3, "=D11*E11", "MEDIUM (9)", "Conduct weekly demo showcases; align UAT criteria at start of Sprint 4.", "Product Manager"]
    ]
    
    for r_idx, row in enumerate(risks, start=2):
        for c_idx, val in enumerate(row, start=1):
            cell = ws5.cell(row=r_idx, column=c_idx, value=val)
            cell.font = regular_font
            cell.border = thin_border
            if c_idx in [1, 2, 4, 5, 6, 7, 9]:
                cell.alignment = Alignment(horizontal="center")
            if "CRITICAL" in str(val) or "HIGH" in str(val):
                cell.fill = p0_fill
                
    # Adjust column widths automatically across all worksheets
    for sheet in wb.worksheets:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val_str = str(cell.value or '')
                if cell.coordinate in sheet.merged_cells:
                    continue
                max_len = max(max_len, len(val_str))
            sheet.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 50)
            
    output_path = r"d:\PROJECTS\NOVA-MVP\NOVA_MVP_Submission\01_Project_Plan\NOVA_MVP_Master_Project_Plan.xlsx"
    wb.save(output_path)
    print(f"Successfully generated Master Project Plan Excel Workbook at: {output_path}")

if __name__ == "__main__":
    create_master_project_plan()

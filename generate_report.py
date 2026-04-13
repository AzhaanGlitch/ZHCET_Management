#!/usr/bin/env python3
"""
ZHCET Management System - Project Documentation PDF Generator
Generates a comprehensive report covering every file, tech stack, and architecture.
"""

from fpdf import FPDF
import os
import textwrap

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ZHCET_Management_Project_Report.pdf")

class ProjectReport(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(0, 85, 0)
        self.cell(0, 8, "ZHCET Management System - Project Documentation", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 85, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.ln(4)
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 85, 0)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 85, 0)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def sub_title(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.set_x(10)
        self.multi_cell(0, 5.5, "  - " + text)
        self.ln(1)

    def code_block(self, text):
        self.set_font("Courier", "", 9)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5, text, fill=True)
        self.ln(2)


def main():
    pdf = ProjectReport()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # ========== COVER PAGE ==========
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(0, 85, 0)
    pdf.cell(0, 15, "ZHCET Management System", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Comprehensive Project Documentation", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "College Faculty and Student Database Management Application", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(30)
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Owned by: https://github.com/Mehwash1505", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Repository: https://github.com/AzhaanGlitch/ZHCET_Management", align="C", new_x="LMARGIN", new_y="NEXT")

    # ========== TABLE OF CONTENTS ==========
    pdf.add_page()
    pdf.section_title("Table of Contents")
    toc_items = [
        "1. Project Overview",
        "2. Technology Stack",
        "3. Project Directory Structure",
        "4. Root Level Files",
        "5. Backend Directory - Detailed File Analysis",
        "   5.1 server.py - API Server",
        "   5.2 database.py - Database Abstraction Layer",
        "   5.3 schema.sql - Database Schema and Seed Data",
        "   5.4 requirements.txt - Python Dependencies",
        "   5.5 .env - Environment Variables",
        "   5.6 README.md - Backend Documentation",
        "6. Frontend Directory - Detailed File Analysis",
        "   6.1 index.html - Landing Page and Authentication",
        "   6.2 dashboard.html - Post-Login Dashboard",
        "   6.3 style.css - Complete Stylesheet",
        "   6.4 app.js - Application Logic",
        "   6.5 logo.png - College Logo Asset",
        "   6.6 banner.jpg - Banner Image Asset",
        "   6.7 .gitignore - Frontend Git Exclusions",
        "7. Supabase Integration and Usage",
        "8. Authentication Flow",
        "9. Role-Based Access Control",
        "10. Local Network Access (LAN Server)",
        "11. How to Run the Project",
    ]
    for item in toc_items:
        pdf.bullet(item)

    # ========== 1. PROJECT OVERVIEW ==========
    pdf.add_page()
    pdf.section_title("1. Project Overview")
    pdf.body_text(
        "The ZHCET Management System is a professional, role-based College Faculty and Student "
        "Database Management Application built for Zakir Husain College of Engineering and Technology (ZHCET), "
        "Aligarh Muslim University. The system provides distinct portals for three user roles: "
        "Administrator, Faculty, and Student."
    )
    pdf.body_text(
        "The application follows a strict 'no-framework' development philosophy. The entire frontend "
        "is built using pure HTML5, CSS3, and Vanilla JavaScript without any libraries, frameworks, "
        "or build tools such as React, Vue, Angular, Tailwind, or Bootstrap. Similarly, the backend "
        "is powered by Python's built-in http.server module, avoiding frameworks like Django or Flask."
    )
    pdf.body_text(
        "Key functionalities include:"
    )
    pdf.bullet("Role-Based Access Control (RBAC) with distinct dashboards for Admin, Faculty, and Student.")
    pdf.bullet("Full CRUD operations: Create, Read, Update, Delete records from the admin panel.")
    pdf.bullet("Self-service Sign Up for Faculty and Students.")
    pdf.bullet("Faculty can view their own profile and edit contact details.")
    pdf.bullet("Students can view their personal profile information.")
    pdf.bullet("Search and filter functionality across Faculty and Student directories.")
    pdf.bullet("Professional, institutional UI design with a government-college aesthetic.")
    pdf.bullet("LAN server support allowing access from mobile devices on the same network.")

    # ========== 2. TECHNOLOGY STACK ==========
    pdf.add_page()
    pdf.section_title("2. Technology Stack")

    pdf.sub_title("Frontend")
    pdf.bullet("HTML5 - Semantic markup for page structure and content.")
    pdf.bullet("CSS3 - Pure vanilla CSS with CSS custom properties (variables) for theming.")
    pdf.bullet("Vanilla JavaScript (ES6+) - All client-side logic, DOM manipulation, and API calls.")
    pdf.bullet("No frameworks, no libraries, no build tools.")

    pdf.sub_title("Backend")
    pdf.bullet("Python 3.x - The core runtime language.")
    pdf.bullet("http.server (BaseHTTPRequestHandler) - Python's built-in HTTP server module used as the API server.")
    pdf.bullet("json module - For parsing and serializing JSON request/response bodies.")
    pdf.bullet("urllib.parse - For URL path parsing.")

    pdf.sub_title("Database")
    pdf.bullet("Supabase (PostgreSQL) - Cloud-hosted PostgreSQL database providing real-time data storage.")
    pdf.bullet("supabase-py - Official Python client library for interacting with the Supabase REST API.")
    pdf.bullet("python-dotenv - For loading environment variables from the .env file.")

    pdf.sub_title("Deployment and Tools")
    pdf.bullet("Vercel - Frontend static deployment (optional).")
    pdf.bullet("Localtunnel / Ngrok - For generating public URLs to access the local server.")
    pdf.bullet("Git and GitHub - Version control and remote repository hosting.")

    # ========== 3. DIRECTORY STRUCTURE ==========
    pdf.add_page()
    pdf.section_title("3. Project Directory Structure")
    pdf.code_block(
        "ZHCET_Management/\n"
        "|\n"
        "|-- .gitignore              # Root-level git exclusion rules\n"
        "|-- README.md               # Project documentation\n"
        "|\n"
        "|-- backend/\n"
        "|   |-- .env                # Environment variables (Supabase credentials)\n"
        "|   |-- README.md           # Backend-specific documentation\n"
        "|   |-- database.py         # Database abstraction layer\n"
        "|   |-- requirements.txt    # Python package dependencies\n"
        "|   |-- schema.sql          # SQL schema + seed data\n"
        "|   |-- server.py           # API HTTP server\n"
        "|\n"
        "|-- frontend/\n"
        "|   |-- .gitignore          # Frontend git exclusion rules\n"
        "|   |-- index.html          # Landing page and authentication\n"
        "|   |-- dashboard.html      # Post-login dashboard page\n"
        "|   |-- style.css           # Complete CSS stylesheet\n"
        "|   |-- app.js              # All JavaScript application logic\n"
        "|   |-- logo.png            # College logo image\n"
        "|   |-- banner.jpg          # Homepage banner image strip\n"
        "|\n"
        "|-- venv/                   # Python virtual environment (git-ignored)\n"
    )

    # ========== 4. ROOT LEVEL FILES ==========
    pdf.section_title("4. Root Level Files")

    pdf.sub_title("4.1 .gitignore")
    pdf.body_text(
        "Located at the project root, this file instructs Git to exclude certain files and directories "
        "from version control. It prevents sensitive or auto-generated content from being pushed to "
        "the remote GitHub repository."
    )
    pdf.body_text("Excluded patterns:")
    pdf.bullet("venv/ - The Python virtual environment directory containing installed packages.")
    pdf.bullet(".env - Environment variable files containing secret Supabase credentials.")
    pdf.bullet("__pycache__/ - Python's compiled bytecode cache directory.")
    pdf.bullet("*.pyc - Individual compiled Python bytecode files.")
    pdf.bullet(".DS_Store - macOS filesystem metadata files.")

    pdf.sub_title("4.2 README.md")
    pdf.body_text(
        "The primary project documentation file displayed on the GitHub repository page. It provides "
        "a professional overview of the project including: key features, the technology stack used, "
        "step-by-step installation and setup instructions (database configuration, backend initialization, "
        "frontend initialization), and ownership attribution. The README follows a clean, professional "
        "format without emojis, adhering to institutional documentation standards."
    )

    # ========== 5. BACKEND FILES ==========
    pdf.add_page()
    pdf.section_title("5. Backend Directory - Detailed File Analysis")

    pdf.sub_title("5.1 server.py - API Server (112 lines)")
    pdf.body_text(
        "This is the core backend file that implements a complete RESTful API server using Python's "
        "built-in http.server module. It does NOT use any web framework like Django or Flask."
    )
    pdf.body_text("Architecture:")
    pdf.bullet("Class: RequestHandler extends BaseHTTPRequestHandler to handle all HTTP methods.")
    pdf.bullet("CORS Support: The _set_headers() method adds Access-Control-Allow-Origin: * headers "
               "to every response, enabling the frontend to communicate with the backend across ports.")
    pdf.ln(2)
    pdf.body_text("Supported HTTP Methods and Endpoints:")
    pdf.bullet("OPTIONS (any path): Handles CORS preflight requests from browsers.")
    pdf.bullet("POST /api/login: Authenticates users. Accepts JSON body with role, identifier, and "
               "password fields. Returns sanitized user data (password_hash removed) on success, "
               "or a 401 status on failure.")
    pdf.bullet("POST /api/{table}: Creates a new record in the specified table (faculty or student). "
               "Used for Sign Up and Admin record creation. Returns 201 on success.")
    pdf.bullet("GET /api/all/{table}: Retrieves all records from the specified table. Password hashes "
               "are stripped from the response for security.")
    pdf.bullet("PUT /api/update/{table}/{id_col}/{id_val}: Updates a specific record identified by "
               "its ID column and value. Used for editing faculty/student records.")
    pdf.bullet("DELETE /api/delete/{table}/{id_col}/{id_val}: Deletes a specific record from the database.")
    pdf.ln(2)
    pdf.body_text(
        "The server runs on port 8000 by default. The run() function binds to all network interfaces "
        "(empty string for host), making it accessible on the local network."
    )

    pdf.add_page()
    pdf.sub_title("5.2 database.py - Database Abstraction Layer (104 lines)")
    pdf.body_text(
        "This file provides a clean abstraction layer between the API server and the actual data storage. "
        "It implements a dual-mode architecture:"
    )
    pdf.bullet("Primary Mode (Supabase): When valid SUPABASE_URL and SUPABASE_KEY environment variables "
               "are present and the supabase Python package is installed, all operations go directly to "
               "the cloud Supabase PostgreSQL database.")
    pdf.bullet("Fallback Mode (Mock DB): When Supabase credentials are missing, the system falls back "
               "to an in-memory Python dictionary (mock_db) that simulates the database locally for "
               "testing purposes.")
    pdf.ln(2)
    pdf.body_text("Functions provided:")
    pdf.bullet("login(role, username_or_email, password): Authenticates a user by role. For admin, "
               "matches against username; for faculty/student, matches against email_id.")
    pdf.bullet("get_all(table_name): Returns all records from the specified table.")
    pdf.bullet("update_record(table_name, id_col, id_val, data): Updates a single record matching "
               "the given ID column and value with the provided data dictionary.")
    pdf.bullet("create_record(table_name, data): Inserts a new record. In mock mode, auto-generates "
               "a UUID for the primary key.")
    pdf.bullet("delete_record(table_name, id_col, id_val): Removes a single record by its identifier.")
    pdf.ln(2)
    pdf.body_text("Current Mock Data (used when Supabase is unavailable):")
    pdf.bullet("Admin: username 'admin', password '000'")
    pdf.bullet("Faculty: Dr. Mohd. Aslam (AI), Dr. Nazia Khatoon (VLSI), Dr. Tameem Ahmad (OOPS)")
    pdf.bullet("Students: Mehwash Nasir (B.Tech CS, Sem 5), Dipanshi Gaur (B.Tech EE, Sem 3)")

    pdf.sub_title("5.3 schema.sql - Database Schema and Seed Data (49 lines)")
    pdf.body_text(
        "This SQL file contains the complete database schema definition and initial seed data. "
        "It is designed to be executed directly in the Supabase SQL Editor to set up the cloud database."
    )
    pdf.body_text("Tables defined:")
    pdf.bullet("admin: Fields - admin_id (UUID, PK, auto-generated), username (unique), password_hash.")
    pdf.bullet("faculty: Fields - faculty_id (UUID, PK), name, department, designation, mobile_number, "
               "email_id (unique), area_of_specialization, password_hash.")
    pdf.bullet("student: Fields - student_id (UUID, PK), name, course_enrollment, current_semester (INT), "
               "email_id (unique), mobile_number, password_hash.")
    pdf.ln(2)
    pdf.body_text(
        "The file also includes INSERT statements that populate the tables with initial dummy data "
        "for testing: one admin account, three faculty members, and two students."
    )

    pdf.sub_title("5.4 requirements.txt - Python Dependencies")
    pdf.body_text(
        "A standard pip requirements file listing the two external Python packages needed by the backend:"
    )
    pdf.bullet("supabase: The official Supabase Python client library that provides methods to "
               "interact with the Supabase REST API (select, insert, update, delete operations).")
    pdf.bullet("python-dotenv: A utility that reads key-value pairs from a .env file and sets them "
               "as environment variables, making configuration management clean and secure.")
    pdf.ln(2)
    pdf.body_text("Install command: pip install -r requirements.txt")

    pdf.sub_title("5.5 .env - Environment Variables")
    pdf.body_text(
        "This file stores sensitive configuration that should never be committed to version control. "
        "It is listed in .gitignore to prevent accidental exposure."
    )
    pdf.body_text("Required variables:")
    pdf.bullet("SUPABASE_URL: The REST API endpoint URL for your Supabase project. "
               "Format: https://(project-id).supabase.co")
    pdf.bullet("SUPABASE_KEY: The anonymous (anon) public API key from your Supabase project settings. "
               "This key enables read/write access via Row Level Security policies.")
    pdf.ln(2)
    pdf.body_text(
        "The python-dotenv library automatically loads these values when database.py is imported. "
        "If these values are empty or missing, the system gracefully falls back to the mock database."
    )

    pdf.sub_title("5.6 backend/README.md")
    pdf.body_text(
        "A brief backend-specific readme file providing quick-start instructions for the API server, "
        "including environment setup and the command to launch the server."
    )

    # ========== 6. FRONTEND FILES ==========
    pdf.add_page()
    pdf.section_title("6. Frontend Directory - Detailed File Analysis")

    pdf.sub_title("6.1 index.html - Landing Page and Authentication (85 lines)")
    pdf.body_text(
        "This is the main entry point of the application. It serves as both the landing page and "
        "the authentication gateway. The page operates as a Single Page Application (SPA) where "
        "different sections are shown/hidden dynamically using JavaScript without page reloads."
    )
    pdf.body_text("Page sections:")
    pdf.bullet("Institutional Header: Displays the college name ('Zakir Husain College of Engineering "
               "and Technology') alongside the college logo image (logo.png).")
    pdf.bullet("Navigation Bar: A dark green bar with direct links to Admin Portal Login, Faculty "
               "Portal Login, and Student Portal Login. Clicking these bypasses the role selection "
               "screen and goes directly to the login form.")
    pdf.bullet("Banner Strip: A full-width image strip (banner.jpg) displayed below the header. "
               "It occupies approximately 45% of the viewport height.")
    pdf.bullet("Hero Section: Contains welcome text and a 'Proceed to Portal' button that reveals "
               "the role selection cards.")
    pdf.bullet("Role Selection: Three cards (Administrator, Faculty, Student) that users click to "
               "choose their portal.")
    pdf.bullet("Login/Sign Up Section: A dynamic form that adapts based on the selected role. "
               "Admin users see only a login form; Faculty and Students see a toggle between Login "
               "and Sign Up modes. Sign Up forms capture all database fields required for registration.")
    pdf.ln(2)
    pdf.body_text(
        "The page includes fade-in CSS animations for smooth transitions between sections."
    )

    pdf.add_page()
    pdf.sub_title("6.2 dashboard.html - Post-Login Dashboard (49 lines)")
    pdf.body_text(
        "This page is loaded after a user successfully logs in. It provides the role-specific "
        "dashboard interface."
    )
    pdf.body_text("Structure:")
    pdf.bullet("Dashboard Navbar: A green header bar showing the application name and a welcome "
               "greeting with the logged-in user's name, plus a Logout button.")
    pdf.bullet("Dashboard Header: Displays the page title (varies by role) along with a search bar "
               "(visible for Admin and Faculty) and an 'Add New Record' button (visible only for Admin).")
    pdf.bullet("Content Area: A dynamic div (#content-area) populated entirely by JavaScript based "
               "on the user's role.")
    pdf.bullet("Modal Overlay: A hidden modal component used for creating and editing records. "
               "Contains a dynamic form (#modal-form) with fields populated by JavaScript at runtime.")

    pdf.sub_title("6.3 style.css - Complete Stylesheet (432 lines)")
    pdf.body_text(
        "The entire visual presentation of the application is defined in this single CSS file. "
        "It uses CSS Custom Properties (CSS Variables) defined in the :root selector for consistent "
        "theming across all components."
    )
    pdf.body_text("Design System - CSS Variables:")
    pdf.bullet("--bg-color: #f4f5f7 (Light grey page background)")
    pdf.bullet("--accent: #005500 (Primary institutional dark green)")
    pdf.bullet("--accent-hover: #003300 (Darker green for hover states)")
    pdf.bullet("--danger: #cc0000 (Red for delete actions and errors)")
    pdf.bullet("--panel-bg: #ffffff (White background for cards and panels)")
    pdf.bullet("--border-color: #cccccc (Consistent border color)")
    pdf.bullet("--font-family: Arial, Helvetica, sans-serif (System fonts for performance)")
    pdf.ln(2)
    pdf.body_text("Key style categories:")
    pdf.bullet("Layout: Flexbox-based layouts for header, navbar, containers, and dashboard.")
    pdf.bullet("Components: Styled role cards, authentication forms, profile cards, data tables, "
               "modals, buttons (primary/secondary/text), search bars.")
    pdf.bullet("Animation: fadeIn keyframe animation (0.4s ease-out) with translateY for smooth "
               "section transitions.")
    pdf.bullet("Banner: Full-viewport-width image strip with 45vh height and object-fit: cover.")
    pdf.bullet("Institutional Theme: Minimal border-radius (2px), flat design, green accent borders, "
               "professional typography - all designed to convey a government/institutional aesthetic.")

    pdf.add_page()
    pdf.sub_title("6.4 app.js - Application Logic (477 lines)")
    pdf.body_text(
        "This is the most complex file in the project. It contains ALL client-side application logic "
        "written in pure Vanilla JavaScript (ES6+). The file handles page routing, authentication, "
        "data fetching, table rendering, modal management, and CRUD operations."
    )
    pdf.body_text("Dynamic API URL:")
    pdf.code_block('const API_URL = "http://" + window.location.hostname + ":8000/api";')
    pdf.body_text(
        "This line is critical for LAN access. Instead of hardcoding 'localhost', it dynamically "
        "reads the current hostname. When accessed from a mobile phone via the laptop's IP address "
        "(e.g., 172.25.255.68:8002), the API calls automatically target the correct backend."
    )
    pdf.ln(2)
    pdf.body_text("Core Functions:")
    pdf.bullet("initIndex(): Handles the landing page (index.html) logic including section navigation, "
               "role selection, login/signup form generation, and form submission.")
    pdf.bullet("initDashboard(): Handles the dashboard page - detects user role from localStorage, "
               "sets up role-specific views, and loads data from the API.")
    pdf.bullet("setAuthMode(mode): Dynamically generates login or signup form fields based on the "
               "selected role. Faculty signup includes fields for name, department, designation, "
               "email, mobile, specialization, and password. Student signup includes name, course, "
               "semester, email, mobile, and password.")
    pdf.bullet("loadAndRenderTables(): Fetches faculty and student data from the API, renders HTML "
               "tables with search/filter functionality. Admin users see Edit and Delete action buttons.")
    pdf.bullet("renderStudentProfile(): Displays a read-only profile card for logged-in students.")
    pdf.bullet("renderFacultyProfile(): Displays the faculty member's profile with an Edit button "
               "restricted to contact information fields only.")
    pdf.bullet("openCreateModal(): Opens the modal with a table-type selector (Faculty/Student) and "
               "dynamic form fields for creating new records. Admin-only functionality.")
    pdf.bullet("openEditModal(): Opens the modal pre-populated with existing record data for editing. "
               "Supports both admin editing (all fields) and self-editing (limited fields).")
    pdf.bullet("deleteRecord(): Sends a DELETE request after confirmation prompt. Reloads page on success.")
    pdf.bullet("activateRoleFlow(): Shared function used by both navbar links and role cards to "
               "initiate the login flow for a specific role.")
    pdf.ln(2)
    pdf.body_text("Session Management:")
    pdf.bullet("Uses localStorage to persist user session data (user object and role string).")
    pdf.bullet("On every page load, checks if a session exists. If found on index.html, auto-redirects "
               "to dashboard.html. If missing on dashboard.html, redirects back to index.html.")
    pdf.bullet("Logout clears localStorage and redirects to the landing page.")

    pdf.sub_title("6.5 logo.png - College Logo Asset")
    pdf.body_text(
        "The official college logo image displayed in the top-right corner of the landing page header. "
        "If this file is missing or fails to load, a fallback image from Wikipedia (AMU logo) is "
        "displayed automatically via the onerror handler in the HTML."
    )
    pdf.body_text("Placement: frontend/logo.png")

    pdf.sub_title("6.6 banner.jpg - Banner Image Asset")
    pdf.body_text(
        "A full-width horizontal banner image displayed beneath the navigation bar on the landing page. "
        "This image strip spans the complete viewport width and occupies approximately 45% of the "
        "viewport height. It serves as a visual identity element for the college portal. If this file "
        "is missing, the banner section gracefully hides itself via the onerror handler."
    )
    pdf.body_text("Placement: frontend/banner.jpg")

    pdf.sub_title("6.7 .gitignore (Frontend)")
    pdf.body_text(
        "A minimal frontend-specific gitignore file that excludes the .vercel directory "
        "(generated during Vercel deployment) from version control."
    )

    # ========== 7. SUPABASE INTEGRATION ==========
    pdf.add_page()
    pdf.section_title("7. Supabase Integration and Usage")
    pdf.body_text(
        "Supabase is used as the cloud-hosted PostgreSQL database for this application. It provides "
        "a fully managed database with auto-generated REST APIs."
    )
    pdf.body_text("How the integration works:")
    pdf.bullet("Step 1: Create a project on supabase.com. This provides a unique project URL and "
               "API keys.")
    pdf.bullet("Step 2: Run the schema.sql file in the Supabase SQL Editor to create the admin, "
               "faculty, and student tables with their respective columns and constraints.")
    pdf.bullet("Step 3: Copy the project URL and anon key into backend/.env.")
    pdf.bullet("Step 4: The database.py file reads these environment variables on startup. If valid, "
               "it initializes the Supabase Python client using create_client(url, key).")
    pdf.bullet("Step 5: All CRUD operations (login, get_all, create_record, update_record, "
               "delete_record) are routed through the Supabase client's chained query methods "
               "(e.g., supabase.table('faculty').select('*').eq('email_id', email).execute()).")
    pdf.ln(2)
    pdf.body_text(
        "To update or replace dummy data in the live database, use the Supabase SQL Editor "
        "to run DELETE and INSERT statements directly. Changes reflect immediately in the "
        "application without restarting the backend server."
    )

    # ========== 8. AUTH FLOW ==========
    pdf.section_title("8. Authentication Flow")
    pdf.body_text("The authentication process follows these steps:")
    pdf.bullet("1. User selects a role (Admin/Faculty/Student) via cards or navbar links.")
    pdf.bullet("2. A dynamic login form is displayed. For Admin: username + password. "
               "For Faculty/Student: email + password.")
    pdf.bullet("3. On form submission, a POST request is sent to /api/login with the role, "
               "identifier, and password.")
    pdf.bullet("4. The backend queries the appropriate Supabase table, matching against the "
               "identifier and password_hash fields.")
    pdf.bullet("5. On success: the user object (minus password_hash) is returned and stored in "
               "localStorage. The browser redirects to dashboard.html.")
    pdf.bullet("6. On failure: an error message is displayed below the form.")
    pdf.bullet("7. For Sign Up: a POST request is sent to /api/{role} with all form fields. "
               "On success, the user is prompted to log in with their new credentials.")

    # ========== 9. RBAC ==========
    pdf.add_page()
    pdf.section_title("9. Role-Based Access Control")
    pdf.body_text("Each role has distinct privileges and dashboard views:")
    pdf.ln(2)
    pdf.sub_title("Administrator")
    pdf.bullet("Can view ALL faculty and student records in tabular format.")
    pdf.bullet("Can search/filter records using the search bar.")
    pdf.bullet("Can create new Faculty or Student records via the 'Add New Record' modal.")
    pdf.bullet("Can edit any record's fields via the Edit button.")
    pdf.bullet("Can delete any record via the Delete button (with confirmation).")
    pdf.bullet("Cannot sign up - admin accounts must be created directly in the database.")
    pdf.ln(2)
    pdf.sub_title("Faculty")
    pdf.bullet("Can view their own profile card with personal details.")
    pdf.bullet("Can edit their own contact information (mobile number, email).")
    pdf.bullet("Can view the Faculty and Student directory tables (read-only).")
    pdf.bullet("Can search/filter records.")
    pdf.bullet("Can self-register via the Sign Up form.")
    pdf.ln(2)
    pdf.sub_title("Student")
    pdf.bullet("Can view their own profile card showing name, course, semester, email, mobile.")
    pdf.bullet("Read-only access - cannot modify any data from the dashboard.")
    pdf.bullet("Can self-register via the Sign Up form.")

    # ========== 10. LAN ACCESS ==========
    pdf.section_title("10. Local Network Access (LAN Server)")
    pdf.body_text(
        "The application supports access from any device on the same Wi-Fi network, turning the "
        "developer's laptop into a local server."
    )
    pdf.body_text("How it works:")
    pdf.bullet("The Python frontend server (python -m http.server 8002) binds to 0.0.0.0 by default, "
               "accepting connections from any network interface.")
    pdf.bullet("The Python backend server (server.py) also binds to all interfaces via server_address = ('', port).")
    pdf.bullet("The JavaScript API URL uses window.location.hostname instead of 'localhost', so when "
               "a mobile phone accesses the frontend via the laptop's IP (e.g., http://172.25.255.68:8002), "
               "API requests are automatically directed to http://172.25.255.68:8000.")
    pdf.bullet("Both the phone (client) and laptop (server) must be connected to the same Wi-Fi network.")

    # ========== 11. HOW TO RUN ==========
    pdf.add_page()
    pdf.section_title("11. How to Run the Project")

    pdf.sub_title("Prerequisites")
    pdf.bullet("Python 3.x installed on your system.")
    pdf.bullet("A Supabase account with a project created (optional - works with mock data without it).")

    pdf.sub_title("Step 1: Clone the Repository")
    pdf.code_block("git clone https://github.com/AzhaanGlitch/ZHCET_Management.git\ncd ZHCET_Management")

    pdf.sub_title("Step 2: Set Up Python Virtual Environment")
    pdf.code_block("python -m venv venv\nsource venv/bin/activate  # Linux/Mac\nvenv\\Scripts\\activate     # Windows")

    pdf.sub_title("Step 3: Install Backend Dependencies")
    pdf.code_block("cd backend\npip install -r requirements.txt")

    pdf.sub_title("Step 4: Configure Environment Variables")
    pdf.body_text("Create or edit backend/.env with your Supabase credentials:")
    pdf.code_block("SUPABASE_URL=https://your-project-id.supabase.co\nSUPABASE_KEY=your_anon_key_here")

    pdf.sub_title("Step 5: Initialize the Database")
    pdf.body_text(
        "Open your Supabase project dashboard, navigate to the SQL Editor, and run the contents "
        "of backend/schema.sql to create the tables and seed data."
    )

    pdf.sub_title("Step 6: Start the Backend Server")
    pdf.code_block("cd backend\npython server.py")
    pdf.body_text("The API server will start on http://localhost:8000")

    pdf.sub_title("Step 7: Start the Frontend Server")
    pdf.code_block("cd frontend\npython -m http.server 8002")
    pdf.body_text("Open http://localhost:8002 in your browser to access the application.")

    pdf.sub_title("Step 8: Access from Mobile (Optional)")
    pdf.body_text(
        "Find your laptop's local IP address using 'ip addr' (Linux) or 'ipconfig' (Windows). "
        "On your mobile phone connected to the same Wi-Fi, open a browser and navigate to "
        "http://(laptop-ip):8002."
    )

    # ========== SAVE PDF ==========
    pdf.output(OUTPUT_PATH)
    print(f"PDF generated successfully: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

# ZHCET Management System

A professional, role-based College Faculty and Student Database Management Application. This project features a framework-less Vanilla JavaScript frontend with a clean, institutional user interface, powered by a Pure Python API Backend.

---

## Key Features

* Role-Based Access Control (RBAC): Distinct layouts and privileges for Administrators, Faculty, and Students.
* Full CRUD Operations: Administrators can create, read, update, and search the entire college database from an interactive dashboard.
* Professional Interface: Designed using pure CSS3 without frameworks, adhering to government and institutional design paradigms.
* Resilient Python API: Features a custom-built HTTP server bridging to Supabase (BaseHTTPRequestHandler), supporting dynamic REST endpoints.

---

## Technology Stack

* Frontend: Pure HTML5, CSS3, Vanilla JavaScript.
* Backend: Pure Python (http.server). 
* Database: Supabase PostgreSQL.

---

## Installation and Setup

### Prerequisites
Make sure you have Python 3.x installed.

### 1. Database Configuration
* Navigate to your Supabase project.
* Run the SQL structures found inside backend/schema.sql via the Supabase SQL editor to create the faculty, student, and admin tables.

### 2. Backend Initialization
1. Navigate into the backend directory: 
```bash
cd backend
```
2. Install the library dependencies:
```bash
pip install -r requirements.txt
```
3. Set your environment variables in a local backend/.env file:
```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_anon_key_here
```
4. Start the Python Server:
```bash
python server.py
```

### 3. Frontend Initialization
Launch the UI by running a simple HTTP server in the frontend directory:
```bash
cd frontend
python -m http.server 8001
```
Navigate to http://localhost:8001 to access the application.

---

## Ownership
This project was designed and is owned by https://github.com/Mehwash1505.

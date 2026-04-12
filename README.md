# ZHCET Management System

![Project Banner](https://img.shields.io/badge/Status-Active-success) ![License](https://img.shields.io/badge/License-MIT-blue) ![PostgreSQL](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-336791)

A professional, role-based College Faculty & Student Database Management Application. This project features a completely framework-less **Vanilla JavaScript frontend** with a responsive **Glassmorphism** UI, powered perfectly by a custom-built, barebones **Pure Python API Backend**.

---

## 🚀 Key Features

* **Role-Based Access Control (RBAC)**: Distinct layouts and privileges dynamically rendered for Administrators, Faculty, and Students.
* **Full CRUD Operations**: Administrators can seamlessly create, read, update, and comprehensively search the entire college database right from an interactive dashboard.
* **Modern Interface**: Designed using pure CSS3 without frameworks, showcasing beautiful Glassmorphism, smooth micro-animations, and dynamic real-time DOM updates.
* **Resilient Python API**: Features a robust, entirely custom-built HTTP server bridging directly to Supabase (`BaseHTTPRequestHandler`), which supports dynamic REST endpoints and seamlessly falls back to a mock database if connection variables are empty.

---

## 🛠️ Technology Stack

* **Frontend**: Pure HTML5, CSS3, Vanilla JavaScript. Custom interactions, no React/Vue/Tailwind constraints.
* **Backend**: Pure Python (`http.server`). 
* **Database**: Supabase PostgreSQL mapped with Python SDK integrations (`supabase`).

---

## 📋 Installation & Setup

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/) installed.

### 1. Database Configuration
* Navigate to your Supabase project.
* Run the SQL structures found inside `backend/schema.sql` via the Supabase SQL editor to create the `faculty`, `student`, and `admin` tables.

### 2. Backend Initialization
1. Navigate into the backend directory: 
```bash
cd backend
```
2. Install the library dependencies:
```bash
pip install -r requirements.txt
```
3. Set your environment variables in a local `backend/.env` file referencing your Supabase API tokens:
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
Navigate to `http://localhost:8001` to access the application.

---

## 👥 Ownership
This project was designed and is proudly owned by [Mehwash1505](https://github.com/Mehwash1505).

---
*Developed for educational excellence and modern architecture standards.*

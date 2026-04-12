import os
from dotenv import load_dotenv

load_dotenv()

try:
    from supabase import create_client, Client
    has_supabase = True
except ImportError:
    has_supabase = False

url = os.environ.get("SUPABASE_URL", "")
key = os.environ.get("SUPABASE_KEY", "")

supabase = None
if has_supabase and url and key:
    supabase = create_client(url, key)

# Simple Mock DB for testing in case real Supabase credentials are not provided
mock_db = {
    "admin": [
        {"admin_id": "a1", "username": "admin", "password_hash": "000"},
    ],
    "faculty": [
        {"faculty_id": "f1", "name": "Dr. Mohd. Aslam", "department": "Computer Engineering", "designation": "Professor", "mobile_number": "9876543210", "email_id": "m.aslam@zhcet.ac.in", "area_of_specialization": "Artificial Intelligence", "password_hash": "password123"},
        {"faculty_id": "f2", "name": "Dr. Nazia Khatoon", "department": "Electronics Engineering", "designation": "Professor", "mobile_number": "9123456780", "email_id": "n.khatoon@zhcet.ac.in", "area_of_specialization": "VLSI Design", "password_hash": "password123"},
        {"faculty_id": "f7", "name": "Dr. Tameem Ahmad", "department": "Computer Engineering", "designation": "Professor", "mobile_number": "9876543210", "email_id": "tameemahmad@gmail.com", "area_of_specialization": "OOPS", "password_hash": "password123"}
    ],
    "student": [
        {"student_id": "s1", "name": "Alice Johnson", "course_enrollment": "B.Tech CS", "current_semester": 5, "email_id": "alice@example.com", "mobile_number": "1112223333", "password_hash": "password123"},
        {"student_id": "s2", "name": "Bob Williams", "course_enrollment": "B.Tech EE", "current_semester": 3, "email_id": "bob@example.com", "mobile_number": "4445556666", "password_hash": "password123"}
    ]
}

def login(role, username_or_email, password):
    if supabase:
        # Use real supabase
        if role == "admin":
            res = supabase.table("admin").select("*").eq("username", username_or_email).eq("password_hash", password).execute()
        elif role == "faculty":
            res = supabase.table("faculty").select("*").eq("email_id", username_or_email).eq("password_hash", password).execute()
        elif role == "student":
            res = supabase.table("student").select("*").eq("email_id", username_or_email).eq("password_hash", password).execute()
        else:
            return None
        if res.data:
            return res.data[0]
        return None
    else:
        # Use mock
        table = mock_db.get(role, [])
        for record in table:
            if role == "admin":
                if record["username"] == username_or_email and record["password_hash"] == password:
                    return record
            else:
                if record["email_id"] == username_or_email and record["password_hash"] == password:
                    return record
        return None

def get_all(table_name):
    if supabase:
        res = supabase.table(table_name).select("*").execute()
        return res.data
    else:
        return mock_db.get(table_name, [])

def update_record(table_name, id_col, id_val, data):
    if supabase:
        res = supabase.table(table_name).update(data).eq(id_col, id_val).execute()
        return res.data[0] if res.data else None
    else:
        # Mock logic
        for record in mock_db.get(table_name, []):
            if record.get(id_col) == id_val:
                record.update(data)
                return record
        return None
        
def create_record(table_name, data):
    if supabase:
        res = supabase.table(table_name).insert(data).execute()
        return res.data[0] if res.data else None
    else:
        # mock insert
        import uuid
        if table_name == "faculty":
            data["faculty_id"] = str(uuid.uuid4())
        elif table_name == "student":
            data["student_id"] = str(uuid.uuid4())
        mock_db.get(table_name, []).append(data)
        return dict(data)
        
def delete_record(table_name, id_col, id_val):
    if supabase:
        res = supabase.table(table_name).delete().eq(id_col, id_val).execute()
        return res.data[0] if res.data else None
    else:
        table = mock_db.get(table_name, [])
        for i, val in enumerate(table):
            if val.get(id_col) == id_val:
                return table.pop(i)
        return None

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create Admin Table
CREATE TABLE admin (
    admin_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Create Faculty Table
CREATE TABLE faculty (
    faculty_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(150) NOT NULL,
    department VARCHAR(100) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(20),
    email_id VARCHAR(150) UNIQUE NOT NULL,
    area_of_specialization TEXT,
    password_hash VARCHAR(255) NOT NULL
);

-- Create Student Table
CREATE TABLE student (
    student_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(150) NOT NULL,
    course_enrollment VARCHAR(100) NOT NULL,
    current_semester INT NOT NULL,
    email_id VARCHAR(150) UNIQUE NOT NULL,
    mobile_number VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL
);

-- Insert Dummy Admin
INSERT INTO admin (username, password_hash) VALUES ('admin', '000');

-- Insert Dummy Faculty
INSERT INTO faculty (name, department, designation, mobile_number, email_id, area_of_specialization, password_hash)
VALUES 
    ('Dr. Mohd. Aslam', 'Computer Engineering', 'Professor', '9876543210', 'm.aslam@zhcet.ac.in', 'Artificial Intelligence', 'password123'),
    ('Dr. Nazia Khatoon', 'Electronics Engineering', 'Professor', '9123456780', 'n.khatoon@zhcet.ac.in', 'VLSI Design', 'password123'),
    ('Dr. Tameem Ahmad', 'Computer Engineering', 'Professor', '9876543210', 'tameemahmad@gmail.com', 'OOPS', 'password123');

-- Insert Dummy Student
INSERT INTO student (name, course_enrollment, current_semester, email_id, mobile_number, password_hash)
VALUES 
    ('Mehwash Nasir', 'B.Tech CS', 5, 'mehwash@gmail.com', '1112223333', 'password123'),
    ('Dipanshi Gaur', 'B.Tech EE', 3, 'dipanshi@gmail.com', '4445556666', 'password123');

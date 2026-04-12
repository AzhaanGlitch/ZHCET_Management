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
INSERT INTO admin (username, password_hash) VALUES ('admin', 'admin123');

-- Insert Dummy Faculty
INSERT INTO faculty (name, department, designation, mobile_number, email_id, area_of_specialization, password_hash)
VALUES 
    ('Dr. John Smith', 'Computer Science', 'Professor', '1234567890', 'john.smith@example.com', 'Machine Learning', 'password123'),
    ('Dr. Jane Doe', 'Electrical Engineering', 'Assistant Professor', '0987654321', 'jane.doe@example.com', 'Control Systems', 'password123');

-- Insert Dummy Student
INSERT INTO student (name, course_enrollment, current_semester, email_id, mobile_number, password_hash)
VALUES 
    ('Alice Johnson', 'B.Tech CS', 5, 'alice@example.com', '1112223333', 'password123'),
    ('Bob Williams', 'B.Tech EE', 3, 'bob@example.com', '4445556666', 'password123');

import sqlite3

# ---------------------------
# OOP CLASSES
# ---------------------------

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name


class Teacher:
    def __init__(self, teacher_id, name, course_code):
        self.teacher_id = teacher_id
        self.name = name
        self.course_code = course_code


# ---------------------------
# DATABASE QUERIES
# ---------------------------

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Count students in MSE800
cursor.execute("""
SELECT COUNT(DISTINCT student_id)
FROM enrollment
WHERE course_code = 'MSE800'
""")
print("Number of students in MSE800:", cursor.fetchone()[0])

# List teachers for MSE801
cursor.execute("""
SELECT name FROM teacher
WHERE course_code = 'MSE801'
""")

print("\nTeachers teaching MSE801:")
for row in cursor.fetchall():
    print("-", row[0])

conn.close()

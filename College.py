import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# DROP OLD TABLES
cursor.execute("DROP TABLE IF EXISTS enrollment")
cursor.execute("DROP TABLE IF EXISTS teacher")
cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("DROP TABLE IF EXISTS course")

# CREATE TABLES
cursor.execute("""
CREATE TABLE student (
    student_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE course (
    course_code TEXT PRIMARY KEY,
    course_name TEXT
)
""")

cursor.execute("""
CREATE TABLE enrollment (
    student_id INTEGER,
    course_code TEXT,
    PRIMARY KEY (student_id, course_code),
    FOREIGN KEY(student_id) REFERENCES student(student_id),
    FOREIGN KEY(course_code) REFERENCES course(course_code)
)
""")

cursor.execute("""
CREATE TABLE teacher (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT,
    course_code TEXT,
    FOREIGN KEY(course_code) REFERENCES course(course_code)
)
""")

# INSERT DATA
cursor.execute("INSERT INTO student VALUES (1,'Mashukh Elahi')")
cursor.execute("INSERT INTO student VALUES (2,'Parul Patel')")

cursor.execute("INSERT INTO course VALUES ('MSE800','Professional Software Engineering')")
cursor.execute("INSERT INTO course VALUES ('MSE801','Research Methods')")

cursor.execute("INSERT INTO enrollment VALUES (1,'MSE800')")
cursor.execute("INSERT INTO enrollment VALUES (1,'MSE801')")
cursor.execute("INSERT INTO enrollment VALUES (2,'MSE800')")

cursor.execute("INSERT INTO teacher VALUES (1,'Arun Kumar','MSE801')")
cursor.execute("INSERT INTO teacher VALUES (2,'Mohammad Rahim','MSE801')")

conn.commit()
conn.close()

print("Database reset and setup complete.")

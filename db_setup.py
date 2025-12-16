import sqlite3

# Connect to database (creates clinic.db if it doesn't exist)
conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# -------------------------
# DROP TABLES (RESET)
# -------------------------
cursor.execute("DROP TABLE IF EXISTS patient")
cursor.execute("DROP TABLE IF EXISTS doctor")
cursor.execute("DROP TABLE IF EXISTS clinic")

# -------------------------
# CREATE CLINIC TABLE
# -------------------------
cursor.execute("""
CREATE TABLE clinic (
    clinic_id INTEGER PRIMARY KEY,
    clinic_name TEXT,
    location TEXT,
    phone TEXT
)
""")

# -------------------------
# CREATE PATIENT TABLE
# -------------------------
cursor.execute("""
CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY,
    full_name TEXT,
    age INTEGER,
    gender TEXT,
    phone TEXT,
    address TEXT,
    clinic_id INTEGER,
    FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
)
""")

# -------------------------
# CREATE DOCTOR TABLE
# -------------------------
cursor.execute("""
CREATE TABLE doctor (
    doctor_id INTEGER PRIMARY KEY,
    full_name TEXT,
    specialisation TEXT,
    clinic_id INTEGER,
    FOREIGN KEY (clinic_id) REFERENCES clinic(clinic_id)
)
""")

# -------------------------
# INSERT CLINIC DATA
# -------------------------
cursor.execute("""
INSERT INTO clinic VALUES
(1,'City Health Clinic','Auckland','021999999')
""")

# -------------------------
# INSERT PATIENT DATA
# -------------------------
cursor.execute("""
INSERT INTO patient VALUES
(1,'John Smith',70,'Male','021111111','Auckland',1),
(2,'Anna Brown',60,'Female','021222222','Wellington',1),
(3,'David Lee',68,'Male','021333333','Hamilton',1)
""")

# -------------------------
# INSERT DOCTOR DATA
# -------------------------
cursor.execute("""
INSERT INTO doctor VALUES
(1,'Dr Adams','Ophthalmology',1),
(2,'Dr Khan','Cardiology',1),
(3,'Dr Patel','Ophthalmology',1)
""")

# -------------------------
# SAVE & CLOSE
# -------------------------
conn.commit()
conn.close()

print("Database setup completed successfully.")

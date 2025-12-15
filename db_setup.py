import sqlite3

conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS patient")
cursor.execute("DROP TABLE IF EXISTS doctor")

cursor.execute("""
CREATE TABLE patient (
    patient_id INTEGER PRIMARY KEY,
    full_name TEXT,
    age INTEGER,
    gender TEXT,
    phone TEXT,
    address TEXT
)
""")

cursor.execute("""
CREATE TABLE doctor (
    doctor_id INTEGER PRIMARY KEY,
    full_name TEXT,
    specialisation TEXT
)
""")

cursor.execute("INSERT INTO patient VALUES (1,'John Smith',70,'Male','021111111','Auckland')")
cursor.execute("INSERT INTO patient VALUES (2,'Anna Brown',60,'Female','021222222','Wellington')")
cursor.execute("INSERT INTO patient VALUES (3,'David Lee',68,'Male','021333333','Hamilton')")

cursor.execute("INSERT INTO doctor VALUES (1,'Dr Adams','Ophthalmology')")
cursor.execute("INSERT INTO doctor VALUES (2,'Dr Khan','Cardiology')")
cursor.execute("INSERT INTO doctor VALUES (3,'Dr Patel','Ophthalmology')")

conn.commit()
conn.close()

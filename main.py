import sqlite3

class Patient:
    def __init__(self, patient_id, full_name, age, gender, phone, address):
        self.patient_id = patient_id
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

class Doctor:
    def __init__(self, doctor_id, full_name, specialisation):
        self.doctor_id = doctor_id
        self.full_name = full_name
        self.specialisation = specialisation

conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# Senior patients
cursor.execute("SELECT * FROM patient WHERE age > 65")
print("Senior Patients:")
for row in cursor.fetchall():
    print(row)

# Ophthalmology doctor count
cursor.execute("SELECT COUNT(*) FROM doctor WHERE specialisation='Ophthalmology'")
print("\nTotal Ophthalmology Doctors:", cursor.fetchone()[0])

conn.close()

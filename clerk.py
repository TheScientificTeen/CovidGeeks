import mysql.connector
import random

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")

def display_deceased():
    mycur.execute("select * from deceased;")
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    f.commit()
    
def display_discharged():
    mycur.execute("select * from discharged;")
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    f.commit()
    

def admit_patient():
    name = input("Enter the patient's name: ")
    age = input("Enter the patient's age: ")
    gender = input("Enter the patient's gender(M/F): ")
    doa = input("Enter the date of admission(YYYY-MM-DD): ")
    status = "mild"
    
    # Selecting a doctor to treat the patient using random
    mycur.execute("select MAX(D_ID) from doctors;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0]
    doc_id = random.randint(1, no)        
        
    # Generating a patient_number for the patient
    mycur.execute("select MAX(ID) from active;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1        
    
    # Selecting a bed for the patient and then changing the bed status to occupied
    mycur.execute("select MAX(B_NO) from beds where STATUS_Vacant_Occupied = 'vacant';")
    dat = mycur.fetchall()
    for line in dat:
        bno = line[0]
    mycur.execute("UPDATE beds SET STATUS_Vacant_Occupied = 'occupied' where B_NO = {};".format(bno,))
        
    mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}',{},'{}','{}');".format(no, bno, name, age, gender, doc_id, doa, status))
    f.commit()

admit_patient()

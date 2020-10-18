import mysql.connector

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")

def display_patients():
    que = "select * from active;"
    mycur.execute(que)
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()
    
def view_patient():
    pid = int(input("Enter patient's id, whom you want to view: "))
    mycur.execute("select * from active where ID = {}".format(pid))
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()

def view_prescription():
    pid = int(input("Enter patient's id, whom you want to view: "))
    mycur.execute("select NAME, MEDICATION, DOSAGE from active, prescriptions where active.ID  = prescriptions.P_ID and P_ID = {}".format(pid))
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()

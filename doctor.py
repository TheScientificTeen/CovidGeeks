import mysql.connector
f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")
idd = int(input("Enter your doctor id: "))

def display_active():
    mycur.execute("select * from active where D_ID = {}".format(idd))
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    f.commit()
        
def view_patient():
    pid = int(input("Enter patient's id, whome you want to view: "))
    mycur.execute("select * from active where ID = {}".format(pid))
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    f.commit()
        
def modify_meds():
    pid = int(input("Enter patient's id, whose medication needs to be modified: "))
    med = input("Enter new medication: ")
    mycur.execute("UPDATE prescriptions SET MEDICATION = '{}' where P_ID = {}".format(med, pid))
    print("Medications modified")
    f.commit()
    
def update_general_status():
    idd = int(input("Enter patient's id, whose status needs to be changed: "))
    stato = input("Enter old status: active/discharged/deceased: ")
    statn = input("Enter new patient status: active/discharged/deceased: ")
    mycur.execute("select * from {} where ID = {}".format(stato, idd))
    dat = mycur.fetchall()
    print(dat)
    for line in dat:
        print(line)
        dats = line
        
    idd = dats[0]
    bno = dats[1]
    nam = dats[2]
    age = dats[3]
    gen = dats[4]
    did = dats[5]
    dadmit = dats[6]
        
    if statn == "active":
        sta = input("Enter status of patient: mild/critical/observation")
        mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}',{},'{}','{}')".format(idd, bno, nam, age, gen, did, dadmit, sta))
        f.commit()
    elif statn == "discharged":
        ddis = input("Enter date of discharge: yyyy-mm-dd: ")
        mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}',{},'{}','{}')".format(idd, bno, nam, age, gen, did, dadmit, ddis))
        f.commit()
    elif statn == "deceased":
        ddea = input("Enter date of death: yyyy-mm-dd: ")
        mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}',{},'{}','{}')".format(idd, bno, nam, age, gen, did, dadmit, ddea))
        f.commit()
    if stato == "active":
        mycur.execute("delete from active where ID = {}".format(idd))
        f.commit()
    elif stato == "discharged":
        mycur.execute("delete from discharged where ID = {}".format(idd))
        f.commit()
    elif stato == "deceased":
        mycur.execute("delete from deceased where ID = {}".format(idd))
        f.commit()
        
def update_active_status():
    idd = int(input("Enter active patient's id, whose status needs updation: "))
    sta = input("Enter new status of patient: mild/critical/observation: ")
    mycur.execute("UPDATE active SET STATUS_Mild_Critical_Observation = '{}' where ID = {}".format(sta, idd))
    print("Status changed")
    f.commit()
    f.close()
    mycur.close()
    
    

update_general_status()
update_active_status()  
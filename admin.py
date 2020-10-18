import mysql.connector
import random

def display_doctor():
    que = "select * from doctors;"
    mycur.execute(que)
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()
    

def add_doctor():
    name = input("Enter the doctor's name: ")
    phone = input("Enter the doctor's phone number: ")
    qual = input("Enter the doctor's qualifications(MD / MBBS): ") 

    mycur.execute("select MAX(D_ID) from doctors;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1
    mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values('{}','{}','{}','{}')".format(no, name, phone, qual))
    print("You added the doctor sucessfully!")
    print()
    f.commit()


def del_doctor():
    doc_id = int(input("Enter the doctors id: "))
    mycur.execute("delete from doctors where D_ID = '{}'".format(doc_id))
    print("You removed the doctor sucessfully!")
    print()
    f.commit()
#-----------------------------------------------------

def display_nurse():
    que = "select * from nurses;"
    mycur.execute(que)
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()

def add_nurse():
    name = input("Enter the nurse's name: ")
    phone = input("Enter the nurse's phone number: ")

    mycur.execute("select MAX(N_ID) from nurses;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1
    mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values('{}','{}','{}')".format(no, name, phone,))
    print("You added the nurse sucessfully!")
    print()
    f.commit()

def del_nurse():
    nur_id = input("Enter the nurse's id: ")
    mycur.execute("delete from nurses where N_ID = '{}'".format(nur_id))
    print("You removed the nurse sucessfully!")
    print()
    f.commit()

#------------------------------------------------------

def display_clerk():
    que = "select * from clerks;"
    mycur.execute(que)
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()

def add_clerk():
    name = input("Enter the clerk's name: ")
    phone = input("Enter the clerk's phone number: ")

    mycur.execute("select MAX(C_ID) from clerks;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1
    mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values('{}','{}','{}')".format(no, name, phone,))
    print("You added the clerk sucessfully!")
    print()
    f.commit()

def del_clerk():
    clerk_id = input("Enter the clerk's id: ")
    mycur.execute("delete from clerks where C_ID = '{}'".format(clerk_id))
    print("You removed the clerk sucessfully!")
    print()
    f.commit()

#------------------------------------------------------


def available_beds():
    mycur.execute("select * from beds where STATUS_Vacant_Occupied = 'vacant' ;")
    dat = mycur.fetchall()
    for line in dat:
        print(line)
    print()
    f.commit()

def add_beds():
    mycur.execute("select MAX(B_NO) from beds;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0]

    num = int(input("Enter the number of beds you want to add: "))

    for i in range(num):
        floor = random.randint(1, 6)
        wing = random.choice(["A", "B", "C", "D", "E"])
        building = random.randint(1, 3)
        no += 1
        mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values('{}','{}','{}','{}','{}')".format(no, floor, wing, building, "vacant"))
    print("You added the beds sucessfully!")
    print()
    f.commit()

#-------------------------------------------------------

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")



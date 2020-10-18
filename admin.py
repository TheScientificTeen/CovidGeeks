import mysql.connector
import random

def display_doctor():
    que = "select * from doctors;"
    mycur.execute(que)
    dat = mycur.fetchall()
    for line in dat:
        print(line)
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
    f.commit()


def del_doctor():
    doc_id = int(input("Enter the doctors id: "))
    mycur.execute("delete from doctors where D_ID = '{}'".format(doc_id))
    f.commit()
#-----------------------------------------------------

def display_nurse():
    que = "select * from nurses;"
    mycur.execute(que)
    dat = mycur.fetchall()
    print(dat)
    f.commit()

def add_nurse():
    name = input("Enter the nurse's name: ")
    phone = input("Enter the nurse's phone number: ")

    mycur.execute("select MAX(N_ID) from nurses;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1
    mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values('{}','{}','{}')".format(no, name, phone,))

    f.commit()

def del_nurse():
    nur_id = input("Enter the nurse's id: ")
    mycur.execute("delete from nurses where N_ID = '{}'".format(nur_id))
    f.commit()

#------------------------------------------------------

def display_clerk():
    que = "select * from clerks;"
    mycur.execute(que)
    dat = mycur.fetchall()
    print(dat)
    f.commit()

def add_clerk():
    name = input("Enter the clerk's name: ")
    phone = input("Enter the clerk's phone number: ")

    mycur.execute("select MAX(C_ID) from clerks;")
    dat = mycur.fetchall()
    for line in dat:
        no = line[0] + 1
    mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values('{}','{}','{}')".format(no, name, phone,))

    f.commit()

def del_clerk():
    clerk_id = input("Enter the clerk's id: ")
    mycur.execute("delete from clerks where C_ID = '{}'".format(clerk_id))
    f.commit()

#------------------------------------------------------


def available_beds():
    mycur.execute("select * from beds where STATUS_Vacant_Occupied = 'vacant' ;")
    dat = mycur.fetchall()
    for line in dat:
        print(line)
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

    f.commit()

#-------------------------------------------------------

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")


while True:

    print("Enter D: Edit doctors")
    print("Enter N: Edit nurses")
    print("Enter C: Edit clerks")
    print("Enter B: Edit beds")
    print("Enter E: Exit")

    opt = input("Enter your option: ")

    if opt == "D" or opt == "d":
        print("Enter 1: Display all the doctors")
        print("Enter 2: Add a doctor")
        print("Enter 3: Remove a doctor")
        print("Enter E: Exit")

        opt = input("Enter your option: ")

        if opt == '1':
            display_doctor()
        if opt == '2':
            add_doctor()
        if opt == '3':
            del_doctor()
        if opt == "E" or opt == "e":
            exit()

    if opt == "N" or opt == "n":
        print("Enter 1: Display all the nurses")
        print("Enter 2: Add a nurse")
        print("Enter 3: Remove a nurse")
        print("Enter E: Exit")

        opt = input("Enter your option: ")

        if opt == '1':
            display_nurse()
        if opt == '2':
            add_nurse()
        if opt == '3':
            del_nurse()
        if opt == "E" or opt == "e":
            exit()


    
    if opt == "C" or opt == "c":
        print("Enter 1: Display all the clerks")
        print("Enter 2: Add a clerk")
        print("Enter 3: Remove a clerk")
        print("Enter E: Exit")

        opt = input("Enter your option: ")

        if opt == '1':
            display_clerk()
        if opt == '2':
            add_clerk()
        if opt == '3':
            del_clerk()
        if opt == "E" or opt == "e":
            exit()   


    if opt == "B" or opt == "b":
        print("Enter 1: Check the number of available beds")
        print("Enter 2: Add new beds")
        print("Enter E: Exit")

        opt = input("Enter your option: ")

        if opt == '1':
            available_beds()
        if opt == '2':
            add_beds()
        if opt == "E" or opt == "e":
            exit()

            
            
            
            
   

import mysql.connector
import admin
import nurse
import doctor
import clerk


def admincall():
    while True:
    
        print("Enter D: Edit doctors")
        print("Enter N: Edit nurses")
        print("Enter C: Edit clerks")
        print("Enter B: Edit beds")
        print("Enter E: Exit")
        print()

        opt = input("Enter your option: ")
    
        
        if opt == "D" or opt == "d":
            while opt != "E" or opt != "e":
                print("Enter 1: Display all the doctors")
                print("Enter 2: Add a doctor")
                print("Enter 3: Remove a doctor")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    admin.display_doctor()
                if opt == '2':
                    admin.add_doctor()
                if opt == '3':
                    admin.del_doctor()

        if opt == "N" or opt == "n":
            while opt != "E"or opt != "e": 
                print("Enter 1: Display all the nurses")
                print("Enter 2: Add a nurse")
                print("Enter 3: Remove a nurse")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    admin.display_nurse()
                if opt == '2':
                    admin.add_nurse()
                if opt == '3':
                    admin.del_nurse()

    
        if opt == "C" or opt == "c":
            while opt != "E"or opt != "e": 
                print("Enter 1: Display all the clerks")
                print("Enter 2: Add a clerk")
                print("Enter 3: Remove a clerk")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    admin.display_clerk()
                if opt == '2':
                    admin.add_clerk()
                if opt == '3':
                    admin.del_clerk()


        if opt == "B" or opt == "b":
            while opt != "E"or opt != "e": 
                print("Enter 1: Check the number of available beds")
                print("Enter 2: Add new beds")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    admin.available_beds()
                if opt == '2':
                    admin.add_beds()
                
                
        if opt == "E"or opt == "e": 
            exit()



def nursecall():
    while True:
    
        print("Enter 1: View all the active patients")
        print("Enter 2: View a particular patient's details")
        print("Enter 3: View a patient's prescription and dosage")
        print("Enter E: Exit")
        print()

        opt = input("Enter your option: ")
    
        if opt == "1":
            nurse.display_patient()
            
        if opt == "2":
            nurse.view_patient()
            
        if opt == "3":
            nurse.view_prescription()
                
        if opt == "E"or opt == "e": 
            exit()
        
def clerkcall():
    while True:
    
        print("Enter 1: View all the deceased patients")
        print("Enter 2: View all the discharged patients")
        print("Enter 3: Admit a new patient")
        print("Enter E: Exit")
        print()

        opt = input("Enter your option: ")
    
        if opt == "1":
            clerk.display_deceased()
            
        if opt == "2":
            clerk.display_discharged()
            
        if opt == "3":
            clerk.admit_patient()
                
        if opt == "E"or opt == "e": 
            exit()
        
def doctorcall():
    while True:
        print("Enter 1: Display all active cases")
        print("Enter 2: View a particular patient")
        print("Enter 3: Modify a patients medication")
        print("Enter 4: Update the Status of a patient(Discharge, Deceased, Active) ")
        print("Enter 5: Update the status of an active case(Mild, Critical, Under observation) ")
        print("Enter E: Exit")
        print()
        
        opt = input("Enter your option: ")
    
        if opt == "1":
            doctor.display_active()
            
        if opt == "2":
            doctor.view_patient()
            
        if opt == "3":
            doctor.modify_meds()
            
        if opt == "4":
            doctor.update_general_status()
            
        if opt == "5":
            doctor.update_active_status()
                
        if opt == "E"or opt == "e": 
            exit()

def passw():
    user = input("Enter your username: ")
    pasw = input("Enter your password: ")
    mycur.execute("select ID from login where USERNAME = '{}' and PASSWORD = '{}'".format(user, pasw))
    dat = mycur.fetchall()
    for line in dat:
        no = line[0]


f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")

mycur.execute("select D_ID from doctors;")
dat = mycur.fetchall()
mycur.execute("select N_ID from nurses;")
dat = mycur.fetchall()
mycur.execute("select C_ID from clerks;")
dat = mycur.fetchall()

user = input("Enter your username: ")
pasw = input("Enter your password: ")
mycur.execute("select ID from login where USERNAME = '{}' and PASSWORD = '{}'".format(user, pasw))
dat = mycur.fetchall()
count = 0
if dat == []:
    print("Incorrect password or username. Please try again.")
    print()
    
#Checking if the username and password are correct and after 5 tries shutting the program
while dat == []:
    passw()
    if count == 4:
        print("You exeeded the number of tries.")
        exit()
    print("Incorrect password or username. Please try again.")
    print()
    count += 1
    
for line in dat:
    no = line[0]

print("Great! Entry Sucessful")
print()

if no == 1:
    admincall()
if no == 2:
    doctorcall()
if no == 3:
    nursecall()
if no == 4:
    clerkcall()

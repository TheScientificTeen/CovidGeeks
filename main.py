import mysql.connector
import admin.py
import nurse.py
import doctor.py
import clerk.py

def admin():
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
                    display_doctor()
                if opt == '2':
                    add_doctor()
                if opt == '3':
                    del_doctor()

        if opt == "N" or opt == "n":
            while opt != "E"or opt != "e": 
                print("Enter 1: Display all the nurses")
                print("Enter 2: Add a nurse")
                print("Enter 3: Remove a nurse")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    display_nurse()
                if opt == '2':
                    add_nurse()
                if opt == '3':
                    del_nurse()

    
        if opt == "C" or opt == "c":
            while opt != "E"or opt != "e": 
                print("Enter 1: Display all the clerks")
                print("Enter 2: Add a clerk")
                print("Enter 3: Remove a clerk")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    display_clerk()
                if opt == '2':
                    add_clerk()
                if opt == '3':
                    del_clerk()


        if opt == "B" or opt == "b":
            while opt != "E"or opt != "e": 
                print("Enter 1: Check the number of available beds")
                print("Enter 2: Add new beds")
                print("Enter E: Exit")
                print()

                opt = input("Enter your option: ")

                if opt == '1':
                    available_beds()
                if opt == '2':
                    add_beds()
                
                
        if opt == "E"or opt == "e": 
            break



def nurse():
    while True:
    
        print("Enter 1: View all the active patients")
        print("Enter 2: View a particular patient's details")
        print("Enter 3: View a patient's prescription and dosage")
        print("Enter E: Exit")
        print()

        opt = input("Enter your option: ")
    
        if opt == "1":
            display_patient()
            
        if opt == "2":
            view_patient()
            
        if opt == "3":
            view_prescription()
                
        if opt == "E"or opt == "e": 
            break
        
def clerk():
    while True:
    
        print("Enter 1: View all the deceased patients")
        print("Enter 2: View all the discharged patients")
        print("Enter 3: Admit a new patient")
        print("Enter E: Exit")
        print()

        opt = input("Enter your option: ")
    
        if opt == "1":
            display_deceased()
            
        if opt == "2":
            display_discharged()
            
        if opt == "3":
            admit_patient()
                
        if opt == "E"or opt == "e": 
            break
        
def doctor():
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
            display_active()
            
        if opt == "2":
            view_patient()
            
        if opt == "3":
            modify_meds()
            
        if opt == "4":
            update_general_status()
            
        if opt == "5":
            update_active_status()
                
        if opt == "E"or opt == "e": 
            break


f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")

mycur.execute("select D_ID from doctors;")
dat = mycur.fetchall()
mycur.execute("select N_ID from nurses;")
dat = mycur.fetchall()
mycur.execute("select C_ID from clerks;")
dat = mycur.fetchall()

def pasw():
    user = input("Enter your username: ")
    pasw = input("Enter your password: ")
    mycur.execute("select ID from login where USERNAME = '{}' and PASSWORD = '{}'".format(user, pasw))
    dat = mycur.fetchall()
    for line in dat:
        no = line[0]
    
#Checking if the username and password are correct and after 5 tries shutting the program
while no == None:
    pasw()
    if count == 5:
        print("You exeeded the number of tries.")
        exit()
    print("Incorrect password or username. Please try again.")
    count += 1
    
    
if no == 1:
    admin()
if no == 2:
    doctor()
if no == 3:
    nurse()
if no == 4:
    clerk()
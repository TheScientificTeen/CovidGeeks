import mysql.connector

#CREATING THE DATABASE

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()
mycur.execute("create database MyHospital;")
print("database created")
f.commit()
f.close()
mycur.close()

#CREATING TABLE USERNAME AND PASSWORD

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")
mycur.execute("create table login(ID integer NOT NULL primary key, USERNAME varchar(20), PASSWORD varchar(30));")
print("login patients table created")
f.commit()

#CREATING TABLE DISCHARGED PATIENTS

mycur.execute("create table discharged(ID integer NOT NULL primary key, B_NO integer, NAME varchar(30), AGE integer, GENDER varchar(20), D_ID varchar(20), DATE_ADMISSION date, DATE_DISCHARGE date);")
print("discharged patients table created")
f.commit()

#CREATING TABLE ACTIVE PATIENTS

mycur.execute("create table active(ID integer NOT NULL primary key, B_NO integer, NAME varchar(30), AGE integer, GENDER varchar(20), D_ID varchar(20), DATE_ADMISSION date, STATUS_Mild_Critical_Observation varchar(20));")
print("active patients table created")
f.commit()

#CREATE TABLE DECEASED PATIENTS

mycur.execute("create table deceased(ID integer NOT NULL primary key, B_NO integer, NAME varchar(30), AGE integer, GENDER varchar(20), D_ID varchar(20), DATE_ADMISSION date, DATE_DEATH date);")
print("deceased patients table created")
f.commit()

#CREATING TABLE DOCTORS

mycur.execute("create table doctors(D_ID integer NOT NULL primary key, NAME varchar(30), PHONE_NO varchar(20), QUALIFICATION varchar(20));")
print("doctors table created")
f.commit()

#CREATING TABLE PRESCRIPTIONS

mycur.execute("create table prescriptions(P_ID integer, D_ID integer, MEDICATION varchar(40), DOSAGE varchar(10));")
print("prescriptions table created")
mycur.execute("insert into prescriptions(P_ID, D_ID, MEDICATION, DOSAGE)values({},{},'{}','{}')".format(1 ,1,'Dolo and Setzin' ,'101'))
f.commit()

#CREATING TABLE BEDS

mycur.execute("create table beds(B_NO integer NOT NULL primary key, FLOOR integer, WING varchar(10), BUILDING integer, STATUS_Vacant_Occupied varchar(20));")
print("beds table created")
f.commit()

#CREATING TABLE NURSE

mycur.execute("create table nurses(N_ID integer NOT NULL primary key, NAME varchar(30), PHONE_NO varchar(20));")
print("nurses table created")
f.commit()

#CREATING TABLE CLERK

mycur.execute("create table clerks(C_ID integer NOT NULL primary key, NAME varchar(30), PHONE_NO varchar(20));")
print("clerks table created")
f.commit()
f.close()
mycur.close()









    



    
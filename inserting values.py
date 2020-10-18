import mysql.connector
f = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "MyHospital")
mycur = f.cursor()
mycur.execute("use MyHospital;")
#INSERTING INTO LOGIN TABLE

mycur.execute("insert into login(ID, USERNAME, PASSWORD)values({},'{}','{}')".format(1 ,'Admin', 'Admin123'))
mycur.execute("insert into login(ID, USERNAME, PASSWORD)values({},'{}','{}')".format(2 ,'Doctor', 'Doctor123'))
mycur.execute("insert into login(ID, USERNAME, PASSWORD)values({},'{}','{}')".format(3 ,'Nurse', 'Nurse123'))
mycur.execute("insert into login(ID, USERNAME, PASSWORD)values({},'{}','{}')".format(4 ,'Clerk', 'Clerk123'))
f.commit()

#INSERTING INTO DISCHARGED TABLE

mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(100 ,6,'Nikhil',21 ,'Male',1,'2020-06-04','2020-07-30'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(101 ,1,'Emily',13 ,'Female',5,'2020-08-04','2020-03-19'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(102 ,3,'Markus',67 ,'Male',4,'2019-06-04','2020-05-09'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(103 ,2,'Dominic',35 ,'Male',2,'2020-07-04','2020-06-03'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(104 ,5,'Sushmita',21 ,'Female',3,'2019-09-04','2020-03-07'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(105 ,4,'Rashmi',28 ,'Female',4,'2020-03-04','2020-07-29'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(106 ,9,'Mason',46 ,'Male',2,'2019-09-04','2020-08-18'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(107 ,8,'Palakh',34 ,'Male',5,'2020-01-04','2020-02-29'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(108 ,7,'Naomi',51 ,'Female',2,'2019-05-04','2020-03-23'))
mycur.execute("insert into discharged(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DISCHARGE)values({},{},'{}',{},'{}','{}','{}','{}')".format(109 ,10,'Nishant',19 ,'Male',3,'2020-06-04','2020-04-12'))
f.commit()

#INSERTING INTO ACTIVE TABLE

mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}','{}','{}','{}')".format(1 ,11,'Rahul',21 ,'Male',1,'2019-06-04','mild'))
mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}','{}','{}','{}')".format(2 ,15,'Abhishek',45 ,'Male',5,'2020-04-24','critical'))
mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}','{}','{}','{}')".format(3 ,13,'Anna',20 ,'Female',3,'2019-12-29','mild'))
mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}','{}','{}','{}')".format(4 ,14,'Sasha',19 ,'Female',4,'2020-03-12','observation'))
mycur.execute("insert into active(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, STATUS_Mild_Critical_Observation)values({},{},'{}',{},'{}','{}','{}','{}')".format(5 ,12,'Pranav',37 ,'Male',2,'2019-08-03','critical'))

#INSERTING INTO DECEASED TABLE

mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}','{}','{}','{}')".format(200 ,21,'Malaeka',21 ,'Female',3,'2019-09-12','2020-01-03'))
mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}','{}','{}','{}')".format(201 ,25,'Rishit',29 ,'Male',2,'2020-04-29','2020-05-03'))
mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}','{}','{}','{}')".format(202 ,24,'Tarun',68 ,'Male',1,'2019-06-18','2020-01-24'))
mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}','{}','{}','{}')".format(203 ,22,'Angelica',52 ,'Female',5,'2019-12-26','2020-02-10'))
mycur.execute("insert into deceased(ID, B_NO, NAME, AGE, GENDER, D_ID, DATE_ADMISSION, DATE_DEATH)values({},{},'{}',{},'{}','{}','{}','{}')".format(204 ,23,'Halent',25 ,'Male',4,'2020-04-21','2020-05-09'))

#INSERTING INTO TABLE DOCTORS

mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values({},'{}','{}','{}')".format(1 ,'Mohan','9667857686' ,'MBBS'))
mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values({},'{}','{}','{}')".format(2 ,'Tarika','9587687584' ,'MBBS'))
mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values({},'{}','{}','{}')".format(3 ,'Johnson','9117263546' ,'MD'))
mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values({},'{}','{}','{}')".format(4 ,'Paren','9478857638' ,'MBBS'))
mycur.execute("insert into doctors(D_ID, NAME, PHONE_NO, QUALIFICATION)values({},'{}','{}','{}')".format(5 ,'Hailey','9212134432' ,'MD'))

#INSERTING INTO TABLE BEDS

mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(1 , 3, 'A',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(2 , 1, 'B',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(3 , 2, 'C',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(4 , 6, 'D',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(5 , 5, 'E',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(6 , 4, 'F',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(7 , 1, 'A',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(8 , 6, 'B',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(9 , 2, 'C',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(10 , 4, 'D',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(11, 3, 'E',2, 'occupied'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(12, 5, 'F',3, 'occupied'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(13, 1, 'A',1, 'occupied'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(14, 6, 'B',1, 'occupied'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(15, 5, 'C',3, 'occupied'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(16 , 4, 'D',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(17, 3, 'E',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(18, 2, 'F',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(19, 1, 'A',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(20, 6, 'B',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(21, 2, 'C',2, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(22, 1, 'D',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(23, 5, 'E',3, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(24, 4, 'F',1, 'vacant'))
mycur.execute("insert into beds(B_NO, FLOOR, WING, BUILDING, STATUS_Vacant_Occupied)values({},{},'{}',{},'{}')".format(25 , 3, 'A',1, 'vacant'))

#INSERTING INTO TABLE NURSES

mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values({},'{}','{}')".format(100 ,'Rebecca','9667757586'))
mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values({},'{}','{}')".format(101 ,'Smith','9776354657'))
mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values({},'{}','{}')".format(102 ,'Harrold','9883645546'))
mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values({},'{}','{}')".format(103 ,'Fernando','875676857'))
mycur.execute("insert into nurses(N_ID, NAME, PHONE_NO)values({},'{}','{}')".format(104 ,'Lily','8374659927'))

#INSERTING INTO TABLE CLERKS

mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values({},'{}','{}')".format(200 ,'Rahul','9627557976'))
mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values({},'{}','{}')".format(201 ,'Mahesh','9775648576'))
mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values({},'{}','{}')".format(202 ,'Nitika','91524354253'))
mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values({},'{}','{}')".format(203 ,'Rajesh','9756746574'))
mycur.execute("insert into clerks(C_ID, NAME, PHONE_NO)values({},'{}','{}')".format(204 ,'Clark','9772635463'))
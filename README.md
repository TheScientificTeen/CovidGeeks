# CovidGeeks

### 8:10PM IST
##### Started creating mysql database with predefined values
##### Started creating admin interface for program

### 11:40PM IST
##### Finished creating database and all required tables
##### Finished creating the admin view on the project

### 9:20AM IST
##### Inserting values into the tables
##### Working on the doctor and nurse view

### 11:00AM IST
##### Finished nurse interface
##### Created additional table prescriptions


### 1:00PM IST
##### Finished clerk interface
##### In process of making doctor interface

### 3:00PM IST
##### Finished doctor iterface
##### Finished the main code (main.py)
##### Started adding the values in the database

### 3:30PM IST
##### Finished adding the values into the database
##### Started debugging all files

### 4:30PM IST
##### Finished debugging
##### Made minor changes
##### Logged off for a break


Covid-19 has affected both developed as well as developing nations. In India, we are running out of capacity in hospitals.Government has set up several Covid Care Centers (CCC) in major cities. These Centers are equipped with good equipment and staff, but need management software. There is a need to create reports at each level so that information is available to everyone in the system. The status changes every hour, so effective information sharing is a key here.

Our piece of code attempts to build an effective solution in a very simple and intuitive manner to manage all the work processes within a Covid Care Center, from the time a patient walks into a center to his/her discharge after treatment. It provides the right level of information to all doctors and medical staff to make the right decision at all times.

At first when the doctor/admin/nurse/clerk want to enter into their account, they will be asked for their username and password.(In our code we decidedto keep it simple by making the doctor username to be "doctor" and password to be "doctor123" and so on for the remaining personas which is admin, nurse and clerk.

Upon loging in with their correct paswword, they will each get to see only a particular set of functions which they can perform, Eg the admin can add, remove or see any doctor, nurse or clerk while the nurse can only see the patients and their required medications and dosages.

Main.py – This is the main entry point of the program, which handles the user authentication and assigns role-based operations. It invokes the other Python files based on the role.
Doctor.py – This gets invoked if the authentication process identifies the user as a doctor. This gives the doctors access to the patients files and update prescriptions.
Nurse.py – This gets invoked if the user is a nursing staff. It is used to check the prescription and to administer dosages
Admin.py – This is used by the center administrators to add capacity, doctors or nurses
Clerk.py – This gets invoked for the clerks for admission and discharge of the patients
Creating database.py – This is a one-time script to create the database tables
Inserting values.py – This is also a one time script to insert some predefined values into your mysql database to perform initial functions.
 


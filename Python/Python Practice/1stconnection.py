#importing mysql connector

import mysql.connector  

#Connecting to MySQL Using Connector/Python

dbpy = mysql.connector.connect(
  host="localhost",  
  user="abc",
  password="password"
)

#Checking connection status

print(dbpy.is_connected()) 

#Creating Cursor object to interact with the MySQL server

dbcur = dbpy.cursor() 

# execute the statement
dbcur.execute("show databases")

for x in dbcur:
    print(x)




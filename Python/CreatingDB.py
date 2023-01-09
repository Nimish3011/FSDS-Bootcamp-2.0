import mysql.connector

dbpy = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(dbpy.is_connected())

dbcur = dbpy.cursor()

dbcur.execute("show databases")

for x in dbcur:
    print(x)

dbcur.execute("use studinfo")

dbcur.execute('create table stud (rollno int,name varchar(20),lname varchar(20),dept varchar(20))')

#dbcur.execute("insert into stud(rollno,name,lname,dept) values(111,'Nimish','Gaikwad','CSE'),(112,'Raju','Kumar','Mech'),(113,'Nisha','Jain','CSE'),(114,'Deva','Rathod','Civil'),(115,'Rashi','Kasat','E&T')")
#dbpy.commit()


#dbcur.execute("select name from studinfo.stud")
for x in dbcur:
  print(x)

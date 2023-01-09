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




import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="jdinterface"
    
)
mycursor=mydb.cursor()


sql = "insert into emp(name,sal,dept_name) values (%s,%s,%s)"

val = ("abc",130,"limdi")

try:
    mycursor.execute(sql,val)
    print(mycursor.rowcount,"Record Inserted ID!",mycursor.lastrowid)
    mydb.commit()
except:
    mydb.rollback()
    print(mycursor.rowcount,"Record not Inserted!")
    mydb.close()

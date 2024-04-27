import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythondb"
)
mycursor=mydb.cursor()
sql="INSERT INTO emp VAlUES(%s,%s,%s,%s)"
no=input("enter Id")
name=input("Enter name:")
depr=input("deperatmente:")
sal=input("Enter Salary")
val = (no,name,depr,sal)
mycursor.execute(sql,val)
mydb.commit()
print("record Inserted")
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tybca"
)
mycursor=mydb.cursor()
sql="Insert into emp VALUES(%s,%s,%s,%s)"
no=input("Enter Id")
name=input("Enter Name")
depr=input("Enter Department")
sal=input("Enter Salary")

val=(no,name,depr,sal)
mycursor.execute(sql,val)
mydb.commit()
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
    
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE jdinterface")
print("DB Created")


try:
    dbs = mycursor.execute("show Database")
except:
    mydb.rollback()
for x  in mycursor:
           print(x)
mydb.close()

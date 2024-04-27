import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="pythondb"
)
mycursor=mydb.cursor()
sql="UPDATE emp SET name='jainam' WHERE id=1"
cursor.execute(sql)

mydb.commit()
print(mycursor.rowcount,"record Inserted")
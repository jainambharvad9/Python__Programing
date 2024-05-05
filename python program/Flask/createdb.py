import sqlite3
conn = sqlite3.connect("mydatabase.db")
conn.execute('''
             Create table student(
                 student_id INT AUTO_INCREMENT PRIMARY KEY,
                name TEXT(50),
                city TEXT(50),
                addr TEXT(200),
                pin INT(10)
             )
            ''')
conn.close()
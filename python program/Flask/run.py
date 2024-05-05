# from flask import Flask,render_template,request,url_for

# import sqlite3 as sql

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template('myhome.html')

# @app.route("/enternew")
# def student_new():
#     return render_template('addstudent.html')

# @app.route("/addres",methods= ['POST','GET'])
# def addres():
#     if request.method == 'POST':
#         try:
#             name.request.form['name']
#             address.request.form['address']
#             city.request.form['city']
#             pin.request.form['pin']
#             with sql.connect("database.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT INTO student (name,address,city,pin) VALUES (?,?,?,?)",(nm,address,city,pin))
#                 con.commit()
#                 msg = "Record Inserted Successfully"
#         except:
#             con.rollback()
#             msg = "Error"
#         finally:
#             return render_template('myresult.html',msg = msg)
#     con.close()
# @app.route('/list')
# def list():
#     con=sql.connect("database.db")
#     con.row_factory = sql.Row
#     cut = con.cursor()
#     cut.execute("select * from students")
#     rows=cut.fetchall()
#     return render_template('list.html',rows = rows)

# if __name__ == '__main__':
#     app.run(debug=True)
       
       
       
from flask import Flask, render_template, request, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('myhome.html')

@app.route("/enternew")
def student_new():
    return render_template('addstudent.html')

@app.route("/addres", methods=['POST','GET'])
def addres():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO student (name, address, city, pin) VALUES (?, ?, ?, ?)", (name, address, city, pin))
                con.commit()
                msg = "Record Inserted Successfully"
        except Exception as e:
            con.rollback()
            msg = f"Error: {str(e)}"
        finally:
            con.close()
            return render_template('myresult.html', msg=msg)

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return render_template('list.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
 
    

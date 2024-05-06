# from flask import Flask,request,url_for,render_template,flash,redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'


# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class students(db.Model):
#     id = db.Column('student_id',db.Integer,primary_key=True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200))
#     pin  = db.Column(db.String(10))
    
#     def __init__(self,name,city,addr,pin):
#         self.name = name
#         self.city = city
#         self.addr = addr
#         self.pin = pin
        
# @app.route('/')
# def show_all():
#     return render_template('show_all.html',students=students.query.all())

# @app.route('/new', methods=['POST','GET'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash("All Fields Are Required",'Error')
#         else:
#             student = students(request.form['name'],
#                               request.form['city'],
#                               request.form['addr'],
#                               request.form['pin'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record Was Added Successfully')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask,request,flash,url_for,redirect,render_template
# from flask_sqlalchemy import SQLAlchemy

# app= Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3'
# app.config['SECRET_KEY']='random string'
# db=SQLAlchemy(app)

# class students(db.Model):
#     id= db.Column('student_id',db.Integer,primary_key=True)
#     name=db.Column(db.String(100))
#     city=db.Column(db.String(50))
#     addr=db.Column(db.String(200))
#     pin=db.Column(db.String(10))
#     def init(self,name,city,addr,pin):
#         self.name=name
#         self.city=city
#         self.addr=addr
#         self.pin=pin
    
# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students=students.query.all())

# @app.route('/new', methods=['GET','POST'])
# def new():
#     if request.method=='POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash('Pls enter all fields')
#         else:
#             student = students(request.form['name'],request.form['city'],request.form['addr'],request.form['pin'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record inserted Successfully')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, url_for, render_template, flash, redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class Student(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     address = db.Column(db.String(200))
#     postal_code = db.Column(db.String(10))

#     def __init__(self, name, city, address, postal_code):
#         self.name = name
#         self.city = city
#         self.address = address
#         self.postal_code = postal_code

#     def __repr__(self):
#         return f"Student('{self.name}', '{self.city}', '{self.address}', '{self.postal_code}')"


# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students=Student.query.all())


# @app.route('/new', methods=['POST', 'GET'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['address']:
#             flash("All Fields Are Required", 'Error')
#         else:
#             student = Student(request.form['name'],
#                               request.form['city'],
#                               request.form['address'],
#                               request.form['postal_code'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record Was Added Successfully')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')


# if __name__ == '__main__':
#     db.create_all()  # Create the database tables
#     app.run(debug=True)

# from flask import Flask, request, url_for, render_template, flash, redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class students(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200))
#     pin  = db.Column(db.String(10))

#     def __init__(self, name, city, addr, pin):
#         self.name = name
#         self.city = city
#         self.addr = addr
#         self.pin = pin

# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students=students.query.all())

# @app.route('/new', methods=['POST', 'GET'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash("All Fields Are Required", 'Error')
#         else:
#             student = students(request.form['name'],
#                               request.form['city'],
#                               request.form['addr'],
#                               request.form['pin'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record Was Added Successfully')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    
    
    
# from flask import Flask,request,url_for,render_template,flash,redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress SQLAlchemy warning

# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class Student(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200))
#     pin  = db.Column(db.String(10))
    
#     def __init__(self, name, city, addr, pin):
#         self.name = name
#         self.city = city
#         self.addr = addr
#         self.pin = pin

# # Create tables
# db.create_all()

# @app.route('/')
# def show_all():
#     return render_template('show_all.html', students=Student.query.all())

# @app.route('/new', methods=['POST','GET'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr']:
#             flash("All Fields Are Required", 'Error')
#         else:
#             student = Student(request.form['name'],
#                               request.form['city'],
#                               request.form['addr'],
#                               request.form['pin'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record Was Added Successfully')
#             return redirect(url_for('show_all'))
#     return render_template('new.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, url_for, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress SQLAlchemy warning
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    
    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def show_all():
    return render_template('show_all.html', students=Student.query.all())

@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash("All Fields Are Required", 'Error')
        else:
            student = Student(request.form['name'],
                              request.form['city'],
                              request.form['addr'],
                              request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record Was Added Successfully')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template,redirect,url_for,request,abort

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('login.html')

# @app.route('/login',methods =['POST','GET'])
# def login():
#     if request.method == 'POST' and request.form['nm']== 'admin':
#         return redirect(url_for('success'))
#     return redirect(url_for('index'))

# @app.route('/success')
# def success():
#     return 'login Is Successfully'

# if __name__ == '__main__':
#     app.run(debug=True)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login',methods =['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['nm']== 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'login Is Successfully'

if __name__ == '__main__':
    app.run(debug=True)
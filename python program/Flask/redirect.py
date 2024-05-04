from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login',methods =['POST','GET'])
def login():
    if request.method == 'POST' and request.form['nm']== 'admin':
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'login Is Successfully'

if __name__ == '__main__':
    app.run(debug=True)
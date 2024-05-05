from flask import Flask, render_template,redirect,request,url_for,flash

app = Flask(__name__)
app.secret_key="rendome string"
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login',methods =['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
                error = 'Invelid username and password'
        else:
            flash('U Have Login Successfully Done....')
            flash('Logout You Before Login...')
            return redirect(url_for('home'))
    return render_template('log_in.html',error = error)

if __name__ == '__main__':
    app.run(debug=True)
    
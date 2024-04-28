from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/admin')
def hello_adimin():
    return 'Aavo Aavo Mota Bhai'

@app.route('/user/<user>')
def hello_user(user):
    return 'Aavo Aavo  %s  Bhai' % user

@app.route('/mainuser/<name>')
def hello_mainuser(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user',user=name))
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,redirect,url_for, request

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome %s' % name


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user=request.form["name"]
        return redirect(url_for('Welcome',name=user))
    else:
        user=request.args.get("name")
        return redirect(url_for('Welcome',name=user))
    
if __name__ == '__main__':
    app.run(debug=True)
        
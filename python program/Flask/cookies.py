from flask import Flask,render_template,request,make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('cookies.html')

@app.route('/sercookie',methods =['POST','GET'])
def setcooki():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcooki.html'))
        resp.set_cookie("userID",user)
        return resp
    
@app.route('/getcooki')
def getcooki():
    name = request.cookies.get('userID')
    return 
    
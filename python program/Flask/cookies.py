from flask import Flask,render_template,request,make_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('cookies.html')

@app.route('/cookies',methods =['POST','GET'])
def cookies():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcooki.html'))
        resp.set_cookie("userID",user)
        return resp
    
@app.route('/getcooki')
def getcooki():
    name = request.cookies.get('userID')
    if name:
        return '<h1> Welcome ' + str(name) + '</h1>'
    else:
        return '<h1> Welcome ' +str(name)+ '</h1>' 

     
if __name__ == '__main__':
    app.run(debug=True)
    
    
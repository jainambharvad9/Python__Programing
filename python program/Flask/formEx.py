from flask import Flask,render_template,request,flash
from wtfform import ContactForm

app = Flask(__name__)
app.secret_key='Devlopment key'

@app.route("/contact",methods = ['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            flash("All Fields Are Required.")
            return render_template('contact.html',form = form)
        else:
            return render_template('success.html' )
    if request.method == 'GET':
        return render_template('contact.html',form = form)
    
if __name__ == '__main__':
    app.run(debug=True)
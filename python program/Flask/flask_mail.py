from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jainambharvad9@gmail.com'
app.config['MAIL_PASSWORD'] = '1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

@app.route("/")
def index():
    msg = Message('Hello', sender='jainambharvad9@gmail.com', recipients=['bcasem320@gmail.com'])
    msg.body = "Kaa Bhai Maja Maa nee Su Kee Baki Su Chale Badha ne"
    mail.send(msg)
    return "Message Sent"

if __name__ == '__main__':
    app.run(debug=True)

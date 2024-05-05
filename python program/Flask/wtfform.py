from flask_wtf import Form
from wtforms import TelField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField,StringField,EmailField
import email_validator
from wtforms import validators,ValidationError

class ContactForm(Form):
    name = StringField("Name Of Student")
    Gender = RadioField("Gender",choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("Address")
    
    email = EmailField("Email")
    
    Age = IntegerField("Age")
    language = SelectField('Languages',choices=[('Cpp','C++'),('Py','Python')])
    submit  = SubmitField("send")
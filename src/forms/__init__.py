from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired 

class BaseAuthForm(FlaskForm):
  email = EmailField("Email", validators=[DataRequired(message="Please type your email")])
  password = PasswordField("Password", validators=[DataRequired(message="Please type your password")])
  submit = SubmitField("Submit", validators=[DataRequired()])
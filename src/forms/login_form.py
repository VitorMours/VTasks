from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired 


class LoginForm(FlaskForm):
  email = EmailField("email", validators=[DataRequired()])
  password = PasswordField("password", validators=[DataRequired()])
  submit = SubmitField("submit", validators=[DataRequired()])
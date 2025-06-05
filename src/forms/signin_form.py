from . import BaseAuthForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class SigninForm(BaseAuthForm):
  first_name = StringField("First name", validators=[DataRequired(message="Plesae type your first name")])
  last_name = StringField("Last name")
  password = PasswordField("Password", validators=[DataRequired(message="Please type your password"), Length(min=8, max=64)])
  confirm_password = PasswordField("Password", validators=[DataRequired(message="Please type your password"), Length(min=8, max=64)])


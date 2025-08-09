from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired 

class BaseAuthForm(FlaskForm):
  email = EmailField("Email", validators=[DataRequired(message="Please type your email")])
  password = PasswordField("Password", validators=[DataRequired(message="Please type your password")])
  submit = SubmitField("Submit", validators=[DataRequired()])

class NoteForm(FlaskForm):
  title = StringField("Title", validators=[DataRequired(message="Please, do not create a titless note...")])
  content = StringField("Content", render_kw={"placeholder":"Type the content of your note..."})
  create = SubmitField("Create Note", validators=[DataRequired()])
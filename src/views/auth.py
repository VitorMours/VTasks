from flask import Blueprint, render_template, flash, redirect
from flask.views import View, MethodView

from ..forms.login_form import LoginForm

bp = Blueprint("auth", __name__, template_folder="templates")

class LoginView(MethodView):
  def get(self):
    form = LoginForm()
    return render_template("pages/login.html", form=form)
  
  def post(self):
    form = LoginForm()
    if form.validate_on_submit():
      pass

class SigninView(View):
  def dispatch_request(self):
    return render_template("pages/signin.html")

bp.add_url_rule("/login/", view_func=LoginView.as_view("login"))
bp.add_url_rule("/signin/", view_func=LoginView.as_view("signin"))





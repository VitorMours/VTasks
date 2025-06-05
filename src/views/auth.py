from flask import Blueprint, render_template, flash, redirect
from flask.views import View, MethodView

from ..forms.login_form import LoginForm
from ..forms.signin_form import SigninForm

bp = Blueprint("auth", __name__, template_folder="templates")

class LoginView(MethodView):
  def get(self) -> str:
    form = LoginForm()
    return render_template("pages/login.html", form=form)

  def post(self) -> str:
    form = LoginForm()
    print(form.email)
    # if form.validate_on_submit():
      # print(form)

class SigninView(MethodView):
  def get(self) -> str:
    form = SigninForm()
    return render_template("pages/signin.html", form=form)

  def post(self) -> str:
    form = SigninForm()
    if form.validate_on_submit():
      return render_template("pages/home.html")
      # TODO: Preciso adicionar a validacao, de forma que as mensagens de erro possam ser passadas e iteradas dentro do tempalte
    return render_template("pages/signin.html", form=form)

bp.add_url_rule("/login/", view_func=LoginView.as_view("login"))
bp.add_url_rule("/signin/", view_func=SigninView.as_view("signin"))





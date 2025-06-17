from flask import Blueprint, render_template, flash, redirect, url_for
from flask.views import View, MethodView
from ..services.impl.auth_service_impl import AuthServiceImpl
from ..forms.login_form import LoginForm
from ..forms.signin_form import SigninForm

bp = Blueprint("auth", __name__)
auth_service = AuthServiceImpl()


class LoginView(MethodView):

  def get(self) -> str:
    form = LoginForm()
    return render_template("login.html", form=form)

  def post(self) -> str:
    form = LoginForm()

    if form.validate_on_submit():
          email = form.data["email"]
          password = form.data["password"]




    return redirect(url_for("views.auth.login"))

class SigninView(MethodView):
  def get(self) -> str:
    form = SigninForm()
    return render_template("signin.html", form=form)

  def post(self) -> str:
    form = SigninForm()

    if form.validate_on_submit():
      data = form.data
      auth_service.create_and_login_user(data)
    return render_template("signin.html", form=form)

bp.add_url_rule("/login/", view_func=LoginView.as_view("login"))
bp.add_url_rule("/signin/", view_func=SigninView.as_view("signin"))





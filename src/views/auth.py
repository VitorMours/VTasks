from flask import Blueprint, render_template, flash, redirect, url_for, g
from flask.views import View, MethodView
from ..services.impl.auth_service_impl import AuthServiceImpl
from ..forms.login_form import LoginForm
from ..forms.signin_form import SigninForm
from ..utils.security import sanitize_request

bp = Blueprint("auth", __name__)


class LoginView(MethodView):

  def get(self) -> str:
    form = LoginForm()
    return render_template("login.html", form=form)

  @sanitize_request
  def post(self) -> str:
    form = LoginForm()

    if form.validate_on_submit():
        try: 
            response = AuthServiceImpl.login_user(g.sanitized_request)
            print(response)
            return redirect(url_for("views.home.home"))
        except Exception as e: 
            flash(f"{e.message}", "warning")
            return redirect(url_for("views.auth.login"))
        
    flash("Não foi possível fazer o login devido algum erro que ocorreu", "danger")
    return redirect(url_for("views.auth.login"))

class SigninView(MethodView):
  def get(self) -> str:
    form = SigninForm()
    return render_template("signin.html", form=form)

  @sanitize_request
  def post(self) -> str:
    form = SigninForm()

    if form.validate_on_submit():
      data = form.data
      authentication = AuthServiceImpl.create_and_login_user(data)

      if authentication:
        return redirect(url_for("views.home.home"))
    return render_template("signin.html", form=form)

class LogoutView(View):
    def dispatch_request(self):
        if AuthServiceImpl.check_session():
            AuthServiceImpl.logout_user()
            return redirect(url_for("views.index"))
        flash("Você não pode fazer logout sem estar dentro de um login","warning")


bp.add_url_rule("/login", view_func=LoginView.as_view("login"))
bp.add_url_rule("/signin", view_func=SigninView.as_view("signin"))
bp.add_url_rule("/logout", view_func=LogoutView.as_view("logout"))




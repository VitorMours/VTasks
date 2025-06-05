from flask import Blueprint, render_template, flash, redirect
from flask.views import View
# from .admin import bp as admin 
from .auth import bp as auth
from ..models.user_model import User
from src.repositories.user_repository import UserRepository
bp = Blueprint("views", __name__, template_folder="templates")

class IndexView(View):
    def dispatch_request(self):
        user_repository = UserRepository(User)
        users = user_repository.get_all()
        print(users)
        return render_template("pages/index.html", users=users)

bp.add_url_rule("/", view_func=IndexView.as_view("index"))


# bp.register_blueprint(admin)
bp.register_blueprint(auth)

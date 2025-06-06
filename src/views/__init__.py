from flask import Blueprint, render_template, flash, redirect
from flask.views import View
from .auth import bp as auth
from .home import bp as home
from ..models.user_model import User

from src.repositories.user_repository import UserRepository
bp = Blueprint("views", __name__)

class IndexView(View):
    def dispatch_request(self):
        user_repository = UserRepository(User)
        users = user_repository.get_all()
        print(users)
        return render_template("index.html", users=users)

bp.add_url_rule("/", view_func=IndexView.as_view("index"))


bp.register_blueprint(auth)
bp.register_blueprint(home)

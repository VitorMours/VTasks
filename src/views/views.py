from flask import Blueprint, render_template, flash, redirect
from flask.views import View

bp = Blueprint("views", __name__, template_folder="templates")


class IndexView(View):
    def dispatch_request(self):
        return render_template("pages/index.html")

bp.add_url_rule("/", view_func=IndexView.as_view("index"))
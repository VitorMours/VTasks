from flask import Blueprint, redirect, render_template, flash 
from flask.views import MethodView, View

bp = Blueprint("home", __name__)

class DashboardView(View):
	def dispatch_request(self) -> str:
		return render_template("dashboard.html")


bp.add_url_rule("/home/", view_func=DashboardView.as_view("dashboard"))

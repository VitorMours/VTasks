from flask import Blueprint, redirect, render_template, flash 
from flask.views import MethodView, View
bp = Blueprint("home", __name__)

class HomeView(View):
	def dispatch_request(self) -> str:
		return render_template("home.html", active_page="home")

class DashboardView(MethodView):
	def get(self) -> str:
		return render_template("dashboard.html", active_page="dashboard")

class TodoView(MethodView):
	def get(self) -> str:
		return render_template("todo.html", active_page="todo")

bp.add_url_rule("/home/", view_func=HomeView.as_view("home"))
bp.add_url_rule("/dashboard/", view_func=DashboardView.as_view("dashboard"))
bp.add_url_rule("/todo/", view_func=TodoView.as_view("todo"))

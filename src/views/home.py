from flask import Blueprint, redirect, render_template, flash, request
from flask.views import MethodView, View
from src.services.impl.task_service_impl import TaskServiceImpl
from src.utils.security import login_required
import json

bp = Blueprint("home", __name__)

class HomeView(View):
    decorators = [login_required]

    def dispatch_request(self) -> str:
        return render_template("home.html", active_page="home")

class DashboardView(MethodView):
    decorators = [login_required]

    def get(self) -> str:
        return render_template("dashboard.html", active_page="dashboard")

class TodoView(MethodView):
    decorators = [login_required]

    def get(self) -> str:
        tasks = TaskServiceImpl.get_all()
        print(tasks)
        return render_template("todo.html", active_page="todo", tasks = tasks)
    
    def post(self) -> str:
        data = request.get_json()
        if not isinstance(data, dict):
            try:
                data = json.loads(data)
            except Exception:
                data = {}
        TaskServiceImpl.create(data)
        return render_template("todo.html", active_page="todo")

bp.add_url_rule("/home", view_func=HomeView.as_view("home"))
bp.add_url_rule("/dashboard", view_func=DashboardView.as_view("dashboard"))
bp.add_url_rule("/todo", view_func=TodoView.as_view("todo"))

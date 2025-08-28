from flask import Blueprint, redirect, render_template, flash, request, url_for, jsonify
from flask.views import MethodView, View
from src.services.impl.task_service_impl import TaskServiceImpl
from src.utils.security import login_required
import json

bp = Blueprint("home", __name__)



class HomeView(View):
    decorators = [login_required]

    def dispatch_request(self) -> str:
        return render_template("home.html", active_page="home")



class NotesView(MethodView):
    decorators = [login_required]

    def get(self) -> str:
        return render_template("notes.html", active_page="notes")

class NoteTakerView(MethodView):
    decorators = [login_required]

    def get(self, note_uuid: int) -> str:
        # TODO: Fazer esse método para retornar um template da nota, especificado com base na rota
        # note = Note
        # return render_template("note_taker.html", note_uuid = note_uuid active_page="notes")
        pass




class TodoView(MethodView):
    decorators = [login_required]

    def get(self) -> str:
        tasks = TaskServiceImpl.get_all(as_json=True)
        return render_template("todo.jinja", active_page="todo", tasks = tasks)
    
    def post(self) -> str:
        data = request.get_json()
        if not isinstance(data, dict):
            try:
                data = json.loads(data)
            except Exception:
                data = {}
        TaskServiceImpl.create(data)
        return redirect(url_for("views.home.todo"))

bp.add_url_rule("/home", view_func=HomeView.as_view("home"))
bp.add_url_rule("/notes", view_func=NotesView.as_view("notes"))
bp.add_url_rule("/note/<int:id>", view_func=NoteTakerView.as_view("note_taker"), Note) # FIXME: Corrigir isso daqui p
bp.add_url_rule("/todo", view_func=TodoView.as_view("todo"))
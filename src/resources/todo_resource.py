from typing import List
from flask_restx import Namespace, Resource, fields
from ..models.task_model import Task
from ..services.user_service import UserService
from ..services.task_service import TaskService
from ..repositories.task_repository import TaskRepository
from ..utils.api import single_task_serializer, user_serializer 

bp = Namespace("todo", description="Endpoint to manage the tasks")




task_model_fields = bp.model("TaskCreation", {
    "task":fields.String(required=True, decription="The task name"),
    "task_description":fields.String(required=True, decription="The task description"),
    "user_id":fields.String(required=True, decription="The task owner uuid"),
})



@bp.route("/")
@bp.response(404, "tasks not found")
@bp.response(201, "Task Created")
@bp.response(200, "Tasks finded")
class TasksList(Resource):
    def get(self) -> List[Task]:
        tasks = TaskService.get_all()
        return tasks

    @bp.expect(task_model_fields)
    def post(self) -> None:
        user = UserService.get_user_by_id(bp.payload["user_id"])
        task = Task(
            task=bp.payload["task"],
            task_description=bp.payload["task_description"],
            task_conclusion=False,
            user_id=bp.payload["user_id"]
        )
        TaskRepository.create(task)

        return single_task_serializer(task)
    
    
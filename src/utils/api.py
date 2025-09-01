from ..models.task_model import Task
from ..models.user_model import User


def user_serializer(users: list[User]):
    return [{"id":user.id,"first_name":user.first_name,"last_name":user.last_name,"email":user.email} for user in users]

def task_serializer(tasks: list[Task]):
    return [{"id":task.id,"first_name":task.task,"last_name":task.task_description,"conclusion":task.task_conclusion} for task in tasks]


def single_task_serializer(task: Task):
    return {"id":task.id,"first_name":task.task,"last_name":task.task_description,"conclusion":task.task_conclusion}

from ..models.task_model import Task
from ..models import db
from typing import List 
from src.models.task_model import Task

class TaskRepository:
    
    @staticmethod 
    def create(task_data: Task) -> None:
        """
        Create a new task in the database based on the user as the foreign key.
        """
        try: 
            task = Task(
                task=task_data["task_name"],
                task_description=task_data.get("task_description", ""),
                user_id=task_data["user_id"]
            )
            db.session.add(task)
            db.session.commit()
        
        except Exception as e:
            raise e
        
    
    @staticmethod
    def get_all_user_tasks(user_id: int) -> List[Task]:
        try:
            tasks = Task.query.filter_by(user_id=user_id).all()
            return tasks
        except Exception as e:
            raise e
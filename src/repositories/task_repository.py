from ..models.task_model import Task
from ..models import db

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
            print(task)
            db.session.add(task)
            db.session.commit()
        
        except Exception as e:
            raise e
        
    
    
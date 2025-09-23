from ..models import db
from typing import List 
from src.models.task_model import Task
from src.models.user_model import User

class TaskRepository:
    
    @staticmethod 
    def create(task_data: dict, user: User) -> None:
        """
        Create a new task in the database based on the user as the foreign key.
        """
        
    @staticmethod
    def update() -> None:
        pass
    @staticmethod
    def delete() -> None:
        pass
    
    @staticmethod
    def get_all() -> None:
        pass
    
    @staticmethod
    def get_by_email() -> None:
        pass
    
    @staticmethod 
    def get_by_id() -> None:
        pass
        
from abc import ABC, abstractmethod
from flask import session
from ..task_service import TaskService
from src.repositories.task_repository import TaskRepository
from src.services.impl.user_service_impl import UserServiceImpl
class TaskServiceImpl(TaskService):
    
    @staticmethod
    def get_all() -> None:
        pass

    @staticmethod
    def delete() -> None:
        pass

    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def toggle_status() -> None:
        pass

    @staticmethod
    def check_owner() -> None:
        pass

    @staticmethod
    def get_one_by_id() -> None:
        pass

    @staticmethod
    def create(data: dict[str, str]) -> None:
        if (user := UserServiceImpl.check_user_by_id(data)):
            print(user)
            data["user_id"] = session["user_id"]
            task = TaskRepository.create(data)
        

    
    

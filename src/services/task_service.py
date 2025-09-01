from abc import ABC, abstractmethod
import json
from flask import session
from ..interfaces.task_service_interface import TaskServiceInterface
from ..services.user_service import UserService
from src.repositories.task_repository import TaskRepository
from src.models.task_model import Task


class TaskService(TaskServiceInterface):
    
    @staticmethod
    def get_all(as_json = False) -> Task | list[dict[str, str | bool]]:
        user_id = session.get("user_id")
        tasks = TaskRepository.get_all_user_tasks(user_id)
        if as_json:
            tasks_list = list()
            if not isinstance(tasks, dict):
                for task in tasks:
                    task_dict = task.to_json()
                    tasks_list.append(task_dict)
            return tasks_list
        return tasks

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
        if (user := UserService.check_user_by_id(data)):
            data["user_id"] = session["user_id"]
            task = TaskRepository.create(data)
        

    
    

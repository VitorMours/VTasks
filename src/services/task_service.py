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
        tasks = TaskRepository.get_all()
        if as_json:
            tasks_list = list()
            if not isinstance(tasks, dict):
                for task in tasks:
                    task_dict = task.to_json()
                    tasks_list.append(task_dict)
            return tasks_list
        return tasks

    @staticmethod
    def get_user_tasks() -> None:
        user_email = session.get("user_email")
        all_tasks = TaskRepository.get_by_email(user_email)
        return all_tasks

    @staticmethod
    def create(data: dict[str, str]) -> None:
        user = UserService.get_user_by_email(session.get("email"))
        if not user:
            raise Exception("User not found.")
        
        created_task = TaskRepository.create(
            task_data={
                "task": data.get("task"),
                "task_description": data.get("task_description"),
                "task_conclusion": data.get("task_conclusion")
            },
            user_id=user.id  # ← Apenas o ID, não o objeto User
        )

        return created_task

    
    
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
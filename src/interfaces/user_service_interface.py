from abc import ABC, abstractmethod
from src.models.task_model import Task

class UserServiceInterface(ABC):

    @abstractmethod
    def create_user(data) -> None:
        pass

    @abstractmethod
    def get_tasks() -> list[Task]:
        pass

    @abstractmethod
    def check_user(data: dict[str, str]) -> bool:
        pass

    @abstractmethod
    def check_password(password: str) -> bool:
        pass

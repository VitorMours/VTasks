from abc import ABC, abstractmethod
from src.models.task_model import Task

class UserService(ABC):


    # TODO: Esse serivo, vai ser pra verificar algumas queestnoes de sanitizacao e de padronizacao, pra eu nao ficar me preocupando em ficar limpando dado, e coisas do tipo

    @abstractmethod
    def create_user(data) -> None:
        pass

    @abstractmethod
    def get_tasks() -> List[Task]
        pass

    @abstractmethod
    def check_user(data: dict[str, str]) -> bool:
        pass

    @abstractmethod
    def check_password(password: str) -> bool:
        pass

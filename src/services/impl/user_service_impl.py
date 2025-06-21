from src.models.task_model import Task

class UserServiceImpl(UserService):
    @staticmethod
    def create_user(data) -> None:
        pass

    @staticmethod
    def get_tasks() -> List[Task]
        pass

    @staticmethod
    def check_user(data: dict[str, str]) -> bool:
        pass

    @staticmethod
    def check_password(password: str) -> bool:
        pass

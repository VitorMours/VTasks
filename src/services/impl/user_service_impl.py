from src.models.task_model import Task
from src.models.user_model import User
from src.utils.erros import UserDoesNotExistsError
from src.repositories.user_repository import UserRepository
from ..user_service import UserService

class UserServiceImpl(UserService):

    @staticmethod
    def create_user(data) -> None:
        try:
            sanitized_data = data.copy()
            for key in ["submit","csrf_token","confirm_password"]:
                sanitized_data.pop(key, None)
            UserRepository.save(sanitized_data)
        except Exception as e:
            raise e

    @staticmethod
    def get_user(data) -> User:
        if UserRepository.user_exists(data):
            user = UserRepository.get_user_by_email(data["email"])
            return user
        return UserDoesNotExistsError("The user does not exists in the database")

    @staticmethod
    def get_tasks() -> list[Task]:
        pass

    @staticmethod
    def check_user(data: dict[str, str]) -> bool:
        user = UserRepository.user_exists(data)
        return user

    @staticmethod
    def check_password(password: str) -> bool:
        pass


from src.models.task_model import Task
from src.models.user_model import User
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
        return UserRepository.get_user_by_email(email=data["email"])

    @staticmethod
    def get_tasks() -> list[Task]:


    @staticmethod
    def check_user(data: dict[str, str]) -> bool:
        email = data["email"]
        user_exists = UserRepository.get_user_by_email(email)
        if len(user_exists) > 0:
            return True
        return False

    @staticmethod
    def check_password(password: str) -> bool:
        pass


from typing import List
from ..interfaces.user_service_interface import UserServiceInterface
from src.models.task_model import Task
from src.models.user_model import User
from src.utils.erros import UserDoesNotExistsError
from src.utils.security import check_password, encrypt_password
from src.repositories.user_repository import UserRepository
from collections.abc import Hashable
from flask import session


class UserService(UserServiceInterface):

    @staticmethod
    def create_user(data) -> None:
        try:
            sanitized_data = data.copy()
            for key in ["submit","csrf_token","confirm_password"]:
                sanitized_data.pop(key, None)
                
            sanitized_data["password"] = encrypt_password(data["password"])
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
    def get_user_by_id(id) -> User:
        user = UserRepository.get_user_by_id(id)
        return user

    @staticmethod
    def get_all_users() -> List[User]:
        user = UserRepository.get_all()
        
        print(user)
        if len(user) > 0:
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
    def check_password(password: str, secured_password: Hashable) -> bool:
        return check_password(password, secured_password)


    @staticmethod
    def check_user_by_id(data: dict[str, str]) -> User:
        """
        Check if the user exists by ID.
        """
        user = UserRepository.get_user_by_id(session.get("user_id"))
        if user is None:
            raise UserDoesNotExistsError("The user does not exists in the database")
        return user
from abc import ABC
from typing import List
from ..interfaces.user_service_interface import UserServiceInterface
from src.models.user_model import User
from src.utils.erros import UserDoesNotExistsError
from src.utils.security import check_password, encrypt_password
from src.repositories.user_repository import UserRepository
from collections.abc import Hashable
from flask import session
from src.utils.security import email_validator

class UserService(UserServiceInterface):

    @staticmethod
    def create_user(data) -> None:
        pass

    @staticmethod
    def get_all_users() -> None:
        pass

    @staticmethod
    def get_user_by_email(data) -> None:
        pass

    @staticmethod
    def update_user(user, data) -> None:
        pass

    @staticmethod
    def delete_user(data) -> None:
        pass
    @staticmethod
    def exists(user: User | str) -> bool:
        """
        Check if user exists
        """
        if type(user) == User:
            email = user.email
            # user = UserRepository.get_by_email(email)
        elif type(user) == str and email_validator(user):
            return True
        else:
            raise TypeError("This function must receive a email, or a user object to search for the user in the database")

    def __str__(self) -> str:
        return "<UserService>"
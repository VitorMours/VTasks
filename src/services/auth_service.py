from ..interfaces.auth_service_interface import AuthServiceInterface
from .user_service import UserService
from ..repositories.user_repository import UserRepository
from src.models.user_model import User
from src.utils import security
from src.utils.erros import (UserAlreadyExistsError,
                             UserDoesNotExistsError,
                             IncorrectCredentialsToLoginError)

from flask import session, redirect, url_for, flash

class AuthService(AuthServiceInterface):

    @staticmethod
    def _check_session() -> bool:
        return True


    @staticmethod
    def create_session(user: User) -> None:
        print(user)
        return True

    @staticmethod
    def destroy_session() -> None:
        return True

    @staticmethod
    def login_user(user_data: dict) -> None:
        print(user_data)
        AuthService.authenticate_user(user_data)
        return True

    @staticmethod
    def logout_user() -> None:
        return True


    @staticmethod
    def authenticate_user(user_data: dict) -> None:
        service = UserService()
        user_email = user_data["email"]
        if user := service.get_user_by_email(user_email):
            print(user)
        return True
    
    @staticmethod 
    def check_password(password: str, confirmation:str) -> bool | IncorrectCredentialsToLoginError:
        if password == confirmation:
            return True
        else:
            raise IncorrectCredentialsToLoginError("A senha e a contrasenha possuem valores diferentes")
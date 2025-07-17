from ..auth_service import AuthService
from .user_service_impl import UserServiceImpl
from src.repositories.user_repository import UserRepository
from src.models.user_model import User
from src.utils import security
from src.utils.erros import (UserAlreadyExistsError,
                             UserDoesNotExistsError,
                             IncorrectCredentialsToLoginError)

from flask import session, redirect, url_for, flash

class AuthServiceImpl(AuthService):

    @staticmethod
    def create_and_login_user(data) -> bool:
        print("criando o usuario")
        try:
            print("criando o usuario")
            if UserServiceImpl.check_user(data):
            
                print("criando o usuario")
                flash("This email is already registered in the database, may you want to login")
                return False
            else:
                UserServiceImpl.create_user(data)
                print(123123123)
                AuthServiceImpl._create_user_session(data)
                return True
        except Exception as e:
            raise e

    @staticmethod
    def login_user(data: dict[str]) -> bool | Exception:
        if UserServiceImpl.check_user(data):
            email = data["email"]
            password = data["password"]
            if (user := UserRepository.get_user_by_email(email)) and UserServiceImpl.check_password(password, user.password):
                AuthServiceImpl._create_user_session(data)
                return True

            raise IncorrectCredentialsToLoginError("As credenciais enviadas por esse usuário estão erradas")
        raise UserDoesNotExistsError("Esse usuário não está cadastrado dentro do banco de dados")

    @staticmethod
    def logout_user() -> None:
        AuthServiceImpl._destroy_user_session()
        return True

    @staticmethod
    def _create_user_session(data: dict[str, str]) -> None:
        user = UserServiceImpl.get_user(data)
        session["first_name"] = f"{user.first_name}"
        session["username"] = f"{user.first_name} {user.last_name}"
        session["user_id"] = f"{user.id}"
        session["email"] = f"{user.email}"
        session["login"] = True

    @staticmethod 
    def check_session() -> bool: 
        if session is not None:
            return True 
        return False

    @staticmethod
    def _destroy_user_session() -> None:
        session.clear()


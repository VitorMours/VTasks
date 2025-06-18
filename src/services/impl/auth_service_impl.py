from ..auth_service import AuthService
from src.repositories.user_repository import UserRepository
from src.models.user_model import User
from src.utils import security
from src.utils.erros import UserAlreadyExistsError, UserDoesNotExistsError, IncorrectCredentialsToLoginError
from flask import session, redirect, url_for

class AuthServiceImpl(AuthService):

    @staticmethod
    def create_and_login_user(data) -> bool:
        try:
            del data["submit"]
            del data["csrf_token"]
            del data["confirm_password"]
            data["password"] = security.encrypt_password(data["password"])

            if AuthServiceImpl.verify_user_register_by_email(data["email"]):
                raise UserAlreadyExistsError("Esse usuário não pode ser cadastro, pois já possui cadastro com esse email.")

            created_user = UserRepository.save(data, return_user = True)

            try:
                AuthServiceImpl._create_user_session(data)
            except Exception as e:
                raise e
            return True

        except Exception as e:
            raise e

    @staticmethod
    def login_user(data: dict[str]) -> bool | Exception:
        if AuthServiceImpl.verify_user_register_by_email(data["email"]):
            email = data["email"]
            password = data["password"]
            user = UserRepository.get_user_by_email(email)

            if len(user) == 1:
                correct_password = security.check_password(password, user[0].password)

            if correct_password:
                AuthServiceImpl._create_user_session(data)
                return True
            raise IncorrectCredentialsToLoginError("Esse usuario tento logar com as credenciais erradas")

        raise UserDoesNotExistsError("Esse usuario nao esta cadastrado dentro do banco de dados")

    @staticmethod
    def _create_user_session(data: dict[str, str]) -> None:
        session["email"] = data["email"]
        user_data = UserRepository.get_user_by_email(data["email"])
        session["username"] = f"{user_data[0].first_name} {user_data[0].last_name}"

    @staticmethod
    def _destroy_user_session() -> None:
        session.clear()

    @staticmethod
    def verify_user_register_by_email(email: str) -> bool:
        query_result = UserRepository.get_user_by_email(email)

        if query_result:
            return True
        return False

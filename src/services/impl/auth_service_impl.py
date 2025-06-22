from ..auth_service import AuthService
from .user_service_impl import UserServiceImpl
from src.repositories.user_repository import UserRepository

from src.models.user_model import User
from src.utils import security
from src.utils.erros import UserAlreadyExistsError, UserDoesNotExistsError, IncorrectCredentialsToLoginError
from flask import session, redirect, url_for

class AuthServiceImpl(AuthService):

    @staticmethod
    def create_and_login_user(data) -> bool:
        try:
            # TODO: se existir, retornar erro
            # TODO: senao, criar mas primeiro codificar a senha
            # TODO: commitar o banco de dados, e retoranr a tela correta

            if UserServiceImpl.check_user(data):
                # TODO: Mandar uma flash message dizendo que o usuario ja existe dentro do banco de dados
                return redirect(url_for("views.auth.login"))
            UserServiceImpl.create_user(data)
            AuthServiceImpl._create_user_session(data)

            return True
        except Exception as e:
            raise e

    @staticmethod
    def login_user(data: dict[str]) -> bool | Exception:
        if AuthServiceImpl.verify_user_register_by_email(data["email"]):
            email = data["email"]
            password = data["password"]

            if (user := UserRepository.get_user_by_email(email)) and security.check_password(password, user.password):
                AuthServiceImpl._create_user_session(data)
                return True

            raise IncorrectCredentialsToLoginError("As credenciais enviadas por esse usuário estão erradas")
        raise UserDoesNotExistsError("Esse usuário não está cadastrado dentro do banco de dados")

    @staticmethod
    def logout_user() -> None:
        pass

    @staticmethod
    def _create_user_session(data: dict[str, str]) -> None:
        user = UserServiceImpl.get_user(data)
        session["username"] = f"{user.first_name} {user.last_name}"

    @staticmethod
    def _destroy_user_session() -> None:
        session.clear()


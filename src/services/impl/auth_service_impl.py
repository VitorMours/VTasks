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
            # TODO: Receber Usuario
            # TODO: verificar dentro do banco de dados
            # TODO: se existir, retornar erro
            # TODO: senao, criar mas primeiro codificar a senha
            # TODO: commitar o banco de dados, e retoranr a tela correta

            if AuthServiceImpl.verify_user_register_by_email(email=data["email"]):
                # TODO: Usuario registrado, redirecionar para tela de login




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
    def _create_user_session(data: dict[str, str]) -> None:
        session["email"] = data["email"]
        user_data = UserRepository.get_user_by_email(data["email"])
        session["username"] = f"{user_data.first_name} {user_data.last_name}"

    @staticmethod
    def _destroy_user_session() -> None:
        session.clear()

    @staticmethod
    def verify_user_register_by_email(email: str) -> bool:
        """
        Verifica se o usuário possui algum registro dentro do banco de dados por meio do email,
        que foi definida como uma chave de cadastro singular
        """

        return UserService.get_user_by_email(email)

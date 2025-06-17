from ..auth_service import AuthService
from src.repositories.user_repository import UserRepository
from src.models.user_model import User
from src.utils import security
from src.utils.erros import UserAlreadyExistsError
from flask import session

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

    def login_user(data: dict[str, str]) -> None:
        if AuthServiceImpl.verify_user_register_by_email(data["email"]):
            email = data["email"]
            password = ["password"]
            user = UserRepository.get_user_by_email(email)
            security.check_password(password, user.password)

        raise UserDoesNotExistsError("Esse usuario nao esta cadastrado dentro do banco de dados")

    @staticmethod
    def _create_user_session(data: dict[str, str]) -> None:
        session["email"] = data["email"]
        session["username"] = f"{data["first_name"]} {data["last_name"]}"

    @staticmethod
    def _destroy_user_session() -> None:
        session.clear()

    @staticmethod
    def verify_user_register_by_email(email: str) -> bool:
        query_result = UserRepository.get_user_by_email(email)

        if query_result:
            return True
        return False

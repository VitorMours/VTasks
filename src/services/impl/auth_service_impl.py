from ..auth_service import AuthService
from src.repositories.user_repository import UserRepository
from src.models.user_model import User
from src.utils import security
from src.utils.erros import UserAlreadyExistsError
from flask import session

class AuthServiceImpl(AuthService):

    @staticmethod
    def create_and_login_user(data) -> None:
        try:
            del data["submit"]
            del data["csrf_token"]
            del data["confirm_password"]
            data["password"] = security.encrypt_password(data["password"])

            if AuthServiceImpl.verify_user_register_by_email(data["email"]):
                raise UserAlreadyExistsError("Esse usuário não pode ser cadastro, pois já possui cadastro com esse email.")

            created_user = UserRepository.save(data, return_user = True)


            # TODO: Feito a autenticacao, precisa-se fazer o redirecionamento, e a criacao de sessao

        except Exception as e:
            raise e

    @staticmethod
    def verify_user_register_by_email(email: str) -> bool:
        query_result = UserRepository.get_user_by_email(email)

        if query_result:
            return True
        return False





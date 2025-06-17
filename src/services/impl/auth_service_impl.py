from ..auth_service import AuthService
from src.repositories.user_repository import UserRepository


class AuthServiceImpl(AuthService):


    @staticmethod
    def create_and_login_user(data) -> None:
        del data["submit"]
        del data["csrf_token"]
        del data["confirm_password"]



        created_user = UserRepository.save(data, return_user = True)
        print(created_user)

    @staticmethod
    def generate_password_hash(self) -> str:
        pass


    @staticmethod
    def decrypt_password_hash(self) -> str:
        pass


from ..auth_service import AuthService


class AuthServiceImpl(AuthService):


    @staticmethod
    def create_and_save_user(data) -> None:
        print(f"Mostrando os dados do usuario: {data}")




    @staticmethod
    def generate_password_hash(self) -> str:
        pass


    @staticmethod
    def decrypt_password_hash(self) -> str:
        pass


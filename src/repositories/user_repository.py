from src.models.user_model import User
from src.models import db
from typing import List
from src.utils.erros import DuplicateRegisterError, UserDoesNotExistsError

class UserRepository:

    @staticmethod
    def save(user_data: User, return_user: bool = False) -> None | User:
        try:
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()

            if return_user:
                return user
#
        except TypeError as e:
            raise TypeError(f"Foi encontrado um erro de tipo durante a criação de um usuário: {e}")

    @staticmethod
    def get_all() -> List[User] | User:
        users = User.query.all()
        return users

    @staticmethod
    def get_user_by_email(email: str) -> list[str]:
        try:
            user = User.query.filter_by(email=email).all()
            if len(user) > 1:
                raise DuplicateRegisterError("""Existem dois registros dentro do banco de dados com o mesmo email.""")
            return user

        except Exception as e:
            raise Exception(e)

    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete(id: int) -> None:
        pass

    @staticmethod
    def get_full_name() -> str:
        return User.full_name

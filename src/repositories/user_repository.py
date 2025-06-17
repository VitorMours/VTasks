from src.models.user_model import User
from src.models import db
from typing import List


class UserRepository:
    @staticmethod
    def save(user_data: User, return_user: bool = False) -> None | User:
        try:
            user = User(**user_data)
            db.session.add(user)
            db.session.commit()

            if return_user:
                return user
        except TypeError as e:
            raise TypeError(f"Foi encontrado um erro de tipo durante a criação de um usuário: {e}")

    @staticmethod
    def get_all() -> List[User] | User:
        users = User.query.all()
        return users

    @staticmethod
    def get_user_by_email(email: str) -> str | int:
        users = User.query.filter_by(email=email)
        if user := len(users) == 1:
            pass
        elif len(users) == 0:
            return 0
        raise ValueError("Existem dois registros dentro do banco de dados com o mesmo email, entre em contato com nossa equipe de suporte para resolutar o problema.")

    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete(id: int) -> None:
        pass

    @staticmethod
    def get_full_name() -> str:
        return User.full_name
    

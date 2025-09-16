import sqlalchemy

from src.models.user_model import User
from src.models import db
from typing import List

from src.utils.erros import UserDoesNotExistsError, IncorrectUserDataError, UserAlreadyExistsError

class UserRepository:
    @staticmethod
    def create(user: User) -> bool | IncorrectUserDataError:
        """
        Method to create a new user in the database

        Returns:
        -------
            Return True if the user was successfully created else IncorrectUserDataErrors
        """
        db.session.add(user)
        db.session.commit()
        return True

    @staticmethod
    def get_all() -> List[User] | User:
        users = User.query.all()
        return users

    @staticmethod
    def get_by_email(email: str) -> list[str]:
        try:
            user = User.query.filter_by(email=email).first()
            if user is None:
                raise UserDoesNotExistsError("The user does not exists.")
            return user

        except UserDoesNotExistsError:
            raise UserDoesNotExistsError("The user does not exists.")
        
    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete(id: int) -> None:
        pass

    def __str__(self) -> str:
        return "<UserRepository>"
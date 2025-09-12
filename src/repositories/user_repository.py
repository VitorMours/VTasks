import sqlalchemy

from src.models.user_model import User
from src.models import db
from typing import List

from src.utils.erros import UserDoesNotExistsError, IncorrectUserDataError, UserAlreadyExistsError


class UserRepository:
    @staticmethod
    def save(user_data: User, return_user: bool = False) -> None | User:
        """
            Method to get a user data, and try to save a user in the the database

            Parameters:
            ----------

            Returns:
            -------
        """

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
    def create(user: User) -> bool | IncorrectUserDataError:
        """
        Method to create a new user in the database

        Returns:
        -------
            Return True if the user was successfully created else IncorrectUserDataErrors
        """
        try:
            # TODO: Ned to add the password encriptation to be more safe
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            if e == sqlalchemy.exc.IntegrityError:
                raise UserAlreadyExistsError("Ja existe um usuario com esse email")

    @staticmethod
    def get_by_email(email: str) -> list[str]:
        try:
            user = User.query.filter_by(email=email).first()
            if user is None:
                raise UserDoesNotExistsError("The user does not exists.")
            return user

        except Exception as e:
            raise Exception(e)
        
    @staticmethod 
    def get_by_id(id: str) -> User:
        try:
            user = User.query.filter_by(id=id).first()
            if user is None:
                raise UserDoesNotExistsError("The user does not exists.")
            return user

        except Exception as e:
            raise Exception(e)


    @staticmethod
    def exists(data: dict[str, str]) -> bool:
        """
        Function that return True if the user exists, and False if does not exists
        """
        try:
            user_email = data["email"]
            user = User.query.filter_by(email=user_email).all()
            if len(user) != 1:
                return False
            return True

        except Exception as e:
            raise e

    @staticmethod
    def update() -> None:
        pass

    @staticmethod
    def delete(id: int) -> None:
        pass

    @staticmethod
    def get_full_name() -> str:
        return User.full_name


    def __repr__(self) -> str:
        return "<UserRepository>"
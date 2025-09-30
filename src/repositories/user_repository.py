from src.models.user_model import User
from src.models import db
from typing import List
from src.utils.security import email_validator
from src.utils.erros import UserDoesNotExistsError, IncorrectUserDataError, UserAlreadyExistsError

class UserRepository:
    @staticmethod
    def create(data: dict) -> bool | IncorrectUserDataError:
        """
        Method to create a new user in the database

        Returns:
        -------
            Return True if the user was successfully created else IncorrectUserDataErrors
        """
        try:
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception:
            db.session.rollback()
            return IncorrectUserDataError("Invalid user data")

    @staticmethod
    def get_all() -> List[User] | User:
        users = User.query.all()
        return users

    @staticmethod
    def get_by_email(email: str) -> list[str]:
        return  User.query.filter_by(email=email).first()
        
    @staticmethod
    def update(user: User, data: dict[str, str | int]) -> User:
        for key in data.keys():
            if key not in user.__dict__:
                raise IncorrectUserDataError("The user does not have the required key '{}'".format(key))
            if not hasattr(user, key):
                raise IncorrectUserDataError("The user does not have the required key '{}'".format(key))
            if key == "email":
                email_validator(data["email"])

        if searched_user := User.query.filter_by(email=user.email).first():
            for key in data.keys():
                if key in searched_user.__dict__:
                    setattr(searched_user, key, data[key])

        db.session.commit()
        return searched_user

    @staticmethod
    def delete(id: int) -> None:
        pass

    def __str__(self) -> str:
        return "<UserRepository>"
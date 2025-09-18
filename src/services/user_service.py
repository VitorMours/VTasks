from abc import ABC
from typing import List
from ..utils.erros import IncorrectUserDataError
from ..interfaces.user_service_interface import UserServiceInterface
from src.models.user_model import User
from src.utils.security import check_password, encrypt_password
from src.repositories.user_repository import UserRepository
from collections.abc import Hashable
from flask import session
from src.utils.security import email_validator

class UserService(UserServiceInterface):

    @staticmethod
    def create_user(data) -> None:
        """
        Função que verifica os dados do dicionario que é passado,
        e caso estejam corretos usa para criar um usuário por meio do
        UserRepository
        """
        virtuals_and_fk_fields_list =["notes","tasks","full_name"]
        necessary_fields = set()
        try:
            if type(data) != dict:
                print(1)
                raise IncorrectUserDataError("Existem valores que foram esquecidos, ou passados incorretamente dentro dos dados.")
            fields = User.__dict__
        
            for field in fields:
                if field.startswith("_") or field.startswith("__") or field in virtuals_and_fk_fields_list:
                    continue
                else:
                    necessary_fields.add(field)
                
            print(f"{len(data.keys())} { len(necessary_fields)}")
            print(f"{data.keys()} { necessary_fields}")
            if len(data.keys()) != len(necessary_fields):
                print(2)
                raise IncorrectUserDataError("Existem valores que foram esquecidos, ou passados incorretamente dentro dos dados.")

            for key in data.keys():
                print(3)
                if key not in necessary_fields:
                    raise IncorrectUserDataError("Existem valores que foram esquecidos, ou passados incorretamente dentro dos dados.")

            return UserRepository.create(**data)
        
        except Exception as e:
            return e

    @staticmethod
    def get_all_users() -> None:
        all_users = UserRepository.get_all()
        return all_users

    @staticmethod
    def get_user_by_email(data) -> None:
        pass

    @staticmethod
    def update_user(user, data) -> None:
        pass

    @staticmethod
    def delete_user(data) -> None:
        pass
    @staticmethod
    def exists(user: User | str) -> bool | None:
        """
        Check if user exists
        """
        try:
            if type(user) == User:
                email = user.email
                if UserRepository.get_by_email(email): #type: ignore
                    return True

            elif type(user) == str and email_validator(user):
                if UserRepository.get_by_email(user):
                    return True
            else:
                raise TypeError
        except Exception as e:
            raise e

    def __str__(self) -> str:
        return "<UserService>"

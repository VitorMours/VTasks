from abc import ABC, abstractmethod

class AuthServiceInterface(ABC):

    @staticmethod
    @abstractmethod
    def create_session():
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def destroy_session():
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def check_session():
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def logout_user() -> None:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def login_user(user_data: dict) -> None:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def authenticate_user(user_data: dict) -> None:
        raise NotImplementedError()

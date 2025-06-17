from abc import ABC, abstractmethod

class AuthService(ABC):

    @abstractmethod
    def create_and_login_user(data) -> None:
        pass

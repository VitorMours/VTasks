from abc import ABC, abstractmethod

class AuthServiceInterface(ABC):

    @abstractmethod
    def create_and_login_user(data) -> None:
        pass

    @abstractmethod
    def _create_user_session():
        pass

    @abstractmethod
    def _destroy_user_session():
        pass

    @abstractmethod 
    def _check_session():
        pass

    @abstractmethod
    def logout_user() -> None:
        pass

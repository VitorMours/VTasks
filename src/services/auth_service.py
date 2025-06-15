from abc import ABC, abstractmethod

class AuthService(ABC):

    @abstractmethod
    def generate_password_hash(self):
        pass

    @abstractmethod
    def decrypt_password_hash(self):
        pass


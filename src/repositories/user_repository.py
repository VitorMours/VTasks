from src.models.user_model import User
from typing import List

class UserRepository:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model

    def save(self) -> None:
        pass

    def get_all(self) -> List[User] | User:
        users = self.user_model.query.all()
        return users

    def get_user(self) -> None:
        pass

    def get_user_attribute(self, attribute) -> None:
        pass

    def update() -> None:
        pass 

    def delete(self, id: int) -> None:
        pass

    
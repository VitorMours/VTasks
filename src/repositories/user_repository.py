from src.models.user_model import User
from typing import List

class UserRepository:
    def __init__(self, user_model: User) -> None:
        self.user_model = user_model


    def save(self) -> None:
        pass 

    def get(self) -> List[User] | User:
        pass 

    def update() -> None:
        pass 

    def delete(self, id: int) -> None:
        pass

    
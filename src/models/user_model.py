from sqlalchemy import String
import uuid
from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(String(50), nullable=False)
    last_name = db.Column(String(50))
    email = db.Column(String(100), nullable=False, unique=True)
    password = db.Column(String(256), nullable=False)
    tasks = db.relationship("Task", back_populates="user")

    @property
    def full_name(self) -> str:
        if self.first_name != "":
            full_name = f"{self.first_name} {self.last_name}"
            return full_name.strip()
        return "O usuario ainda nao possui nome cadastrado"

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.email}"

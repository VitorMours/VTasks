from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
import uuid
from . import db

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    tasks: Mapped[List["Task"]] = relationship(back_populates="user") # type:ignore
    notes: Mapped[List["Note"]] = relationship(back_populates="owner") # type:ignore
    
    @property
    def full_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}".strip()
        if self.first_name:
            return self.first_name
        return "O usuário ainda não possui nome cadastrado"

    def __repr__(self) -> str:
        return f"<User(id='{self.id}', email='{self.email}')>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.email}"
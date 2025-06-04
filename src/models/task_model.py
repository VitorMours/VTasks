from sqlalchemy import String, Boolean, Integer 
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class Task(db.Model):
    id: Mapped[str] = mapped_column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    task: Mapped[str] = mapped_column(String(50), nullable=False)
    task_description: Mapped[str] = mapped_column(String(300))
    task_conclusion: Mapped[bool] = mapped_column(nullable=False, default=False)
    
    # TODO: Precisa adicionar um task owner, vou ver no livro como faco para trabalhar com relacionamentos dentrodo banco de dados
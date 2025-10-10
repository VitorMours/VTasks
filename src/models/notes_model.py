from sqlalchemy import String, Boolean, DateTime, func
from .user_model import User 
from . import db
import uuid 
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class Note(db.Model):
    __tablename__ = "note"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))

    title: Mapped[str] = mapped_column(String(50), nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str | None] = mapped_column()
    # author Preciso adicionar o autor da nota de forma que seja a chave estrangeira de informacao do usuario 
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.now())




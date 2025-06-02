from flask_sqlalchemy import SQLAlchemy
import uuid
from . import db
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import mapped_column, Mapped

class User(db.Model):

    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]  = mapped_column(String(256), nullable=False)



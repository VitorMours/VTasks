from sqlalchemy import String
import uuid
from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(String(50), nullable=False)
    last_name = db.Column(String(50))
    email = db.Column(String(100), nullable=False)
    password = db.Column(String(256), nullable=False)
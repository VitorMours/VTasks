from sqlalchemy import String, Boolean
import uuid
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from . import db 

class Task(db.Model):
    __tablename__= "task"

    id = db.Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    task = db.Column(String(50), nullable=False)
    task_description = db.Column(String(300))
    task_conclusion = db.Column(db.Boolean, nullable=False, default=False)


    # TODO: preciso adicionar o relacionamento de chave estrangeira par aque o usuario possa ser dono dessa task

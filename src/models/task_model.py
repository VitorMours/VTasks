from sqlalchemy import String, Boolean
import uuid
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from . import db 

class Task(db.Model):
    __tablename__= "tasks"

    id = db.Column(String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    task = db.Column(String(50), nullable=False)
    task_description = db.Column(String(300))
    task_conclusion = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="tasks")


    # @staticmethod
    # def toggle_conclusion() -> None:
        # self.task_conclusion = not(task_conclusion)

    # TODO: preciso adicionar o relacionamento de chave estrangeira par aque o usuario possa ser dono dessa task

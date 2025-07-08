from sqlalchemy import String, Boolean
import uuid
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from . import db 

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.String(36), primary_key=True, nullable=False, default=lambda: str(uuid.uuid4()))
    task = db.Column(db.String(50), nullable=False)
    task_description = db.Column(db.String(300))
    task_conclusion = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id", name="fk_tasks_user_id"))
    user = db.relationship("User", back_populates="tasks")

    def toggle_conclusion(self) -> None:
        self.task_conclusion = not self.task_conclusion

    def __str__(self) -> str:
        return f"<{self.user_id} -> {self.task} {self.task_conclusion}>"

    # TODO: preciso adicionar o relacionamento de chave estrangeira para que o usuario possa ser dono dessa task

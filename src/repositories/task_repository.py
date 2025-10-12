from ..models import db
from typing import List 
from src.models.task_model import Task
from src.models.user_model import User

class TaskRepository:
    
    @staticmethod 
    def create(task_data: dict, user_id: User) -> None:
        """
        Create a new task in the database based on the user as the foreign key.
        """
        needed_fields = ["task","task_description","task_conclusion"]
        
        for field in needed_fields:
            if field not in task_data.keys():
                return False

        new_task = Task(
                task = task_data["task"],
                task_description = task_data["task_description"],
                task_conclusion = task_data["task_conclusion"],
                user_id = user_id
                )
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    @staticmethod   
    def update() -> None:
        """
        Deve atualziar uma task com base nos dados do usuario e no novo conteudo
        que e passado, deve retornar a task modificada dentro do banco de dados 
        se a modificacao for bem sucedida
        """
        pass

    @staticmethod
    def delete() -> None:
        """
        Deve deletar uma task com base no seu id, retornando true se for deletado
        """
        pass
    
    @staticmethod
    def get_all() -> None:
        """
        Pega todas as tasks presentes dentro do banco de dados
        """
        if Task.query.count() == 0:
            return []
        return Task.query.all()  
    
    @staticmethod
    def get_by_email(email: str) -> None:
        """
        Retorna todas as tasks baseadas no email do usuario dono
        dessa determinada task
        """
        if Task.query.count() == 0:
            return []
        return Task.query.join(User).filter(User.email == email).all()        

    def __repr__(self) -> str:
        return "<TaskRepository>"

    def __str__(self) -> str:
        return "<TaskRepository>"

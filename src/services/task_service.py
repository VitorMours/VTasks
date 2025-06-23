from abc import ABC, abstractmethod

class TaskService(ABC):

    @abstractmethod
    def get_all() -> None:
        pass

    @abstractmethod
    def delete() -> None:
        pass

    @abstractmethod
    def update() -> None:
        pass

    @abstractmethod
    def toggle_status() -> None:
        pass

    @abstractmethod
    def check_owner() -> None:
        pass

    @abstractmethod
    def get_one_by_id() -> None:
        pass

    @abstractmethod
    def create() -> None:
        pass



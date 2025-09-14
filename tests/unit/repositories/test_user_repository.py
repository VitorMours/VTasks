import pytest 
import importlib
from src.repositories.user_repository import UserRepository
class TestUserRepository:

    def test_if_its_running(self) -> None:
        assert True == True
    
    def test_if_import_repository(self) -> None:
        import src.repositories.user_repository
        assert True == True
    
    def test_if_import_user_model(self) -> None:
        from src.models import user_model 
        assert True == True

    def test_if_can_instantiate_user_repository(self) -> None:
        repository = UserRepository() 
import pytest
import importlib
from src.models.user_model import User
from src.repositories.user_repository import UserRepository


class TestUserRepository:
    def test_if_is_running(self) -> None:
        assert True

    def test_if_user_repository_can_be_imported(self):
        module = importlib.import_module("src.repositories.user_repository")
        assert module is not None
        assert hasattr(module, "UserRepository")

    def test_instantiate_user_repository(self) -> None:
        user_repository = UserRepository()
        assert user_repository is not None

    def test_user_repository_primitive_type(self) -> None:
        user_repository = UserRepository()
        assert isinstance(user_repository, UserRepository)

    def test_user_repository_repr(self) -> None:
        user_repository = UserRepository()
        assert repr(user_repository) == "<UserRepository>"

    def test_if_repository_have_correct_methods(self, create_user_repository) -> None:
        repository = create_user_repository
        required_methods = [
            "save", "create","update", "delete",
            "get_by_id", "get_by_email",
            "get_all", "exists"
        ]

        for method_name in required_methods:
            assert hasattr(repository, method_name), f"Missing method: {method_name}"
            assert callable(getattr(repository, method_name)), f"{method_name} is not a callable method"


    def test_if_get_all_return_list_when_more_than_one(self, app, create_user_repository) -> None:
        with app.app_context():
            query = create_user_repository.get_all()
            assert len(query) >= 1

    def test_if_get_all_return_only_users(self, app, create_user_repository) -> None:
        with app.app_context():
            query = create_user_repository.get_all()
            for user in query:
                assert isinstance(user, User)

    # def test_if_can_save_user_in_the_database(self, app, create_default_user, create_user_repository) -> None:
    #     with app.app_context():
    #         query = create_user_repository.save(
    #             User(
    #                 first_name="Maria",
    #                 last_name="Smith",
    #                 email="malu.reis@gmail.com",
    #                 password="new_password1!"
    #             ))
    #         assert query is not None


    def test_if_can_create_user_with_repository(self, app, create_user_repository) -> None:
        with app.app_context():
            user_instance = User(
                    first_name="Maria",
                    last_name="Smith",
                    email="malu.rei123123s123asd@gm123ail.com",
                    password="new_password1!"
            )
            user = create_user_repository.create(user_instance)
            assert user == True






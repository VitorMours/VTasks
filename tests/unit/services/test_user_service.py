import pytest
import importlib
from src.services.user_service import UserService

class TestUserService:
    def test_if_is_running(self) -> None:
        assert True
    def test_if_user_service_can_be_imported(self):
        module = importlib.import_module("src.services.user_service")
        assert module is not None
        assert hasattr(module, "UserService")

    def test_instantiate_user_service(self) -> None:
        user_service = UserService()
        assert user_service is not None

    def test_user_service_primitive_type(self) -> None:
        user_service = UserService()
        assert isinstance(user_service, UserService)

    def test_user_service_str(self) -> None:
        user_service = UserService()
        assert str(user_service) == "<UserService>"

    def test_user_service_exists_raise_error(self) -> None:
        service = UserService()
        with pytest.raises(TypeError):
            service.exists(123)

    def test_user_service_exists_function_with_email_string(self) -> None:
        user_service = UserService()
        assert user_service.exists("email@email.com")

    def test_user_service_exists_function_with_not_email_string(self) -> None:
        user_service = UserService()
        with pytest.raises(TypeError):
            assert user_service.exists("emailemail.com")



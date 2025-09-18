import pytest
import importlib
from src.services.auth_service import AuthService
from src.utils.erros import IncorrectCredentialsToLoginError

class TestAuthService:
    def test_is_running(self) -> None:
        assert True

    def test_service_have_check_session_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "_check_session")
        assert callable(module.AuthService._check_session)

    def test_service_check_session_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService._check_session()

    def test_service_have_create_session_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "create_session")
        assert callable(module.AuthService.create_session)

    def test_service_create_session_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.create_session()

    def test_service_delete_session_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "destroy_session")

    def test_service_destroy_session_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.destroy_session()

    def test_service_login_user_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "login_user")

    def test_service_login_user_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.login_user(user_data={"email":"data"})

    def test_service_logout_user_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "logout_user")

    def test_service_logout_user_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.logout_user()

    def test_service_authenticate_user_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "authenticate_user")

    def test_service_authenticate_user_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.authenticate_user(user_data={"email":"data"})

    def test_service_check_password_user_method(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert hasattr(module.AuthService, "check_password")

    def test_service_check_password_user_method_implementation(self) -> None:
        module = importlib.import_module("src.services.auth_service")
        assert module.AuthService.check_password(password="123123123aA!", confirmation="123123123aA!")

    def test_service_check_password_raise_error_correctly(self) -> None:
        with pytest.raises(IncorrectCredentialsToLoginError):
            module = importlib.import_module("src.services.auth_service")
            assert module.AuthService.check_password(password="123123123aA!", confirmation="1231223123aA!")
    


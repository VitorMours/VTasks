import importlib

class TestUtils:

    def test_email_validator(self) -> None:
        module = importlib.import_module("src.utils.security")
        assert hasattr(module, "email_validator")
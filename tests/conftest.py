import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.user_model import User
from wsgi import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def create_default_user():
    return User(
        first_name="Lucas",
        last_name="Moura",
        email="lucas.moura@email.com",
        password="32322916aA!",
    )
    

@pytest.fixture
def create_second_user():
    return User(
        first_name="John",
        last_name="Doe",
        email="john.doe@email.com",
        password="32322916aA!",
    )
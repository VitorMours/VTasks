import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.repositories.user_repository import UserRepository
from src.models.user_model import User
from wsgi import create_app

@pytest.fixture()
def app():
    """
    Creating a app with a database functionality working. to test the models necessities
    """
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()
        # db.session.add()
        # db.session.commit()

        yield app
        db.drop_all()

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


@pytest.fixture
def create_user_repository():
    return UserRepository()
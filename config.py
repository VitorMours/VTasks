import os
from pathlib import Path
from dotenv import load_dotenv

dotenv = Path(".env")
load_dotenv(dotenv_path=dotenv)

class Config:
    """Configurações base da aplicação."""
    SECRET_KEY = os.getenv("SECRET_KEY") or "uma_chave_padrao_fortissima"
    SESSION_PERMANENT = os.getenv("SESSION_PERMANENT") == "True"
    SESSION_COOKIE_SAMESITE = os.getenv("SESSION_COOKIE_SAMESITE") or "Strict"
    SESSION_COOKIE_HTTPONLY = os.getenv("SESSION_COOKIE_HTTPONLY") == "True"
    MONGO_URI = os.getenv("MONGO_URI") or "CHANGE-ME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_ADMIN_SWATCH = 'spacelab'
    FLASK_ADMIN = 'jvrezendemoura@gmail.com'

    @staticmethod
    def init_app(app):
        """Método de inicialização para extensões de aplicação."""
        pass


class DevelopmentConfig(Config):
    """Configurações para o ambiente de desenvolvimento."""
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or f"sqlite:///db.sqlite3"


class TestConfig(Config):
    """Configurações para o ambiente de teste."""
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    TESTING = True


class ProductionConfig(Config):
    """Configurações para o ambiente de produção."""
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

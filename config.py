import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
dotenv = Path(".env")
load_dotenv(dotenv_path=dotenv)


class Config:
    """Configurações base da aplicação."""
    # A chave secreta é essencial para a segurança de sessões e cookies.
    # A chave padrão é apenas para desenvolvimento, NUNCA use em produção!
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
    # A URL do banco de dados de desenvolvimento.
    # 'instance' é um bom lugar para guardar arquivos que não devem ir para o Git.
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or f"sqlite:///db.sqlite3"


class TestConfig(Config):
    """Configurações para o ambiente de teste."""
    # Usa um banco de dados de teste isolado para garantir que os testes não interfiram
    # nos dados de desenvolvimento.
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Desativa o logging do SQL em testes para não poluir o output
    SQLALCHEMY_ECHO = False
    TESTING = True


class ProductionConfig(Config):
    """Configurações para o ambiente de produção."""
    # Em produção, a URL do banco de dados DEVE ser definida via variável de ambiente.
    # Exemplo: SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

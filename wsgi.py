from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from pathlib import Path 
from src.models import db
from src.models.user_model import User
from src.models.task_model import Task
from src.views.admin import admin, admin_add_views
from src.views import bp
import os

dotenv_file = Path(".env")
load_dotenv(dotenv_path = dotenv_file)

def create_app() -> Flask:
    app = Flask(__name__, template_folder="src/templates/pages")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["EXPLAINS_TEMPLATE_LOADING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config['FLASK_ADMIN_SWATCH'] = 'spacelab'


    # Initializing Extensions
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Adding Views
    app.register_blueprint(bp)
    admin_add_views([User, Task])
    admin.init_app(app)
    # print(app.url_map)
    return app



if __name__ == "__main__":
    app = create_app()
    app.run()

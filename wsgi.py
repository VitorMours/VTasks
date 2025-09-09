from flask import Flask, render_template
from dotenv import load_dotenv
from pathlib import Path 
from src.models import db
from flask_migrate import Migrate
from src.models.user_model import User
from src.models.task_model import Task
from src.models.note_model import Note
from flask_admin import Admin
from src.views.admin import admin_add_views
from src.views import bp
from src.resources import api_bp
import os

dotenv_file = Path(".env")
load_dotenv(dotenv_path = dotenv_file)

def create_app() -> Flask:
    app = Flask(__name__, template_folder="src/templates/pages")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or "development_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI") or f"sqlite:///db.sqlite3"
    app.config["SESSION_PERMANENT"] = os.getenv("SESSION_PERMANENT") or True
    app.config["SESSION_COOKIE_SAMESITE"] = os.getenv("SESSION_COOKIE_SAMESITE") or "Strict"
    app.config["SESSION_COOKIE_HTTPONLY"] = os.getenv("SESSION_COOKIE_HTTPONLY") or True
    app.config['FLASK_ADMIN_SWATCH'] = 'spacelab'
    app.config['FLASK_ADMIN'] = 'jvrezendemoura@gmail.com'

    def render_http_error(error):
        code = getattr(error, 'code', 500)
        return render_template("error.html", error=error, code=code), code

    for err_code in [404, 405, 500]:
        app.register_error_handler(err_code, render_http_error)


    # Adding template extensions 
    app.jinja_env.add_extension('jinja2.ext.do')
    

    # Initializing Extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()


    admin = Admin()
    admin_add_views(admin, [User, Task, Note])
    admin.init_app(app)

    # Adding Views
    app.register_blueprint(bp)
    app.register_blueprint(api_bp)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run()

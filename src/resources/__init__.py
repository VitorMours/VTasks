from flask import Blueprint
from flask_restx import Api
from .user_resource import bp as user

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp, title='VTasks API', version='1.0', docs="/docs")


api.add_namespace(user)

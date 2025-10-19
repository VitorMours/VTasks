from flask_restx import Namespace, Resource
from ..services.user_service import UserService
from ..utils.api import user_serializer, single_user_serializer
from .api_models import user_model, user_model_creation
from src.models.user_model import User as Q
bp = Namespace("user", description="Api resource to access the users data")

user_entity = bp.model("User", user_model)
user_entity_creation = bp.model("UserCreation", user_model_creation)
@bp.route("/")
@bp.response(404, "User not found")
@bp.response(405, "HTTP Method not allowed")
class UserList(Resource):
    
    @bp.doc("Get all the users data")
    @bp.marshal_list_with(user_entity)
    def get(self):
        users = UserService.get_all_users()
        return user_serializer(users)

    @bp.doc("Create a new user with body data")
    @bp.expect(user_entity_creation)
    def post(self):
        return {"Creating":"user"}

@bp.route("/<uuid:user_id>")
@bp.param("user_id", "The user identifier")
@bp.response(404, "User not found")
@bp.response(200, "OK")
@bp.response(204, "No content in the request")
class User(Resource):
    
    @bp.doc("Get a specific user by the id")
    def get(self, user_id):
        """Get user by UUID"""
        # Converte para string para usar no UserService / DB
        user_id_str = str(user_id)

        user = UserService.get_user_by_uuid(user_id_str)
        if not user:
            return {"message": "User not found"}, 404

        user_serialized = single_user_serializer(user)
        return {"user": user_serialized}, 200

    def put(self, user_id) -> None: 
        return {"Returing": "MOdified user"}
    
    
    

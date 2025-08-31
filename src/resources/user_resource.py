from flask_restx import Namespace, Resource
from ..services.impl.user_service_impl import UserServiceImpl
from ..utils.api import user_serializer
bp = Namespace("user", description="Api resource to access the users data")

@bp.route("/")
@bp.response(404, "User not found")
@bp.response(405, "HTTP Method not allowed")
class UserList(Resource):
    @bp.doc("Get all the users data")
    def get(self):
        users = UserServiceImpl.get_all_users()
        return user_serializer(users)

    @bp.doc("Create a new user with body data")
    def post(self):
        return {"Creating":"user"}

@bp.route("/<int:id>")
@bp.param("id", "The user identifier")
@bp.response(404, "User not found")
@bp.response(200, "OK")
@bp.response(204, "No content in the request")
class User(Resource):
    
    @bp.doc("Get a specific user by the id")
    def get(self, id):
        return {"Returning specific user"}


    def put(self, id) -> None: 
        return {"Returing": "MOdified user"}
    
    
    

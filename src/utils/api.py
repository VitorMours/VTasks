from src.models.user_model import User


def user_serializer(users: list[User]):
    return [{"id":user.id,"first_name":user.first_name,"last_name":user.last_name,"email":user.email} for user in users]
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from src.models import db
admin = Admin()

def admin_add_views(views: list):
    for view in views:
        admin.add_view(ModelView(view, db.session))
from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for, g, request
from functools import wraps
from markupsafe import escape

salt = 16

def encrypt_password(password: str) -> str:
    global salt
    encrypt_password = generate_password_hash(password, "scrypt", salt)
    return encrypt_password

def check_password(password: str, hashed_password: str) -> str:
    password_validation = check_password_hash(hashed_password, password)
    return password_validation


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
                return redirect(url_for("views.auth.login"))
        return view(**kwargs)
    return wrapped_view


def sanitize_request(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        sanitized = {}

        if request.form:
            sanitized.update({k: escape(v) for k, v in request.form.items()})

        g.sanitized_request = sanitized
        return view(*args, **kwargs)
    return wrapped_view

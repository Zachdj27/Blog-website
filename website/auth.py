from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Login"

@auth.route("/sign-up")
def sign_up():
    return "Sign Up"

@auth.route("/log-out")
def log_out():
    return "Log Out"
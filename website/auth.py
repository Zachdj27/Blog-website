from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Log In"

@auth.route("/sign-up")
def sign_up():
    return "Sign Up"

@auth.route("/logout")
def log_out():
    return "Log Out"
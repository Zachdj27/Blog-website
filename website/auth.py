from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db 
from .models import User


auth = Blueprint("auth", __name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1= request.form.get("password1")
        password2 = request.form.get("password2")
        
        #filter database to check is email=email
        email_exists = User.query.fliter_by(email=email).first() 
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("Email is already in use", category='error')
        elif username_exists:
            flash("Username is already in use", category='error')
        elif password1 != password2:
            flash("Passwords dont't match", category='error')
        elif len(username) < 2:
            flash("Username must be at least 3 characters long", category='error')
        elif len(password1) < 6:
            flash("Password must be at least 6 characters long", category='error')
            
            
    
    return render_template("signup.html")

@auth.route("/logout")
def log_out():
    #return to home page
    return redirect(url_for("views.home"))
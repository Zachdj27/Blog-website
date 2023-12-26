from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db 
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            if check_password_hash(user_exists.password, password):
                flash("Logged in", category="success")
                #stores what user the person is signed in as in the session
                login_user(user_exists, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Password is incorrect.", category='error')
        else:
            flash("Email does not exist", category='error')
        
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1= request.form.get("password1")
        password2 = request.form.get("password2")
        
        #filter database to check is email=email
        email_exists = User.query.filter_by(email=email).first() 
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
        elif len(email) < 4:
            flash("Email is invalid", category='error')
        else:
            #if user account is valid then add user to database
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            #login user after creating account
            login_user(new_user,remember=True)
            flash("Account created!")
            return redirect(url_for('views.home'))
               
    return render_template("signup.html")


@auth.route("/logout")
@login_required #only possible to log out if you're signed out
def log_out():
    logout_user()
    #return to home page
    return redirect(url_for("views.home"))
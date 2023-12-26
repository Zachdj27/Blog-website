from . import db 
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model, UserMixin):
    #columns for databse
    id = db.Column(db.Integer, primary_key=True) #generates unique ids
    email = db.Column(db.String(150), unique=True) #verify for unique emails
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.Date(timezone=True), default=func.now())#date of account creation
from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    #columns for databse
    id = db.Column(db.Integer, primary_key=True) #generates unique ids
    email = db.Column(db.String(150), unique=True) #verify for unique emails
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())#date of account creation
    #reference all posts that a user has, backref: access posts with Post.user, passive_deletes: allows all posts of user to be deleted
    posts = db.relationship("Post", backref="user", passive_deletes=True)
    comments = db.relationship("Comment", backref="user", passive_deletes=True)
    
    
    
 #model for posts
 
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text =  db.Column(db.Text, nullable=False)#must have some text
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())#date of account creation
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False) #accessing User.id
        #CASCADE: delete all posts user has when his account is deleted
    comments = db.relationship("Comment", backref="post", passive_deletes=True)
        
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text =  db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
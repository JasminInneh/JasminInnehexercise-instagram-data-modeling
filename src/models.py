import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__= "user"
    id=Column(Integer, primary_key = True)
    name = Column(String(60), nullable= False)
    post_id =  Column(Integer, ForeignKey("post.id"))

class Post(Base):
    __tablename__= "post"
    id=Column(Integer, primary_key = True)
    content = Column(String(60), nullable= False)
    user_id =  Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__= "comment"
    id=Column(Integer, primary_key = True)
    comment = Column(String(60), nullable= False)
    post_id =  Column(Integer, ForeignKey("post.id"))
    commenter = relationship("Follower", backref="comment")

class Reaction(Base):
    __tablename__= "reaction"
    id=Column(Integer, primary_key = True)
    type = Column(String(60), nullable= False)
    post_id =  Column(Integer, ForeignKey("post.id"))
    reactor = relationship("Follower", backref="reaction")

class Followers(Base):
    __tablename__= "followers"
    id=Column(Integer, primary_key = True)
    comment_id = Column(String(60), ForeignKey("comment.id"))
    following =  Column(Integer, ForeignKey("user.id"))
    reaction_id = Column(String(60), ForeignKey("reaction.id"))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

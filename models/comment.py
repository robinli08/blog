import sqlalchemy as sc

from datetime import datetime
from sqlalchemy.orm import relationship, backref
from common.db import Base
from models.post import Post

class Comment(Base):
  __tablename__ = 'comments'

  id = sc.Column(sc.Integer, primary_key=True)
  create_time = sc.Column(sc.Date)
  content = sc.Column(sc.String)
  user_email = sc.Column(sc.String)
  username = sc.Column(sc.String)
  post_id = sc.Column(sc.Integer, sc.ForeignKey('posts.id'))

  post = relationship('Post', backref=backref('comments', order_by=create_time))

  def __init__(self, **data):
    self.create_time = datetime.now()
    attrs = ('content', 'username', 'user_email', 'post_id')
    for attr in attrs:
      setattr(self, attr, data[attr])

  def get_dict(self):
    attrs = ('create_time', 'content', 'username', 'user_email', 'post_id')
    return {attr: getattr(self, attr) for attr in attrs}

  def __repr__(self):
    return str(self.get_dict())

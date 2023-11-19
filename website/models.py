from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(200), unique=True)
  password = db.Column(db.String(200))
  first_name = db.Column(db.String(200))

  #Define all the columns / layout
  # #Set primary key (to diferenciate users / data)
  #Link cart to customer database
  #cart = db.relationship('referenced table class - look at many to one relationships')


class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  product_name = db.Column(db.String(100))
  price = db.Column(db.Float)
  image_path = db.Column(db.String(100))
  carbon_footprint = db.Column(db.Integer)


from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

class ClientData(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(150))
    new_customer = db.Column(db.Boolean)
    gallons_requested = db.Column(db.Integer)
    profit_margin = db.Column(db.Integer)
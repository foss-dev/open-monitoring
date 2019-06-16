from flask_sqlalchemy import SQLAlchemy
from om_core import app

# We didn't pass app instance here.
db = SQLAlchemy()

class User(db.Model):
    """ Model for user management """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, email, password, name, surname, active, created_at, updated_at):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at
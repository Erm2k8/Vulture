from app.app import db
from datetime import datetime
import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(90), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def create(self):
        db.session.add(self)


    def read(self):
        user_info = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }
        return json.dumps(user_info)


    def delete(self):
        db.session.delete(self)


    def __repr__(self):
        return f"User {self.email}"
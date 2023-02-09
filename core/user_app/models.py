from core import db

db.metadata.clear()


class UserDetails(db.Model):
    __tablename__ = 'user_details'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    username = db.Column(db.String())
    password = db.Column(db.String())
    age = db.Column(db.Integer, nullable=True)

    def __int__(self, first_name, last_name, email, username, password, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.age = age

    def __repr__(self):
        return f"user {self.username}"

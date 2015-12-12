from flask_crud import db,bcrypt


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(60))
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __init__(self,fullname,username,email,password):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' %self.username

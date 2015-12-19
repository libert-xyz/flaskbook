from crud import db,bcrypt


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(60))
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(110), unique=True)
    password = db.Column(db.String(80))

    def __init__(self,fullname,username,email,password):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


    def __repr__(self):
        return '<User %r>' %self.username

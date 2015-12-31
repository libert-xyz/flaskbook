import unittest
from flask.ext.testing import TestCase
from crud import app,db
from crud.models import *
from datetime import datetime, timedelta


class FlaskTestCase(unittest.TestCase):

    #def setUp(self):
    #    self.db_fd, app.config['DATABASE'] = 'sqlite:///:memory:'
    #    app.config['TESTING'] = True
    #    self.app = app.test_client()
    #    flaskr.init_db()

    def setUp(self):

        self.app = app
        self.client = self.app.test_client()
        DEBUG = True
        TESTING =  True
        WTF_CSRF_ENABLED = False
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_createUser(self):
        #u = User(fullname='john', username='john',email='admin@test.com',password='pass')
        #db.session.add(u)
        db.session.add(User("admin root", "admin","ad@min.com", "pass"))
        db.session.commit()
        query = User.query.filter_by(username="admin").first()
        assert query.username == 'admin'

    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data

    def test_follow(self):
        u1 = User('jon san','jon','jon@jon.com','jon')
        u2 = User('jan son','jan','jan@jan.com','jan')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1.unfollow(u2) is None
        u = u1.follow(u2)
        db.session.add(u)
        db.session.commit()
        assert u1.follow(u2) is None
        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().username == 'jan'
        assert u2.followers.count() == 1
        assert u2.followers.first().username == 'jon'
        u = u1.unfollow(u2)
        assert u is not None
        db.session.add(u)
        db.session.commit()
        assert not u1.is_following(u2)
        assert u1.followed.count() == 0
        assert u2.followers.count() == 0


    def test_follow_posts(self):
        # make four users
        u1 = User('jonh c','john','john@example.com','john')
        u2 = User('susan c','susan','susan@example.com','susan')
        u3 = User('mary c','mary','mary@example.com','mary')
        u4 = User('david c','david','david@example.com','david')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        # make four posts
        utcnow = datetime.utcnow()
        p1 = Post(body="post from john", user_id=u1.id, timestamp=utcnow + timedelta(seconds=1))
        p2 = Post(body="post from susan", user_id=u2.id, timestamp=utcnow + timedelta(seconds=2))
        p3 = Post(body="post from mary", user_id=u3.id, timestamp=utcnow + timedelta(seconds=3))
        p4 = Post(body="post from david", user_id=u4.id, timestamp=utcnow + timedelta(seconds=4))
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()
        # setup the followers
        u1.follow(u1)  # john follows himself
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u2)  # susan follows herself
        u2.follow(u3)  # susan follows mary
        u3.follow(u3)  # mary follows herself
        u3.follow(u4)  # mary follows david
        u4.follow(u4)  # david follows himself
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.add(u4)
        db.session.commit()
        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        assert len(f1) == 3
        assert len(f2) == 2
        assert len(f3) == 2
        assert len(f4) == 1
        assert f1 == [p4, p2, p1]
        assert f2 == [p3, p2]
        assert f3 == [p4, p3]
        assert f4 == [p4]

if __name__ == '__main__':
    unittest.main()

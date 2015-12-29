import unittest
from flask.ext.testing import TestCase
from crud import app,db
from crud.models import User

class BaseTestCase(TestCase):

    def setUp(self):
        DEBUG = True
        TESTING =  True
        WTF_CSRF_ENABLED = False
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def add_user(self):
        db.session.add(User("admin root","adin", "ad@min.com", "admin"))
        db.session.commit()

    def test_index(self):
        response = self.client.get('/login',content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_avatar(self):
        # create a user
        u = User(fullname="admin root",username="adin",email="ad@min.com",password="admin")
        avatar = u.avatar(128)
        expected = 'http://www.gravatar.com/avatar/' + \
            'd4c74594d841139328695756648b6bd6'
        assert avatar[0:len(expected)] == expected


if __name__ == 'main':
    unittest.main()

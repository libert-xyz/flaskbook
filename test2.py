import unittest
from flask.ext.testing import TestCase
from crud import app,db
from crud.models import User


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


if __name__ == '__main__':
    unittest.main()

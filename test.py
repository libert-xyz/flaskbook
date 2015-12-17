import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from flask.ext.testing import TestCase
from flask_crud import app,db
from crud.models import User

class BaseTestCase(TestCase):

    def create_app(self):

        self.db_uri = 'mysql://%s:%s@%s:3306/%s' %(DB_USERNAME,DB_PASSWORD,MARIA_D,BLOG_DATABASE_NAME)
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED']
        app.config['BLOG_DATABASE_NAME'] = 'db_test'
        app.config['SQL_ALCHEMY_DATABASE_URI'] = self.db_uri + app.config['BLOG_DATABASE_NAME']
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('CREATE DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        db.create_all()
        conn.close()
        self.app = app.test_client()


    def tearDown(self):

        db.session.remove()
        engine = sqlalchemy.create_engine(self.db_uri)
        conn = engine.connect()
        conn.execute('commit')
        conn.execute('DROP DATABASE ' + app.config['BLOG_DATABASE_NAME'])
        conn.close()



    def setUp(self):
        db.create_all()
        db.session.add(User('super admin','admin','admin@internet.god','admin'))
        db.session.commit()

    def remoVE(self):
        db.session.remove()
        db.drop_all()

if __name__ == 'main':
    unittest.main()

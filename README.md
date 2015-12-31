FlaskBook Microbloging in Flask MicroFramework.

Functionality v5.0 Beta
-----------------------


- Log In && Log Out

- User registration

- Avatar Images uses Gravatar API

- Posts in the User Profile

- Followers and Following


Installation:
--------------

pip install -r requirements.txt

Edit config.py Databse

SECRET_KEY = 'secret!'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = 'pass'
BLOG_DATABASE_NAME = 'crud'
MARIA_D = '172.17.0.1'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:3306/%s' %(DB_USERNAME,DB_PASSWORD,MARIA_D,BLOG_DATABASE_NAME)

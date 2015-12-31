#Create the Database

#import os, sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import app
import sqlalchemy

try:

    db_uri = 'mysql://%s:%s@%s:3306/' % (app.config['DB_USERNAME'],app.config['DB_PASSWORD'],app.config['MARIA_D'])
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE " + app.config['BLOG_DATABASE_NAME'])
    conn.close()

except:
    print "Database exists"


from flaskbook import db

from book.models import *

db.create_all()

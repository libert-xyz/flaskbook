#import os, sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from book import app,db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate,MigrateCommand

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

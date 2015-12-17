import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_crud import db
from crud.models import User
try:

    db.session.add(User('evo cumple','evo','glinera@generacionevo.com','evo'))
    db.session.commit()

except:

    print "user exists!"

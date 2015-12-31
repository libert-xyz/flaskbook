SECRET_KEY = 'secret!'
DEBUG = True
#DB_USERNAME = 'root'

DB_USERNAME = 'pkyeiuuliulvll'

#DB_PASSWORD = 'pass'
DB_PASSWORD = '3V9brJhnXLABJPmP1nLEVp0kXL'

#BLOG_DATABASE_NAME = 'crud'
BLOG_DATABASE_NAME = 'ddeipmdin4d01s'

MARIA_D = '172.17.0.1'
#SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:3306/%s' %(DB_USERNAME,DB_PASSWORD,MARIA_D,BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = 'postgres://pkyeiuuliulvll:3V9brJhnXLABJPmP1nLEVp0kXL@ec2-54-204-8-138.compute-1.amazonaws.com:5432/ddeipmdin4d01s'
#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#SQLALCHEMY_DATABASE_URI ='sqlite:////tmp/test.db'

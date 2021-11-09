import os

BASE_DIR = os.path.dirname(__file__)

# main db connection - mariadb start ===============
db = {
    'user' : os.getenv('MYSQL_USER'),
    'password' : os.getenv('MYSQL_PASSWORD'),
    'host' : os.getenv('MYSQL_HOST'),
    'port' : os.getenv('MYSQL_PORT'),
    'database' : os.getenv('MYSQL_DATABASE')
}

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@" \
         f"{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False

#  ================ connection end

class Testing:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'testing.sqlite')
    JWT_SECRET_KEY = "super-secret"

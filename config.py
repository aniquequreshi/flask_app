import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')\
        or 'mysecretkey123456789'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Environment Variable in Windows Environment use SET, otherwise EXPORT
#set FLASK_APP=app
#set FLASK_ENV=development
# set SECRET_KEY="your secret key"
#set DATABASE_URI="postgresql://username:password@host:port/database_name"
import os


basedir = os.path.abspath(os.path.dirname(__file__))
start_app = True
database_name = 'basement'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'L3tmein!'

SQLALCHEMY_DATABASE_URI = 'postgresql://' + 'postgres' + ':@localhost/' + database_name
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


import pymysql
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'job_2'
PASSWORD = 'CHANGE_ME_BEFORE_RUNNING'
DATABASE = 'job_python'
HOST = '127.0.0.1'
PORT = 3306

DB_URI = f'mysql+pymysql://demo:CHANGE_ME_BEFORE_RUNNING@127.0.0.1/{DATABASE}'

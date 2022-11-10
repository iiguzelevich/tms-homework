import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEBUG = os.getenv('DEBUG')

DIALECT_DB = os.getenv('DIALECT_DB')
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
NAME_DB = os.getenv('NAME_DB')

basedir = os.path.abspath((os.path.dirname(__file__)))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'{DIALECT_DB}+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/'
    f'{NAME_DB}?charset=utf8'
)

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

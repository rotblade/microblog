import os
from pathlib import Path
basedir = Path(__file__).absolute().parent

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + str(basedir/'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

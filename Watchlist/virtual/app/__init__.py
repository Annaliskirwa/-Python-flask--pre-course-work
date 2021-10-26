from flask import Flask
from .config import Config, DevConfig
#INitliazing our application
app = Flask(__name__)
#Setting up the configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
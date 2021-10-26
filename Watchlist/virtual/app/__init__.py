from flask import Flask
from .config import Config, DevConfig
#INitliazing our application
app = Flask(__name__)
#Setting up the configuration
app.config.from_object(DevConfig)

from app import views
from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello world </h1>'

@app.route('/name')
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello')
def hello():
    return 'Hello, World'
from flask import Flask, g
import models
from flask_cors import CORS

from resources.posts import post
from resources.users import user

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'What is up George'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
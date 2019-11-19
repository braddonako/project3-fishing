import models
from flask import Flask, g
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


CORS(post, origins=['http://localhost:3000'], support_credentials=True)
app.register_blueprint(post, url_prefix='/api/v1/posts')

CORS(user, origins=['http://localhost:3000'], support_credentials=True)
app.register_blueprint(user, url_prefix='/api/v1/users')

@app.route('/')
def index():
    return 'What is up George'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)

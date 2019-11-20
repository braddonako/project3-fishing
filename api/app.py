import models
from flask import Flask, g, request, jsonify
from flask_cors import CORS
from flask_login import LoginManager
from resources.posts import post
from resources.users import user
from playhouse.shortcuts import model_to_dict

DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'fjkdsaljfaldksjdsthisisoursecretkeyhahahjkfdhsa'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.get(models.User.id == user_id)
    except models.DoesNotExist:
        return None

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

import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


post = Blueprint('posts', 'post')


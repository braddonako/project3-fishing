import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


post = Blueprint('posts', 'post')

## show all posts
@post.route('/', methods=["GET"])
def get_all_posts():
    try:
        posts = [model_to_dict(post) for post in models.Post.select()]
        print(posts)
        return jsonify(data=posts, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

## create route
@post.route('/', methods=["POST"])
def create_posts():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    post = models.Post.create(**payload)
    ## see the object
    print(post.__dict__)
    ## Look at all the methods
    print(dir(post))
    # Change the model to a dict
    print(model_to_dict(post), 'model to dict')
    post_dict = model_to_dict(post)
    return jsonify(data=post_dict, status={"code": 201, "message": "Success"})

## show route
@post.route('/<id>', methods=["GET"])
def get_one_post(id):
    print(id, 'yeeet')
    post = models.Post.get_by_id(id)
    print(post.__dict__)
    return jsonify(data=model_to_dict(post), status={"code": 200, "message": "Success"})

## update route
@post.route('/<id>', methods=["PUT"])
def update_post(id):
    payload = request.get_json()
    query = models.Post.update(**payload).where(models.Post.id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Post.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

@post.route('/<id>', methods=["Delete"])
def delete_post(id):
    query = models.Post.delete().where(models.Post.id==id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})
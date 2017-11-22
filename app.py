#!/usr/bin/evn python
# coding=utf-8


from flask import Flask, request
from flask_restful import Resource, Api
# from pymongo import MongoClient
from celery_app import task
from celery_app.task import posts

app = Flask(__name__)
api = Api(app)
# client = MongoClient()
# db = client['jinshuju']
# posts = db.data


class Jinshuju(Resource):
    def post(self):
        info = request.get_json()['entry']
        id = str(posts.insert(info))
        task.push.delay(
            id, '3ad6ce86f476952c6c3f5ff010bfc471a2bcdbd6349db4fe20c2b9984249b9d2')
        return 200


api.add_resource(Jinshuju, '/jinshuju')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

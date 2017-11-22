#!/usr/bin/evn python
# coding=utf-8


from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from celery_app import task


app = Flask(__name__)
api = Api(app)
client = MongoClient()
db = client['jinshuju']
posts = db.data


class Jinshuju(Resource):
    def post(self):
        info = request.get_json()['entry']
        id = str(posts.insert(info))
        task.push.delay(id)
        return 200


api.add_resource(Jinshuju, '/jinshuju')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

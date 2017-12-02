#!/usr/bin/evn python
# coding=utf-8


from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
# from pymongo import MongoClient
from celery_app import task
from celery_app.task import posts

app = Flask(__name__)
api = Api(app)
# client = MongoClient()
# db = client['jinshuju']
# posts = db.data


class Jinshuju(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'entry', type=str, required=True, help="Date Error!", location='json')
        # print(self.reqparse.parse_args())

    def post(self, token):
        info = request.get_json()['entry']
        id = str(posts.insert(info))
        task.push.delay(id, token)
        return Response(status=200)


api.add_resource(Jinshuju, '/jinshuju/<string:token>')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

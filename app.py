#!/usr/bin/evn python
# coding=utf-8


from flask import Flask, request
from flask.ext import restful
from pymongo import MongoClient
from celery_app import task


app = Flask(__name__)
api = restful.Api(app)
client = MongoClient()
db = client['jinshuju']
posts = db.data


class Hello(restful.Resource):
	def get(self):
		return {'hello': 'world'}


class Jinshuju(restful.Resource):
	def post(self):
		info = request.get_json()['entry']
		id = str(posts.insert(info))
		task.push.delay(id)
		return 200


api.add_resource(Jinshuju, '/jinshuju')
# api.add_resource(Hello, '/')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

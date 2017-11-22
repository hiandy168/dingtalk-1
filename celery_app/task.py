#!/usr/bin/evn python
# coding=utf-8


from celery_app.celery_ding import app
from pymongo import MongoClient
from celery_app.DingTalkBot import Message
from bson.objectid import ObjectId
# from dingtalk.app import posts

client = MongoClient()
db = client['jinshuju']
posts = db.data


@app.task
def push(objectId):
    post = posts.find_one({"_id": ObjectId(objectId)})
    title = "有新的报名信息！"
    text = "## 信息推送\n\n" + "#### 姓名：{0}\n\n#### 学校：{1}\n\n#### 联系人姓名：{2}\n\n#### 联系人方式：{3}\n\n#### 报名分校：{4}\n\n#### 学生年级：{5}\n\n#### 预报科目：{6}\n\n#### 报名时间：{7}".format(
        post['field_1'], post['field_2'], post['field_8'], post['field_6'], post['field_4'], post['field_7'], "，".join(post['field_9']), post['created_at'].split(" ")[1])
    msg = Message(
        'https://oapi.dingtalk.com/robot/send?access_token=3ad6ce86f476952c6c3f5ff010bfc471a2bcdbd6349db4fe20c2b9984249b9d2')
    msg.send_markdown(title, text)

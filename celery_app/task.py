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
info = db.info


@app.task
def push(objectId, token):

    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' + token
    post = posts.find_one({"_id": ObjectId(objectId)})
    title = "有新的报名信息！"
    try:
        phones = info.find_one({"school": post['field_6']})['phone']
    except Exception as e:
        at_mobiles = ""
        phones = []
    else:
        at_mobiles = ' '.join(['@' + x for x in phones])
    finally:
        pass
    text = "> ## 信息推送\n\n### {0}\n\n".format(at_mobiles) + "#### 姓名：{0}\n\n#### 学校：{1}\n\n#### 联系人姓名：{2}\n\n#### 联系人方式：{3}\n\n#### 报名分校：{4}\n\n#### 学生年级：{5}\n\n#### 预报科目：{6}\n\n#### 报名时间：{7}".format(
        post['field_1'], post['field_2'], post['field_4'], post['field_8'], post['field_6'], post['field_7'], "，".join(post['field_9']), post['created_at'].split(" ")[1])
    msg = Message(webhook)
    return msg.send_markdown(title, text, phones)

#!/usr/bin/evn python
# coding=utf-8


import sys
from celery import Celery


sys.path.append('../')

app = Celery("task")
app.config_from_object('celery_app.celeryconfig')
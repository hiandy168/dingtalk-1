#!/usr/bin/evn python
# coding=utf-8


import sys
from celery import Celery


sys.path.append('../')

app = Celery("celery_app", include=['celery_app.task'])
app.config_from_object('celery_app.celeryconfig')


if __name__ == '__main__':
    app.start()

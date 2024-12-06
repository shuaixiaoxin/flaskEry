# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/07/09
# @Author  : xiao xin
# @File    : cron.py
"""
from celery import Celery
from celery.schedules import crontab

celery_beat = Celery('beat')
celery_beat.config_from_object('app.conf.celery_beat_app')

celery_beat.conf.beat_schedule = {
    'task': {
        'task': 'app.celery_task.tasks.beatTask',
        'schedule': crontab(minute='*/1'),
        'args': (5, 7),
    },
}




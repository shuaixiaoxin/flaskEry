# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/12/03
# @Author  : xiao xin
# @File    : tasks.py
"""

from app.celery_task.init_celery import celery, CustomTask
from app.celery_task.cron import celery_beat
import time
import random


@celery.task(base=CustomTask)
def celeryTask(*args, **kwargs):
    time.sleep(random.choice(range(1, 30)))
    print(kwargs)
    return "OK!"


@celery_beat.task(base=CustomTask)
def beatTask(x, y):
    print(f"x+y={x+y}")
    return x+y


if __name__ == '__main__':
    pass

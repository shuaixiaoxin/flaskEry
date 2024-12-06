# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/18
# @Author  : xiao xin
# @File    : init_celery.py
"""

from celery import Celery, Task

celery = Celery('tasks')
celery.config_from_object('app.conf.celery_config', namespace='NEW_CELERY')


class CustomTask(Task):
    """
    自定义回调
    """
    def on_success(self, retval, task_id, args, kwargs):
        return super(CustomTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        return super(CustomTask, self).on_failure(exc, task_id, args, kwargs, einfo)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        return super(CustomTask, self).after_return(status, retval, task_id, args, kwargs, einfo)

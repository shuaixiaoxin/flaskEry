# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/13
# @Author  : xiao xin
# @File    : urls.py
"""

from app.plugin.exts import api
from app.blueprints.user import UserResource, Refresh_token, UserInfo, user_blueprint
from app.blueprints.tasksery import celery_task, task_blueprint
from flask_restful import Api

user_api = Api(user_blueprint)
tasks_api = Api(task_blueprint)

user_api.add_resource(UserInfo, '/userinfo')
api.add_resource(UserResource, '/get_token')
api.add_resource(Refresh_token, '/refresh')
tasks_api.add_resource(celery_task, '/celery_task')


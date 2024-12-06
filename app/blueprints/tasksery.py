# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/12/03
# @Author  : xiao xin
# @File    : tasksery.py
"""
from flask import Blueprint
from flask_restful import Resource
from app.utils.response import CustomResponse
from app.celery_task.tasks import celeryTask


task_blueprint = Blueprint('task', __name__, url_prefix='/tasks')


class celery_task(Resource):
    def get(self):
        celeryTask.apply_async(kwargs={"code": 0, "data": None})
        return CustomResponse.make_response(code=200, message='异步任务提交成功.')

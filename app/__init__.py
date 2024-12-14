# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/04
# @Author  : xiao xin
# @File    : __init__.py
"""
import os
from flask import Flask, request
from app.blueprints.user import user_blueprint
from app.blueprints.tasksery import task_blueprint
from app.conf.settings import DevelopmentConfig, Config
from app.plugin.exts import init_ext
from app.urls import *
from app.utils.commands import register_user
from flask import jsonify
from flask_limiter.errors import RateLimitExceeded


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    # app.config.from_object(Config)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(task_blueprint)

    @app.before_request
    def handle_before_request():
        """在每次请求之前都被执行"""
        app.logger.warning('全局日志 - 请求方法：{} 请求路径：{} 请求地址：{}'.format(request.method, request.path, request.remote_addr))

    # @app.after_request
    # def handle_after_request(response):
    #     """在每次请求之后都被执行"""
    #     pass

    @app.errorhandler(RateLimitExceeded)
    def handle_ratelimit_error(e):
        return jsonify({
            "error": "Too many requests",
            "status_code": 429,
            "details": str(e.description)  # 包含限流的详细信息
        }), 429

    # 初始化插件
    init_ext(app)
    register_user(app)

    return app

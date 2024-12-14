# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/13
# @Author  : xiao xin
# @File    : exts.py
"""

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from app.utils.LogHandler import getLogHandler
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


api = Api()
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cache = Cache()
limiter = Limiter(key_func=get_remote_address, default_limits=['1/minute'])


def init_ext(app):
    api.init_app(app=app)
    jwt.init_app(app=app)
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app, config={'CACHE_TYPE': 'simple'})
    limiter.init_app(app=app)

    app.logger.addHandler(getLogHandler())

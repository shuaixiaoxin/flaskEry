# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/02
# @Author  : xiao xin
# @File    : settings.py
"""
from datetime import timedelta


class Config:
    DEBUG = False

    REDIS_HOST = '192.168.0.101'
    REDIS_PORT = 6379
    REDIS_PASSWORD = 'redis123456'

    MYSQL_HOST = '192.168.0.101'
    MYSQL_PORT = 2433
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DATABASE = 'flaskEry'

    JWT_SECRET_KEY = 'qzQsUxin30qjq85hZLSMt17XukOZH7fvVRG4'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"
    SQLALCHEMY_ECHO = False


class DevelopmentConfig:
    DEBUG = True

    REDIS_HOST = '192.168.0.101'
    REDIS_PORT = 6379
    REDIS_PASSWORD = 'redis123456'

    MYSQL_HOST = '192.168.0.101'
    MYSQL_PORT = 2433
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DATABASE = 'flask_celery'

    JWT_SECRET_KEY = 'qzQsUxin30qjq85hZLSMt17XukOZH7fvVRG4'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"
    SQLALCHEMY_ECHO = True




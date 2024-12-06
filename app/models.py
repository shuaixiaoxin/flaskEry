# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/14
# @Author  : xiao xin
# @File    : models.py
"""
from datetime import datetime

"""
flask db init
flask db migrate
flask db upgrade
flask db downgrade
"""
from app.plugin.exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'auth_user'

    id = db.Column(db.Integer, primary_key=True, doc='主键ID')
    username = db.Column(db.String(20), unique=True, doc='用户名称')
    password = db.Column(db.String(1000), doc='哈希密码')

    @classmethod
    def set_password(cls, password):
        return generate_password_hash(password)

    @classmethod
    def check_password(cls, hash_password, password):
        return check_password_hash(hash_password, password)

# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/04
# @Author  : xiao xin
# @File    : user.py
"""

import json
from marshmallow import Schema, fields, validates, ValidationError, validates_schema
from app.models import User


class UserSchema(Schema):

    class Meta:
        model = User
        ordered = True
        fields = ["id", "username", "password"]

    id = fields.Int()
    username = fields.String(required=True)
    password = fields.String(load_only=True, required=True)

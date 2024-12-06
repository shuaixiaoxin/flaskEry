# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/04
# @Author  : xiao xin
# @File    : response.py
"""

from flask import jsonify
from flask_restful import Resource


class CustomResponse(Resource):
    @staticmethod
    def make_response(code=0, data=None, message=None, *args, **kwargs):
        response_data = {"code": code, "data": data, "message": message}
        return jsonify(response_data, *args, **kwargs)

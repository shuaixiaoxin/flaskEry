# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/09
# @Author  : xiao xin
# @File    : user.py
"""
from flask import Blueprint, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from app.serializers.user import UserSchema
from app.models import User
from app.plugin.exts import db
from app.utils.response import CustomResponse


user_blueprint = Blueprint('user', __name__, url_prefix='/user')


class UserResource(Resource):
    def post(self):
        us = UserSchema()
        receive_data = request.form
        try:
            validated_data = us.load(receive_data)
            user = User.query.filter_by(username=validated_data["username"]).first()
            if user and user.check_password(user.password, validated_data["password"]):
                access_token = create_access_token(identity=validated_data["username"])
                refresh_token = create_refresh_token(identity=validated_data["username"])
                data = [{"access_token": access_token}, {"refresh_token": refresh_token}]
                return CustomResponse.make_response(code=200, data=data, message='校验成功,请保存好token.')
            else:
                raise Exception("用户或密码校验失败")
        except Exception as e:
            return CustomResponse.make_response(code=400, message=str(e))


class Refresh_token(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        data = [{"access_token": new_access_token}]
        return CustomResponse.make_response(code=200, data=data, message='刷新Token成功.')


class UserInfo(Resource):
    @jwt_required()
    def get(self):
        us = UserSchema(many=True)
        user = User.query.all()
        return CustomResponse.make_response(code=200, data=us.dump(user), message='获取用户成功.')

    @jwt_required()
    def post(self):
        receive_data = request.form
        us = UserSchema()
        try:
            validated_data = us.load(receive_data)
            validated_data['password'] = User.set_password(validated_data['password'])
            db.session.add(User(**validated_data))
            db.session.commit()
        except Exception as e:
            return CustomResponse.make_response(code=400, message=str(e))
        return CustomResponse.make_response(code=200, message='创建用户成功.')

    @jwt_required()
    def delete(self):
        receive_data = request.form
        if receive_data["username"]:
            delete_res = User.query.filter_by(username=receive_data["username"]).first()
            db.session.delete(delete_res)
            db.session.commit()
        return CustomResponse.make_response(code=200, message='删除用户成功.')



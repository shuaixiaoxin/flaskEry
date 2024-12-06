# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/10/10
# @Author  : xiao xin
# @File    : commands.py.py
"""

import click
from flask import Flask
from app.models import User
from app.plugin.exts import db


def register_user(app: Flask):
    @app.cli.command("create_user")
    @click.argument("username")
    @click.argument("password")
    def create_user(username, password):
        """create user."""
        new_user = User(username=username, password=User.set_password(password=password))
        db.session.add(new_user)
        db.session.commit()
        print("The user has been created successfully.")

# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/04
# @Author  : xiao xin
# @File    : app.py
"""

from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0')

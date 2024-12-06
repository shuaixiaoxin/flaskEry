# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/05
# @Author  : xiao xin
# @File    : LogHandler.py
"""
import os
import logging
import time
from logging.handlers import RotatingFileHandler


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)


def getLogHandler():
    log_dir_name = "logs"
    log_file_name = 'logger-Flaskery.log'

    log_file_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name

    logging.basicConfig(level=logging.WARNING)
    file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024, backupCount=10, encoding='UTF-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    file_log_handler.setFormatter(formatter)

    return file_log_handler

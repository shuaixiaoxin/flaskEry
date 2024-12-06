# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/07/09
# @Author  : xiao xin
# @File    : celery_beat_app.py
"""

from kombu import Exchange, Queue
from app.conf.settings import DevelopmentConfig

# 使用redis作为任务队列
broker_url = f'redis://:{DevelopmentConfig.REDIS_PASSWORD}@{DevelopmentConfig.REDIS_HOST}:{DevelopmentConfig.REDIS_PORT}/3'

# 使用redis存储任务执行结果
result_backend = f'redis://:{DevelopmentConfig.REDIS_PASSWORD}@{DevelopmentConfig.REDIS_HOST}:{DevelopmentConfig.REDIS_PORT}/4'

# 每个worker并发数量
worker_concurrency = 2

# 指定任务接受的序列化类型
accept_content = ['json']

# 设置时区
timezone = 'Asia/Shanghai'

# 时区设置
CELERY_ENABLE_UTC = False

# 单个任务的运行时间限制，否则会被杀死
task_time_limit = 3600

# 每个worker执行指定次任务即销毁
worker_max_tasks_per_child = 100


task_queues = (
    Queue("default", Exchange("default"), routing_key="default.#"),
)


# 设置默认的队列名称
task_default_queue = "default"



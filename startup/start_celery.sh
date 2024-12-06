#!/bin/bash

cd /data/flask_celery
mkdir -p /data/log/celery/
source /data/python_venv/flask_celery/bin/activate;/data/python_venv/flask_celery/bin/celery -A app.celery_task.init_celery worker -l info -Q default,public >> /data/log/celery/celery.log 2>&1

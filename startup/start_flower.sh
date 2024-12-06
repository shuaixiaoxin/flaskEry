#!/bin/bash

cd /data/flask_celery
mkdir -p /data/log/celery/

source /data/python_venv/flask_celery/bin/activate;/data/python_venv/flask_celery/bin/celery -A app.celery_task.init_celery flower --basic-auth=admin:kxKbMp17hWYBu8 --broker=redis://:1SXgvoxF3kQlE8If@127.0.0.1:26380/1 --address=0.0.0.0 --port=5001 --purge_offline_workers=3600 --inspect_timeout=10000 --persistent=True >> /data/log/celery/celery_flower.log 2>&1
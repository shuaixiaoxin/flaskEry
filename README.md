# flaskEry项目

## 介绍
**这是一个基于 Flask 和 Celery 的高性能分布式任务调度和处理框架，专为需要异步任务处理、任务队列管理、定时任务以及高并发需求的应用设计。项目结构清晰、易于扩展，支持快速集成第三方插件，为开发者提供开箱即用的功能。**

## 特性
- 模块化设计：解耦的架构使代码更易维护和扩展。
- 高性能任务队列：基于 Celery 实现任务异步处理和分布式队列管理。
- 灵活配置：支持自定义任务优先级、队列、超时等配置，满足不同业务需求。
- 多任务支持：支持周期性任务、延迟任务等多种任务调度类型。
- 高可用：支持多节点扩展，支持主流消息队列（如 RabbitMQ、Redis）。

## 整备
- python3.6+
- mysql数据库
- 消息队列（redis、rabbitMQ）推荐使用redis

## 部署

- 下载项目
```shell
git clone git@github.com:shuaixiaoxin/flaskEry.git
```

- 修改项目配置文件
```shell
# Flaskery/app/conf/settings.py
生产环境：Config
开发环境：DevelopmentConfig
主要修改redis、mysql信息
```

- 安装依赖库
```shell
pip3 install -r requirements.txt
```

- 数据库初始化
```shell
flask db init
flask db migrate
flask db upgrade
```

- 创建默认用户
```shell
flask create_user root 123456
```

- 启动flask
```shell
python3 api.py
```

- 启动celery
```shell
celery -A app.celery_task.init_celery.celery worker -l info
```

- 启动周期任务
```shell
celery -A app.celery_task.cron.celery_beat worker -l info
celery -A app.celery_task.cron.celery_beat beat -l info
```

如果是windows启动则可以使用以下方式启动：
```shell
# celery
celery -A app.celery_task.init_celery.celery worker -l info -P eventlet
# beat
celery -A app.celery_task.cron.celery_beat worker -l info -P eventlet
# beat
celery -A app.celery_task.cron.celery_beat beat -l info
```

# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/26
# @Author  : xiao xin
# @File    : redis_manager.py
"""
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3, decode_responses=True)
# pool = redis.ConnectionPool(host='127.0.0.1', port=26380, db=3, password='1SXgvoxF3kQlE8If', decode_responses=True)
rs = redis.StrictRedis(connection_pool=pool)


def redis_obj():
    """
    redis操作对象
    :return:
    """
    return rs


def set_key_expire(task_key, seconds):
    """
    设置键的过期时间
    :param task_key: 列表的键
    :param seconds: 过期时间（秒）
    :return: 设置成功返回 True，否则返回 False
    """
    return rs.expire(task_key, seconds)


class Redis_string:
    @staticmethod
    def set_string(key, value):
        """
        设置字符串键的值
        :param key: 字符串键
        :param value: 要设置的值
        :return: 设置成功返回 True，否则返回 False
        """
        return rs.set(key, value)

    @staticmethod
    def get_string(key):
        """
        获取字符串键的值
        :param key: 字符串键
        :return: 键的值，如果键不存在则返回 None
        """
        return rs.get(key)

    @staticmethod
    def incr_string(key, amount=1):
        """
        递增字符串键的值
        :param key: 字符串键
        :param amount: 递增量，默认为1
        :return: 递增后的值
        """
        return rs.incr(key, amount)

    @staticmethod
    def decr_string(key, amount=1):
        """
        递减字符串键的值
        :param key: 字符串键
        :param amount: 递减量，默认为1
        :return: 递减后的值
        """
        return rs.decr(key, amount)

    @staticmethod
    def append_string(key, value):
        """
        在字符串值的末尾追加内容
        :param key: 字符串键
        :param value: 要追加的值
        :return: 追加后的字符串长度
        """
        return rs.append(key, value)


class Redis_list:
    @staticmethod
    def push_list(task_key, push_list):
        """
        向列表左侧添加一个或多个元素
        :param task_key: 列表的键
        :param push_list: 要添加到列表的元素列表
        :return: 添加后列表的长度
        """
        return rs.lpush(task_key, *push_list)

    @staticmethod
    def pop_list(task_key):
        """
        移除并返回列表最左侧的元素
        :param task_key: 列表的键
        :return: 列表最左侧的元素
        """
        return rs.lpop(task_key)

    @staticmethod
    def remove_element(task_key, element):
        """
        移除列表中的特定元素
        :param task_key: 列表的键
        :param element: 要移除的元素
        :return: 被移除元素的数量
        """
        return rs.lrem(task_key, 0, element)

    @staticmethod
    def range_list(task_key, start, end):
        """
        获取列表指定范围内的元素
        :param task_key: 列表的键
        :param start: 起始索引
        :param end: 结束索引
        :return: 指定范围内的元素列表
        """
        return rs.lrange(task_key, start, end)

    @staticmethod
    def length_list(task_key):
        """
        获取列表的长度
        :param task_key: 列表的键
        :return: 列表的长度
        """
        return rs.llen(task_key)


class Redis_hash:
    @staticmethod
    def hset_hash(task_key, key, value):
        """
        创建hash键值
        :param task_key:
        :param key:
        :param value:
        :return:
        """
        return rs.hset(task_key, key, value)

    @staticmethod
    def hmset_hash(task_key, mapping):
        """
        设置多个hash字段的值
        :param task_key:
        :param mapping: 字段-值映射字典
        :return:
        """
        return rs.hmset(task_key, mapping)

    @staticmethod
    def hvals_hash(task_key):
        """
        获取单个hash表中的所有值
        :param task_key:
        :return:
        """
        return rs.hvals(task_key)

    @staticmethod
    def hgetall_hash(task_key):
        """
        获取哈希表中所有的键值对
        :param task_key:
        :return:
        """
        return rs.hgetall(task_key)

    @staticmethod
    def hkeys_hash(task_key):
        """
        获取哈希表中的所有键名
        :param task_key:
        :return:
        """
        return rs.hkeys(task_key)

    @staticmethod
    def hlen_hash(task_key):
        """
        获取哈希表中键的数量
        :param task_key:
        :return:
        """
        return rs.hlen(task_key)

    @staticmethod
    def hget_hash(task_key, field):
        """
        获取哈希表中指定字段的值
        :param task_key:
        :param field:
        :return:
        """
        return rs.hget(task_key, field)

    @staticmethod
    def hdel_hash(task_key, *fields):
        """
        删除哈希表中一个或多个字段
        :param task_key:
        :param fields:
        :return:
        """
        return rs.hdel(task_key, *fields)

    @staticmethod
    def hexists_hash(task_key, field):
        """
        检查哈希表中是否存在指定字段
        :param task_key:
        :param field:
        :return:
        """
        return rs.hexists(task_key, field)

    @staticmethod
    def hincrby_hash(task_key, field, increment=1):
        """
        自增哈希表中指定字段的值
        :param task_key:
        :param field:
        :param increment:
        :return:
        """
        return rs.hincrby(task_key, field, increment)

    @staticmethod
    def hmget_hash(task_key, *fields):
        """
        获取哈希表中所有字段的值
        :param task_key:
        :param fields:
        :return:
        """
        return rs.hmget(task_key, *fields)

    @staticmethod
    def expire_hash(task_key, seconds):
        """
        设置hash表过期时间
        :param task_key:
        :param seconds: 过期时间（秒）
        :return:
        """
        return rs.expire(task_key, seconds)

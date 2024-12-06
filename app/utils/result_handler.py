# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
# @version : V1
# @Time    : 2024/03/12
# @Author  : xiao xin
# @File    : result_handler.py
"""
import json


def create_result(status, message, data=None, format_dict=False, **kwargs):
    """
    创建一个包含结果、消息和可选数据的字典

    Parameters:
    - status (str): 结果状态，例如 '0' 或 '1'
    - message (str): 相关消息
    - data (any, optional): 可选的额外数据
    - format_dict (bool): 是否格式化输出信息
    - kwargs (any) 其他自定义返回参数

    Returns:
    dict: 包含结果、消息和可选数据的字典
    """
    result = {'status': status, 'message': message, **kwargs}
    if data is not None:
        result['data'] = data
    if format_dict:
        return json.dumps(result, ensure_ascii=False, indent=4)
    else:
        return result


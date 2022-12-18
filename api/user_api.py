#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/16 20:09 
# @Author : XiaoMa
# @Version：V 0.1
# @File : user_api.py
# @desc :

from core.api_util import api_util
from utils.response_util import process_response


def send_code(mobile):
    """
    获取短信验证码
    :param data:
    :return:
    """

    json_data = {
        'mobile': str(mobile)
    }
    response = api_util.get_code(json=json_data)
    return process_response(response)



def register(code, pwd, mobile):
    """
    注册接口
    :param code:
    :param mobile:
    :return:
    """
    json_data = {
        "code": str(code),
        "password": pwd,
        "username": mobile
    }
    response = api_util.register_mobile(json=json_data)
    return process_response(response)

def login(username, pwd):
    """
    用户登录接口
    :param username:
    :param password:
    :return:
    """
    json_data = {
        "username": username,
        "password": pwd
    }
    response = api_util.user_login(json=json_data)
    return process_response(response)
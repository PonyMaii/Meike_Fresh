#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/16 14:03 
# @Author : XiaoMa
# @Version：V 0.1
# @File : utils.py
# @desc :
import yaml
import pymysql
import requests

def get_yaml(path):
    with open(path, 'r', encoding='UTF-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
    return data



class UtilsSession:
    _api_session = None

    @classmethod
    def get_api_session(cls):
        if cls._api_session is None:
            cls._api_session = requests.session()
        return cls._api_session

    @classmethod
    def quit_api_session(cls):
        if cls._api_session is not None:
            cls._api_session.__exit__()
            cls._api_session = None
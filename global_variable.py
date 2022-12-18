#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/16 19:16 
# @Author : XiaoMa
# @Version：V 0.1
# @File : global_variable.py
# @desc :
import configparser
import sys,os


if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


CONF = configparser.ConfigParser()
CONF.read(BASE_DIR+"/configs/settings.ini", encoding="UTF-8")
URL = CONF['host']['api_sit_url']

DB = CONF['mysql']
print(*DB)
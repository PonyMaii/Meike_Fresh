#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/17 20:04 
# @Author : XiaoMa
# @Version：V 0.1
# @File : conftest.py
# @desc :
import os
from global_variable import BASE_DIR
import pytest

from utils.mysql_util import db

def get_address_num(signer_mobile):
    sql = "SELECT count(1) FROM `vue_shop`.`user_operation_useraddress` WHERE `signer_mobile` = '{}' ".format(signer_mobile)
    result = db.select_db_one(sql)
    return result['count(1)']

def judge_address_num(address_id):
    sql = "SELECT count(1) FROM `vue_shop`.`user_operation_useraddress` WHERE `id` = '{}' ".format(address_id)
    result = db.select_db_one(sql)
    return result['count(1)']

if __name__ == '__main__':
    with open(BASE_DIR+"/configs/logging.conf", "r", encoding="UTF-8") as f:

        while True:
            try:
                f.readline()
            except:
                break

        c = f.readlines()
        print(c)

        x = "1"
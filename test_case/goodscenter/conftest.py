#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/17 20:04 
# @Author : XiaoMa
# @Version：V 0.1
# @File : conftest.py
# @desc :
import os

import pytest

from utils.mysql_util import db


@pytest.fixture()
def banner_num():
    sql = "select count(1) as banner_num from goods_banner;"
    result = db.select_db_one(sql)
    return result['banner_num']

def get_shop_cart_num(good_id):
    # 查询UID
    id = user_id(os.environ['mobile'])
    sql = "select nums from trade_shoppingcart where user_id = %d and goods_id = %d" % (id, good_id)
    result = db.select_db_one(sql)
    return result['nums']

# 查询userid
def user_id(mobile):
    sql = "select id from users_userprofile where mobile = '%s';" % mobile
    result = db.select_db_one(sql)
    return result['id']

# 查询订单
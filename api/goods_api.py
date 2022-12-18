#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/17 19:52 
# @Author : XiaoMa
# @Version：V 0.1
# @File : goods_api.py
# @desc :
from conftest import get_headers
from core.api_util import api_util
from utils.response_util import process_response
import os



def get_banner():
    """
    首页商品查询
    :return:
    """
    response = api_util.banner()
    return process_response(response)

def add_shopping_cart(data):
    """
    添加购物车操作
    :return:
    """
    json_data = {
        "nums": data["nums"],
        "goods": data["goods"]
    }
    response = api_util.shopping_add(json=json_data, headers=get_headers())
    return process_response(response)

def get_shopcarts():
    """
    获取购物车列表
    :return:
    """
    response = api_util.shopcarts_get(headers=get_headers())
    return process_response(response)




def add_order(data):
    """
    下单操作
    :param data:
    :param token:
    :return:
    """
    if not data['singer_mobile']:
        singer_mobile = os.environ['mobile']
    else:
        singer_mobile = data['singer_mobile']
    json_data = {
        "post_script": data['post_script'],
        "order_mount": data['order_mount'],
        "address": data['address'],
        "signer_name": data['signer_name'],
        "singer_mobile": singer_mobile
    }
    response = api_util.orders_add(json=json_data, headers=get_headers())
    return process_response(response)


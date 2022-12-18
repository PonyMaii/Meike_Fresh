#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/18 15:38 
# @Author : XiaoMa
# @Version：V 0.1
# @File : address_api.py
# @desc :
from conftest import get_headers
from core.api_util import api_util
from utils.response_util import process_response
import os


def get_address():
    response = api_util.address_get(headers=get_headers())
    return process_response(response)

def add_address(data):
    json_data = {
        "addr": data['addr'],
        "area": data['area'],
        "province": data['province'],
        "city": data['city'],
        "district": data['district'],
        "address": data['address'],
        "phone": data['phone'],
        "receiveName": data['receiveName'],
        "signer_mobile": data['signer_mobile'],
        "signer_name": data['signer_name']
    }
    response = api_util.address_add(json=json_data, headers=get_headers())
    return process_response(response)

def del_address(data):
    response = api_util.address_del(address_id=str(data['address_id']), headers=get_headers())
    return response.text
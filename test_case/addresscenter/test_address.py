#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/18 15:49 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_address.py
# @desc :
import pytest
import allure
from utils.utlis import get_yaml
from global_variable import BASE_DIR
from test_case.addresscenter.conftest import get_address_num, judge_address_num
from api.address_api import get_address, del_address, add_address
import os

data = get_yaml(BASE_DIR+"/data/test_case_data/testAddress")

@allure.feature("收获地址操作中心")
class TestAddress:

    @allure.story("获取收货地址")
    @allure.title("获取收货地址操作")
    def test_get_address(self):
        result = get_address()
        assert result.success is True
        assert get_address_num(os.environ['mobile']) == len(result.body)

    @allure.story("添加收货地址")
    @allure.title("添加收货地址操作")
    @pytest.mark.parametrize("datas", data['test_add_address'])
    def test_add_address(self, datas):

        result = add_address(datas)
        assert result.success is True
        assert len(get_address().body) == get_address_num(os.environ['mobile'])

        # if datas['expected'] != "add_time":
        #     del_address({"address_id": result.body[-1]['id']})
        assert datas['expected'] in str(result.body)


    # @allure.story("删除收获地址")
    # @allure.title("删除收获地址操作")
    # @pytest.mark.parametrize("datas", data['test_del_address'])
    # def test_del_address(self, datas):
    #
    #     datas['address_id'] = get_address().body[-1]['id']
    #     del_address(datas)
    #     assert 0 == judge_address_num(datas['address_id'])



if __name__ == '__main__':
    print(get_address())
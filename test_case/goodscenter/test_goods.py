#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/17 19:51 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_goods.py
# @desc :
from utils.utlis import get_yaml
from global_variable import BASE_DIR
import allure
import pytest
from api.goods_api import get_banner, add_shopping_cart, get_shopcarts, add_order
from api.address_api import get_address
from test_case.goodscenter.conftest import get_shop_cart_num


data = get_yaml(BASE_DIR+"/data/test_case_data/testGoods")

@allure.feature("商品操作中心")
class TestGoods:

    @allure.story("查询商品")
    @allure.title("查询商品列表")
    def test_goods(self, banner_num):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num

    @allure.story("购物车相关")
    @allure.title("添加购物车操作")
    @pytest.mark.parametrize("datas", data['test_shopping_cart'])
    def test_shopping_cart(self, datas):
        result = add_shopping_cart(datas)
        assert result.success is True
        if datas['expected']:
            assert datas['expected'] in str(result.body)
        else:
            assert get_shop_cart_num(datas['goods']) == result.body['nums']

    @allure.story("下单相关")
    @allure.title("下单操作")
    @pytest.mark.parametrize("datas", data['test_add_order'])
    def test_add_order(self, datas):
        add_shopping_cart(datas) # 添加商品到购物车
        if not datas['order_mount'] and not datas['address']:
            shopcarts_mount = get_shopcarts().body
            address = get_address().body[0]
            datas['order_mount'] = sum([i['nums']*i['goods']['shop_price'] for i in shopcarts_mount])
            datas['address'] = address['address']+address['city']+address['district']
        result = add_order(datas)
        assert result.success is True
        assert datas['expected'] in str(result.body)


if __name__ == '__main__':
    pass

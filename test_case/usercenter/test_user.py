#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/16 20:03 
# @Author : XiaoMa
# @Version：V 0.1
# @File : test_user.py
# @desc :

from utils.utlis import get_yaml
from global_variable import BASE_DIR
import allure
import pytest
from api.user_api import send_code, register, login
from test_case.usercenter.conftest import get_code, delete_user, delete_code, get_shop_cart_num, update_code




data = get_yaml(BASE_DIR+r"\data\test_case_data\testUser")


@allure.feature("用户中心模块")
class TestUser:


    @allure.story("用户注册获取验证码")
    @allure.title("注册手机号获取验证码")
    @pytest.mark.parametrize("datas", data['test_send_code'])
    def test_send_code(self, datas):
        result = send_code(datas['mobile'])
        assert result.success is True
        assert datas['expected'] in result.body['mobile']

    @allure.story("用户注册后登入")
    @allure.title("用户注册")
    @pytest.mark.parametrize("datas", data['test_register'])
    def test_register(self, datas):
        result = send_code(datas['mobile'])
        assert result.success is True
        code = get_code(datas['mobile'])
        if datas['expected'] == '请先获取验证码':
            delete_code(datas['mobile'])
        elif datas['expected'] == '验证码过期':
            update_code(datas['mobile'])
        result = register(code=code, pwd=datas['pwd'], mobile=datas['mobile'])
        print(str(result.body))
        assert result.success is True
        assert datas['expected'] in str(result.body)

        delete_user(datas['mobile'])
        delete_code(datas['mobile'])

    @allure.story("用户登入")
    @allure.title("用户手机登入")
    @pytest.mark.parametrize("datas", data['test_login'])
    def test_login(self, datas):
        result = login(datas['username'], datas['password'])
        assert result.success is True
        assert datas['expected'] in str(result.body)



if __name__ == '__main__':
    print(data['test_login'][1])
    TestUser().test_login(data['test_login'][1])


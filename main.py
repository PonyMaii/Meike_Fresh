#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/12/16 13:56 
# @Author : XiaoMa
# @Version：V 0.1
# @File : main.py
# @desc :
import pytest
from utils.auto_email import AutoEmail
from global_variable import BASE_DIR

if __name__ == '__main__':

    pytest.main(["-v",
                 "--alluredir", "./reports/temp_allure"])

    """
    -s: 输出用例中所有需要打印的内容
    """
    import os
    os.system(rf"allure generate {BASE_DIR}/reports/temp_allure -o {BASE_DIR}/reports/report_allure/ --clean")
    # generate 后面指的是执行收集的用例目录
    # -o 标识生成的报告放在哪个目录


    # ae = AutoEmail() #创建邮箱类的对象
    # report = (BASE_DIR+"/reports/report.html").replace("\\", "/")
    # ae.send_email(report, "小马", "Dangdang API Automation TestReport")
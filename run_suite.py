"""测试套件（程序入口）"""
import time
import unittest
from base import *
from config import BASE_DIR
from script.joinCartTestTPShop import JoinCartTestTPShop
from script.loginTestTPShop import LoginTestTPShop
from script.orderTestTPShop import OrderPayTestTPShop
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverTools

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LoginTestTPShop))
suite.addTest(unittest.makeSuite(JoinCartTestTPShop))
suite.addTest(unittest.makeSuite(OrderPayTestTPShop))

DriverTools.change_quit_status(False)

# unittest.TextTestRunner().run(suite)
file_name = BASE_DIR + '/report/%s.html' % time.strftime('%Y%m%d_%H%M%S')
with open(file_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title='web 自动化测试报告', description='系统：Windows10 浏览器：谷歌 语言：python')
    runner.run(suite)

DriverTools.change_quit_status(True)
DriverTools.quit_driver()




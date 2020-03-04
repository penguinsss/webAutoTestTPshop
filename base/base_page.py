"""
PO文件基类  利用基类统一封装来自Selenium框架的方法，如果框架方法出现问题或需要更换，只需要修改基类中方法的内部实现即可
"""
from utils import DriverTools


class BasePage:
    def __init__(self):
        self.driver = DriverTools.get_driver()

    def find_element_func(self, location):
        return self.driver.find_element(location[0], location[1])


class BaseHandle:
    """操作层基类"""

    # 封装元素输入方法
    @staticmethod   # ★ 静态方法相当于是存在于类定义内部的函数
    def input_element(element, text_arg):
        element.clear()
        element.send_keys(text_arg)

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def get_msg(element):
        return element.text




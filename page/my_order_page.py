"""我的订单页"""
from base.base_page import BasePage, BaseHandle
import page


class MyOrderPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_wait_pay(self):
        return self.find_element_func(page.wait_pay)

    def find_now_pay(self):
        return self.find_element_func(page.now_pay)


class MyOrderHandle(BaseHandle):
    def __init__(self):
        self.my_order_page = MyOrderPage()

    def click_wait_pay(self):
        self.click_element(self.my_order_page.find_wait_pay())

    def click_now_pay(self):
        self.click_element(self.my_order_page.find_now_pay())


class MyOrderProxy(object):
    def __init__(self):
        self.my_order_handle = MyOrderHandle()

    def go_to_order_pay(self):
        self.my_order_handle.click_wait_pay()
        self.my_order_handle.click_now_pay()

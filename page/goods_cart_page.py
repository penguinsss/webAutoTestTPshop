"""购物车页面"""
import page
from base.base_page import BasePage, BaseHandle


class GoodCartPage(BasePage):
    def __init__(self):
        super().__init__()


    def find_is_election(self):
        return self.find_element_func(page.check_all)

    def find_pay_btn(self):
        return self.find_element_func(page.pay_btn)


class GoodCartHandle(BaseHandle):
    def __init__(self):
        self.good_cart_page = GoodCartPage()

    def click_check_all(self):
        ele = self.good_cart_page.find_is_election()
        if not ele.is_selected():
            self.click_element(ele)

    def click_pay_btn(self):
        self.click_element(self.good_cart_page.find_pay_btn())


class GoodCartProxy(object):
    def __init__(self):
        self.good_cart_handle = GoodCartHandle()

    # 点击全选，去结算，跳转至订单确认页面方法
    def go_to_order_check(self):
        self.good_cart_handle.click_check_all()
        self.good_cart_handle.click_pay_btn()

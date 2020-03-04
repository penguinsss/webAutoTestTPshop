"""订单确认页面"""

from base.base_page import BasePage, BaseHandle
import page


class OrderCheckPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_commit_order(self):
        return self.find_element_func(page.commit_order)


class OrderCheckHandle(BaseHandle):
    def __init__(self):
        self.order_check_page = OrderCheckPage()

    def click_commit_order(self):
        self.click_element(self.order_check_page.find_commit_order())


class OrderCheckProxy(object):
    def __init__(self):
        self.order_check_handle = OrderCheckHandle()

    # 点击提交订单，跳转至订单支付页
    def go_to_order_pay(self):
        self.order_check_handle.click_commit_order()

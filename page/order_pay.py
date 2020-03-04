"""订单支付页面"""

from base.base_page import BasePage, BaseHandle
import page


class OrderPayPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_after_pay(self):
        return self.find_element_func(page.after_pay)

    def find_confirm_pay(self):
        return self.find_element_func(page.confirm_pay)


class OrderPayHandle(BaseHandle):
    def __init__(self):
        self.order_pay_page = OrderPayPage()

    def click_after_pay(self):
        self.click_element(self.order_pay_page.find_after_pay())

    def click_confirm_pay(self):
        self.click_element(self.order_pay_page.find_confirm_pay())


class OrderPayProxy(object):
    def __init__(self):
        self.order_pay_handle = OrderPayHandle()

    # 选择货到付款，点击支付跳转至成功页
    def go_to_success_pay(self):
        self.order_pay_handle.click_after_pay()
        self.order_pay_handle.click_confirm_pay()

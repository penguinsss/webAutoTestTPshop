import unittest
from time import sleep
from page.goods_cart_page import GoodCartProxy
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_check_page import OrderCheckProxy
from page.order_pay import OrderPayProxy
from utils import DriverTools, get_text_element, switch_new_windows


class OrderPayTestTPShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverTools.get_driver()
        cls.index = IndexProxy()
        cls.good_cart = GoodCartProxy()
        cls.order_check = OrderCheckProxy()
        cls.my_order_proxy = MyOrderProxy()
        cls.order_pay_proxy = OrderPayProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverTools.quit_driver()

    def setUp(self) -> None:
        DriverTools.get_func()

    # ★★
    # 测试用例之间的依赖处理方式：
    #     a. 套件
    #     b. 放到同一个测试用例类中执行
    #           不过，需要注意执行顺序，因为unittest框架测试用例执行顺序由方法名称决定，依据Ascii表的顺序执行

    def test_order(self):
        self.index.go_to_my_cart()
        self.good_cart.go_to_order_check()
        self.order_check.go_to_order_pay()
        sleep(5)
        result = get_text_element('订单提交成功')
        self.assertTrue(result)

    def test_order_pay(self):
        self.index.go_to_my_order()
        switch_new_windows()
        self.my_order_proxy.go_to_order_pay()
        switch_new_windows()
        self.order_pay_proxy.go_to_success_pay()
        result = get_text_element('订单提交成功')
        self.assertTrue(result)

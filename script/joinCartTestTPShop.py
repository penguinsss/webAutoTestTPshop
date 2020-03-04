import sys
import time
import unittest
from time import sleep
from parameterized import parameterized

from config import BASE_DIR
from page.goods_detail_page import GoodsDetailProxy
from page.index_page import IndexProxy
from page.searchList_page import SearchListProxy
from read_data.read_json import build_join_cart_data
from utils import DriverTools


class JoinCartTestTPShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverTools.get_driver()
        cls.index_proxy = IndexProxy()
        cls.search_list_proxy = SearchListProxy()
        cls.goods_detail_proxy = GoodsDetailProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverTools.quit_driver()

    def setUp(self) -> None:
        DriverTools.get_func()

    # ★★ Cookie应用场景之一：用户未登录状态下可以加入商品到购物车
    @parameterized.expand(build_join_cart_data())
    def test_join_cart(self, kw, location_info, except_arg):
        self.index_proxy.search_goods(kw)   # 输入关键字并点击搜索
        sleep(5)
        # 点击商品跳转至详情页
        self.search_list_proxy.go_to_goods_details(location_info)
        # 加入商品到购物车
        self.goods_detail_proxy.join_cart()
        sleep(5)
        msg = self.goods_detail_proxy.get_join_cart_result_func()
        print(except_arg, msg)
        try:
            self.assertIn(except_arg, msg)
        except AssertionError as e:
            self.driver.get_screenshot_as_file(BASE_DIR + '/screenshot/bug-%s.png'.format(time.strftime('%Y%m%d_%H%M%S')))
            # ★★ sys.exc_info()：可输出错误信息，比如'我的账户' not found in '……'
            print(sys.exc_info())
            # ★★ 还原用例执行状态，不然用例就pass通过了
            raise e

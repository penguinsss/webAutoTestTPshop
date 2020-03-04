"""商品详情页"""
from base.base_page import BasePage, BaseHandle
from utils import DriverTools
import page


class GoodsDetailPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_join_cart(self):
        return self.find_element_func(page.join_cart)

    def get_join_cart_result(self):
        return self.find_element_func(page.assert_info)


class GoodsDetailHandle(BaseHandle):
    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    def click_join_cart(self):
        self.click_element(self.goods_detail_page.find_join_cart())

    def get_join_cart_result(self):
        driver = DriverTools.get_driver()
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        return self.get_msg(self.goods_detail_page.get_join_cart_result())


class GoodsDetailProxy(object):
    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    # 加入商品到购物车
    def join_cart(self):
        self.goods_detail_handle.click_join_cart()

    # 验证是否成功加入购物车
    def get_join_cart_result_func(self):
        return self.goods_detail_handle.get_join_cart_result()

"""商品列表页"""
from base.base_page import BasePage, BaseHandle
import page


class SearchListPage(BasePage):
    def __init__(self):
        super().__init__()

    def find_goods(self, kw):
        temp = page.goods[0], page.goods[1].format(kw)
        return self.find_element_func(temp)


class SearchListHandle(BaseHandle):
    def __init__(self):
        self.search_list_page = SearchListPage()

    def click_goods(self, kw):
        self.click_element(self.search_list_page.find_goods(kw))


class SearchListProxy(object):
    def __init__(self):
        self.search_list_handle = SearchListHandle()

    # 跳转到商品详情页
    def go_to_goods_details(self, kw):
        self.search_list_handle.click_goods(kw)

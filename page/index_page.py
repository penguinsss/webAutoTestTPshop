from base.base_page import BasePage, BaseHandle
import page


class IndexPage(BasePage):
    """对象库层"""

    def __init__(self):
        super().__init__()

    def find_login_link(self):
        return self.find_element_func(page.login)

    def find_search_bar(self):
        return self.find_element_func(page.search_bar)

    def find_search(self):
        return self.find_element_func(page.search)

    def find_my_cart_btn(self):
        return self.find_element_func(page.my_cart_btn)

    def find_my_order(self):
        return self.find_element_func(page.my_order)


class IndexHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.index_page = IndexPage()

    def click_login(self):
        self.click_element(self.index_page.find_login_link())

    def input_search_bar(self, keyword):
        self.input_element(self.index_page.find_search_bar(), keyword)

    def click_search(self):
        self.click_element(self.index_page.find_search())

    def click_my_cart_btn(self):
        self.click_element(self.index_page.find_my_cart_btn())

    def click_my_order(self):
        self.click_element(self.index_page.find_my_order())


class IndexProxy(object):
    """业务层"""

    def __init__(self):
        self.index_handle = IndexHandle()

    def go_to_login(self):
        self.index_handle.click_login()

    # 输入关键字，点击搜索
    def search_goods(self, keyword):
        self.index_handle.input_search_bar(keyword)
        self.index_handle.click_search()

    def go_to_my_cart(self):
        self.index_handle.click_my_cart_btn()

    # 点击我的订单，跳转到我的订单页面
    def go_to_my_order(self):
        self.index_handle.click_my_order()

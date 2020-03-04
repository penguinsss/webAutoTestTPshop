from selenium.webdriver.common.by import By
from base.base_page import BasePage, BaseHandle
import page


class LoginPage(BasePage):
    """对象库层"""

    def __init__(self):
        super().__init__()

    def find_username(self):
        return self.find_element_func(page.username)

    def find_password(self):
        return self.find_element_func(page.password)

    def find_verify_code(self):
        return self.find_element_func(page.verify_code)

    def find_login_btn(self):
        return self.find_element_func(page.login_btn)


class LoginHandle(BaseHandle):
    """操作层"""

    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.input_element(self.login_page.find_username(), username)

    def input_password(self, pwd):
        self.input_element(self.login_page.find_password(), pwd)

    def input_verify_code(self, verify_code):
        self.input_element(self.login_page.find_verify_code(), verify_code)

    def click_login_btn(self):
        self.click_element(self.login_page.find_login_btn())


class LoginProxy(object):
    """业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self, username, pwd, verify_code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(pwd)
        self.login_handle.input_verify_code(verify_code)
        self.login_handle.click_login_btn()

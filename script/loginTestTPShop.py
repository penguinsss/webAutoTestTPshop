import unittest
from time import sleep
import logging
from parameterized import parameterized
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from read_data.read_json import build_login_data
from utils import DriverTools


class LoginTestTPShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverTools.get_driver()
        cls.index_proxy = IndexProxy()
        cls.login_proxy = LoginProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverTools.quit_driver()

    def setUp(self) -> None:
        DriverTools.get_func()

    @parameterized.expand(build_login_data())
    def test_login(self, username, password, verify_code, except_arg):
        self.index_proxy.go_to_login()
        self.login_proxy.login(username, password, verify_code)
        sleep(5)
        result = self.driver.title
        # ★★
        logging.info(result)
        self.assertIn(except_arg, result)

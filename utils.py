"""公共方法类"""

from selenium import webdriver


# 切换窗口
def switch_new_windows():
    driver = DriverTools.get_driver()
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


# ★★
def get_text_element(text):
    """通过特定文字信息定位目标元素，搜索范围是打开的所有页面"""
    xpath = '//*[contains(text(),"{}")]'.format(text)
    try:
        driver = DriverTools.get_driver()
        return driver.find_element_by_xpath(xpath)
    except Exception:
        return False


class DriverTools(object):
    driver = None
    status = True

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get('http://127.0.0.1/')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def get_func(self):
        self.driver.get('http://127.0.0.1/')

    @classmethod
    def quit_driver(cls):
        if cls.driver and cls.status:  # ★★
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def change_quit_status(cls, b):
        cls.status = b


if __name__ == '__main__':
    pass

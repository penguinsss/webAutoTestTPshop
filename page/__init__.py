"""PO文件"""

from selenium.webdriver.common.by import By

# 首页页面
login = By.CSS_SELECTOR, '.red'
search_bar = By.CSS_SELECTOR, '#q'  # 搜索框
search = By.CSS_SELECTOR, '.ecsc-search-button'
my_cart_btn = By.CSS_SELECTOR, '.share-shopcar-index'
my_order = By.PARTIAL_LINK_TEXT, '我的订单'

# 登录页面
username = By.CSS_SELECTOR, '#username'
password = By.CSS_SELECTOR, '#password'
verify_code = By.CSS_SELECTOR, '#verify_code'
login_btn = By.CSS_SELECTOR, '.login_bnt .J-login-submit'

# 商品列表页
goods = By.XPATH, "//*[@class='shop_name2']/*[contains(text(),'{}')]"

# 商品详情页
join_cart = By.CSS_SELECTOR, '#join_cart'
assert_info = By.PARTIAL_LINK_TEXT, '继续购物'

# 购物车页面
check_all = By.CSS_SELECTOR, '.gwx-xm-dwz .checkCartAll'
pay_btn = By.PARTIAL_LINK_TEXT, '去结算'

# 我的订单页
wait_pay = By.PARTIAL_LINK_TEXT, '待付款'
now_pay = By.PARTIAL_LINK_TEXT, '立即支付'

# 订单确认页面
commit_order = By.PARTIAL_LINK_TEXT, '提交订单'

# 订单支付页面
after_pay = By.CSS_SELECTOR, '[value="pay_code=cod"]'
confirm_pay = By.PARTIAL_LINK_TEXT, '确认支付方式'


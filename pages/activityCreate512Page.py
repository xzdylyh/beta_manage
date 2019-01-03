from selenium.webdriver.common.by import By
from pages.activityCreate1024Page import ActivityCreate1024

class ActivityCreate512(ActivityCreate1024):
    """消费返券"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #返券方式
    ret_rule_locs = (By.XPATH, "//input[@name='returnRule']/..")
    #返券设置;0循环赠送；1当次消费仅赠送一次
    ret_coupon_loc = (By.XPATH, "//input[@name='returnCoupon']/..")
    #菜品设置
    ret_dishesSet_locs = (By.XPATH, "//input[@name='dishesSet']/..")
    #菜品设置－菜品输入
    ret_dishes_loc = (By.NAME, "dishes")
    #奖励范围；0现金消费；1现金储值消费
    ret_cash_loc = (By.XPATH, "//input[@name='cashCharge']/..")
    #上限设置
    ret_limit_locs = (By.XPATH, "//input[@name='returnCouponLimit']/..")
    #赠券设置－张数
    ret_climit_loc = (By.NAME, "returnCouponTimes")
    #增加券下拉框
    ret_add_loc = (By.XPATH, "//button[contains(text(),'代金券')]")
    #活动说明
    ret_desc_loc = (By.XPATH, "//*[@id='inputRestriction']")
    #标题
    assert_title_loc = (
        By.CSS_SELECTOR,
        'div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > span'
    )
    #状态
    assert_status_loc = (
        By.CSS_SELECTOR,
        "div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(5)"
    )
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_rule_button(self, index):
        """返券方式"""
        self.click_btn_index(
            '返券方式',
            index,
            *(self.ret_rule_locs)
        )

    def click_add_coupon(self):
        """增加券下拉"""
        self.click_button(
            '增加券下拉框',
            *(self.ret_add_loc)
        )

    def click_return_coupon(self, index):
        """返券设置"""
        self.click_btn_index(
            '返券设置',
            index,
            *(self.ret_coupon_loc)
        )

    def click_return_cash(self, index):
        """奖励范围"""
        self.click_btn_index(
            '奖励范围',
            index,
            *(self.ret_cash_loc)
        )

    def click_limit_radio(self, index):
        """赠券上限"""
        self.click_btn_index(
            '赠券上限',
            index,
            *(self.ret_limit_locs)
        )

    def input_custom_limit(self, text):
        """赠券设置－自定义次数"""
        self.input_text(
            text,
            '自定义',
            *(self.ret_climit_loc)
        )

    def click_dishes_set(self, index):
        """菜品设置"""
        self.click_btn_index(
            '菜品设置',
            index,
            *(self.ret_dishesSet_locs)
        )

    def input_dishes_text(self, text):
        """返券需要满足菜品"""
        self.input_text(
            text,
            '返券需要满足菜品',
            *(self.ret_dishes_loc)
        )

    def assert_add_success(self, text, status):
        """断言成功"""
        status = str(status).strip()
        title = str(self.get_tag_text(
            'text',
            *(self.assert_title_loc)
        )).strip()
        st = str(
            self.get_tag_text(
                'text',
                *(self.assert_status_loc)
            )).strip()
        self.get_image
        if not (title == text and st == status):
            return False
        return True

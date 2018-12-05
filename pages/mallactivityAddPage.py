from selenium.webdriver.common.by import By
from base.basepage import BasePage

class MallactivityAdd(BasePage):
    """限时秒杀"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>
    #活动名称
    activity_name_loc = (By.ID, "field_title")
    #活动开始时间
    activity_sdate_loc = (By.ID, "inputDateStart")
    #活动结束时间
    activity_edate_loc = (By.ID, "inputDateEnd")
    #限购设置
    activity_limit_locs = (By.XPATH, "//input[@name='set_limit']/../span[1]")
    #每人限购数
    activity_lnum_loc = (By.NAME, "limit_number")
    #选择商品
    activity_product_loc = (By.PARTIAL_LINK_TEXT, "选择商品")
    #商品
    activity_checkbox_locs = (By.XPATH, "//input[@name='product']/..")
    #确认
    activity_confirm_loc = (By.XPATH, "//*[contains(text(),'确认')]")
    #秒杀价格
    activity_price_loc = (By.NAME, "flashsale_price[]")
    #秒杀数量
    activity_num_loc = (By.NAME, "amount[]")
    #保存
    activity_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    #删除
    activity_del_loc = (By.LINK_TEXT, "删除")
    #标题
    assert_title_loc = (
        By.CSS_SELECTOR,
        'div.we-table-responsive > table > tbody > tr > td:nth-child(2)'
    )
    # assert_title_loc = (By.XPATH, "/tbody/tr[1]/td[2]")
    #状态
    assert_status_loc = (
        By.CSS_SELECTOR,
        'div.we-table-responsive > table > tbody > tr > td:nth-child(5)'
    )
    # assert_status_loc =  (By.XPATH, "/tbody/tr[1]/td[5]")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>
    def input_activtity_name(self, text):
        """活动名称"""
        self.input_text(
            text,
            '活动名称',
            *(self.activity_name_loc)
        )

    def input_start_date(self, text):
        """活动开始时间"""
        self.clear_input_text(*(self.activity_sdate_loc))
        self.input_text(
            text,
            "活动开始时间",
            *(self.activity_sdate_loc)
        )

    def input_end_date(self, text):
        """活动结束时间"""
        self.clear_input_text(*(self.activity_edate_loc))
        self.input_text(
            text,
            '活动结束时间',
            *(self.activity_edate_loc)
        )

    def click_limit_shop(self, index, text=1):
        """限购设置;0不限购;1每人限购text件"""
        self.click_btn_index(
            '限购设置',
            index,
            *(self.activity_limit_locs)
        )
        if int(index) == 1:
            self.input_text(
                text,
                '每人限购',
                *(self.activity_lnum_loc)
            )

    def click_add_product(self):
        """选择商品"""
        self.click_button(
            '选择商品',
            *(self.activity_product_loc)
        )

    def click_product_checkbox(self, index):
        """勾选商品复选框"""
        self.click_btn_index(
            '勾选商品',
            index,
            *(self.activity_checkbox_locs)
        )

    def click_confirm_button(self):
        """确认"""
        self.click_button(
            '确认',
            *(self.activity_confirm_loc)
        )

    def input_price_text(self, text):
        """秒杀价格"""
        self.input_text(
            text,
            '秒杀价格',
            *(self.activity_price_loc)
        )

    def input_number_text(self, text):
        """秒杀数量"""
        self.input_text(
            text,
            '秒杀数量',
            *(self.activity_num_loc)
        )

    def click_save_button(self):
        """保存"""
        self.click_button(
            '保存',
            *(self.activity_save_loc)
        )


    def click_del_button(self):
        """删除"""
        self.click_button(
            '删除',
            *(self.activity_del_loc)
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
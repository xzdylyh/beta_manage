from selenium.webdriver.common.by import By
from base.basepage import BasePage


class ActivityCreate2057(BasePage):
    """定向调研"""
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>定位<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    #活动名称
    activity_name_loc = (By.ID, "inputName")
    #资历券复选框
    activity_check_loc = (By.NAME, "checkcoupon")
    #添加券
    activity_add_loc = (By.ID, "dropdownCoupon")
    #选择券
    coupon_type = ['代金券', '礼品券']
    #使用
    activity_used_locs = (By.LINK_TEXT, "使用")
    #发券提醒
    activity_send_locs = (By.XPATH, "//input[@name='sendRemind']/..")
    #券到期提醒
    activity_expire_locs = (By.XPATH, "//input[@name='expireRemind']/..")
    #资历积分复选框
    activity_credit_loc = (By.XPATH, "//labal[contains(text(),'奖励积分')]/..")
    #输入积分数
    activity_num_loc = (By.ID, "integralValue")
    #问券设置
    activity_set_loc = (By.NAME, "uQuestionId")
    #保存
    activity_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>操作<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def input_activity_name(self, text):
        """活动名称"""
        self.input_text(
            text,
            '活动名称',
            *(self.activity_name_loc)
        )

    def click_check_coupon(self):
        """奖励券"""
        self.click_button(
            '奖励券',
            *(self.activity_check_loc)
        )

    def click_add_coupon(self):
        """添加券"""
        self.click_button(
            '添加券',
            *(self.activity_add_loc)
        )

    def select_coupon_type(self, index):
        """选择券类型"""
        self.click_btn_index(
            '选择券类型',
            index,
            *(By.LINK_TEXT, self.coupon_type[index])
        )

    def click_used_button(self, index):
        """使用"""
        self.click_btn_index(
            '使用',
            index,
            *(self.activity_used_locs)
        )

    def click_send_radio(self, index):
        """发送提醒"""
        self.click_btn_index(
            '发券提醒',
            index,
            *(self.activity_send_locs)
        )

    def click_expire_radio(self, index):
        """券到期提醒"""
        self.click_btn_index(
            '券到期提醒',
            index,
            *(self.activity_expire_locs)
        )

    def click_credit_checkbox(self):
        """奖励积分"""
        self.click_button(
            '奖励积分',
            *(self.activity_credit_loc)
        )

    def input_credit_text(self, text):
        """输入积分"""
        self.input_text(
            text,
            '奖励积分',
            *(self.activity_num_loc)
        )

    def select_question_list(self, index):
        """选择问题设置"""
        select = self.select_list(*(self.activity_set_loc))
        select.select_by_index(index)

    def click_save_button(self):
        """保存"""
        self.click_button(
            '保存',
            *(self.activity_save_loc)
        )


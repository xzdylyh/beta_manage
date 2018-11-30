from selenium.webdriver.common.by import By
from base.basepage import BasePage

class ActivityCreate64(BasePage):
    """营销－开卡关怀"""
    #>>>>>>>>>>>>>>定位<<<<<<<<<<<<<<<<<
    #活动名称
    activity_name_loc = (By.ID, "inputName")
    #赠券设置
    activity_set_loc = (By.ID, "dropdownCoupon")
    #券类型选择
    activity_coupon_type = ['代金券', '礼品券']
    #使用券;0第一个券，1第二个，依此类推
    activity_used_locs = (By.XPATH, "//a[contains(text(),'使用')]")
    #使用券张数
    activity_usednum_loc = (By.NAME, "couponCount[]")
    #发券提醒;0不提醒；1短信提醒
    activity_send_locs = (By.XPATH, "//input[@name='sendRemind']/..")
    #券到期提醒;0不提醒；1短信提醒
    activity_expire_locs = (By.XPATH, "//input[@name='expireRemind']/..")
    #赠送积分
    activity_credit_loc = (By.NAME, "creditNum")
    #赠送储值
    activity_charge_loc = (By.NAME, "chargeNum")
    #活动类别-更改链接
    activity_atype_loc = (By.XPATH, "//input[@name='ccids']/../button[1]")
    #活动类别－确定
    activity_confirm_loc = (By.XPATH, "//button[contains(text(),'确定')]")
    #活动开始时间
    activity_stime_loc = (By.ID, "inputStartDate")
    #活动结束时间
    activity_etime_loc = (By.ID, "inputEndDate")
    #保存
    activity_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    activity_sconfirm_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    #删除
    activity_delete_loc = (By.LINK_TEXT, "删除")
    #断言
    activity_assert_loc = (
        By.CSS_SELECTOR,
        "div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(1)"
    )

    #>>>>>>>>>>>>>>组件<<<<<<<<<<<<<<<<<
    def input_activity_name(self, text):
        """输入活动名称"""
        self.input_text(
            text,
            '活动名称',
            *(self.activity_name_loc)
        )

    def click_add_coupon(self):
        """赠券设置，添加券按钮"""
        self.click_button(
            '添加券',
            *(self.activity_set_loc)
        )

    def click_coupon_type(self, index):
        """选择券类型；0代金券；1礼品券"""
        index = int(index)
        self.click_button(
            self.activity_coupon_type[index],
            *(By.LINK_TEXT, self.activity_coupon_type[index])
        )

    def click_coupon_used(self, index):
        """使用券；0第一张券；1第二张，依此类推"""
        self.click_btn_index(
            '使用',
            index,
            *(self.activity_used_locs)
        )

    def click_send_remind(self, index):
        """发券提醒；0不提醒；1短信提醒"""
        self.click_btn_index(
            '发券提醒',
            index,
            *(self.activity_send_locs)
        )

    def click_expire(self, index):
        """到期提醒;0不提醒；1短信提醒"""
        self.click_btn_index(
            '到期提醒',
            index,
            *(self.activity_expire_locs)
        )

    def input_credit(self, text):
        """赠送积分"""
        self.input_text(
            text,
            '赠送积分',
            *(self.activity_credit_loc)
        )


    def input_charge(self, text):
        """赠送储值"""
        self.input_text(
            text,
            '赠送储值',
            *(self.activity_charge_loc)
        )


    def input_start_time(self, text):
        """活动开始时间"""
        self.clear_input_text(
            *(self.activity_stime_loc)
        )
        self.input_text(
            text,
            '活动开始时间',
            *(self.activity_stime_loc)
        )

    def input_end_time(self, text):
        """活动结束时间"""
        self.clear_input_text(
            *(self.activity_etime_loc)
        )
        self.input_text(
            text,
            '活动结束时间',
            *(self.activity_etime_loc)
        )

    def click_save_button(self):
        """保存"""
        self.click_button(
            '保存',
            *(self.activity_save_loc)
        )

    def click_sconfirm_btn(self):
        """保存确认按钮"""
        self.click_button(
            '确认',
            *(self.activity_sconfirm_loc)
        )

    def click_card_type(self):
        """活动卡类别"""
        self.click_button(
            '活动卡类别',
            *(self.activity_atype_loc)
        )
        self.click_button(
            '确定',
            *(self.activity_confirm_loc)
        )

    def click_delete_button(self):
        """删除"""
        self.click_button(
            '删除',
            *(self.activity_delete_loc)
        )
        self.click_button(
            '确认',
            *(self.activity_sconfirm_loc)
        )

    def assert_add_success(self, text):
        """断言新增开卡关怀活动成功"""
        txt = self.get_tag_text(
            'text',
            *(self.activity_assert_loc)
        )
        txt = str(txt).strip()
        text = str(text).strip()
        self.get_image
        if not txt != text:
            return False
        return True


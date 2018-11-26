from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64

class ActivityCreate2(ActivityCreate64):
    """给开卡未消费会员赠券"""
    """
    此功能中预计发放人数,当天开卡次日生效
    """
    # >>>>>>>>>>>>>>>>>>>>>定位<<<<<<<<<<<<<<<<<<<<<<<<<
    # 发券日期
    coupon_date_loc = (By.NAME, "startDate")
    # 开始时间
    coupon_time_loc = (By.ID, "inputTime")

    # 下一步按钮
    coupon_next_loc = (By.XPATH, "//button[contains(text(),'下一步')]")
    # 群活动消息;0不发送;1发送提醒消息
    coupon_msg_locs = (By.XPATH, "//input[@name='sendMessage']/..")
    #消息内容
    coupon_content_loc = (By.XPATH, "//*[@name='weixinMessage']/../div[1]")
    #提交
    coupon_submit_loc = (By.XPATH, "//button[contains(text(),'提交')]")
    # 提交确认
    coupon_sconfirm_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    #断言增加成功
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
    #删除
    coupon_delete_loc = (By.LINK_TEXT, "删除")
    # >>>>>>>>>>>>>>>>>>>>>操作<<<<<<<<<<<<<<<<<<<<<<<<<
    def input_start_date(self, text):
        """输入开始日期"""
        self.clear_input_text(*(self.coupon_date_loc))
        self.input_text(
            text,
            '发券开始日期',
            *(self.coupon_date_loc)
        )

    def input_start_time(self, text):
        """输入开始时间"""
        self.input_text(
            text,
            '发券开始时间',
            *(self.coupon_time_loc)
        )


    def click_next_button(self):
        """单击下一步button"""
        self.click_button(
            '下一步',
            *(self.coupon_next_loc)
        )

    def click_activity_msg(self, index, msg='群发提醒消息'):
        """群发活动消息"""
        index = int(index)
        self.click_btn_index(
            '群发活动消息',
            index,
            *(self.coupon_msg_locs)
        )
        if index == 1:
            self._input_msg_content(msg)


    def _input_msg_content(self, text):
        """输入消息内容"""
        self.input_text(
            text,
            '消息内容',
            *(self.coupon_content_loc)
        )


    def click_submit_button(self):
        """提交"""
        self.click_button(
            '提交',
            *(self.coupon_submit_loc)
        )

    def click_sconfirm_btn(self, index):
        """提交确认"""
        self.click_btn_index(
            '确认',
            index,
            *(self.coupon_sconfirm_loc)
        )

    def assert_add_success(self, text, status):
        """断言成功"""
        self.get_image
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
        if not (title == text and st == status):
            return False
        return True
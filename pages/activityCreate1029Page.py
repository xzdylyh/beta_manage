from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64

class ActivityCreate1029(ActivityCreate64):
    """消费评价"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #奖励券
    ac_reward_coupon_loc = (By.XPATH, "//input[@name='checkcoupon']/..")
    #勾选状态
    reward_check_attr = ['we-checkbox checked','we-checkbox']

    #积分勾选框
    ac_reward_credit_loc = (By.XPATH, "//input[@name='integral']/..")
    #积分输入框
    ac_credit_loc = (By.NAME, "integralValue")
    #问卷设置
    ac_question_loc = (By.NAME, "uQuestionId")
    #问卷推送条件
    ac_push_loc = (By.NAME, "pushCondition")
    #满多少员
    ac_amount_loc = (By.NAME, "pushAmount")
    #活动说明
    ac_desc_loc = (By.XPATH, "//*[@name='summary']/../div[1]")
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
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def input_activity_desc(self, text):
        """活动说明"""
        self.input_text(
            text,
            '活动说明',
            *(self.ac_desc_loc)
        )

    def select_push(self, index):
        """问卷推送条件"""
        st = self.select_list(*(self.ac_push_loc))
        st.select_by_index(int(index))

    def input_push_amount(self, text):
        """推送金额"""
        self.input_text(
            text,
            '每满{}元'.format(text),
            *(self.ac_amount_loc)
        )

    def select_question(self, index):
        """问卷设置"""
        st = self.select_list(*(self.ac_question_loc))
        st.select_by_index(int(index))


    def select_reward_credit(self, is_select, text):
        """
        评价奖励;is_select为0勾选复选框;为1不选择复选框;
        index是定位到多个元素按索引选择
        """
        attr = self.get_element_attribute(
            'class',
            *(self.ac_reward_credit_loc)
        )
        #等于0,说明要勾选,并输入积分
        if int(is_select) == 0:
            if (not 'checked' in attr):
                self.click_button(
                    '奖励积分',
                    *(self.ac_reward_credit_loc)
                )
            self.clear_input_text(*(self.ac_credit_loc))
            self.input_text(
                text,
                '奖励积分',
                *(self.ac_credit_loc)
            )
        if int(is_select) == 1:
            if 'checked' in attr:
                self.click_button(
                    '奖励积分',
                    *(self.ac_reward_credit_loc)
                )

    def select_reward_coupon(self, is_select, c_type, c_index):
        """
        评价奖励;is_select为0勾选复选框;为1不选择复选框;
        index是定位到多个元素按索引选择
        """
        attr = self.get_element_attribute(
            'class',
            *(self.ac_reward_coupon_loc)
        )
        #等于0,说明要勾选,并输入积分
        if int(is_select) == 0:
            if (not 'checked' in attr):
                self.click_button(
                    '奖励券',
                    *(self.ac_reward_coupon_loc)
                )
            self.click_add_coupon()
            self.click_coupon_type(int(c_type)) #0代金券
            self.click_coupon_used(int(c_index)) #第一张券

        if int(is_select) == 1:
            if 'checked' in attr:
                self.click_button(
                    '奖励券',
                    *(self.ac_reward_coupon_loc)
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




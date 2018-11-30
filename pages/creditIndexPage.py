from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.basepage import BasePage


class CreditIndexPage(BasePage):
    """"封装积分页面的元素及操作"""
    # <<<<<<<<<<<<<<<元素定位>>>>>>>>>>>>>>>>>>>>>>>>>
    # 功能状态，0：开启；1：关闭
    credit_stateRadio_loc = (By.XPATH, "//input[@name='state']/..")
    # ------------发放积分---------------------
    # 消费奖励积分 开启或关闭
    credit_consumpoint_loc = (By.XPATH, "//input[@name='consumpoints']/..")
    # 0,消费后立即奖励,1完成消费评价后奖励
    credit_consumpointsmode_loc = (By.XPATH,
                                   "//input[@name='consumpointsmode']/..")

    # 奖励规则
    credit_baseline_loc = (By.NAME, "baseline")
    # 奖励范围,0：现金消费；1：现金和储值消费
    credit_giftRangeRadio_loc = (By.XPATH, "//input[@name='giftRange']/..")
    # 积分有效期,0:当年发放的所有积分，在下一年度的;1:自发放之日起一年后过期（逐笔过期）
    # 2:永久有效
    credit_termRadio_loc = (By.XPATH, "//input[@name='term']/..")
    # 月份
    credit_months_loc = (By.NAME, 'months')
    # 天数
    credit_days_loc = (By.NAME, 'days')
    # -----------消耗积分-----------------------
    # 选择消耗积分类型，0:积分门店消费抵现；1：积分线上消费抵现 ；2：积分换礼
    credit_pointeExchange_loc = (By.XPATH, "//input[@type='checkbox']/..")
    # 添加兑换规则
    credit_rules_loc = (By.XPATH, "//label[@data-exchange='rules']")
    # credit_rules_loc = (By.XPATH, "//div[@class='panel-body']/form/div[2]/div[7]/div/div/div[3]/label")
    # 积分数量
    credit_ruleNum_loc = (By.NAME, 'ruleNum0')
    # 积分兑换,0:实物礼品;1:优惠券
    credit_pointWay_loc = (By.XPATH, "//input[@name='point-coupon0']/..")
    # 礼品名称和数量
    credit_pointWayGift_loc = (By.NAME, 'ruleName[]')
    # 添加优惠券按钮
    credit_weCoupon_loc = (By.NAME, "//button[@data-toggle='dropdown']")
    # 选择代金券/礼品券,0选择代金券，1选择礼品券:
    credit_selectMenuitem_loc = (By.XPATH, "//a[@role='menuitem']/..")
    # 使用代金券/礼品券
    credit_couponD_loc = (By.XPATH, "//a[@data-toggle='coupon.apply']")
    # 删除兑换规则按钮
    credit_removeConfirm_loc = (By.XPATH,
                                "//button[@data-toggle='popover.confirm.close']"
                                )
    # 删除确定按钮
    credit_okBtn_loc = (By.XPATH,
                        ".//*[starts-with(@id,'popover')]/div[2]/div[2]/button[1]")

    # 添加子规则按钮
    credit_ruleAdd_loc = (By.XPATH, "//a[@data-toggle='rule.add']")
    # 积分换礼规则输入框
    credit_iframe_loc = (By.ID, 'ueditor_0')

    # 限制与说明
    credit_editorInput_loc = (By.CLASS_NAME, 'form-control editor-input')
    # 积分名称
    credit_screenname_loc = (By.NAME, 'screenname')
    # 保存按钮
    credit_submitBtn_loc = (By.XPATH, "//button[@type='submit']")
    # 修改按钮
    credit_modify_loc = (By.XPATH, "//button[@data-toggle='point.modify']")
    #
    credit_assert_text_loc = (By.XPATH,
                              "//div[@class='form-output']//div[8]//p")

    # <<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def select_state_radio(self, index):
        """选择开启/关闭,0：开启；1：关闭"""
        self.click_btn_index('选择开启/关闭', index,
                             *(self.credit_stateRadio_loc)
                             )

    def click_modify_btn(self):
        """点击修改按钮"""
        self.click_button('修改', *(self.credit_modify_loc))

    def select_consumpoint(self, index):
        """消费奖励积分,0开启,1关闭"""
        self.click_btn_index('消费奖励积分', index,
                             *(self.credit_consumpoint_loc)
                             )

    def select_consumpointsmode(self, index):
        """0,消费后立即奖励,1完成消费评价后奖励"""
        self.click_btn_index('奖励积分模式', index,
                             *(self.credit_consumpointsmode_loc)
                             )

    def input_baseline_text(self, text):
        """输入奖励规则"""
        self.clear_input_text(*(self.credit_baseline_loc))
        self.input_text(text, '奖励规则', *(self.credit_baseline_loc))

    def select_giftRange_radion(self, index):
        """选择奖励范围,0：现金消费；1：现金和储值消费"""
        self.click_btn_index('奖励范围', index,
                             *(self.credit_giftRangeRadio_loc)
                             )

    def select_termRadio_radio(self, index):
        """积分有效期
           0:当年发放的所有积分，在下一年度的;
           1:自发放之日起一年后过期（逐笔过期）
           2:永久有效
        """
        self.click_btn_index('积分有效期', index,
                             *(self.credit_termRadio_loc)
                             )

    def select_monthAndDay(self, month, day):
        """选择月份,日"""
        # 通过索引选择月份
        month_element = self.find_element(*(self.credit_months_loc))
        Select(month_element).select_by_index(month)
        print("选择的月份是：{}".format(month))
        # 通过索引选择日
        day_element = self.find_element(*(self.credit_days_loc))
        Select(day_element).select_by_index(day)
        print("选择的日子是：{}".format(day))

    def select_pointeExchange_radio(self, index):
        """选择消耗积分类型，
           0:积分门店消费抵现；
           1：积分线上消费抵现 ；
           2：积分换礼
        """
        self.click_btn_index('消耗积分类型选择', index,
                             *(self.credit_pointeExchange_loc))

    def select_rules(self, desc):
        """选择添加兑换规则"""
        self.click_button(desc, *(self.credit_rules_loc))

    def input_ruleNum_text(self, num):
        """输入积分数量"""
        self.clear_input_text(*(self.credit_ruleNum_loc))
        self.input_text(num, '积分数量',
                        *(self.credit_ruleNum_loc)
                        )

    def select_pointWay(self, index):
        """积分兑换,0:实物礼品;1:优惠券"""
        self.click_btn_index('积分兑换', index,
                             *(self.credit_pointWay_loc)
                             )

    def input_pointWayGift_text(self, text):
        """输入礼品名称和数量"""
        self.clear_input_text(*(self.credit_pointWayGift_loc))
        self.input_text(text, '礼品名称和数量',
                        *(self.credit_pointWayGift_loc)
                        )

    def click_weCoupon_btn(self, index):
        """点击"+",添加优惠券按钮,然后在进行代金券/礼品券的选择
            0:代金券
            1：礼品券
        """
        # 点击添加优惠券按钮
        self.click_button('添加优惠券按钮', *(self.credit_weCoupon_loc))
        # 选择代金券/礼品券
        self.click_btn_index('选择代金券/礼品券', index,
                             *(self.credit_selectMenuitem_loc)
                             )

    def selectCoupon(self, index):
        """使用代金券/礼品券，存在代金券/礼品券，点击使用按钮"""
        self.click_btn_index(
            '代金券/礼品券',
            index,
            *(self.credit_couponD_loc)
        )

    def click_removeConfirm_btn(self):
        """点击删除兑换规则按钮"""
        self.click_button('删除兑换规则', *(self.credit_removeConfirm_loc))

    def click_Ok_btn(self):
        """点击删除确定按钮"""
        self.click_button('确定', *(self.credit_okBtn_loc))

    def click_ruleadd_btn(self):
        """点击添加子规则按钮"""
        self.click_button('添加子规则',*(self.credit_ruleAdd_loc))

    def input_screenName_text(self, text):
        """输入积分名称"""
        self.clear_input_text(*(self.credit_screenname_loc))
        self.input_text(text, '积分名称',
                        *(self.credit_screenname_loc)
                        )

    def click_submit(self):
        """点击保存按钮"""
        self.click_button('保存', *(self.credit_submitBtn_loc))

    def get_modify_text(self):
        """获取修改后的值"""
        text = self.get_tag_text('text', *(self.credit_assert_text_loc))
        print("修改后的值为：{}".format(text))
        self.get_image
        return text










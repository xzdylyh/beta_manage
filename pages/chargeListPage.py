
"""
create:2018/11/7
by:ts
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.basepage import BasePage


class ChargeList(BasePage):
    """
    此类用于封装新建门店储值规则页面元素、操作
    """
    # ----------------------元素定位器-----------------------
    # 规则名称：
    charge_inputRuleName_loc = (By.NAME, 'name')
    # 充值金额(元）：
    charge_inputPrepaidValue_loc = (By.NAME, 'prepaidValue[]')
    # ---------------固定金额------------------------
    # 固定金额checkbox：
    charge_checkAmount_loc = (By.XPATH, "//label[@data-exchange='amount']")
    # 固定金额/实收金额的：
    charge_selectAccount_loc = (By.NAME, 'inputAccount[]')
    # 送固定金额（元）/送实收金额的（%）
    charge_presentValue_loc = (By.NAME, 'presentValue[]')
    # ---------------固定积分------------------------
    # 固定积分checkbox：
    charge_checkIntegral_loc = (By.XPATH, "//label[@data-exchange='integral']")
    # 固定积分/实收金额的：
    charge_selectIntegral_loc = (By.NAME, 'inputIntegral[]')
    # 送固定积分（个）/送实收金额的（%个）
    charge_integralValue_loc = (By.NAME, 'integralValue[]')
    # --------------代金券/礼品券----------------------
    # 代金券/礼品券checkbox:
    charge_checkGift_loc = (By.XPATH, "//label[@data-exchange='gift']")
    # 代金券/礼品券按钮:
    charge_selectGift_loc = (By.CSS_SELECTOR, ' div.umar-10.coupon-position > div > div > button')
    # 选择代金券/礼品券,0选择代金券，1选择礼品券:
    charge_selectMenuitem_loc = (By.XPATH, "//a[@role='menuitem']/..")
    # 使用代金券
    charge_couponD_loc = (By.XPATH, "//a[@data-toggle='coupon.apply']")

    # 保存按钮
    charge_submitBtn_loc = (By.XPATH, "//button[@type='submit']")
    # 判断是否成功
    charge_sucessText_loc = (By.CSS_SELECTOR, 'div.panel-body>div>h4')
    # 保存成功后点击返回按钮
    charge_backBtn_loc = (By.LINK_TEXT, '返回')
    # 删除规则
    charge_delBtn_loc = (By.LINK_TEXT, '删除')
    # 删除确定按钮
    charge_okBtn_loc = (By.XPATH, ".//*[starts-with(@id,'popover')]/div[2]/div[2]/button[1]")
    # 删除成功
    charge_delSussecc_loc = (By.XPATH, "//a[@href='/charge/edit?type=shop']")

    def inputRuleNameValue(self, value):
        """输入规则名称"""
        self.input_text(value, '规则名称', *(self.charge_inputRuleName_loc))

    def inputPrepaidValue(self, value):
        """输入充值金额"""
        self.input_text(value, '充值金额', *(self.charge_inputPrepaidValue_loc))

    def selectStoreRule(self, index):
        """选择储值规则"""
        if index == 0:
            # self.click_button('选择固定金额', *(self.charge_checkAmount_loc))
            pass
        elif index == 1:
            self.click_button('选择固定金额', *(self.charge_checkAmount_loc))
            self.click_button('选择固定积分', *(self.charge_checkIntegral_loc))
        elif index ==2:
            self.click_button('选择固定金额', *(self.charge_checkAmount_loc))
            self.click_button('选择代金券/礼品券', *(self.charge_checkGift_loc))
        else:
            self.click_button('选择固定积分', *(self.charge_checkIntegral_loc))
            self.click_button('选择代金券/礼品券', *(self.charge_checkGift_loc))


    def selectInputAccount(self,index):
        """
        选择固定金额/实收金额的
        index:0 固定金额
        index:1 实收金额的
        """
        element = self.find_element(*(self.charge_selectAccount_loc))
        Select(element).select_by_index(index)

    def inputPresentValue(self, value):
        """
        :param value: 金额数(0-100000)/百分比（1-100%)
        :return: 无
        """
        self.input_text(value, '固定金额（元）/实收金额的（%）',
                        *(self.charge_presentValue_loc))

    def selectInputIntegral(self, index):
        """选择固定积分/实收金额的"""
        element = self.find_element(
            *(self.charge_selectIntegral_loc)
        )
        Select(element).select_by_index(index)


    def inputIntegralValue(self, value):
        """输入金额/百分比"""
        self.input_text(
            value,
            '金额/百分比',
            *(self.charge_integralValue_loc)
        )

    def selectGift(self, index):
        """"首先点击代金券/礼品券按钮，然后在进行代金券/礼品券的选择
            0:代金券
            1：礼品券
        """
        self.click_button(
            '点击代金券/礼品券按钮',
            *(self.charge_selectGift_loc)
        )
        self.click_btn_index(
            '选择代金券/礼品券',
            index,
            *(self.charge_selectMenuitem_loc)
        )

    def selectCoupon(self,index):
        """使用代金券/礼品券，存在代金券/礼品券，点击使用按钮"""
        self.click_btn_index(
            '代金券/礼品券',
            index,
            *(self.charge_couponD_loc)
        )

    def clictSubmitBtn(self):
         """点击保存按钮"""
         self.click_button('保存', *(self.charge_submitBtn_loc))

    def getScuessText(self):
        """获取保存成功提示"""
        success_test = self.get_tag_text(
            'text',
            *(self.charge_sucessText_loc)
        )
        self.get_image
        return success_test

    def clickBcakBtn(self):
        """"点击返回按钮"""
        self.click_button('返回', *(self.charge_backBtn_loc))

    def clickDelBtn(self):
        """点击删除按钮"""
        self.click_button('删除', *(self.charge_delBtn_loc))

    def clickOkBtn(self):
        """点击删除确定按钮"""
        self.click_button('确定', *(self.charge_okBtn_loc))

    def getDelInfo(self):
        """获取删除成功后的信息"""
        info = self.get_tag_text('text', *(self.charge_delSussecc_loc))
        self.get_image
        return info

    def click_btb(self):
        self.click_button('test', *(self.charge_delSussecc_loc))










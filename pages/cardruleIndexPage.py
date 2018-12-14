from selenium.webdriver.common.by import By
from base.basepage import BasePage

class Cardrule(BasePage):
    """封装升降级规则设置页面元素、操作"""
    # <<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 升级规则-修改按钮
    rule_modify_loc = (By.XPATH, "//a[@data-toggle='upgrade.modify']")
    # 降级规则-修改按钮
    rule_subdmote_loc = (By.XPATH, "//a[@data-toggle='upgrade.subdmote']")
    # 升级规则选项
    rule_up_loc = (By.XPATH, "//input[@type='checkbox']/..")
    # 规则输入框
    rule_input = "//dicv[@class='upgrade-modal-info']/div[{}]//input"
    rule_input_loc = (By.XPATH, "//input[@type='text']")
    # 升级确认
    rule_upsure_loc = (By.XPATH,
                     "//button[@class='btn btn-primary we-btn price-btn']"
                     )
    # 取消
    rule_cancel_loc = (By.XPATH,
                       "//button[@class='btn btn-default we-btn']"
                       )
    # 降级规则选项
    rule_down_loc = (By.XPATH, "//input[@type='checkbox']/..")
    # 降级确认
    rule_downsure_loc = (By.XPATH,
                     "//button[@class='btn btn-primary we-btn demote-btn']"
                     )
    # 会员储值余额不足
    rule_money_loc = (By.NAME, 'money')
    # 会员当前等级满
    rule_sizes_loc = (By.NAME, 'sizes')
    # 单位
    rule_unit_loc = (By.NAME, 'unit')
    # 会员在当前等级每
    rule_monthTime_loc = (By.NAME, 'monthTime')
    # 个月累计消费未达到
    rule_monthMoney_loc = (By.NAME, 'monthMoney')
    # 会员在当前等级每
    rule_monthRechargeTime_loc = (By.NAME, 'monthRechargeTime')
    # 个月累计充值(实收+奖励)未达到
    rule_monthRechargeMoney_loc = (By.NAME, 'monthRechargeMoney')
    # 保存
    rule_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")

    # <<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_modify(self):
        """点击升级规则-修改"""
        self.click_button('修改', *(self.rule_modify_loc))

    def click_subdmote(self):
        """点击降级规则-修改"""
        self.click_button('修改', *(self.rule_subdmote_loc))

    def select_up(self, text, index):
        """选择升级规则,并输入相应规则内容"""
        ele = self.find_elements(*(self.rule_up_loc))[int(index)]
        checked_text = ele.get_attribute('class')
        if 'checked' not in checked_text:
            self.click_btn_index('升级规则', index, *(self.rule_up_loc))
            if int(index) != 5:
                self.input_text_index('升级规则内容', text, index, *(self.rule_input_loc))

    def click_up_sure(self):
        """点击升级确认"""
        self.click_button('确认', *(self.rule_upsure_loc))

    def click_down_sure(self):
        """点击降级确认"""
        self.click_button('确认', *(self.rule_downsure_loc))

    def click_cancle(self):
        """点击取消"""
        self.click_button('取消', *(self.rule_cancel_loc))

    def select_down(self, index):
        """选择升级规则"""
        ele = self.find_elements(*(self.rule_down_loc))[int(index)]
        checked_text = ele.get_attribute('class')
        if 'checked' not in checked_text:
            self.click_btn_index('降级规则', index, *(self.rule_down_loc))

    def input_money(self, money):
        """输入会员余额"""
        if str(money).upper() != '%NONE%':
            self.clear_input_text(*(self.rule_money_loc))
            self.input_text(money, '会员余额', *(self.rule_money_loc))

    def input_sizes(self, sizes, unit):
        """输入会员当前等级满"""
        if str(sizes).upper() != '%NONE%':
            self.clear_input_text(*self.rule_sizes_loc)
            self.input_text(sizes, '会员余额', *self.rule_sizes_loc)
            self.select_unit(unit)

    def select_unit(self, unit):
        """选择单位"""
        units = self.select_list(*(self.rule_unit_loc))
        if str(unit).upper() != '%NONE%':
            units.select_by_index(unit)

    def input_month_time(self, monthTime, monthMoney):
        """会员在当前等级每"""
        if str(monthTime).upper() != '%NONE%':
            self.clear_input_text(*(self.rule_monthTime_loc))
            self.clear_input_text(*(self.rule_monthMoney_loc))
            self.input_text(monthTime, '会员在当前等级每',
                            *(self.rule_monthTime_loc)
                            )
            self.input_text(monthMoney, '月累计消费未达到',
                            *(self.rule_monthMoney_loc)
                            )

    def input_month_money(self, monthMoney):
        """月累计消费未达到"""
        if str(monthMoney).upper() != '%NONE%':
            self.clear_input_text(*(self.rule_monthMoney_loc))
        self.input_text(monthMoney, '月累计消费未达到',
                        *(self.rule_monthMoney_loc)
                        )

    def input_recharge_time(self, rechargeTime, rechargeMoney):
        """输入会员在当前等级每"""
        if str(rechargeTime).upper() != '%NONE%':
            self.clear_input_text(*(self.rule_monthRechargeTime_loc))
            self.clear_input_text(*(self.rule_monthRechargeMoney_loc))
            self.input_text(rechargeTime, '会员在当前等级每',
                            *(self.rule_monthRechargeTime_loc)
                            )
            self.input_text(rechargeMoney, '月累计充值(实收+奖励)未达到',
                            *(self.rule_monthRechargeMoney_loc)
                            )

    def input_recharge_money(self, rechargeMoney):
        """输入月累计充值(实收+奖励)未达到"""
        if str(rechargeMoney).upper() != '%NONE%':
            self.clear_input_text(*(self.rule_monthRechargeMoney_loc))
        self.input_text(rechargeMoney, '月累计充值(实收+奖励)未达到',
                        *(self.rule_monthRechargeMoney_loc)
                        )


    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.rule_save_loc))

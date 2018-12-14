from selenium.webdriver.common.by import By
from base.basepage import BasePage

class MonitorSet(BasePage):
    """异常交易监控设置"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>
    #消费金额
    #单卡单笔消费金额超过
    monitor_amount_locs = (By.XPATH, "//input[@name='conSingle']/..")
    #单卡日累计消费金额超过
    monitor_total_loc = (By.XPATH, "//input[@name='conDay']/..")
    #单卡周累计消费金额超过
    monitor_week_loc = (By.XPATH, "//input[@name='conWeek']/..")

    #消费次数
    #单卡日累计消费次数超过
    monitor_daynum_loc = (By.XPATH, "//input[@name='conDayNum']/..")
    #单卡周累计消费次数超过
    monitor_wekknum_loc = (By.XPATH, "//input[@name='tmrConsumerCountWeek']/..")



    #消费时间
    monitor_time_locs = (By.XPATH, "//input[@name='conTime']/..")

    #充值金额
    #单卡单笔充值金额超过
    monitor_camount_locs = (By.XPATH, "//input[@name='chargeSingleAmount']/..")
    #单卡日累计充值金额
    monitor_chargetotal_loc = (By.XPATH, "//input[@name='chargeTotalAmount']/..")
    #单卡周累计充值金额超过
    monitor_weekamount_loc = (By.XPATH, "//input[@name='chargeAmountWeek']/..")


    #充值次数
    monitor_cnum_locs = (By.XPATH, "//input[@name='chargeCountNum']/..")
    monitor_weeknum_loc = (By.XPATH, "//input[@name='chargeCountWeekNum']/..")

    #充值时间
    monitor_ctime_locs = (By.XPATH, "//input[@name='chargeTime']/..")
    #保存
    monitor_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")

    #单卡单笔消费金额
    consume_single_loc = (By.NAME, "tmrConsumerAmount")
    # 单卡日累计充值金额超过
    consume_total_loc = (By.NAME, "tmrConsumerTotalAmount")
    #单卡周累计消费金额超过
    consume_amountweek_loc = (By.NAME, "tmrConsumerTotalAmountWeek")
    #单卡日累计消费次数超过
    consumt_count_loc = (By.NAME, "tmrConsumerCount")
    #单卡周累计消费次数超过
    consumt_countweek_loc = (By.NAME, "tmrConsumerCountWeek")
    #单卡单笔充值金额超过
    charge_amount_loc = (By.NAME, "tmrChargeAmount")
    #单卡日累计充值金额超过
    charge_total_loc = (By.NAME, "tmrChargeTotalAmount")
    #单卡周累计充值金额超过
    charge_amoutweek_loc = (By.NAME, "tmrChargeTotalAmountWeek")
    # 单卡日累计充值次数超过
    charge_count_loc = (By.NAME, "tmrChargeCount")
    #单卡周累计充值次数超过
    charge_countweek_loc = (By.NAME, "tmrChargeCountWeek")

    #单卡单笔消费金额超过
    select_csmamout_loc = (By.NAME, "tmrConsumerAmountLocked")
    #单卡日累计消费金额超过
    select_total_loc = (By.NAME, "tmrConsumerTotalAmountLocked")
    #单卡周累计消费金额超过
    select_amoutweek_loc = (By.NAME, "tmrConsumerTotalAmountWeekLocked")
    #单卡日累计消费次数超过
    select_count_loc = (By.NAME, "tmrConsumerCountLocked")
    #单卡周累计消费次数超过
    select_countweek_loc = (By.NAME, "tmrConsumerCountWeekLocked")
    #单卡单笔充值金额超过
    select_chgeamount_loc = (By.NAME, "tmrChargeAmountLocked")
    #单卡日累计充值金额超过
    select_chgetotal_loc = (By.NAME, "tmrChargeTotalAmountLocked")
    #单卡周累计充值金额超过
    select_chgeweektotal_loc = (By.NAME, "tmrChargeTotalAmountWeekLocked")
    #单卡日累计充值次数超过
    select_chgecount_loc = (By.NAME, "tmrChargeCountLocked")
    #单卡周累计充值次数超过
    select_chgeweekcount_loc = (By.NAME, "tmrChargeCountWeekLocked")

    #断言，保存成功
    assert_success_loc = (By.XPATH, "//*[contains(text(),'保存成功')]")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>
    def _click_check_box(self, *loc, **kwargs):
        """复选框选择，如果iselect为True最终状态则要选择中复选框"""
        if not 'iselect' in kwargs:
            kwargs['iselect'] = True

        pro = self.get_element_attribute('class', *loc)
        print(pro)
        if ((not 'checked' in pro) and kwargs['iselect']) or \
                (('checked' in pro) and not kwargs['iselect']):
            self.click_button(
                kwargs['desc'],
                *loc
            )


    def _set_option(self, **kwargs):
        """消费金额－单卡单笔消费金额超过"""
        self._click_check_box(
            *(kwargs['checkbox_loc']),
            iselect=kwargs['iselect'],
            desc=kwargs['desc'],
        )
        if kwargs['iselect']:
            #"""单卡单笔消费金额超过"""
            self.clear_input_text(*(kwargs['input_loc']))
            self.input_text(
                kwargs['amount'],
                kwargs['desc'],
                *(kwargs['input_loc'])
            )
            #"""单卡单笔消费金额超过-是否锁定"""
            select = self.select_list(*(kwargs['select_loc']))
            select.select_by_index(int(kwargs['select_index']))


    def select_consume_single(self, amount, select_index=0, bool=True):
        """单卡单笔消费金额"""
        self._set_option(
            checkbox_loc=self.monitor_amount_locs,
            iselect=bool,
            desc='消费金额-单卡单笔消费金额超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.consume_single_loc,
            select_loc=self.select_csmamout_loc
        )


    def select_consume_total(self, amount, select_index=0, bool=True):
        """单卡单笔消费金额"""
        self._set_option(
            checkbox_loc=self.monitor_total_loc,
            iselect=bool,
            desc='消费金额-单卡日累计消费金额超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.consume_total_loc,
            select_loc=self.select_total_loc
        )

    def select_consume_week(self, amount, select_index=0, bool=True):
        """单卡单笔消费金额"""
        self._set_option(
            checkbox_loc=self.monitor_week_loc,
            iselect=bool,
            desc='消费金额-单卡日累计消费金额超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.consume_amountweek_loc,
            select_loc=self.select_amoutweek_loc
        )

    def select_consume_num(self, amount, select_index=0, bool=True):
        """单卡日累计消费次数超过"""
        self._set_option(
            checkbox_loc=self.monitor_daynum_loc,
            iselect=bool,
            desc='消费金额-单卡日累计消费次数超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.consumt_count_loc,
            select_loc=self.select_count_loc
        )

    def select_consume_weeknum(self, amount, select_index=0, bool=True):
        """单卡日累计消费次数超过"""
        self._set_option(
            checkbox_loc=self.monitor_wekknum_loc,
            iselect=bool,
            desc='消费金额-单卡日累计消费次数超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.consumt_countweek_loc,
            select_loc=self.select_countweek_loc
        )

    def select_charge_amount(self, amount, select_index=0, bool=True):
        """单卡日累计消费次数超过"""
        self._set_option(
            checkbox_loc=self.monitor_camount_locs,
            iselect=bool,
            desc='消费金额-单卡日累计消费次数超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.charge_amount_loc,
            select_loc=self.select_chgeamount_loc
        )


    def select_charge_total(self, amount, select_index=0, bool=True):
        """单卡日累计充值金额超过"""
        self._set_option(
            checkbox_loc=self.monitor_chargetotal_loc,
            iselect=bool,
            desc='消费金额-单卡日累计充值金额超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.charge_total_loc,
            select_loc=self.select_chgetotal_loc
        )

    def select_charge_weektotal(self, amount, select_index=0, bool=True):
        """单卡周累计充值金额超过"""
        self._set_option(
            checkbox_loc=self.monitor_weekamount_loc,
            iselect=bool,
            desc='消费金额-单卡周累计充值金额超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.charge_amoutweek_loc,
            select_loc=self.select_chgeweektotal_loc
        )

    def select_charge_count(self, amount, select_index=0, bool=True):
        """单卡日累计充值次数超过"""
        self._set_option(
            checkbox_loc=self.monitor_cnum_locs,
            iselect=bool,
            desc='消费金额-单卡日累计充值次数超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.charge_count_loc,
            select_loc=self.select_chgecount_loc
        )


    def select_charge_weekcount(self, amount, select_index=0, bool=True):
        """单卡周累计充值次数超过"""
        self._set_option(
            checkbox_loc=self.monitor_weeknum_loc,
            iselect=bool,
            desc='消费金额-单卡周累计充值次数超过',
            amount=amount,
            select_index=select_index,
            input_loc=self.charge_countweek_loc,
            select_loc=self.select_chgeweekcount_loc
        )

    def click_save_button(self):
        """保存"""
        self.click_button(
            '保存',
            *(self.monitor_save_loc)
        )

    def assert_success_bool(self):
        """断言保存成功字样，在页面展示"""
        txt = self.get_tag_text('text', *(self.assert_success_loc))
        if not '保存成功' in txt:
            return False
        return True
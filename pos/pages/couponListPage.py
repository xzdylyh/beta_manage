#_*_coding=utf8_*_
"""
create:2018/10/24
by: ts
"""
from selenium.webdriver.common.by import By
from pos.base.basepage import BasePage


class CouponList(BasePage):
    """此类用于封装券管理页元素，操作"""
    # ----------------元素定位器-----以下---------------------
    # 券管理链接
    coupon_list_loc = (By.LINK_TEXT, "券管理")
    # 创建新的券
    coupon_Create_loc = (By.ID, "dropdownCoupon")
    # 下拉选择增加券类型(代金券，礼品券，等等；li[1]为下拉第一个元素 代金券)
    coupon_select_type = ["代金券", "礼品券", "券包"]
    # 输入券面值
    coupon_InputValue_loc = (By.ID, "inputValue")
    # 输入券名称
    coupon_inputName_loc = (By.ID, "inputName")
    # 属性 -0普通; 1微信群发消息专用
    coupon_radio_xpath = (By.XPATH, "//input[@name='messageonly']/..")
    # 客户端展示券名称；0显示；1不显示
    coupon_viewName_loc = (By.XPATH, "//input[@name='showname']/..")


    # 消费总金额
    coupon_minvalue_loc = (By.ID, "minvalue")
    # 消费总金额每满
    coupon_minvalue1_loc = (By.ID, "minvalue1")
    # 每次消费最多可使用
    coupon_sheets_loc = (By.ID, "sheets")

    # 与其他券混用：0可以，1不可以，2部分可以
    coupon_mix_loc = (By.XPATH, "//input[@name='mix']/..")
    # 转赠好友0可以； 1不可以
    coupon_givefriend_loc = (By.XPATH, "//input[@name='givefriend']/..")


    # 启用时间，输入为天
    coupon_time_loc = (By.NAME, "enabled")
    # 自券发出之日起
    coupon_inputTerm_loc = (By.ID, "inputTerm")
    # 使用固定日期链接button
    coupon_inputTermBtn_loc = (By.XPATH, "//input[@id=inputTerm]/../button")
    #开始日期
    coupon_inputDateStart_loc = (By.ID, "inputDateStart")
    # 结束日期
    coupon_inputDateEnd_loc = (By.ID, "inputDateEnd")
    # 时间段设置
    coupon_clicksEattime_loc = (By.XPATH, "//input[@name='eattime[]'/..]")

    # 适用门店; 更改链接
    coupon_changeShop_loc = (By.LINK_TEXT, "更改")
    # 门店搜索
    coupon_searchShop_loc = (By.ID, "search")
    # 门店选择页面，确定按钮
    coupon_button_loc = (By.LINK_TEXT, "确定")

    # 扩展ID输入框
    coupon_extend_loc = (By.ID, "inputExtend")
    # 限制与说明文本域
    coupon_area_loc = (By.NAME, "restriction")

    # 保存按钮，根据返回查找
    coupon_save_loc = (By.XPATH, "//button[contains(text(), '保存')]")

    # 确认按钮
    coupon_confirm_loc = (By.XPATH, "//button[contains(text(), '确认')]")


    coupon_assert_loc = (By.CSS_SELECTOR, "div.voucher-box>p>b:nth-child(1)")

    ########################操作########################################
    def clickCouponManage_Link(self):
        """单击券管理链接，进入创建券页面"""
        self.clickBtn('券管理链接', *(self.coupon_list_loc))

    def clickCouponCreate_Btn(self):
        """单击创建新的券"""
        self.clickBtn('创建新的券', *(self.coupon_Create_loc))


    def clickCouponType(self, index):
        """单击选择券类型"""
        self.clickBtn(
            self.coupon_select_type[index],
            *(By.LINK_TEXT, self.coupon_select_type[index])
        )

    def clickCouponPro(self, index):
        """选择券属性0普通；1微信群发消息专用"""
        self.clickBtnIndex('属性', index, *(self.coupon_radio_xpath))


    def inputCouponValue(self, value):
        """输入券面值 元"""
        self.inputText(value, '面值', *(self.coupon_InputValue_loc))


    def inputCouponName(self, name, op=None):
        """输入名称"""
        if op == 1:
            self.clear_input_text(*(self.coupon_inputName_loc))
        self.inputText(name, '名称', *(self.coupon_inputName_loc))

    def inputCouponMinValue(self, value):
        """输入 消费总金额 满"""
        self.clickBtn(
            '设置焦点为消费总金额输入框',
            *(self.coupon_minvalue_loc)
        )
        self.inputText(
            value,
            '消费总金额满多少元不可用',
            *(self.coupon_minvalue_loc)
        )

    def inputCouponMinValue1(self, value):
        """输入 消费总金额每满 xxx元可用1张"""
        self.clickBtn(
            '消费总金额每满xx元可用1张,输入框焦点',
            *(self.coupon_minvalue1_loc)
        )
        self.inputText(
            value,
            '消费总金额每满多少元可用1张',
            *(self.coupon_minvalue1_loc)
        )

    def inputCouponSheets(self, value):
        """每次消费最多可使用券数量"""
        self.inputText(
            value,
            '每次消费最多可使用几张',
            *(self.coupon_sheets_loc)
        )

    def clickCouponMix(self, index):
        """与其它券混合使用；0可以；1不可以；2部分不可以"""
        self.clickBtnIndex('与其它券混合使用', index, *(self.coupon_mix_loc))


    def clickCouponShowName(self, index):
        """客户端展示券名称"""
        self.clickBtnIndex('客户端显示券名称', index, *(self.coupon_viewName_loc))


    def clickCouponGiveFriend(self, index):
        """转赠好友是否可以"""
        self.clickBtnIndex(
            '转赠好友',
            index,
            *(self.coupon_givefriend_loc)
        )

    def inputCouponEnabledTime(self, text):
        """输入券启用时间"""
        self.inputText(
            text,
            '启用时间',
            *(self.coupon_time_loc)
        )


    def _inputCouponTerm(self, text):
        """券有效期"""
        self.inputText(
            text,
            '有效期－相对日期',
            *(self.coupon_inputTerm_loc)
        )

    def _inputCouponT(self, text):
        """有效期－固定日期"""
        self.clickBtn('使用固定有效期', *(self.coupon_inputTermBtn_loc))
        self.clear_input_text(*(self.coupon_inputDateStart_loc))
        self.inputText(text, '开始日期', *(self.coupon_inputDateStart_loc))
        self.clear_input_text(*(self.coupon_inputDateEnd_loc))
        self.inputText(text, '结束日期', *(self.coupon_inputDateEnd_loc))


    def inputCouponTerm(self, op=0, **kwargs):
        """有效期"""

        if op == 0: #相对日期，默认为相对日期
            self.clear_input_text(*(self.coupon_inputTerm_loc))
            self.inputText(
                kwargs['text'],
                '相对日期',
                *(self.coupon_inputTerm_loc)
            )
        if op == 1:
            self.clear_input_text(*(self.coupon_inputDateStart_loc))
            self.clickBtn(
                '使用固定有效期',
                *(self.coupon_inputTermBtn_loc)
            )
            self.inputText(
                kwargs['startDate'],
                '开始日期',
                *(self.coupon_inputDateStart_loc)
            )
            self.clear_input_text(*(self.coupon_inputDateEnd_loc))
            self.inputText(
                kwargs['endDate'],
                '结束日期',
                *(self.coupon_inputDateEnd_loc)
            )


    def clickCouponEatTime(self, index):
        """时间段设置，复选框"""
        self.clickBtnIndex(
            '时间段设置',
            index,
            *(self.coupon_clicksEattime_loc)
        )


    def inputCouponArea(self, text):
        """输入限制与说明"""
        self.inputText(
            text,
            '限制与说明',
            *(self.coupon_area_loc)
        )


    def clickCouponSave(self):
        """保存，提交券信息"""
        self.clickBtn('保存', *(self.coupon_save_loc))

    def clickCouponConfirm(self):
        """提交后，确认按钮"""
        self.clickBtn('确认', *(self.coupon_confirm_loc))

    def getCouponNum(self):
        """获取券数量"""
        couponNum = self.get_tag_text('text', *(self.coupon_assert_loc))
        print('当前券数量为:{}'.format(couponNum))
        return couponNum


    def assertAddCoupon(self, oldNum, newNum):
        """断言新建券是否成功，通过增加券后，数量是否变化来判断"""
        oldNum = int(oldNum)
        newNum = int(newNum)
        if newNum - 1 == oldNum:
            print('新增加券成功,当前总数为:{}'.format(newNum))
        else:
            print('新增加券失败,当前总数为:{}'.format(oldNum))
            return False
        self.get_image
        return True


if __name__ == "__main__":
    pass

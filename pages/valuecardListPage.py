
"""
create:2018/11/22
by:ts
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.basepage import BasePage


class ValueCardList(BasePage):
    """封装储值卡页面的元素、操作"""
    # 功能状态
    valuecard_control_loc = (By.XPATH, "//input[@name='state']/..")
    # 创建储值卡按钮
    valuecard_create_loc = (By.LINK_TEXT, '创建储值卡')
    # 卡号密码下载链接
    valuecard_number_loc = (By.LINK_TEXT, '卡号密码下载')
    # 储值卡名称
    valuecard_name_loc = (By.ID, 'inputName')
    # 面额（元）
    valuecard_denomination_loc = (By.ID, 'inputDenomination')
    # 售价（元）
    valuecard_price_loc = (By.ID, 'inputPrice')
    # 总量
    valuecard_total_loc = (By.ID, 'inputTotal')
    # 有效期选择按钮
    valuecard_prepaid_term_loc = (By.XPATH, "//input[@name='term']/..")
    # 自售出之日起多少天有效-输入框
    valuecard_prepaid_term_count_loc = (By.NAME, 'termCount')
    # 保存按钮
    valuecard_save_loc = (By.XPATH, "//button[@type='submit']")
    # 返回按钮
    valuecard_return_loc = (By.XPATH, "//[contains(text(),'返回')]")
    # 创建成功后显示的储值卡名称
    valuecard_success_name_loc = (By.CSS_SELECTOR,
                                  " table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2)")

    def select_control(self, index):
        """功能状态：index=0，开启；index=1，关闭"""
        self.click_btn_index('功能状态', index, *(self.valuecard_control_loc))

    def click_cardCreateBtn(self):
        """点击创建储值卡按钮"""
        self.click_button('创建储值卡', *(self.valuecard_create_loc))

    def get_loadText(self):
        """获取卡号密码下载文本"""
        self.get_tag_text('卡号密码下载', *(self.valuecard_number_loc))

    def input_name(self, text):
        """输入储值卡名称"""
        self.input_text(text, '储值卡名称', *(self.valuecard_name_loc))

    def input_denomination(self, text):
        """输入面额"""
        self.input_text(text, '面额', *(self.valuecard_denomination_loc))

    def input_price(self, text):
        """输入售价"""
        self.input_text(text, '售价', *(self.valuecard_price_loc))

    def input_total(self, text):
        """输入总量"""
        self.input_text(text, '总量', *(self.valuecard_total_loc))

    def select_prepaid_term(self, index):
        """有效期选择，index=0,永久有效；index=1,一段时间后有效"""
        self.click_btn_index('有效期', index, *(self.valuecard_prepaid_term_loc))

    def input_prepaidTermCount(self, text):
        """输入天数"""
        self.input_text(text, '天数', *(self.valuecard_prepaid_term_count_loc))

    def clickSaveBtn(self):
        """点击保存按钮"""
        self.click_button('保存', *(self.valuecard_save_loc))

    def clickRturnBtn(self):
        """点击返回按钮"""
        self.click_button('返回', *(self.valuecard_return_loc))

    def get_successNameText(self):
        """获取创建成功，页面中显示储值卡的名称"""
        name = self.get_tag_text('text', *(self.valuecard_success_name_loc))
        print("储值卡名称为：{}".format(name))
        self.get_image
        return name








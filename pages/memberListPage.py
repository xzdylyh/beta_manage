from selenium.webdriver.common.by import By
from base.basepage import BasePage

class MemberList(BasePage):
    """会员资料修改"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>.
    #输入会员手机号或卡号
    member_input_loc = (By.ID, "inputMemberId")
    #查询按钮
    member_search_loc = (By.XPATH, "//button[contains(text(),'查询')]")
    #修改资料
    member_change_loc = (By.LINK_TEXT, "修改资料")
    #卡名
    member_name_loc = (By.NAME, "cardName")
    #性别 0;男；1女
    member_sex_locs = (By.XPATH, "//input[@name='cardSex']/..")
    #会员等级 select
    member_level_loc = (By.ID, "cardVIPLevel")
    #0公历，1农历
    member_cale_locs = (By.XPATH, "//input[@name='cardCalendar']/..")
    #生日2018-12-26
    member_birthday_loc = (By.ID, "cardBirthday")
    #确认
    member_confirm_loc = (
        By.CSS_SELECTOR,
        "div.modal.fade.we-modal.edit-actual-modal.in > div > div > div.modal-footer > button.btn.btn-primary.we-btn")
    #断言
    assert_text_loc = (
        By.CSS_SELECTOR,"body > div.main > div > div.main-content > div.mainbody.member-home > div > div.panel-body > div:nth-child(4) > div.section-body > div:nth-child(1) > div > dl:nth-child(1) > dd:nth-child(4)")
    #<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>.
    def input_card_no(self, text):
        """卡号"""
        self.input_text(
            text,
            '卡号',
            *(self.member_input_loc)
        )

    def click_serarch_button(self):
        """单击查询按钮"""
        self.click_button('查询', *(self.member_search_loc))

    def click_change_button(self):
        """修改资料"""
        self.click_button(
            '修改资料',
            *(self.member_change_loc)
        )

    def input_card_name(self, text):
        """输入卡名"""
        self.clear_input_text(*(self.member_name_loc))
        self.input_text(
            text,
            '卡名',
            *(self.member_name_loc)
        )

    def click_sex_button(self, index):
        """性别"""
        self.click_btn_index(
            '性别',
            index,
            *(self.member_sex_locs)
        )

    def select_member_level(self, index):
        """会员等级"""
        select = self.select_list(*(self.member_level_loc))
        select.select_by_index(index)

    def click_date_type(self, index):
        """选择公历还是农历"""
        self.click_btn_index(
            '日期类型',
            index,
            *(self.member_cale_locs)
        )

    def input_birthday_text(self, text):
        """生日"""
        self.clear_input_text(*(self.member_birthday_loc))
        self.input_text(
            text,
            '生日',
            *(self.member_birthday_loc)
        )
    def click_confirm_button(self):
        """确认"""
        self.click_button(
            '确认',
            *(self.member_confirm_loc)
        )

    def assert_success_text(self, index):
        """断言生日公历；农力是否修改成功"""
        birthday = self.get_tag_text('text',*(self.assert_text_loc))

        birth_type = None
        if index ==0:
            birth_type = '公历'
        if index ==1:
            birth_type = '农历'

        if not birth_type in birthday:
            return False
        return True
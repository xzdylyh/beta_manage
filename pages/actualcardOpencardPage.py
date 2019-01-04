from selenium.webdriver.common.by import By
from base.basepage import BasePage

class ActualCardOpen(BasePage):
    """实体卡开卡"""
    ##################################定位###############################
    #实体卡号
    card_no_loc = (By.ID, "inputActualNo")
    #手机号
    card_phone_loc = (By.ID, "inputMobile")
    #姓名
    card_name_loc = (By.ID, "inputName")
    #性别
    card_sex_locs = (By.XPATH, "//input[@name='gender']/..")
    #生日，公历，农历
    card_birth_locs = (By.XPATH, "//input[@name='birthFlag']/..")
    #生日，日期2018-09-08
    card_birthdate_locs = (By.ID, "inputBirthday")
    #确认开卡
    card_confirm_loc = (By.XPATH, "//button[contains(text(),'确认开卡')]")
    #断言
    assert_success_loc = (By.CSS_SELECTOR, "body > div.we-msg.fade > span")
    ##################################操作###############################
    def input_card_no(self, text):
        """实体卡卡号"""
        self.input_text(
            text,
            '实体卡号',
            *(self.card_no_loc)
        )

    def input_mobile_text(self, text):
        """手机号"""
        self.input_text(
            text,
            '手机号',
            *(self.card_phone_loc)
        )

    def input_name_text(self, text):
        """姓名"""
        self.input_text(
            text,
            '姓名',
            *(self.card_name_loc)
        )

    def click_sex_button(self, index):
        """性别"""
        self.click_btn_index(
            '性别',
            index,
            *(self.card_sex_locs)
        )

    def click_birth_button(self, index):
        """生日，公历，农历"""
        self.click_btn_index(
            '公历，农历',
            index,
            *(self.card_birth_locs)
        )

    def input_birth_text(self, text):
        """生日"""
        self.clear_input_text(*(self.card_birthdate_locs))
        self.input_text(
            text,
            '生日',
            *(self.card_birthdate_locs)
        )

    def click_confirm_open(self):
        """确认开卡"""
        self.click_button(
            '确认开卡',
            *(self.card_confirm_loc)
        )

    def assert_success(self, text):
        """断言成功"""
        txt = self.get_tag_text('text', *(self.assert_success_loc))
        if str(txt).strip() != str(text).strip():
            return False
        return True
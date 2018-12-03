from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64

class ActivityCreate256(ActivityCreate64):
    """给生日会员赠券"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

    #终止
    activity_stop_loc = (By.LINK_TEXT, "终止")
    #终止确认
    activity_confirm_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_stop_button(self):
        """终止"""
        self.click_button(
            '终止',
            *(self.activity_stop_loc)
        )

    def click_stop_confirm(self, index):
        """确认"""
        self.click_btn_index(
            '确认',
            index,
            *(self.activity_confirm_loc)
        )
        self.wait(5000)


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
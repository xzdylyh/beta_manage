from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64

class ActiviteCreate1030(ActivityCreate64):
    """积分排行"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>
    #活动描述
    activity_desc_loc = (By.XPATH, "//*[@name='ruleSummary']/../div[1]")
    #活动说明
    activity_summary_loc = (By.XPATH, "//*[@name='summary']/../div[1]")
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
    #<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>
    def input_activity_desc(self, text):
        """活动描述"""
        self.input_text(
            text,
            '活动描述',
            *(self.activity_desc_loc)
        )

    def input_activity_summary(self, text):
        """活动说明"""
        self.clear_input_text(*(self.activity_summary_loc))
        self.input_text(
            text,
            '活动说明',
            *(self.activity_summary_loc)
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
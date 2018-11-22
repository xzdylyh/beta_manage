from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64


class ActivityCreate128(ActivityCreate64):
    """填资料赠券"""
    #>>>>>>>>>>>>>>>>>>>>>>>>>>定位<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    activity_desc_loc = (By.XPATH, "//*[@name='summary']/../div")
    assert_AName_loc = (
        By.CSS_SELECTOR,
        "div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > span"
    )
    #状态－执行中
    assert_exec_loc = (
        By.CSS_SELECTOR,
        "div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td.success"
    )
    #状态－已终止
    assert_ystop_loc = (
        By.CSS_SELECTOR,
        "div.we-table-responsive > table:nth-child(1) > tbody > tr:nth-child(1) > td.muted"
    )
    #终止
    activity_stop_loc = (By.LINK_TEXT, "终止")
    #终止确认
    activity_sbutton_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    #>>>>>>>>>>>>>>>>>>>>>>>>>>操作<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def input_activity_desc(self, text):
        """输入活动说明"""
        self.input_text(
            text,
            '活动说明',
            *(self.activity_desc_loc)
        )

    def click_stop_button(self):
        """终止操作"""
        self.click_button(
            '终止',
            *(self.activity_stop_loc)
        )

    def click_cstop_button(self, index):
        """终止确认"""
        self.click_btn_index(
            '确认',
            index,
            *(self.activity_sbutton_loc)
        )

    def assert_success(self, text, status):
        """断言增加成功;列表中，标题与状态"""
        aname = str(self.get_tag_text(
            'text',
            *(self.assert_AName_loc)
        )).strip()

        if status == '执行中':
            status_loc = self.assert_exec_loc
        if status == '已终止':
            status_loc = self.assert_ystop_loc
        astatus = str(self.get_tag_text(
            'text',
            *(status_loc)
        )).strip()
        self.get_image
        if not (aname == text and astatus == status):
            return False
        return True

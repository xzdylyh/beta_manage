from selenium.webdriver.common.by import By
from pages.activityCreate64Page import ActivityCreate64

class ActivityCreate1024(ActivityCreate64):
    """累计消费返券"""
    #<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>
    #赠券设置
    reach_type_loc = (By.NAME, "reachType")
    #每满xx元
    reach_rmb_loc = (By.ID, "inputCondition")
    #活动说明
    activity_desc_loc = (By.ID, "inputRestriction")
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
    #<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>
    def select_list_index(self, index):
        """赠券设置－累计消费；0金额；1次数"""
        st = self.select_list(
            *(self.reach_type_loc)
        )
        st.select_by_index(index)

    def input_amount_rmb(self, text):
        """输入金额"""
        self.input_text(
            text,
            '金额',
            *(self.reach_rmb_loc)
        )

    def input_activity_desc(self, text):
        """输入活动说明"""
        self.input_text(
            text,
            '活动说明',
            *(self.activity_desc_loc)
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
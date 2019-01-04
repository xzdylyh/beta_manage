from selenium.webdriver.common.by import By
from base.basepage import BasePage


class RechargeDetailPage(BasePage):
    """封装财务报表-充值页面元素、操作"""
    # 财务报表
    rech_finance_loc = (By.LINK_TEXT, '财务报表')
    # 充值
    rech_recharge_loc = (By.LINK_TEXT, '充值')
    # 备注
    rech_noteth_loc = (By.XPATH,
                       "//div[@class='we-table-responsive scroll-height']"
                       "/table[1]//tr[1]/td[18]")

    def click_finance(self):
        """点击财务报表"""
        self.click_button('财务报表', *(self.rech_finance_loc))

    def click_recharge(self):
        """点击充值"""
        self.click_button('充值', *(self.rech_recharge_loc))

    def get_noteth(self):
        """获取备注名称"""
        noteth = self.get_tag_text('text',
                                   *(self.rech_noteth_loc)
                                   )
        self.get_image
        return noteth

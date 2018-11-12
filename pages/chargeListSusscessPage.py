

from selenium.webdriver.common.by import By
from base.basepage import BasePage


class chargeListSusscess(BasePage):
    """储值成功页面，验证储值成功与返回其他界面，简单的操作，不需要数据表"""

    # 界面‘保存成功’文本
    charge_sucessText_loc = (By.CSS_SELECTOR, 'div.panel-body>div>h4')
    # 保存成功‘返回’按钮
    charge_backBtn_loc = (By.LINK_TEXT, '返回')

    def getScuessText(self):
        """获取保存成功提示"""
        success_test = self.get_tag_text('text',
                                         *(self.charge_sucessText_loc)
                                         )
        self.get_image
        return success_test

    def clickBcakBtn(self):
        """"点击返回按钮"""
        self.click_button('返回', *(self.charge_backBtn_loc))

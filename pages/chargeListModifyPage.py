

from selenium.webdriver.common.by import By
from base.basepage import BasePage

class chargeListModify(BasePage):
    """储值规则修改页面，封装了修改，删除操作"""
    # 修改规则
    charge_modBtn_loc = (By.LINK_TEXT, '修改')
    # 删除规则
    charge_delBtn_loc = (By.LINK_TEXT, '删除')
    # 删除确定按钮
    charge_okBtn_loc = (By.XPATH,
                        ".//*[starts-with(@id,'popover')]/div[2]/div[2]/button[1]")
    # 删除成功后文本提示信息
    charge_delSussecc_loc = (By.XPATH, "//a[@href='/charge/edit?type=shop']")

    def clickModBtn(self):
        """点击修改按钮"""
        self.click_button('修改', *(self.charge_modBtn_loc))

    def clickDelBtn(self):
        """点击删除按钮"""
        self.click_button('删除', *(self.charge_delBtn_loc))

    def clickOkBtn(self):
        """点击删除确定按钮"""
        self.click_button('确定', *(self.charge_okBtn_loc))

    def getDelInfo(self):
        """获取删除成功后的信息"""
        info = self.get_tag_text('text', *(self.charge_delSussecc_loc))
        self.get_image
        return info
    def click_btb(self):
        '''点击 添加门店储值规则'''
        self.click_button('添加门店储值规则', *(self.charge_delSussecc_loc))

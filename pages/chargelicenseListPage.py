

from selenium.webdriver.common.by import By
from base.basepage import BasePage


class ChargeLicenseList(BasePage):
    """储值授信"""
    # <<<<<<<<<<<<<元素定位>>>>>>>>>>>>>>>>>>>>>>>
    # 修改按钮
    charge_editinkBtn_loc = (By.LINK_TEXT, "修改")
    # 解除授信链接
    charge_licenseRemoveLink_loc = (By.LINK_TEXT, '解除授信')
    # 开启授信链接
    charge_licenseOpenLink_loc = (By.LINK_TEXT, '开启授信')
    # 授信记录链接
    charge_licenseLogLink_loc = (By.LINK_TEXT, '授信记录')
    # 授信额度选项，0：增加；1：减少
    charge_creditLimitRadio_loc = (By.XPATH, "//input[@name='increase']/..")
    # 增加多少元
    charge_increaseText_loc = (By.NAME, 'increaseNum')
    # 减少多少元
    charge_decreaseText_loc = (By.NAME, 'decreaseNum')
    # 预警额度
    charge_warningLimitText_loc = (By.ID, 'warningLimit')
    # 预警通知：手机号
    charge_phoneNumText_loc = (By.ID, 'inputPhone0')
    # 保存
    charge_submitBtn_loc = (By.XPATH, "//button[@type='submit']")
    # 返回
    charge_returnBtn_loc = (By.LINK_TEXT, '返回')
    # 确认‘解除’按钮
    charge_licenseRemoveBtn_loc = (By.XPATH,
                                   "//button[@data-toggle='license.confirmremove']"
                                   )
    # 授信开启’开启‘按钮
    charge_licenseOpenBtn_loc = (By.XPATH,
                                 "//button[@data-toggle='license.confirmopen']"
                                 )
    # 确认‘取消‘按钮
    charge_dismissBtn_loc = (By.XPATH, "//button[@data-dismiss='modal']")
    # 累计授权额度
    charge_total_loc = (By.XPATH, ".//*[@id='tableSummary']/table/tbody/tr/td[6]")

    # <<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def get_totalText(self):
        """获取累计授权额度"""
        total = self.get_tag_text('text', *(self.charge_total_loc))
        print("累计授权额度: {}".format(total))
        return total

    def click_eidit_btn(self):
        """点击修改按钮"""
        self.click_button('修改', *(self.charge_editinkBtn_loc))

    def remove_license(self):
        """解除授信"""
        self.click_button('解除授信', *(self.charge_licenseRemoveLink_loc))
        self.click_button('解除', *(self.charge_licenseRemoveBtn_loc))

    def open_license(self):
        """开启授信"""
        self.click_button('开启授信', *(self.charge_licenseOpenLink_loc))
        self.click_button('开启', *(self.charge_licenseOpenBtn_loc))

    def click_licenseLog(self):
        """点击授信记录按钮"""
        self.click_button('授信记录', *(self.charge_licenseLogLink_loc))

    def select_creditLimit(self, index):
        """选择授信额度，0：增加；1：减少"""
        self.click_btn_index("授信额度", index,
                             *(self.charge_creditLimitRadio_loc)
                             )

    def input_increase(self, text):
        """输入增加  元"""
        self.input_text(text, "增加额度", *(self.charge_increaseText_loc))

    def input_decrease(self, text):
        """输入减少  元"""
        self.input_text(text, "减少额度", *(self.charge_decreaseText_loc))

    def input_warningLimit(self, text):
        """输入预警额度"""
        self.clear_input_text(*(self.charge_warningLimitText_loc))
        self.input_text(text, "预警额度", *(self.charge_warningLimitText_loc))

    def input_phone(self, phonenum):
        """输入手机号"""
        self.input_text(phonenum, "手机号", *(self.charge_phoneNumText_loc))

    def click_submit(self):
        """点击保存按钮"""
        self.click_button('保存', *(self.charge_submitBtn_loc))

    def click_return(self):
        """点击返回按钮"""
        self.click_button('返回', *(self.charge_returnBtn_loc))

    def assertEditCreditLimitTrue(self, old_num, modify_num, new_num):
        """判断修改额度是否成功，通过比较修改前后额度值判断"""
        old_num = int(float(old_num))
        modify_num = int(modify_num)
        new_num = int(float(new_num))
        if old_num + modify_num == new_num:
            print("授信额度修改成功，当前额度为：{}".format(new_num))
        elif old_num - modify_num == new_num:
            print("授信额度修改成功，当前额度为：{}".format(new_num))
        else:
            print("授信额度修改失败，当前额度为：{}".format(old_num))
            return False
        self.get_image
        return True

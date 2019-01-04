from selenium.webdriver.common.by import By
from base.basepage import BasePage


class ListCompaniesPage(BasePage):
    """封装集团消费页面元素、操作"""

    # <<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>
    # 添加集团
    comp_groupcreate_loc = (By.LINK_TEXT, '添加集团')
    # 集团名称
    comp_inputName_loc = (By.ID, 'inputName')
    # 挂帐额度
    comp_overdraft_loc = (By.ID, 'inputNumber')
    # 联系人姓名
    comp_contacts_loc = (By.NAME, 'contacts')
    # 手机号
    comp_mobile_loc = (By.ID, 'inputPhone')
    # 备注
    comp_desc_loc = (By.XPATH,
                     "//div[@class='form-input']/div[5]/div/div"
                     )
    # 下一步
    comp_next_loc = (By.XPATH, "//button[contains(text(),'下一步')]")
    # 保存
    comp_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 集团名称-首页
    comp_inputGroupper_loc = (By.ID, 'inputGroupper')
    # 手机号-首页
    comp_inputTel_loc = (By.ID, 'inputTel')
    # 查询
    comp_seach_loc = (By.XPATH, "//button[contains(text(),'查询')]")
    # 列表中的集团名称
    comp_findName_loc = (By.XPATH,
                         "//div[@id='tableOpencard']//td[1]")

    # <<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>
    def input_groupper_name(self, groupper):
        """输入首页集团名称"""
        self.clear_input_text(*self.comp_inputGroupper_loc)
        self.input_text(groupper, '首页集团名称',
                        *self.comp_inputGroupper_loc
                        )

    def input_tel(self, tel):
        """输入首页集团手机号"""
        self.clear_input_text(*self.comp_inputTel_loc)
        self.input_text(tel, '首页集团手机号',
                        *self.comp_inputTel_loc
                        )

    def click_groupcreate(self):
        """点击添加集团"""
        self.click_button('集团', *(self.comp_groupcreate_loc))

    def input_merber_name(self, merbername):
        """输入集团名称"""
        self.clear_input_text(*self.comp_inputName_loc)
        self.input_text(merbername, '集团名称',
                        *self.comp_inputName_loc
                        )

    def input_overdraft(self, overdraft):
        """输入挂帐额度"""
        self.clear_input_text(*self.comp_overdraft_loc)
        self.input_text(overdraft, '挂帐额度',
                        *self.comp_overdraft_loc
                        )

    def input_contacts(self, contacts):
        """输入联系人姓名"""
        self.clear_input_text(*self.comp_contacts_loc)
        self.input_text(contacts, '联系人姓名',
                        *self.comp_contacts_loc
                        )

    def input_phone(self, phone):
        """输入手机号"""
        self.clear_input_text(*self.comp_mobile_loc)
        self.input_text(phone, '手机号',
                        *self.comp_mobile_loc
                        )

    def input_desc(self, desc):
        """输入备注"""
        self.clear_input_text(*self.comp_desc_loc)
        self.input_text(desc, '备注',
                        *self.comp_desc_loc
                        )

    def click_search(self):
        """点击查询"""
        self.click_button('查询', *(self.comp_seach_loc))

    def click_next(self):
        """点击下一步"""
        self.click_button('下一步', *(self.comp_next_loc))

    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.comp_save_loc))

    def get_group_name(self):
        name = self.get_tag_text('text',
                                 *(self.comp_findName_loc)
                                 )
        self.get_image
        return name

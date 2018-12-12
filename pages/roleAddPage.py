from selenium.webdriver.common.by import By
from base.basepage import BasePage

class RoleAdd(BasePage):
    """权限与角色-创建角色"""
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #角色名称
    role_name_loc = (By.NAME, "roleName")
    #备注
    role_remark_loc = (By.NAME, "remarks")
    #选择全部
    role_all_loc = (By.ID, "allchecked")
    #保存
    role_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    #断言创建角色按钮
    role_add_loc = (By.LINK_TEXT, "创建角色")


    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def input_role_name(self, text):
        """角色名称"""
        self.input_text(
            text,
            '角色名称',
            *(self.role_name_loc)
        )

    def input_remark_text(self, text):
        """备注"""
        self.input_text(
            text,
            '备注',
            *(self.role_remark_loc)
        )

    def click_select_all(self):
        """选择全部"""
        self.click_button(
            '选择全部',
            *(self.role_all_loc)
        )

    def click_save_button(self):
        """保存"""
        self.click_button(
            '保存',
            *(self.role_save_loc)
        )


    def assert_add_success(self, text):
        """断言成功"""
        title = str(self.get_tag_text(
            'text',
            *(self.role_add_loc)
        )).strip()
        self.get_image
        if not (title == text) :
            return False
        return True
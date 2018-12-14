from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.basepage import BasePage


class RegionIndex(BasePage):
    """封装区域设置页面元素、操作"""
    # <<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 添加一级
    region_create_area_loc = (By.LINK_TEXT, '添加一级')
    # 输入区域名称
    region_area_name_loc = (By.XPATH, "//input[@class='form-control']")
    # 保存
    region_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 取消
    region_dismiss_loc = (By.XPATH, "//button[contains(text(),'取消')]")
    #
    region_table_loc = (By.XPATH, "//td[@class='area-td']")
    # 删除
    region_delete_loc = (By.XPATH, "//a[@class='act delete_area']")
    # 删除确认
    region_sure_loc = (By.XPATH,
                       "//button[@class='btn btn-primary we-btn submit']"
                       )

    # 删除-取消
    region_cancel_loc = (By.XPATH,
                         "//button[@class='btn btn-primary we-btn']"
                         )
    # <<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def click_create_area(self):
        """点击添加一级"""
        self.click_button('添加一级', *(self.region_create_area_loc))

    def input_area_name(self, areaName, areaIndex):
        """输入区域名称"""
        self.input_text_index('区域名称', areaName, areaIndex,
                              *(self.region_area_name_loc)
                              )

    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.region_save_loc))

    def click_dismiss(self):
        """点击取消"""
        self.click_button('取消', *(self.region_dismiss_loc))

    def click_delete(self):
        """点击删除"""
        elm = self.find_element(*(self.region_table_loc))
        ActionChains(self.driver).move_to_element(elm).perform()
        self.click_button('删除', *(self.region_delete_loc))

    def click_sure(self):
        """点击确定"""
        self.click_button('确定', *(self.region_sure_loc))

    def click_cancle(self):
        """点击取消"""
        self.click_button('取消', *(self.region_cancel_loc))

    def get_name(self):
        """获取保存后的名字"""
        name = self.get_tag_text('text', *(self.region_table_loc))
        self.get_image
        return name

from selenium.webdriver.common.by import By
from base.basepage import BasePage

class PrivilegeList(BasePage):
    """封装特权管理页面元素、操作"""
    # <<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>
    # 新增特权
    privi_addprivilegebox_loc = (By.CLASS_NAME, 'addprivilegebox')
    # 删除
    privi_delete_loc = (By.XPATH,
                        "//div[@data-toggle='popover.confirm']"
                        )
    # 删除-确定
    privi_sure_loc = (By.XPATH, "//button[contains(text(),'确定')]")
    # 删除-取消
    privi_cancle_loc = (By.XPATH, "//button[contains(text(),'取消')]")
    # 特权名称
    privi_privilege_name_loc = (By.NAME, 'name')
    # 图标方式
    privi_privilege_icon_loc = (By.XPATH,
                                "//input[@name='privilegeIcon']/.."
                                )
    # 图片
    privi_opt_icon_img_loc = (By.CLASS_NAME, 'opt_icon')
    # 确定
    privi_ok_loc = (By.XPATH,
                    "//div[@class='modal-content']//button[.='确定']"
                    )
    # 取消
    privi_dismiss_loc = (By.XPATH,
                         "//div[@class='modal-content']//button[.='取消']"
                         )

    # 展示特权
    privi_show_loc = (By.XPATH, "//input[@name='show']/..")
    # 享受特权
    privi_enjoy_loc = (By.XPATH, "//input[@name='enjoy']/..")
    # 特权内容
    privi_textarea_loc = (By.CSS_SELECTOR, ".explain")
    # 保存
    privi_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 获取保存成功后的特权名称
    privi_name_loc = (By.XPATH, "//li[@class='privilege-list activelist']/div")

    #<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>
    def click_addprivilegebox(self):
        """点击新增特权"""
        self.click_button('新增特权', *(self.privi_addprivilegebox_loc))

    def input_privilege_name(self, privilegeName):
        """输入特权名称"""
        self.input_text(privilegeName, '特权名称',
                        *(self.privi_privilege_name_loc)
                        )

    def select_privilege_icon(self, privilegeIcon):
        """选择图标方式"""
        self.click_btn_index('图标', privilegeIcon,
                             *(self.privi_privilege_icon_loc)
                             )

    def select_opt_icon_img(self, imgIndex):
        """选择图片"""
        self.click_btn_index('图片', imgIndex,
                             *(self.privi_opt_icon_img_loc)
                             )

    def click_sure(self):
        """点击删除-确定"""
        self.click_button('确定', *(self.privi_sure_loc))

    def click_cancle(self):
        """点击删除-取消"""
        self.click_button('取消', *(self.privi_cancle_loc))

    def click_ok(self):
        """点击确定"""
        self.click_button('确定', *(self.privi_ok_loc))

    def click_show(self, showIndex):
        """选择是否展示特权"""
        self.click_btn_index('展示特权', showIndex, *(self.privi_show_loc))

    def click_enjoy(self, enjoyIndex):
        """选择是否享受特权"""
        self.click_btn_index('享受特权', enjoyIndex, *(self.privi_enjoy_loc))

    def input_textarea(self, textarea, areaIndex):
        """输入特权说明内容"""
        self.input_text_index('特权说明', textarea, areaIndex,
                              *(self.privi_textarea_loc)
                              )
    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.privi_save_loc))

    def get_name(self):
        """获取特权名称"""
        name = self.get_tag_text('text', *(self.privi_name_loc))
        self.get_image
        return name

    def click_delete(self):
        """点击删除特权"""
        self.click_button('删除', *(self.privi_delete_loc))

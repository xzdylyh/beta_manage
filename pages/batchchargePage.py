from selenium.webdriver.common.by import By
import autoit,time
from base.basepage import BasePage


class BatchchargePage(BasePage):
    """封装批量充值页面元素、操作"""
    # <<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 上传文件按钮
    batch_upload_loc = (By.XPATH, "//input[@name='file']")
    # 备注
    batch_recharge_desc_loc = (By.ID, 'recharge_desc')
    # 确认充值
    batch_submit_loc = (By.XPATH, "//button[@type='submit']")

    # <<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def upload_file(self, path):
        """上传文件"""
        self.click_button('上传文件', *(self.batch_upload_loc))
        autoit.control_set_text(
            '打开',
            '[Class:Edit; instance:1]',
            path
        )
        autoit.control_click(
            '打开',
            '[Class:Button; INSTANCE:1]'
        )

    def input_rechargedesc(self, desc):
        """输入备注"""
        self.clear_input_text(*(self.batch_recharge_desc_loc))
        self.input_text(desc, '备注',
                        *(self.batch_recharge_desc_loc)
                        )

    def click_submit(self):
        """确认"""
        self.click_button('确认', *(self.batch_submit_loc))

    def up(self, url):
        """通过js修改前端元素属性，输入上传路径"""
        js = 'document.getElementsByName("mallUpload")[0].removeAttribute("type")'
        self.execute_script(js)
        time.sleep(2)
        self.click_button('上传文件', *(By.XPATH, "//div[@class='upload-step-one']/div"))
        self.input_text(url, '文件路径', *(By.NAME, 'mallUpload'))

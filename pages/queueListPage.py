from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.basepage import BasePage

class queueListPage(BasePage):
    """封装等位页面元素定位、操作"""
    # <<<<<<<<<<<<<<<<<<<<元素定位>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 功能状态
    queue_state_loc = (By.XPATH, "//input[@name='state']/..")
    # 创建等位队列
    queue_create_loc = (By.XPATH, "//a[contains(text(),'创建等位队列')]")
    # 删除
    queue_del_loc = (By.XPATH, "//a[contains(text(),'删除')]")
    # 修改
    queue_modify_loc = (By.LINK_TEXT, '修改')
    # 确认
    queue_sure_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    # 取消
    queue_cancle_loc = (By.XPATH,
                        "//button[@class='btn btn-default we-btn']"
                        )
    # 列队名称
    queue_queueName_loc = (By.ID, 'queueName')
    # 最少
    queue_minRange_loc = (By.ID, 'minRange')
    # 最多
    queue_maxRange_loc = (By.ID, 'maxRange')
    # 叫号前缀
    queue_prefix_loc = (By.ID, 'selected')
    queue_prefixNum = "//ul[@class='dropdown-menu']/li[{}]/a"
    # 起始号码
    queue_startNum_loc = (By.ID, 'startNum')
    # 号码格式
    queue_format_loc = (By.XPATH, "//input[@name='format']/..")
    # 到号提醒
    queue_warn_loc = (By.XPATH, "//input[@name='format']/..")
    # 提前多少桌提醒
    queue_warnNum_loc = (By.ID, 'warnNum')
    # 保存
    queue_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 返回
    queue_return_loc = (By.XPATH, "//button[contains(text(),'返回')]")
    # 创建后的队列名称
    queue_getname_loc = (By.CSS_SELECTOR,
                         "table > tbody > tr > td:nth-child(1)"
                         )

    # <<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def select_state(self, index):
        """功能状态选择"""
        self.click_btn_index('功能状态', index, *(self.queue_state_loc))
        if index == 1:
            self.exist_and_click(*(self.queue_sure_loc))

    def click_remove(self):
        """点击删除"""
        self.click_button('删除', *(self.queue_del_loc))

    def click_sure(self):
        """点击确认"""
        self.click_button('确认', *(self.queue_sure_loc))

    def click_modify(self):
        """点击修改"""
        self.click_button('修改', *(self.queue_modify_loc))

    def click_create(self):
        """创建等位队列"""
        self.click_button('创建等位队列', *(self.queue_create_loc))

    def input_queue_name(self, queueName):
        """输入列队名称"""
        self.input_text(queueName, '列队名称', *(self.queue_queueName_loc))

    def input_min_range(self, minRange):
        """输入人数范围最少"""
        self.input_text(minRange,'最少', *(self.queue_minRange_loc))

    def input_max_range(self, maxRange):
        """输入人数范围最多"""
        self.input_text(maxRange, '最多', *(self.queue_maxRange_loc))

    def select_prefix(self, prefixNum):
        """选择叫号前缀"""
        self.click_button('叫号前缀', *(self.queue_prefix_loc))
        self.click_button('叫号前缀',
                          *(By.XPATH,
                            self.queue_prefixNum.format(prefixNum))
                          )

    def input_start_num(self, startNum):
        """输入起始号码"""
        self.clear_input_text(*(self.queue_startNum_loc))
        self.input_text(startNum, '起始号码', *(self.queue_startNum_loc))

    def select_format(self, format):
        """选择号码格式"""
        self.click_btn_index('号码格式', format, *(self.queue_format_loc))

    def select_warn(self, warn, warnNum=1):
        """选择到号提醒方式"""
        self.click_btn_index('到号提醒', warn, *(self.queue_warn_loc))
        if warn == 1:
            self.input_warn_num(warnNum)

    def input_warn_num(self, warnNum):
        """输入提前多少桌提醒"""
        self.clear_input_text(*(self.queue_warnNum_loc))
        self.input_text(warnNum, '提前多少桌提醒', *(self.queue_warnNum_loc))

    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.queue_save_loc))

    def click_return(self):
        """点击返回"""
        self.click_button('返回', *(self.queue_return_loc))

    def get_name(self):
        """获取保存成功后的等位队列名称"""
        name = self.get_tag_text('text', *(self.queue_getname_loc))
        self.get_image
        return name

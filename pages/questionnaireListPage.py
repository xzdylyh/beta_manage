from selenium.webdriver.common.by import By
from base.basepage import BasePage

class QuestionnaireList(BasePage):
    """封装评价问卷页面元素、操作"""
    # <<<<<<<<<<<<<<<<<<<<<<<元素>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 新建问卷
    quest_create_loc = (By.CSS_SELECTOR, 'button.btn')
    # 设置差评提醒
    quest_noti_loc = (By.LINK_TEXT, '设置差评提醒')
    # 版本选择
    quest_edition_loc = (By.XPATH, "//a[@class='edition-btn']")
    # 删除问卷
    quest_remove_loc = (By.XPATH, "//a[contains(text(),'删除')]")
    # 删除-确定
    quest_popover_confirm_loc = (By.XPATH,
                                 "//div[@class='popover-buttons']//button[.='确定']"
                                 )
    # 删除-取消
    quest_cancle_loc = (By.XPATH, "//button[contains(text(),'取消')]")
    # 精准版
    quest_nversion1_loc = (By.LINK_TEXT, '精准版')
    # 标准版
    quest_version2_loc = (By.LINK_TEXT, '标准版')
    # 主题
    quest_subject_loc = (By.NAME, 'subject')
    # 题目
    quest_problem_title_loc = (By.XPATH,
                               "//input[starts-with(@name,'title')]"
                               )
    # 选项
    quest_option_loc = (By.XPATH,
                        "//input[@class='form-control input-option']"
                        )
    # 添加选项按钮
    quest_option_add_loc = (By.XPATH, "//span[@class='option-add']")
    # 添加题目
    quest_add_problem_loc = (By.LINK_TEXT, '添加题目')
    # 删除题目
    quest_del_loc = (By.XPATH, "//button[contains(text(),'删除')]")
    # 保存
    quest_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")
    # 返回
    quest_return_loc = (By.XPATH, "//a[contains(text(),'返回')]")
    # 确认
    quest_sure_loc = (By.XPATH, "//button[contains(text(),'确认')]")
    # 修改
    quest_modify_loc = (By.XPATH, "//a[contains(text(),'修改')]")
    # 保存成功后问卷的主题名称
    quest_name_loc = (By.XPATH,
                      "//table[@class='table table-striped we-table']//tr[1]/td[2]")

    # <<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_create(self):
        """点击新建问卷按钮"""
        self.click_button('新建问卷', *(self.quest_create_loc))

    def select_edition(self, edition):
        """选择问卷类型"""
        self.click_btn_index('问卷类型', edition, *(self.quest_edition_loc))

    def input_subject(self, subject):
        """输入主题"""
        self.input_text(subject, '主题"', *(self.quest_subject_loc))

    def input_problem_title(self, title, titleIndex):
        """输入问题"""
        self.input_text_index('问题', title, titleIndex,
                              *(self.quest_problem_title_loc)
                              )

    def input_option(self, option, optionIndex):
        """输入选项内容"""
        self.input_text_index('选项内容', option, optionIndex,
                              *(self.quest_option_loc)
                              )

    def click_option_add(self):
        """点击添加选项按钮"""
        self.click_button('添加选项', *(self.quest_option_add_loc))

    def click_add_problem(self):
        """点击添加题目按钮"""
        self.click_button('添加题目', self.quest_add_problem_loc)

    def click_del(self, delindex):
        """删除问题按钮"""
        self.click_btn_index('删除问题', delindex, *(self.quest_del_loc))

    def click_sure(self):
        """点击确认"""
        self.click_button('确认', *(self.quest_sure_loc))

    def click_save(self):
        """点击保存"""
        self.click_button('保存', *(self.quest_save_loc))

    def click_reture(self):
        """点击返回"""
        self.click_button('返回', *(self.quest_return_loc))

    def click_modyfi(self):
        """点击修改"""
        self.click_button('修改', *(self.quest_modify_loc))

    def get_name(self):
        """获取保存成功后的问卷名称"""
        name = self.get_tag_text('text', *(self.quest_name_loc))
        self.get_image
        return name

    def click_remove(self, removeIndex):
        """点击删除"""
        self.click_btn_index('删除', removeIndex,
                             *(self.quest_remove_loc))

    def click_remove_sure(self):
        """点击确认删除"""
        self.click_button('确认', *(self.quest_popover_confirm_loc))

    def click_cancle(self):
        """点击取消删除"""
        self.click_button('取消', *(self.quest_cancle_loc))
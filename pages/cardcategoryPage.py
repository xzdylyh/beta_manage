from selenium.webdriver.common.by import By
import autoit
from base.basepage import BasePage


class Cardcategory(BasePage):
    """封装会员卡管理-卡类别管理页面元素，与操作"""
    # <<<<<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 添加卡类别
    cardcategory_cardAdd_loc = (By.LINK_TEXT, '添加卡类别')
    # 卡类别名称 (By.XPATH, "//div[@class='level-list']/h4")
    cardcategory_cardName = "//div[@class='vip-list']/div[{}]/h4"
    # 会员卡-删除
    cardcategory_remove_loc = (By.LINK_TEXT, "删除")

    # 会员卡-删除-确认
    cardcategory_sure_loc = (By.XPATH,
                             "//button[@data-url='/cardcategory/remove']"
                             )
    # 会员卡-删除-取消
    cardcategory_dismiss_loc = (By.XPATH, "//button[@data-dismiss='modal']"
                                )
    # 卡类别属性
    cardcategory_cardattribute_loc = (By.XPATH, "//input[@name='attribute']/..")
    # 卡类别名称
    cardcategory_inputName_loc = (By.ID, 'inputName')
    # 卡面样式
    cardcategory_cardType_loc = (By.XPATH, "//input[@name='cardType']/..")
    # 卡面名称使用
    cardcategory_cardname_loc = (By.XPATH, "//input[@name='cardName']/..")
    # 上传卡面
    cardcategory_uploadface_loc = (By.XPATH,
                               "//div[@data-section='face']//div[@class='we-file file-sm']")
    # 上传logo
    cardcategory_uploadlogo_loc = (By.XPATH,
                               "//div[@data-section='logo.face']//div[@class='we-file file-sm']")

    # 储值
    cardcategory_inputStored_loc = (By.XPATH, "//input[@name='stored']/..")
    # 积分
    cardcategory_pointValue_loc = (By.XPATH, "//input[@name='point']/..")
    # cardcategory_pointValue_loc = (By.XPATH, "//div[@class='form-input']/div[9]/div/ul/li[1]/label")
    # 开启/关闭-确定按钮
    card_confirmsubmit_loc = (By.XPATH,
                              "//button[@data-toggle='popover.confirm.submit']"
                              )
    # 开启/关闭-取消按钮
    card_confirmcancel_loc = (By.XPATH,
                              "//button[@data-toggle='popover.confirm.cancel']"
                              )

    # 会员价
    cardcategory_vipPrice_loc = (By.NAME, 'vipPrice')
    # 积分特权
    cardcategory_creditPrice_loc = (By.NAME, 'creditPrice')
    # 特权1：
    cardcategory_privilege_id = "inputPrivilege{}"
    # 删除特权
    cardcategory_listdel_loc = (By.XPATH,
                                "//button[contains(text(),'删除特权']"
                                )
    # 添加特权
    cardcategory_listadd_loc = (By.XPATH,
                                "//button[contains(text(),'添加特权']"
                                )
    # 确定
    cardcategory_submit_loc = (By.XPATH, "//button[@type='submit']")
    # 取消
    cardcategory_cancel_loc = (By.XPATH, "//a[contains(text(),'取消']")

    # <<<<<<<<<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_cardAdd(self):
        """点击添加卡类别"""
        self.click_button('添加卡类别', *(self.cardcategory_cardAdd_loc))

    def click_remove(self, index):
        """点击删除"""
        self.click_btn_index('删除', index, *(self.cardcategory_remove_loc))
        # self.click_button('', *(self.cardcategory_remove_loc))
    def click_sure(self):
        """点击确定"""
        self.click_button('确认', *(self.cardcategory_sure_loc))

    def click_dismiss(self):
        """点击取消"""
        self.click_button('取消', *(self.cardcategory_dismiss_loc))

    def get_sussesscard_name(self, nameindex):
        """获取创建成功的卡名称"""
        name = self.get_tag_text('text', *(By.XPATH,
                                           self.cardcategory_cardName.format(nameindex)))
        self.get_image
        return name

    def select_cardattribute(self, cardindex):
        """选择卡类别属性，0：；普通会员卡，1：不记名卡"""
        self.click_btn_index('卡类别属性', cardindex,
                             *(self.cardcategory_cardattribute_loc)
                             )

    def input_inputName(self, inputname):
        """输入卡类别名称"""
        self.input_text(inputname, '卡类别名称',
                        *(self.cardcategory_inputName_loc)
                        )

    def select_cardType(self, cardtype, path):
        """选择卡面样式,0:默认颜色，1：自定义卡面 """
        self.click_btn_index('卡面样式', cardtype,
                             *(self.cardcategory_cardType_loc)
                             )
        if cardtype == 1:
            self.up_image(path, *(self.cardcategory_uploadface_loc))

    def select_cardname(self, cardname, path):
        """卡面名称使用,0:文字，1：logo"""
        self.click_btn_index('卡面名称使用', cardname,
                             *(self.cardcategory_cardname_loc)
                             )
        if cardname == 1:
            self.up_image(path, *(self.cardcategory_uploadlogo_loc))

    def up_image(self, path, *loc):
        """上传图片"""
        self.click_button('上传', *loc)
        # autoit处理
        autoit.control_set_text(
            '打开',
            '[Class:Edit; instance:1]',
            path
        )
        autoit.control_click(
            '打开',
            '[Class:Button; INSTANCE:1]'
        )

    def select_inputStored(self, inputstored):
        """选择储值，0开启，1关闭"""
        self.click_btn_index('储值', inputstored,
                             *(self.cardcategory_inputStored_loc)
                             )
        self.exist_and_click(*(self.card_confirmsubmit_loc))

    def selcet_pointValue(self, pointvalue):
        """选择积分，0开启，1关闭"""

        self.click_btn_index('积分', pointvalue,
                             *(self.cardcategory_pointValue_loc)
                             )

        # self.click_button('', *(self.cardcategory_pointValue_loc))
        self.exist_and_click(*(self.card_confirmsubmit_loc))

    def click_confirmsubmit(self):
        """点击开启-确定按钮"""
        self.click_button('开启-确定按钮',
                          *(self.card_confirmsubmit_loc)
                          )

    def click_confirmcancel(self):
        """点击开启-取消按钮"""
        self.click_button('开启-取消按钮',
                          *(self.card_confirmcancel_loc)
                          )

    def input_vipPrice(self, vipprice):
        """输入会员价"""
        self.clear_input_text(*(self.cardcategory_vipPrice_loc))
        self.input_text(vipprice, '会员价',
                        *(self.cardcategory_vipPrice_loc)
                        )

    def input_creditPrice(self, creditprice):
        """积分特权：每消费现金"""
        if creditprice != '%NONE%':
            self.clear_input_text(*(self.cardcategory_creditPrice_loc))
        self.input_text(creditprice, '积分特权,每消费现金',
                        *(self.cardcategory_creditPrice_loc)
                        )

    def input_privilege(self, index, privilege):
        """输入积分特权内容，index：输入的区域，privilege：内容"""
        self.input_text(privilege, '积分特权',
                        *(By.ID,
                          self.cardcategory_privilege_id.format(index))
                        )

    def click_submit(self):
        """点击确定"""
        self.click_button('确定', *(self.cardcategory_submit_loc))

    def click_cancle(self):
        """点击取消"""
        self.click_button('取消', *(self.cardcategory_cancel_loc))


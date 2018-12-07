from selenium.webdriver.common.by import By
import autoit
from base.basepage import BasePage
from pages.chargeListSusscessPage import ChargeListSusscess


class ActualcardList(ChargeListSusscess, BasePage):
    """封装创建实体卡页面，元素及操作"""

    # <<<<<<<<<<<<<<<<<<元素定位>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 申请实体卡
    actualcard_addcard_loc = (By.LINK_TEXT, '申请实体卡')
    # 实体卡开卡需验证用户手机号\绑定实体卡需验证用户手机号
    actualcard_verify_loc = (By.XPATH, "//input[@id='verify']/..")
    # 批次名
    actualcard_batchName_loc = (By.ID, 'batchName')
    # 普通会员卡\不记名卡
    actualcard_cardType_lco =(By.XPATH, "//input[@name='attribute']/..")
    # 所属卡类别
    actualcard_cardCategory_loc = (By.NAME, 'category')
    # 卡号生成规则
    actualcard_cardRule_loc = (By.XPATH, "//input[@name='rule']/..")
    # 开卡方式
    actualcard_cardWay_loc = (By.XPATH, "//input[@name='way']/..")
    # 上传手机号（手机号必须11位）/不上传手机号
    actualcard_uploadPhone_loc = (By.XPATH, "//input[@name='uploadPhone']/..")
    # 上传文件-选择文件
    actualcard_mallUploadFile_loc = (By.XPATH, "//div[@class='we-file file-sm']")
    # 申请张数
    actualcard_cardNumber_loc = (By.ID, 'inputNumber')
    # 开卡售价
    actualcard_cardPrice_loc = (By.ID, 'inputPrice')
    # 保存
    actualcard_submit_loc = (By.XPATH, "//button[@type='submit']")
    # 获取保存成功后的批次名称
    actualcard_name_loc = (By.XPATH, "//div[@class='we-table-responsive']//td[2]")

    # <<<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def click_addcard_btn(self):
        """点击申请实体卡"""
        self.click_button('申请实体卡', *(self.actualcard_addcard_loc))

    def select_verify_checkbox(self, index):
        """0:实体卡开卡需验证用户手机号;1:绑定实体卡需验证用户手机号"""
        element = self.find_elements(*(self.actualcard_verify_loc))[int(index)]
        value = element.get_attribute('class')
        if 'checked' not in value:
            element.click()

    def input_batchName(self, name):
        """输入批次名称"""
        self.input_text(name, '批次名称',
                        *(self.actualcard_batchName_loc)
                        )

    def select_cardType(self, cardtype):
        """选择卡类别属性,0:普通会员卡;1:不记名卡"""
        self.click_btn_index('卡类别属性', cardtype,
                             *(self.actualcard_cardType_lco)
                             )

    def select_cardCategory(self, cardcategory):
        """选择所属卡类别，0：普通会员卡，1：VIP卡"""
        self.select_list(*(self.actualcard_cardCategory_loc)).\
            select_by_index(cardcategory)

    def select_cardRule(self, cardrule):
        """选择卡号生成规则，0：随机卡号，1：自定义卡号"""
        self.click_btn_index('卡号生成规则', cardrule,
                             *(self.actualcard_cardRule_loc)
                             )

    def select_cardWay(self, cardway):
        """选择开卡方式，0：仅创建批次，1：创建批次并开卡 """
        self.click_btn_index('开卡方式', cardway,
                             *(self.actualcard_cardWay_loc)
                             )
    def select_uploadPhone(self, uploadphone):
        """0:上传手机号（手机号必须11位）;1:不上传手机号"""
        self.click_btn_index('上传手机号（手机号必须11位）/不上传手机号',
                             uploadphone,
                             *(self.actualcard_uploadPhone_loc)
                             )

    def upload_csv_file(self, path):
        """上传csv文件
        path：csv文件路径
        """
        self.click_button('选择文件', *(self.actualcard_mallUploadFile_loc))
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

    def input_cardNumber(self, cardnumber):
        """输入申请张数"""
        # self.clear_input_text(*(self.actualcard_cardNumber_loc))
        self.input_text(cardnumber, '申请张数',
                        *(self.actualcard_cardNumber_loc)
                        )

    def input_cardPrice(self, cardprice):
        """输入开卡售价"""
        if str(cardprice).strip().upper() != '%NONE%':
            self.clear_input_text(*(self.actualcard_cardPrice_loc))
        self.input_text(cardprice, '开卡售价',
                        *(self.actualcard_cardPrice_loc)
                        )

    def click_submitBtn(self):
        """点击保存"""
        self.click_button('保存', *(self.actualcard_submit_loc))

    def get_successNameText(self):
        """获取创建成功，页面中显示储值卡的名称"""
        name = self.get_tag_text('text', *(self.actualcard_name_loc))
        print("储值卡名称为：{}".format(name))
        self.get_image
        return name


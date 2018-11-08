
from selenium.webdriver.common.by import By
import autoit
from base.basepage import BasePage

class ActivityCreate63(BasePage):
    """营销->膨胀红包活动"""
    #########膨胀红包－基础设置######
    #活动名称
    activity_name_loc = (By.ID, "field_title")
    #活动时间
    activity_stime_loc = (By.ID, "activity_start_time")
    #结束时间
    activity_etime_loc = (By.ID, "activity_end_time")
    #活动说明
    activity_desc_loc = (By.NAME, "activity_desc")
    #商家LOGO上传按钮
    activity_upload_locs = (By.CSS_SELECTOR, "div.upload-step-one > div > input[type='file']")

    #########膨胀红包-奖品设置########
    #－－－－奖品1；奖品2；奖品3-------#
    #选择优惠券
    coupon_drop_locs = (By.ID, "dropdownCoupon")
    #券类型选择;代金券；礼品券
    coupon_types = ['代金券', '礼品券']

    #奖品名称
    coupon_prize_locs = (By.NAME, "prize_title[]")
    #兑换所需人数
    coupon_value_locs = (By.NAME, "prize_value[]")

    ##########页面配置
    #文字及按钮颜色
    page_color_loc = (By.XPATH, "//input[@name='title_color']/../ui[0]/li[1]")
    #主题背景色
    page_back_loc = (By.NAME, "activity_background")
    #小程序分享标题
    page_share_loc = (By.NAME, "share_titile")
    #保存
    page_save_loc = (By.XPATH, "//button[contains(text(),'保存')]")


    #########################页面操作###################
    def input_activity_name(self, text):
        """输入活动名称"""
        self.input_text(
            text,
            '活动名称',
            *(self.activity_name_loc)
        )

    def input_activity_stime(self, text):
        """输入活动开始时间"""
        self.input_text(
            text,
            '活动开始时间',
            *(self.activity_stime_loc)
        )

    def input_activity_etime(self, text):
        """输入活动结束时间"""
        self.input_text(
            text,
            '活动结束时间',
            *(self.activity_etime_loc)
        )

    def input_activity_desc(self, text):
        """输入活动说明"""
        self.input_text(
            text,
            '活动说明',
            *(self.activity_desc_loc)
        )


    def click_ac_upload(self, index, path):
        """
        单击上传按钮；通过索引来决定点击哪个上传功能
        :param index: 索引为找到元素索引
        :param path: 上传图片所在绝对路径
        :return:
        """
        self.click_btn_index(
            '上传',
            index,
            *(self.activity_upload_locs)
        )
        #autoit处理
        autoit.control_set_text(
            '打开',
            '[Class:Edit; instance:1]',
            path
        )
        autoit.control_click(
            '打开',
            '[Class:Button; INSTANCE:1]'
        )


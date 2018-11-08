"""
create:2018/10/23
by:yhleng
"""
import os
import unittest
import ddt
from pages.couponListPage import CouponList
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)




@ddt.ddt
class TestCouponListPage(unittest.TestCase):
    """券管理"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/manage'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass




    @ddt.data(*get_data('couponListPage', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """创建券"""
        self.clist = CouponList(self.url, self.driver, data['title'])
        # 打开创建营销活动页面
        self.clist.open
        # 券管理
        self.clist.clickCouponManage_Link()
        #获取当前券列表，券数量
        old_num = self.clist.getCouponNum()
        # 创建新的券
        self.clist.clickCouponCreate_Btn()
        # 选择券类型，0代金券；1礼品券；2券包
        self.clist.clickCouponType(data['couponType'])
        # 属性;0普通；1微信群发消息专用
        self.clist.clickCouponPro(data['property'])
        # 面值
        self.clist.inputCouponValue(data['inputValue'])
        # 名称;op=1清空输入框
        self.clist.inputCouponName(data['name'], op=1)
        # 客户端展示券名称;0显示；1不显示
        self.clist.clickCouponShowName(data['clientShow'])
        # 起用金额
        self.clist.inputCouponMinValue(data['minValue'])
        # 每次消费最多张数
        self.clist.inputCouponSheets(data['dealNum'])
        # 与其它券混合使用；0可以；1不可以；2部分可以
        self.clist.clickCouponMix(data['mixUsed'])
        # 券是否可以转赠给好友
        self.clist.clickCouponGiveFriend(data['isGiveFriend'])
        # 启用时间，0为当日启用，输入其它按天数启用
        self.clist.inputCouponEnabledTime(data['enabledTime'])
        # 有效期
        self.clist.inputCouponTerm(
            op=data['termTimeOption'],
            text=data['termTime'],
            startDate=data['termStartTime'],
            endDate=data['termEndTime']
        )
        # 时间段设置;0为全天可用;1为自动化全天
        self.clist.clickCouponEatTime(data['eatTime'])
        #限制与说明
        self.clist.inputCouponArea(data['restriction'])
        #保存，提交
        self.clist.clickCouponSave()
        #提交，确认
        self.clist.clickCouponConfirm()
        #当前券数量
        new_num = self.clist.getCouponNum()
        #断言增加券是否成功
        self.assertTrue(
            self.clist.assertAddCoupon(old_num, new_num)
        )






if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestCouponListPage)
    ]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print(filePath)

    with open(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yhleng"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)

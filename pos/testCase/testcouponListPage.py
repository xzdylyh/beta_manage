#coding=utf-8
"""
create:2018/10/23
by:yhleng
"""
import os
import unittest
import ddt
from pos.pages.couponListPage import CouponList
from pos.lib.scripts import (
    select_Browser_WebDriver,
    replayCaseFail
)
from pos.lib import (
    gl,
    HTMLTESTRunnerCN
)


case1Data = [
    {'title':'创建营销活动 - 自动化测试专用'}
]


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

    @ddt.data(*case1Data)
    @replayCaseFail(num=3)
    def testCase1(self, data):
        """创建券"""
        self.clist = CouponList(self.url, self.driver, data['title'])
        # 打开创建营销活动页面
        self.clist.open
        # 券管理
        self.clist.clickCouponManage_Link()
        # 创建新的券
        self.clist.clickCouponCreate_Btn()
        # 选择券类型，0代金券；1礼品券；2券包
        self.clist.clickCouponType(0)
        # 属性;0普通；1微信群发消息专用
        self.clist.clickCouponPro(1)
        # 面值
        # 名称
        # 客户端展示券名称;0显示；1不显示
        self.clist.clickCouponShowName(1)
        # 与其它券混合使用；0可以；1不可以；2部分可以
        self.clist.clickCouponMix(2)



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

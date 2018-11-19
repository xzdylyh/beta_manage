import os
import unittest
import ddt
from pages.chargeListPage import ChargeList
from pages.chargeListSusscessPage import chargeListSusscess
from pages.chargeListModifyPage import chargeListModify
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
class TestChargeListWeixinPage(unittest.TestCase):
    """储值规则设置--微信规则"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/charge/edit?type=weixin'  # 微信规则入口
        cls.url_s = ''  # 保存成功页面url，默认为空
        cls.url_m = ''  # 保存储值规则修改页面url，默认为空

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    # @unittest.skip('调试')
    @ddt.data(*get_data('chargeListWeixinPage', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """"创建储值规则-单独设置--固定金额"""
        self.clist = ChargeList(self.url, self.driver, data['title'])
        # 打开创建储值规则页面
        self.clist.open
        # 输入规则名称
        self.clist.inputRuleNameValue(data['name'])
        # 适用子规则，0:单独设置，1:使用各门店储值规则
        self.clist.clickWeRadioBtn(data['radioIndex'])
        # 输入充值金额
        self.clist.inputPrepaidValue(data['charge'])
        # 选择充值送的类型;0:固定金额，1：固定积分，2：代金券/礼品券
        self.clist.selectStoreRule(data['storeRule'])
        # 选择固定金额
        self.clist.selectInputAccount(data['account'])
        # 选择固定金额（元）/实收金额的送（%）
        self.clist.inputPresentValue(data['presentValue'])
        # 点击保存
        self.clist.clictSubmitBtn()
        # 断言是否保存成功
        self.sclist = chargeListSusscess(self.url_s, self.driver, 'savesuss')
        self.assertEqual(self.sclist.getScuessText(), data['successText'], data['msg'])
        # 点击返回
        self.sclist.clickBcakBtn()
        # 点击删除
        self.mclist = chargeListModify(self.url_m, self.driver, 'modify')
        self.mclist.clickDelBtn()
        # 点击确定
        self.mclist.clickOkBtn()
        # 验证删除成功
        self.assertEqual(self.mclist.getDelInfo(), data['delInfo'], '删除门店储值规则成功')

    # @unittest.skip('调试')
    @ddt.data(*get_data('chargeListWeixinPage', 'CASE2'))
    @reply_case_fail(num=3)
    def testcase2(self, data):
        """"创建储值规则-固定积分"""
        self.clist = ChargeList(self.url, self.driver, data['title'])
        # 打开创建储值规则页面
        self.clist.open
        # 输入规则名称
        self.clist.inputRuleNameValue(data['name'])
        # 适用子规则，0:单独设置，1:使用各门店储值规则
        self.clist.clickWeRadioBtn(data['radioIndex'])
        # 输入充值金额
        self.clist.inputPrepaidValue(data['charge'])
        # 选择充值送的类型;0:固定金额，1：固定积分，2：代金券/礼品券
        self.clist.selectStoreRule(data['storeRule'])
        # 选择固定积分
        self.clist.selectInputIntegral(data['integra'])
        # 选择固定金额（元）/实收金额的送（%）
        self.clist.inputIntegralValue(data['integralValue'])
        # 点击保存
        self.clist.clictSubmitBtn()
        # 断言是否保存成功
        self.sclist = chargeListSusscess(self.url_s, self.driver, 'savesuss')
        self.assertEqual(self.sclist.getScuessText(), data['successText'], data['msg'])
        # 点击返回
        self.sclist.clickBcakBtn()
        # 点击删除
        self.mclist = chargeListModify(self.url_m, self.driver, 'modify')
        self.mclist.clickDelBtn()
        # 点击确定
        self.mclist.clickOkBtn()
        # 验证删除成功
        self.assertEqual(self.mclist.getDelInfo(), data['delInfo'], '删除门店储值规则成功')

    # @unittest.skip('ok')
    @ddt.data(*get_data('chargeListWeixinPage', 'CASE3'))
    @reply_case_fail(num=3)
    def testcase3(self, data):
        """"创建储值规则-代金券/礼品券"""
        self.clist = ChargeList(self.url, self.driver, data['title'])
        # 打开创建储值规则页面
        self.clist.open
        # 输入规则名称
        self.clist.inputRuleNameValue(data['name'])
        # 适用子规则，0:单独设置，1:使用各门店储值规则
        self.clist.clickWeRadioBtn(data['radioIndex'])
        # 输入充值金额
        self.clist.inputPrepaidValue(data['charge'])
        # 选择充值送的类型;0:固定金额，1：固定积分，2：代金券/礼品券
        self.clist.selectStoreRule(data['storeRule'])
        # 选择代金券/礼品券，0：代金券，1：礼品券
        self.clist.selectGift(data['couponIndex'])
        # 点击使用代金券,0：默认使用当前第一个券
        self.clist.selectCoupon(data['couponValue'])
        # 点击保存
        self.clist.clictSubmitBtn()
        # 断言是否保存成功
        self.sclist = chargeListSusscess(self.url_s, self.driver, 'savesuss')
        self.assertEqual(self.sclist.getScuessText(), data['successText'], data['msg'])
        # 点击返回
        self.sclist.clickBcakBtn()
        # 点击删除
        self.mclist = chargeListModify(self.url_m, self.driver, 'modify')
        self.mclist.clickDelBtn()
        # 点击确定
        self.mclist.clickOkBtn()
        # 验证删除成功
        self.assertEqual(self.mclist.getDelInfo(), data['delInfo'], '删除门店储值规则成功')

    @ddt.data(*get_data('chargeListWeixinPage', 'CASE4'))
    @reply_case_fail(num=3)
    def testcase4(self, data):
        """"创建储值规则-使用各门店储值规则"""
        self.clist = ChargeList(self.url, self.driver, data['title'])
        # 打开创建储值规则页面
        self.clist.open
        # 输入规则名称
        self.clist.inputRuleNameValue(data['name'])
        # 适用子规则，0:单独设置，1:使用各门店储值规则
        self.clist.clickWeRadioBtn(data['radioIndex'])
        # 点击保存
        self.clist.clictSubmitBtn()
        # 断言是否保存成功
        self.sclist = chargeListSusscess(self.url_s, self.driver, 'savesuss')
        self.assertEqual(self.sclist.getScuessText(), data['successText'], data['msg'])
        # 点击返回
        self.sclist.clickBcakBtn()
        # 点击删除
        self.mclist = chargeListModify(self.url_m, self.driver, 'modify')
        self.mclist.clickDelBtn()
        # 点击确定
        self.mclist.clickOkBtn()
        # 验证删除成功
        self.assertEqual(self.mclist.getDelInfo(), data['delInfo'], '删除门店储值规则成功')


if __name__ == "__main__":
    # unittest.main(verbosity=2)

    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestChargeListWeixinPage)
    ]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print(filePath)

    with open(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yecc"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)

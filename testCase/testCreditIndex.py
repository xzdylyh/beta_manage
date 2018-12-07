import os
import unittest
import ddt
from pages.chargeListSusscessPage import ChargeListSusscess
from pages.creditIndexPage import CreditIndexPage
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    genrandomstr
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)


@ddt.ddt
class TestCreditIndex(unittest.TestCase):
    """积分修改"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = "http://manage.beta.acewill.net/credit/index"
        cls.url_ = ""

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    @ddt.data(*get_data('creditIndexPage', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """积分修改"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.cIndex = CreditIndexPage(self.url, self.driver, data['title'])
        self.cIndex.open
        # 点击修改按钮
        self.cIndex.click_modify_btn()
        # 选择开启,删除已存在的积分规则
        self.cIndex.select_state_radio(data['index'])
        self.cIndex.click_removeConfirm_btn()
        self.cIndex.click_Ok_btn()
        # 消费奖励积分开启、关闭
        self.cIndex.select_consumpoint(data['consumpoint'])
        # 0,消费后立即奖励,1完成消费评价后奖励
        self.cIndex.select_consumpointsmode(data['consumpointsmode'])
        # 输入奖励规则
        self.cIndex.input_baseline_text(data['baseline'])
        # 选择奖励范围 ,奖励范围,0：现金消费；1：现金和储值消费
        self.cIndex.select_giftRange_radion(data['giftRange'])
        # 选择积分有效期，积分有效期,0:当年发放的所有积分，在下一年度的;
        # 1:自发放之日起一年后过期（逐笔过期）2:永久有效
        index = data['termRadio']
        self.cIndex.select_termRadio_radio(index)
        if index == 0:
            # 当选择0:当年发放的所有积分，在下一年度的，可以选择月、日
            self.cIndex.select_monthAndDay(data['month'], data['day'])
        # 选择你消耗积分的类型
        # 选择消耗积分类型，0:积分门店消费抵现；1：积分线上消费抵现 ；2：积分换礼
        # self.cIndex.select_pointeExchange_radio(data['pointe'])
        # 当选择积分换礼后，需选择添加积分规则；
        self.cIndex.select_rules(data['desc'])
        # 添加子规则
        self.cIndex.click_ruleadd_btn()
        # 输入积分数量
        self.cIndex.input_ruleNum_text(data['num'])
        # 积分兑换,0:实物礼品;1:优惠券
        self.cIndex.select_pointWay(data['pointWay'])
        if data['pointWay'] == 0:
            # 如果选择实物礼品，输入礼品名称和数量
            self.cIndex.input_pointWayGift_text(data['nameNum'])
        else:
            # 如果选择优惠券，则进行代金券、礼品券选择
            # 0:代金券1：礼品券
            self.cIndex.click_weCoupon_btn(data['couponIndex'])
            self.cIndex.selectCoupon(data['couponValue'])
        # 输入积分名称
        self.cIndex.input_screenName_text(data['screenName'])
        # 点击保存按钮
        self.cIndex.click_submit()
        # 点击返回按钮
        self.slist = ChargeListSusscess(self.url_, self.driver, data['title'])
        self.slist.clickBcakBtn()
        # 验证是否成功
        self.assertEqual(self.cIndex.get_modify_text(), data['modifiedText'])



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestCreditIndex)
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












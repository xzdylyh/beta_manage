import os
import unittest
import ddt
from time import sleep
from pages.cardruleIndexPage import Cardrule
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    genrandomstr,
    join_url
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)


@ddt.ddt
class TestCardrule(unittest.TestCase):
    """升降级规则设置(VIP会员)"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/cardrule/index')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    # @unittest.skip('')
    @ddt.data(*get_data('cardRule', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """升级规则设置"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.cindex = Cardrule(self.url, self.driver, data['title'])
        self.cindex.open
        # 点击修改
        self.cindex.click_modify()
        # 选择升级规则，并输入内容
        self.cindex.select_up(data['rule_text'], data['up_index'])
        sleep(2)
        # 点击确认
        self.cindex.click_up_sure()
        # 点击保存
        self.cindex.click_save()

    # @unittest.skip('')
    @ddt.data(*get_data('cardRule', 'CASE2'))
    @reply_case_fail(num=1)
    def testcase2(self, data):
        """降级规则设置"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.cindex = Cardrule(self.url, self.driver, data['title'])
        self.cindex.open
        # 点击修改
        self.cindex.click_subdmote()
        # 选择降级规则，并输入内容(输入的内容与选择的规则要对应)
        self.cindex.select_down(data['down_index'])
        # 月累计消费未达到
        self.cindex.input_money(data['money'])
        # 会员当前等级满
        self.cindex.input_sizes(data['sizes'], data['unit'])
        # 会员在当前等级每
        self.cindex.input_month_time(data['monthTime'],
                                     data['monthMoney']
                                     )
        # 会员在当前等级每
        self.cindex.input_recharge_time(data['rechargeTime'],
                                        data['rechargeMoney']
                                        )
        sleep(2)
        # 点击确认
        self.cindex.click_down_sure()
        # 点击保存
        self.cindex.click_save()

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestCardrule)
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



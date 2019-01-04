import os
import unittest
import ddt
from time import sleep
from pages.batchchargePage import BatchchargePage
from pages.rechargeDetailPage import RechargeDetailPage
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
class TestBatchcharge(unittest.TestCase, RechargeDetailPage):
    """会员管理--批量充值"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/member/batchcharge/index')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('batchcharge', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """批量充值"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.batch = BatchchargePage(self.url, self.driver,
                                     data['title']
                                     )
        self.batch.open
        # 上传文件
        # self.batch.upload_file(os.path.join(gl.dataPath,
        #                                    '批量充值模板.csv')
        #                      )
        self.batch.up(data['url'])
        # 输入备注
        desc = data['desc'] + genrandomstr(5)
        self.batch.input_rechargedesc(desc)
        # 点击确认
        self.batch.click_submit()
        # 点击财务报表
        self.click_finance()
        # 点击充值
        self.click_recharge()
        # 检查是否充值成功
        self.assertEqual(self.get_noteth(), desc)

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestBatchcharge)
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
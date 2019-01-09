import os
import unittest
import ddt
from pages.activityCreate2057Page import ActivityCreate2057
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    join_url
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)

@ddt.ddt
class TestActivityCreate2057(unittest.TestCase):
    """定向调研"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/activity/create/1030')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate2057', 'CASE1'))
    @reply_case_fail(num=1)
    def testCase1(self, data):
        """积分排行"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        tc = ActivityCreate2057(self.url,self.driver,data['page_title'])
        tc.open
        #活动名称
        tc.input_activity_name(data['activity_name'])



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestActivityCreate2057
        )
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

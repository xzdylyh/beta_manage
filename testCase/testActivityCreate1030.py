import os
import unittest
import ddt
from pages.activityCreate1030Page import ActiviteCreate1030
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
class TestActivityCreate1030(unittest.TestCase):
    """积分排行"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/activity/create/1030')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate1030', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """积分排行"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        self.tc = ActiviteCreate1030(self.url,self.driver,data['page_title'])
        self.tc.open
        #活动名称
        self.tc.input_activity_name(data['activity_name'])
        #活动描述
        self.tc.input_activity_desc(data['activity_desc'])
        #活动开始时间
        self.tc.input_start_time(data['start_time'])
        #－结束时间
        self.tc.input_end_time(data['end_time'])
        #活动说明
        self.tc.input_activity_summary(data['activity_desc'])
        #保存-确认
        self.tc.click_save_button()
        self.tc.click_sconfirm_btn()
        #断言
        self.assertTrue(
            self.tc.assert_add_success(
            data['activity_name'],
            data['activity_status']
            )
        )
        #删除
        self.tc.click_delete_button()
        self.assertFalse(
            self.tc.assert_add_success(
            data['activity_name'],
            data['activity_status']
            )
        )


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestActivityCreate1030
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

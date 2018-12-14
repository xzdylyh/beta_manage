import os
import unittest
import ddt
from pages.monitorSetPage import MonitorSet
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
class TestMonitorSet(unittest.TestCase):
    """异常交易监控－设置"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/monitor/index?type=set')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('MonitorSet', 'CASE1'))
    @reply_case_fail(num=1)
    def testCase1(self, data):
        """异常交易监控－设置"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        tc = MonitorSet(self.url,self.driver,data['page_title'])
        tc.open
        #单卡单笔消费金额超过
        tc.select_consume_single(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡日累计消费金额超过
        tc.select_consume_total(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )

        # 单卡日累计消费金额超过
        tc.select_consume_week(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )

        #单卡日累计消费次数超过
        tc.select_consume_num(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡周累计消费次数超过
        tc.select_consume_weeknum(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡单笔充值金额超过
        tc.select_charge_amount(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡日累计充值金额超过
        tc.select_charge_total(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡周累计充值金额超过
        tc.select_charge_weektotal(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #单卡日累计充值次数超过
        tc.select_charge_count(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )

        #单卡周累计充值次数超过
        tc.select_charge_weekcount(
            data['single_amount'],
            select_index=data['select_index'],
            bool=data['lock_bool']
        )
        #保存
        tc.click_save_button()
        self.assertTrue(tc.assert_success_bool())




if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestMonitorSet
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

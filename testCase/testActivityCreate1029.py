import os
import unittest
import ddt
from pages.activityCreate1029Page import ActivityCreate1029
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
class TestActivityCreate1029(unittest.TestCase):
    """消费评价"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/activity/create/1029')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate1029', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """消费评价"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        self.tc = ActivityCreate1029(self.url,self.driver,data['page_title'])
        self.tc.open
        #活动名称
        self.tc.input_activity_name(data['activity_name'])
        #评价奖励券
        self.tc.select_reward_coupon(
            data['is_select_coupon'],
            data['coupon_type'],
            data['coupon_index']
        )
        #评价奖励积分
        self.tc.select_reward_credit(
            data['is_select_credit'],
            data['credit_num']
        )
        #选择问卷设置;0第一个
        self.tc.select_question(data['qs_index'])
        #问卷推送条件
        self.tc.select_push(data['push_index'])
        #每满多少元
        self.tc.input_push_amount(data['push_amount'])

        #发券提醒;0不提醒；1短信提醒
        self.tc.click_send_remind(data['remind_index'])
        #券到期提醒;0不提醒；1短信提醒
        self.tc.click_expire(data['expire_index'])
        #活动开始时间
        self.tc.input_start_time(data['start_time'])
        #－结束时间
        self.tc.input_end_time(data['end_time'])
        #活动说明
        self.tc.input_activity_desc(data['activity_desc'])
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
            TestActivityCreate1029
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

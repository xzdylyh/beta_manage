import os
import unittest
import ddt
from pages.activityCreate1024Page import ActivityCreate1024
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
class TestActivityCreate1024(unittest.TestCase):
    """营销－累计消费返券"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/create/1024'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate1024', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """开卡关怀"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        self.tc = ActivityCreate1024(self.url,self.driver,data['page_title'])
        self.tc.open
        #活动名称
        self.tc.input_activity_name(data['activity_name'])
        #赠券设置；0金额；1次数
        self.tc.select_list_index(data['coupon_index'])
        #输入金额
        self.tc.input_amount_rmb(data['amount'])
        #赠券设置-增加券
        self.tc.click_add_coupon()
        #券类型;0代金券；1礼品券
        self.tc.click_coupon_type(data['coupon_type'])
        #使用
        self.tc.click_coupon_used(data['coupon_index'])
        #发券提醒;0不提醒；1短信提醒
        self.tc.click_send_remind(data['remind_index'])
        #券到期提醒;0不提醒；1短信提醒
        self.tc.click_expire(data['expire_index'])
        #活动开始时间－结束时间
        self.tc.input_start_time(data['start_time'])
        self.tc.input_end_time(data['end_time'])
        #活动说明
        self.tc.input_activity_desc(data['activity_desc'])
        #保存-确认
        self.tc.click_save_button()
        self.tc.click_sconfirm_btn()
        #断言
        self.tc.assert_add_success(
            data['activity_name'],
            data['status']
        )
        #删除
        self.tc.click_delete_button()
        self.tc.wait(3000)
        #删除断言
        self.tc.assert_add_success(
            data['activity_name'],
            data['status']
        )



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestActivityCreate1024
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

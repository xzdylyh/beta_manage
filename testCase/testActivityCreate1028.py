import os
import unittest
import ddt
from pages.activityCreate1028Page import ActivityCreate1028
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
class TestActivityCreate1028(unittest.TestCase):
    """升级赠礼"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/activity/create/1028')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate1028', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """升级赠礼"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        self.tc = ActivityCreate1028(self.url,self.driver,data['page_title'])
        self.tc.open
        #活动名称
        self.tc.input_activity_name(data['activity_name'])
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
        #活动卡类别
        self.tc.click_card_type()
        #赠送积分
        self.tc.input_credit(data['credit_num'])
        #赠送储值
        self.tc.input_charge(data['charge_num'])
        #活动开始时间
        self.tc.input_start_time(data['start_time'])
        #－结束时间
        self.tc.input_end_time(data['end_time'])
        #保存-确认
        self.tc.click_save_button()
        self.tc.click_sconfirm_btn()
        #断言
        self.tc.assert_add_success(data['start_time'])
        #删除
        self.tc.click_delete_button()



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestActivityCreate1028
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

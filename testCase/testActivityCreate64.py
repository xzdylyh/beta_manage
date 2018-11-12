import os
import unittest
import ddt
from pages.activityCreate64Page import ActivityCreate64
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    get_yaml_field
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)

@ddt.ddt
class TestActivityCreate64(unittest.TestCase):
    """营销－开卡关怀"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/create/64'

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass


    @ddt.data(*get_data('activityCreate64', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """开卡关怀"""
        self.tc = ActivityCreate64(
            self.url,
            self.driver,
            data['page_title']
        )
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
        #活动开始时间－结束时间
        self.tc.input_start_time(data['start_time'])
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
            TestActivityCreate64
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

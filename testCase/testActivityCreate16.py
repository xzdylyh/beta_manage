import os
import unittest
import ddt
from pages.activityCreate16Page import ActivityCreate16
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
class TestActivityCreate16(unittest.TestCase):
    """给新会员赠券"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/create/16'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('activityCreate16', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """给新会员赠券"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        #实例化page对象
        ts = ActivityCreate16(self.url, self.driver, data['Title'])
        # 打开给新会员赠券页面
        ts.open
        #活动名称
        ts.input_activity_name(data['activiy_name'])
        #新赠券
        ts.click_add_coupon()
        # 选择券类型;0代金券；1礼品券
        ts.click_coupon_type(data['coupon_type'])
        # 使用券
        ts.click_coupon_used(data['used_index'])
        #发券提醒;0不提醒；1短信提醒
        ts.click_send_remind(data['remind_index'])
        #券到期提醒；0不提醒；1短信提醒
        ts.click_expire(data['expire_index'])
        #发券日期
        ts.input_start_date(data['start_date'])
        #发券时间
        ts.input_start_time(data['start_time'])
        #下一步
        ts.click_next_button()
        #群发活动消息；0不发送；1发送提醒消息
        ts.click_activity_msg(data['activity_msg'])
        #提交
        ts.click_submit_button()
        #提交确认 #确认按钮索引；1为提交确认
        ts.click_sconfirm_btn(data['button_index'])
        #断言
        self.assertTrue(
            ts.assert_add_success(
                data['activiy_name'],
                data['activity_status']
            )
        )
        #删除
        ts.click_delete_button()
        #删除确认
        ts.click_sconfirm_btn(data['delete_sbtn'])
        ts.wait(3000)
        #断言删除
        self.assertFalse(
            ts.assert_add_success(
                data['activiy_name'],
                data['activity_status']
            )
        )





if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestActivityCreate16            )
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
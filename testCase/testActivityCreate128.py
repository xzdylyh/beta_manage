import os
import unittest
import ddt
from pages.activityCreate128Page import ActivityCreate128
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
    """营销－填资料赠券"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/create/128'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass



    @ddt.data(*get_data('activityCreate128', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """填资料赠券"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        po = ActivityCreate128(self.url, self.driver, data['Title'])
        po.open #打开赠券页面
        # 活动名称
        po.input_activity_name(data['Name'])
        #单击增加券
        po.click_add_coupon()
        #选择券;0代金券；1礼品券
        po.click_coupon_type(data['coupon_index'])
        #使用券;0第一张；1第二张，依此类推
        po.click_coupon_used(data['used_index'])
        #发券提醒;0不提醒；1短信提醒
        po.click_send_remind(data['remind_index'])
        #券到期提醒
        po.click_expire(data['exremind_index'])
        #活动说明
        po.input_activity_desc(data['desc'])
        #保存
        po.click_save_button()
        #保存确认
        po.click_sconfirm_btn()
        #断言
        self.assertTrue(
            po.assert_success(data['Name'], data['add_status'])
        )
        #终止
        po.click_stop_button()
        #终止确认
        po.click_cstop_button(data['button_index'])
        #单击终止确认弹框要等几秒才会消失
        po.wait(3000)
        #终止断言
        self.assertTrue(
            po.assert_success(data['Name'], data['stop_status'])
        )


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

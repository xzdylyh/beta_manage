import os
import unittest
import ddt
from pages.activityCreate512Page import ActivityCreate512
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
class TestActivityCreate512(unittest.TestCase):
    """营销－消费返券"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/activity/create/512')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('activityCreate512', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """消费返券"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        self.tc = ActivityCreate512(self.url, self.driver, data['page_title'])
        self.tc.open
        #活动名称
        self.tc.input_activity_name(data['activity_name'])
        #返券方式;0满额返券；1阶梯返券
        self.tc.click_rule_button(data['rule_index'])
        #单笔消费满x元
        self.tc.input_amount_rmb(data['amount'])
        #赠券设置-增加券
        self.tc.click_add_coupon()
        #券类型;0代金券；1礼品券
        self.tc.click_coupon_type(data['coupon_type'])
        #使用
        self.tc.click_coupon_used(data['coupon_index'])
        #菜品设置;0返券无需满足菜品；1返券需满足菜品(需要填菜品信息)
        self.tc.click_dishes_set(data['dishes_index'])
        #菜品
        self.tc.input_dishes_text(data['dishes_id'])
        #返券设置;0循环赠送；1当次消费仅赠送一次
        self.tc.click_return_coupon(data['ret_index'])
        #赠券上限;0无限制；1自定义张数
        self.tc.click_limit_radio(data['limit_index'])
        #赠券上限－自定义张数
        self.tc.input_custom_limit(data['limmit_num'])
        #奖励范围；0现金消费；1现金储值消费
        self.tc.click_return_cash(data['cash_index'])
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
        self.assertTrue(
            self.tc.assert_add_success(
                data['activity_name'],
                data['activity_status']
            )
        )
        #删除
        self.tc.click_delete_button()
        #断言
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
            TestActivityCreate512
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

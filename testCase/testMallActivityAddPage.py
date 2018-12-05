import os
import unittest
import ddt
from pages.mallactivityAddPage import MallactivityAdd
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
class TestMallactivityAdd(unittest.TestCase):
    """限时秒杀"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/mallactivity/add')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('mallactivityAdd', 'CASE1'))
    @reply_case_fail(num=1)
    def testCase1(self, data):
        """限时秒杀"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        tc = MallactivityAdd(self.url,self.driver,data['page_title'])
        tc.open
        #活动名称
        tc.input_activtity_name(data['activity_name'])
        #活动开始时间
        tc.input_start_date(data['start_date'])
        #活动结束时间
        tc.input_end_date(data['end_date'])
        #限购设置;0不限购;1限购,并填入数量
        tc.click_limit_shop(data['limit_index'], data['limit_num'])
        #增加商品
        tc.click_add_product()
        #选择商品;0选择第一个商品,依此类推
        tc.click_product_checkbox(data['checkbox_index'])
        #确认
        tc.click_confirm_button()
        #秒杀价格
        tc.input_price_text(data['ses_price'])
        #秒杀数量
        tc.input_number_text(data['ses_num'])
        #保存
        tc.click_save_button()
        #断言
        self.assertTrue(
            tc.assert_add_success(
                data['activity_name'],
                data['activity_status']
            )
        )

        #删除
        tc.click_del_button()
        #删除确认
        tc.click_confirm_button()
        tc.wait(3000)
        #断言
        self.assertFalse(
            tc.assert_add_success(
                data['activity_name'],
                data['activity_status']
            )
        )








if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestMallactivityAdd
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

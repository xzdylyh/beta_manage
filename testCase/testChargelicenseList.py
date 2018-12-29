import os
import unittest
import ddt
from pages.chargeListSusscessPage import ChargeListSusscess
from pages.chargelicenseListPage import ChargeLicenseList
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    genrandomstr,
    join_url
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)


@ddt.ddt
class TestChargelicense(unittest.TestCase):
    """储值授信"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/chargelicense/list')  # 储值授信入口
        cls.url_ = ""

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #  pass

    @ddt.data(*get_data('chargelicenseListPage', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """储值授信修改_增加"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.clist = ChargeLicenseList(self.url, self.driver, data['title'])
        self.clist.open
        # 获取修改之前额度
        old_num = self.clist.get_totalText()
        # 点击修改按钮
        self.clist.click_eidit_btn()
        # 选择增加
        self.clist.select_creditLimit(data['index'])
        # 输入增加金额
        self.clist.input_increase(data['increase'])
        # 输入减少金额
        self.clist.input_decrease(data['decrease'])
        # 输入预警额度
        self.clist.input_warningLimit(data['warningLimit'])
        # 输入手机号
        self.clist.input_phone(data['phone'])
        # 点击保存按钮
        self.clist.click_submit()
        # 保存成功，点击返回按钮
        self.slist = ChargeListSusscess(self.url_, self.driver,
                                        '授信规则设置 - 自动化测试专用')
        self.slist.clickBcakBtn()

        # 获取修改后的额度
        new_num = self.clist.get_totalText()
        # 判断是否修改成功
        if data['index'] == 0:
            # 判断增加额度是否成功
            self.assertTrue(self.clist.assertEditCreditLimitTrue(old_num,
                                                                 data['increase'],
                                                                 new_num))
        else:
            # 判断减少额度是否成功
            self.assertTrue(self.clist.assertEditCreditLimitTrue(old_num,
                                                                 data['decrease'],
                                                                 new_num)
                            )


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestChargelicense)
    ]
    suite.addTests(tests)
    filePath = os.path.join(gl.reportPath, 'Report.html')  # 确定生成报告的路径
    print(filePath)

    with open(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'UI自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yecc"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)


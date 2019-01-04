import os
import unittest
import ddt
from pages.actualcardOpencardPage import ActualCardOpen
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    join_url,
    rndint
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)
from lib.excel import Excel

@ddt.ddt
class TestActualCardOpen(unittest.TestCase):
    """实体卡开卡"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/actualcard/opencard')
        cls.toexcel = Excel(os.path.join(gl.dataPath, 'actualopencard.xls'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('actualcardopencard', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """实体卡开卡"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        actual = ActualCardOpen(self.url, self.driver, data['title'])
        actual.open
        #获取实体卡号
        card_no = self.toexcel.getCardNo(cell_col=1)
        print(card_no)
        #实全卡号
        actual.input_card_no(card_no)
        #手机号
        actual.input_mobile_text('1371865{}'.format(rndint(min=1000, max=9999)))
        #姓名
        actual.input_name_text(data['name'])
        #性别;0男；1女
        actual.click_sex_button(data['sex_index'])
        #生日；0公历；1农历
        actual.click_birth_button(data['birth_index'])
        #生日－格式2018－09－08
        actual.input_birth_text(data['birth_date'])
        #确认开卡
        actual.click_confirm_open()
        #断言
        self.assertTrue(actual.assert_success(data['card_assert']))



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestActualCardOpen)
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
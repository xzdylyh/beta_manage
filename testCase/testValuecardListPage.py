import os
from time import sleep
import unittest
import ddt
from pages.chargeListSusscessPage import ChargeListSusscess
from pages.valuecardListPage import ValueCardList
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
class TestValuecardList(unittest.TestCase):
    """储值卡--创建"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/valuecard/list')  # 储值卡入口
        cls.url_s = ""

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('valuecardListPage', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """创建储值卡--永久有效"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.vlist = ValueCardList(self.url, self.driver, data['title'])
        # 打开储值卡页面
        self.vlist.open
        # 点击开启按钮
        self.vlist.select_control(data['on-off'])
        # sleep(2)
        # 点击创建储值卡按钮，进入创建、编辑页面
        self.vlist.click_cardCreateBtn()
        # 输入储值名称
        card_name = data['name'] + genrandomstr(6)
        self.vlist.input_name(card_name)
        # 输入面额
        self.vlist.input_denomination(data['denomination'])
        # 输入售价
        self.vlist.input_price(data['price'])
        # 输入总量
        self.vlist.input_total(data['total'])
        # 选择有效期 0：永久有效；1：多少天后有效
        self.vlist.select_prepaid_term(data['index'])
        # 当选择有效期为1，输入天数
        self.vlist.input_prepaidTermCount(data['prepaidTermCount'])
        # 点击保存按钮
        self.vlist.clickSaveBtn()
        # 保存成，点击返回按钮
        self.slist = ChargeListSusscess(self.url_s, self.driver, data['title'])
        self.slist.clickBcakBtn()
        # 断言是否成功创建储值卡
        sleep(2)
        self.assertEqual(self.vlist.get_successNameText(), card_name)


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestValuecardList)
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








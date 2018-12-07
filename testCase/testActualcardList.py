import os
import unittest
import ddt
from time import sleep
from pages.chargeListSusscessPage import ChargeListSusscess
from pages.actualcardListPage import ActualcardList
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
class TestActualcard(unittest.TestCase):
    """申请创建实体卡"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/actualcard/list')
        cls.url_s = ''

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('actualcardListPage', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """ 创建卡"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.alist = ActualcardList(self.url, self.driver, data['title_first'])
        self.alist.open
        # 选择绑定实体卡需验证用户手机号，实体卡开卡需验证用户手机号
        self.alist.select_verify_checkbox(data['index'])
        # 申请实体卡
        self.alist.click_addcard_btn()
        # 输入批次名称
        name = data['name'] + genrandomstr(4)
        self.alist.input_batchName(name)
        # 卡类别属性
        self.alist.select_cardType(data['cardtype'])
        # 所属卡类别
        self.alist.select_cardCategory(data['cardcategory'])
        # 卡号生成规则
        self.alist.select_cardRule(data['cardrule'])
        # 开卡方式
        self.alist.select_cardWay(data['cardway'])
        # 是否上传手机号
        self.alist.select_uploadPhone(data['uploadphone'])
        # 上传文件
        sleep(2)
        if data['uploadphone'] != '%NONE%':
            self.alist.upload_csv_file(os.path.join(gl.dataPath,
                                                '随机卡号+手机号模版.csv')
                                       )

        # 申请张数
        self.alist.input_cardNumber(data['cardnumber'])
        # 开卡售价
        self.alist.input_cardPrice(data['cardprice'])
        # 保存
        self.alist.click_submitBtn()
        # 返回
        self.alist.clickBcakBtn()
        # 断言
        self.assertEqual(self.alist.get_successNameText(), name)


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestActualcard)
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
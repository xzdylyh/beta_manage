import os
import unittest
import ddt
from time import sleep
from pages.chargeListSusscessPage import ChargeListSusscess
from pages.cardcategoryPage import Cardcategory
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
class TestCardCategory(unittest.TestCase):
    """卡类别管理"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/cardcategory/index')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    @ddt.data(*get_data('cardCategory', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """添加卡类别"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.clist = Cardcategory(self.url, self.driver, data['title'])
        self.clist.open
        # 点击添加卡类别按钮
        self.clist.click_cardAdd()
        # 选择卡类别属性
        self.clist.select_cardattribute(data['cardindex'])
        # 输入卡类别名称
        self.clist.input_inputName(data['inputname'])
        # 选择卡面样式
        self.clist.select_cardType(data['cardtype'],
                                   os.path.join(gl.dataPath, 'back.png')
                                   )
        # 卡面名称使用
        self.clist.select_cardname(data['cardname'], os.path.join(gl.dataPath, 'logo.png'))
        # 选择储值
        self.clist.select_inputStored(data['inputstored'])
        sleep(2)
        # 选择积分
        self.clist.selcet_pointValue(data['pointvalue'])
        # 输入会员价
        self.clist.input_vipPrice(data['vipprice'])
        # 积分特权：每消费现金
        self.clist.input_creditPrice(data['creditprice'])
        # 输入积分特权内容
        self.clist.input_privilege(data['index'], data['privilege'])
        # 点击确定按钮
        self.clist.click_submit()
        self.assertEqual(self.clist.get_sussesscard_name(data['nameindex']), data['inputname'])
        # 点击删除按钮
        self.clist.click_remove(data['remove_index'])
        # 点击确定
        self.clist.click_sure()



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestCardCategory)
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





import os
import unittest
import ddt
import time
from pages.listCompaniesPage import ListCompaniesPage
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data,
    genrandomstr,
    join_url,
    createphone
)
from lib import (
    gl,
    HTMLTESTRunnerCN
)


@ddt.ddt
class TestListCompanies(unittest.TestCase):
    """集团消费"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/group/listCompanies')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('listCompanies', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """添加集团消费"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.list = ListCompaniesPage(self.url, self.driver,
                                      data['title']
                                      )
        self.list.open
        # 添加集团
        self.list.click_groupcreate()
        # 集团名称
        merbername = data['merbername'] + genrandomstr(6)
        self.list.input_merber_name(merbername)
        # 挂帐额度
        self.list.input_overdraft(data['overdraft'])
        # 联系人姓名
        self.list.input_contacts(data['contacts'])
        # 手机号
        phone = createphone()
        self.list.input_phone(phone)
        # 备注
        self.list.input_desc(data['desc'])
        # 保存
        self.list.click_save()
        # 首页集团名称
        self.list.input_groupper_name(merbername)
        # 查询
        self.list.click_search()
        # 断言是否添加成功
        self.assertEqual(self.list.get_group_name(), merbername)


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestListCompanies)
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

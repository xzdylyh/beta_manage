import os
import unittest
import ddt
from pages.roleAddPage import RoleAdd
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
class TestRoleAdd(unittest.TestCase):
    """积分排行"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/role/add')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass


    @ddt.data(*get_data('roleAdd', 'CASE1'))
    @reply_case_fail(num=3)
    def testCase1(self, data):
        """角色与权限－创建角色"""
        print('========★{}★========'.format(data['case_desc'])) #case描述
        tc = RoleAdd(self.url, self.driver, data['page_title'])
        tc.open
        #角色名称
        tc.input_role_name(data['role_name'])
        #备注
        tc.input_remark_text(data['role_remark'])
        #选择全部模块
        tc.click_select_all()
        #保存
        tc.click_save_button()
        #断言
        self.assertTrue(tc.assert_add_success(data['role_add']))






if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = [
        unittest.TestLoader().loadTestsFromTestCase(
            TestRoleAdd
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


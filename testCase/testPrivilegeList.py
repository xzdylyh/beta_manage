import os
import unittest
from time import sleep
import ddt
from pages.privilegeList import PrivilegeList
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
class TestpPrivilegeList(unittest.TestCase):
    """特权管理"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('privilege/list')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('privilegeList', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """特权管理"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.plist = PrivilegeList(self.url, self.driver, data['title'])
        self.plist.open
        # 新增特权
        self.plist.click_addprivilegebox()
        # 特权名称
        self.plist.input_privilege_name(data['privilegeName'])
        # 选择图标
        self.plist.select_privilege_icon(data['privilegeIcon'])
        # 选择图片
        self.plist.select_opt_icon_img(data['imgIndex'])
        # 点击确定
        self.plist.click_ok()
        # 选择是否展示特权
        self.plist.click_show(data['showIndex'])
        # 选择是否享受特权
        self.plist.click_enjoy(data['enjoyIndex'])
        # 输入特权说明内容
        self.plist.input_textarea(data['textarea'], data['areaIndex'])
        #  点击保存
        self.plist.click_save()
        # 断言是否保存成功
        self.assertEqual(self.plist.get_name(), data['privilegeName'])
        # 删除特权
        self.plist.click_delete()
        # 确定删除
        self.plist.click_sure()

if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestpPrivilegeList)
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
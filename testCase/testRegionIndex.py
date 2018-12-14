import os
import unittest
import ddt
from time import sleep
from pages.regionIndexPage import RegionIndex
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
class TestRegionIndex(unittest.TestCase):
    """区域设置"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/region/index')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('regionIndex', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """区域设置"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.rIndex = RegionIndex(self.url, self.driver, data['title'])
        self.rIndex.open
        # 添加一级
        self.rIndex.click_create_area()
        # 区域名称
        self.rIndex.input_area_name(data['areaName'], data['areaIndex'])
        # 保存
        self.rIndex.click_save()
        # 断言是否保存成功
        self.assertEqual(self.rIndex.get_name(), data['areaName'])
        # 删除
        self.rIndex.click_delete()
        # 确定
        self.rIndex.click_sure()


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestRegionIndex)
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
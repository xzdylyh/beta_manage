import os
import unittest
from time import sleep
import ddt
from pages.queueListPage import queueListPage
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
class TestQueueList(unittest.TestCase):
    """等位设置"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/queue/list')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*(get_data('queueList', 'CASE1')))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """等位设置"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.qlist = queueListPage(self.url, self.driver, data['title'])
        self.qlist.open
        # 开启
        sleep(2)
        self.qlist.select_state(data['state'])
        # 创建等位队列
        self.qlist.click_create()
        #  输入列队名称
        self.qlist.input_queue_name(data['queueName'])
        # 输入人数范围
        self.qlist.input_min_range(data['minRange'])
        self.qlist.input_max_range(data['maxRange'])
        # 选择叫号前缀
        self.qlist.select_prefix(data['prefixNum'])
        # 输入起始号码
        self.qlist.input_start_num(data['startNum'])
        # 选择号码格式
        self.qlist.select_format(data['format'])
        # 选择到号提醒方式，并输入提前多少桌提醒
        self.qlist.select_warn(data['warn'], data['warnNum'])
        # 保存
        self.qlist.click_save()
        # 判断是否保存成功
        self.assertEqual(self.qlist.get_name(), data['queueName'])
        # 删除
        self.qlist.click_remove()
        self.qlist.click_sure()


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestQueueList)
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

"""
create:2018/10/23
by:yhleng
"""
import os
import unittest
import ddt
from beta_manage.pages.activityCreate63Page import ActivityCreate63
from beta_manage.lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data
)
from beta_manage.lib import (
    gl,
    HTMLTESTRunnerCN
)




@ddt.ddt
class TestActivityCreate63(unittest.TestCase):
    """膨胀红包"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = 'http://manage.beta.acewill.net/activity/create/63'

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass




    @ddt.data(*get_data('activityCreate63', 'CASE1'))
    @reply_case_fail(num=1)
    def testCase1(self, data):
        """膨胀红包"""
        self.ac = ActivityCreate63(self.url, self.driver, data['title'])
        # 打开创建营销活动页面
        self.ac.open
        #活动名称
        self.ac.input_activity_name(data['activity_name'])
        #活动开始时间
        self.ac.input_activity_stime(data['activity_stime'])
        #活动结束时间
        self.ac.input_activity_etime(data['activity_etime'])
        #活动说明
        self.ac.input_activity_desc(data['activity_desc'])
        #上传商家logo
        # 0上传logo；
        # 1奖品一奖品展示图；2奖品一奖品缩略图
        # 3奖品二奖品展示图；4奖品二奖品缩略图
        # 5奖品三奖品展示图；6奖品三奖品缩略图
        # 6顶部宣传纸
        self.ac.click_ac_upload(
            data['upload'],
            os.path.join(gl.dataPath, 'upload.png')
        )




if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestActivityCreate63)
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

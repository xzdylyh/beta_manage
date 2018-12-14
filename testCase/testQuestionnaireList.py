import os
import unittest
from time import sleep
import ddt
from pages.questionnaireListPage import QuestionnaireList
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
class TestQuestionnaireList(unittest.TestCase):
    """问卷设置"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/questionnaire/list')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*get_data('questionnaireList', 'CASE1'))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """问卷设置"""

        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.qlist = QuestionnaireList(self.url, self.driver, data['title'])
        self.qlist.open
        # 点击创建问卷
        self.qlist.click_create()
        # 选择问卷版本
        self.qlist.select_edition(data['editon'])
        # 输入主题
        self.qlist.input_subject(data['subject'])
        # 输入问题题目
        self.qlist.input_problem_title(data['problimTitle'],
                                       data['titleIdex']
                                       )
        # 输入选项内容
        self.qlist.input_option(data['option_1'], data['optionIndex_1'])
        self.qlist.input_option(data['option_2'], data['optionIndex_2'])
        # 保存
        self.qlist.click_save()
        # 确认
        self.qlist.click_sure()
        # 断言是否保存成功
        self.assertEqual(self.qlist.get_name(), data['subject'])
        # 删除问卷
        self.qlist.click_remove(data['removeIndex'])
        # 删除确认
        self.qlist.click_remove_sure()


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestQuestionnaireList)
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
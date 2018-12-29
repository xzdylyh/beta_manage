import os
import unittest
import ddt
import time
from pages.memberListPage import MemberList
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
class TestMemberList(unittest.TestCase):
    """修改会员卡资料"""
    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/member/list')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    @ddt.data(*(get_data('memberlist', 'CASE1')))
    @reply_case_fail(num=3)
    def testcase1(self, data):
        """修改会员卡资料"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        mlist = MemberList(self.url, self.driver, data['Title'])
        mlist.open
        #输入会员卡号
        mlist.input_card_no(data['cardNo'])
        #点击查询
        mlist.click_serarch_button()
        #点击修改资料
        mlist.click_change_button()
        #输入卡名称
        mlist.input_card_name(data['cardName'])
        #性别
        mlist.click_sex_button(data['sex_index'])
        #会员等级
        mlist.select_member_level(data['member_level'])
        #公历
        mlist.click_date_type(data['date_type'])
        #生日
        mlist.input_birthday_text(data['birthday'])
        #确认
        mlist.click_confirm_button()
        #断言
        self.assertTrue(mlist.assert_success_text(data['date_type']))







if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestMemberList)
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

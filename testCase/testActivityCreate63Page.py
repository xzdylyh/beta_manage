"""
create:2018/10/23
by:yhleng
"""
import os
import unittest
import ddt
from pages.activityCreate63Page import ActivityCreate63
from lib.scripts import (
    select_Browser_WebDriver,
    reply_case_fail,
    get_data
)
from lib import (
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



    def prize_set(self, **data):
        """奖品设置共三个"""
        #>>>>>>>>>>>>>>>>>>>>>>奖品一<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #添加优惠券;0奖品一添加；1奖品二添加；2奖品三添加；
        self.ac.click_add_coupon(data['acindex'])
        #选择券索引；0奖品一；1奖品二；2奖品三
        #类型；0代金券；1礼品券
        self.ac.click_coupon_type(
            data['prize_index'],
            data['coupon_type']
        )
        #使用 #使用券0为第一张券；以此类推
        self.ac.click_used(data['used_index'])
        #奖品名称 #奖品名称元素索引;0为奖品一；1为奖品二；2为奖品三
        self.ac.input_prize_name(
            data['prize_name'],
            data['pname_index']
        )

        self.ac.input_prize_value(
            data['prize_value'],
            data['pvalue_index']
        )

        self.ac.click_ac_upload(
            data['upload'],
            os.path.join(gl.dataPath, 'upload.png')
        )

        self.ac.click_ac_upload(
            data['upload1'],
            os.path.join(gl.dataPath, 'upload.png')
        )


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

        # #奖品一数据
        # self.prize_set(
        #             acindex=data['acindex'], ##0奖品一；1奖品二；2奖品三 增加券
        #             prize_index=data['prize_index'], #选择券索引；0奖品一；1奖品二；2奖品三
        #             coupon_type=data['coupon_type'], #类型；0代金券；1礼品券
        #             used_index=data['used_index'], #使用券0为第一张券；以此类推
        #             prize_name=data['prize_name'], #奖品名称
        #             pname_index=data['pname_index'], #奖品名称元素索引;0为奖品一；1为奖品二；2为奖品三
        #             prize_value=data['prize_value'], #兑换所需人数
        #             pvalue_index=data['pvalue_index'], #兑换所需人数元素索引；0为奖品二；1为奖品3
        #             upload=data['upload1'], #上传1，奖品一
        #             upload1=data['upload1_1'] #上传2,奖品一
        #         )
        # 奖品二数据
        # self.prize_set(
        #     acindex=data['acindex2'], ##0奖品一；1奖品二；2奖品三 增加券
        #     prize_index=data['prize_index2'], #选择券索引；0奖品一；1奖品二；2奖品三
        #     coupon_type=data['coupon_type2'], #类型；0代金券；1礼品券
        #     used_index=data['used_index2'], #使用券0为第一张券；以此类推
        #     prize_name=data['prize_name2'], #奖品名称
        #     pname_index=data['pname_index2'], #奖品名称元素索引;0为奖品一；1为奖品二；2为奖品三
        #     prize_value=data['prize_value2'], #兑换所需人数
        #     pvalue_index=data['pvalue_index2'], #兑换所需人数元素索引；0为奖品二；1为奖品3
        #     upload=data['upload2'], #上传3，奖品一
        #     upload1=data['upload2_2'] #上传4,奖品一
        # )


        self.prize_set(
            acindex=data['acindex'], ##0奖品一；1奖品二；2奖品三 增加券
            prize_index=data['prize_index'], #选择券索引；0奖品一；1奖品二；2奖品三
            coupon_type=data['coupon_type'], #类型；0代金券；1礼品券
            used_index=data['used_index'], #使用券0为第一张券；以此类推
            prize_name=data['prize_name'], #奖品名称
            pname_index=data['pname_index'], #奖品名称元素索引;0为奖品一；1为奖品二；2为奖品三
            prize_value=data['prize_value'], #兑换所需人数
            pvalue_index=data['pvalue_index'], #兑换所需人数元素索引；0为奖品二；1为奖品3
            upload=data['upload1'], #上传1，奖品一
            upload1=data['upload1_1'] #上传2,奖品一
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

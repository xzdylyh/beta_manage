import os
import unittest
import ddt
from time import sleep
from pages.mallProductListPage import mallProductList
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
class TestMallProductList(unittest.TestCase):
    """商城设置"""

    @classmethod
    def setUpClass(cls):
        cls.driver = select_Browser_WebDriver()
        cls.url = join_url('/mall/productList')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    @unittest.skip('调试')
    @ddt.data(*get_data('mallProductList', 'CASE1'))
    @reply_case_fail(num=1)
    def testcase1(self, data):
        """商城设置-添加商品-电子优惠券"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.mlist = mallProductList(self.url, self.driver, data['title'])
        self.mlist.open
        # 功能状态
        self.mlist.selcet_mall_list_state(data['liststate'])
        # 添加商品
        self.mlist.click_addGoods()
        # 选择商品类型
        self.mlist.select_goods_type(data['goodsType'])
        # 商品名称
        self.mlist.input_product_name(data['productName'])
        # 简介
        self.mlist.input_product_desc(data['productDesc'])
        # 添加券
        self.mlist.click_weCoupon_btn(data['couponType'])
        # 使用券
        self.mlist.selectCoupon(data['couponIndex'])
        # 售卖方式
        self.mlist.select_sale_state(data['saleState'])
        # 标准价格
        self.mlist.input_price(data['price'])
        # 积分
        self.mlist.inpiut_integral(data['integral'])
        # 等级折扣
        self.mlist.select_gradePrice(data['gradePrice'],
                                     data['gradeindex'],
                                     data['singleGradePrice']
                                     )

        # 库存数量
        self.mlist.input_product_onhand(data['product_onhand'])
        # 限购设置、限购数量
        self.mlist.select_limit_buy(data['limitbuy'],
                                    data['limitbuycount']
                                    )
        # 商品类别
        self.mlist.click_good_way()
        # 下一步
        self.mlist.click_next()
        # 保存
        self.mlist.click_submit()
        # 断言是否保存成功
        self.assertEqual(self.mlist.get_name(), data['productName'])
        # 删除
        self.mlist.click_remove()
        # 确定
        self.mlist.click_sure()

    @unittest.skip('调试')
    @ddt.data(*get_data('mallProductList', 'CASE2'))
    @reply_case_fail(num=3)
    def testcase2(self, data):
        """商城设置-实物商品"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.mlist = mallProductList(self.url, self.driver, data['title'])
        self.mlist.open
        # 功能状态
        self.mlist.selcet_mall_list_state(data['liststate'])
        # 添加商品
        self.mlist.click_addGoods()
        # 选择商品类型
        self.mlist.select_goods_type(data['goodsType'])
        # 商品名称
        self.mlist.input_product_name(data['productName'])
        # 简介
        self.mlist.input_product_desc(data['productDesc'])
        # 介绍
        self.mlist.input_product_intro(data['productintro'])
        sleep(2)
        # 上传
        self.mlist.up_load(os.path.join(gl.dataPath, 'back.png'))
        # 售卖方式
        self.mlist.select_sale_state(data['saleState'])
        # 库存\规格
        self.mlist.select_spec_state(data['specstate'])
        # 单规格标准价格
        self.mlist.input_single_price(data['singleprice'])
        # 单规格库存数量
        self.mlist.input_single_onhand(data['singleonhand'])
        # 单规格积分
        self.mlist.input_single_integral(data['singleintegral'])
        # 规格名称
        self.mlist.input_spec_name(data['specname'])
        # 多规格标准价格
        self.mlist.input_spec_price(data['specprice'])
        # 多规格库存数量
        self.mlist.input_spec_onhand(data['speconhand'])
        # 多规格积分
        self.mlist.input_spec_integral(data['specintegral'])
        # 等级折扣
        self.mlist.select_gradePrice(data['gradePrice'],
                                     data['gradeindex'],
                                     data['singleGradePrice']
                                     )
        # 限购设置、限购数量
        self.mlist.select_limit_buy(data['limitbuy'],
                                    data['limitbuycount']
                                    )
        # 商品类别
        self.mlist.click_good_way()
        # 下一步
        self.mlist.click_next()
        # 保存
        self.mlist.click_submit()
        # 断言是否保存成功
        self.assertEqual(self.mlist.get_name(), data['productName'])
        # 删除
        self.mlist.click_remove()
        # 确定
        self.mlist.click_sure()

    @ddt.data(*get_data('mallProductList', 'CASE3'))
    @reply_case_fail(num=1)
    def testcase3(self, data):
        """商城设置-添加商品-会员等级"""
        print('========★{}★========'.format(data['case_desc']))  # case描述
        self.mlist = mallProductList(self.url, self.driver, data['title'])
        self.mlist.open
        # 功能状态
        self.mlist.selcet_mall_list_state(data['liststate'])
        # 添加商品
        self.mlist.click_addGoods()
        # 选择商品类型
        self.mlist.select_goods_type(data['goodsType'])
        # 商品名称
        self.mlist.input_product_name(data['productName'])
        # 简介
        self.mlist.input_product_desc(data['productDesc'])
        # 选择会员等级
        self.mlist.select_grade_cardid(data['gradeCardId'])
        sleep(2)
        # 上传
        self.mlist.up_load(os.path.join(gl.dataPath, 'back.png'))
        # 售卖方式
        self.mlist.select_sale_state(data['saleState'])
        # 标准价格
        self.mlist.input_price(data['price'])
        # 积分
        self.mlist.inpiut_integral(data['integral'])
        # 等级折扣
        self.mlist.select_gradePrice(data['gradePrice'],
                                     data['gradeindex'],
                                     data['singleGradePrice']
                                     )

        # 库存数量
        self.mlist.input_product_onhand(data['product_onhand'])
        # 商品类别
        self.mlist.click_good_way()
        # 下一步
        self.mlist.click_next()
        # 保存
        self.mlist.click_submit()
        # 断言是否保存成功
        self.assertEqual(self.mlist.get_name(), data['productName'])
        # 删除
        self.mlist.click_remove()
        # 确定
        self.mlist.click_sure()



if __name__ == "__main__":
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(TestMallProductList)
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

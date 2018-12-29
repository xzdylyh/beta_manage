from selenium.webdriver.common.by import By
import autoit
from base.basepage import BasePage


class mallProductList(BasePage):
    """封装商城设置页面元素、操作"""
    # <<<<<<<<<<<<<<<定位>>>>>>>>>>>>>>>>>>>>>>>>>
    # 功能状态
    mall_list_state = (By.XPATH, "//input[@name='state']/..")
    # 商城设置
    mall_setPage_loc = (By.LINK_TEXT, '商城设置')
    # 添加商品
    mall_addGoods_loc = (By.ID, 'addGoodsBtn')
    # 商品类别管理
    mall_categoryPage_loc = (By.LINK_TEXT, '商品类别管理')
    # 商品排序
    mall_sortPage_loc = (By.LINK_TEXT, '商品排序')
    # 删除
    mall_delProduct_loc = (By.LINK_TEXT, '删除')
    # 确定
    # manager_sure_loc = (By.XPATH, "//button[contains(text(),'确定')]")
    mall_sure_loc = (By.XPATH, "//button[contains(text(),'确定')]")
    # 取消
    mall_cancle_loc = (By.XPATH, "//button[contains(text(),'取消')]")
    # 保存成功后的商品名称
    mall_name_loc = (By.XPATH,
                     "//div[@class='we-table-responsive mall-table-list']"
                     "/table[1]//tr[1]/td[1]//p"
                     )
    # 商品类型选择
    mall_goods_type_loc = (By.XPATH, "//div[@class='modal-body']/a")
    # 名称
    mall_product_name_loc = (By.ID, 'product_name')
    # 简介
    mall_product_desc_loc = (By.ID, 'product_desc')
    # 介绍
    mall_product_intro_loc = (By.ID, 'product_intro')
    # 添加券
    mall_dropdownCoupon_loc = (By.ID, 'dropdownCoupon')
    # 选择代金券/礼品券,0选择代金券，1选择礼品券:
    mall_selectMenuitem_loc = (By.XPATH, "//a[@role='menuitem']/..")
    # 使用代金券/礼品券
    mall_couponD_loc = (By.XPATH,
                        "//a[@data-toggle='coupon.apply']"
                        )
    # 上传按钮
    mall_upload_loc = (By.XPATH, "//div[@class='we-file file-sm']")
    # 售卖方式
    mall_sale_state_loc = (By.XPATH, "//input[@name='sale']/..")
    # 库存\规格
    mall_spec_state_loc = (By.XPATH, "//input[@name='specState']/..")
    # 规格名称
    mall_spec_name_loc = (By.NAME, 'specName[]')
    # 单规格标准价格
    mall_single_price_loc = (By.NAME, 'singlePrice')
    # 单规格库存数量
    mall_single_onhand_loc = (By.NAME, 'singleOnhand')
    # 单规格积分
    mall_single_integral_loc = (By.NAME, 'singleIntegral')
    # 多规格价格
    mall_spec_price_loc = (By.NAME, 'specPrice[]')
    # 多规格库存数量
    mall_spec_onhand_loc = (By.NAME, 'specOnhand[]')
    # 多规格积分
    mall_spec_integral_loc = (By.NAME, 'specIntegral[]')
    # 添加商品规格
    mall_add_spec_loc = (By.CLASS_NAME,
                         'mall-spec-detail mall-spec-btn add-spec-rule'
                         )
    # 删除商品规格
    mall_del_mall_loc = (By.XPATH, "//[@data-toggle='mall.del']")
    # 标准价格
    mall_price_loc = (By.NAME, 'price')
    # 积分
    mall_integral_loc = (By.NAME, 'integral')
    # 等级折扣
    mall_gradePrice_loc = (By.XPATH,
                           "//input[@name='gradePrice']/.."
                           )
    # 选择等级
    mall_grade_name_loc = (By.NAME, 'singleGrade[]')
    # 折扣
    mall_singleGradePrice_loc = (By.NAME, 'singleGradePrice[]')
    # 添加等级
    mall_add_grade_loc = (By.CLASS_NAME, 'mall-grade-btn add-grade')
    # 删除等级
    mall_del_grade_loc = (By.CLASS_NAME, 'mall-grade-del')
    # 库存数量
    mall_product_onhand_loc = (By.ID, 'product_onhand')
    # 限购设置
    mall_limit_buy_loc = (By.XPATH,
                          "//input[@name='limit_buy']/.."
                          )
    # 限购数量
    mall_limit_buycount_loc = (By.XPATH,
                               "//input[@name='limitBuyCount']")
    # 商品类别
    mall_good_way_loc = (By.CLASS_NAME, 'checkbox-inline')
    # 下一步
    mall_next_loc = (By.XPATH,
                     "//div[@id='step1']//button[.='下一步']"
                     )
    # 完成
    mall_submit_loc = (By.XPATH, "//button[contains(text(),'完成')]")
    # 上一步
    mall_returnToStep1_loc = (By.XPATH, "//a[contains(text(),'上一步')]")
    # 会员等级
    mall_grade_CardId_loc = (By.NAME, 'gradeCardId')
    # <<<<<<<<<<<<<<<<操作>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def selcet_mall_list_state(self, liststate):
         """选择功能状态"""
         self.click_btn_index('功能状态 ', liststate,
                              *(self.mall_list_state)
                              )

    def click_addGoods(self):
        """点击添加商品"""
        self.click_button('添加商品', *(self.mall_addGoods_loc))

    def select_goods_type(self, goodstype):
        """选择商品类型"""
        self.click_btn_index('商品类型', goodstype,
                             *(self.mall_goods_type_loc)
                             )

    def input_product_name(self, productname):
        """输入商品名称"""
        self.clear_input_text(*(self.mall_product_name_loc))
        self.input_text(productname, '商品名称',
                        *(self.mall_product_name_loc)
                        )

    def input_product_desc(self, productdesc):
        """输入简介"""
        self.clear_input_text(*(self.mall_product_desc_loc))
        self.input_text(productdesc, '简介',
                        *(self.mall_product_desc_loc)
                        )

    def input_product_intro(self, productintro):
        """输入介绍"""
        self.clear_input_text(*(self.mall_product_intro_loc))
        self.input_text(productintro, '介绍',
                        *(self.mall_product_intro_loc)
                        )

    def click_weCoupon_btn(self, index):
        """点击"+",添加优惠券按钮,然后在进行代金券/礼品券的选择
            0:代金券
            1：礼品券
        """
        # 点击添加优惠券按钮
        self.click_button('添加优惠券按钮',
                          *(self.mall_dropdownCoupon_loc))
        # 选择代金券/礼品券
        self.click_btn_index('选择代金券/礼品券', index,
                             *(self.mall_selectMenuitem_loc)
                             )

    def selectCoupon(self, index):
        """使用代金券/礼品券，存在代金券/礼品券，点击使用按钮"""
        self.click_btn_index(
            '代金券/礼品券',
            index,
            *(self.mall_couponD_loc)
        )

    def up_load(self, path):
        """上传图片"""
        self.click_button('上传', *(self.mall_upload_loc))
        # autoit处理
        autoit.control_set_text(
            '打开',
            '[Class:Edit; instance:1]',
            path
        )
        autoit.control_click(
            '打开',
            '[Class:Button; INSTANCE:1]'
        )

    def select_sale_state(self, salestate):
        """选择售卖方式"""
        self.click_btn_index('售卖方式', salestate,
                             *(self.mall_sale_state_loc)
                             )

    def select_spec_state(self, specstate):
        """选择库存\规格"""
        self.click_btn_index('库存\规格', specstate,
                             *(self.mall_spec_state_loc)
                             )

    def input_spec_name(self, specname):
        """输入规格名称"""
        self.input_text(specname, '规格名称', *(self.mall_spec_name_loc))

    def input_single_price(self, singleprice):
        """输入单规格价格"""
        if singleprice != '%NONE%':
            self.clear_input_text(*(self.mall_single_price_loc))
        self.input_text(singleprice, '价格',
                        *(self.mall_single_price_loc)
                        )

    def input_single_onhand(self, singleonhand):
        """输入单规格库存数量"""
        if singleonhand != '%NONE%':
            self.clear_input_text(*(self.mall_single_onhand_loc))
        self.input_text(singleonhand, '库存数量',
                        *(self.mall_single_onhand_loc)
                        )

    def input_single_integral(self, singleintegral):
        """输入单规格积分"""
        if singleintegral != '%NONE%':
            self.clear_input_text(*(self.mall_single_integral_loc))
        self.input_text(singleintegral, '积分',
                        *(self.mall_single_integral_loc)
                        )

    def input_spec_integral(self, specintegral):
        """输入多规格积分"""
        if specintegral != '%NONE%':
            self.clear_input_text(*(self.mall_spec_integral_loc))
        self.input_text(specintegral, '积分',
                        *(self.mall_spec_integral_loc)
                        )

    def input_spec_price(self, specprice):
        """输入多规格价格"""
        if specprice != '%NONE%':
            self.clear_input_text(*(self.mall_spec_price_loc))
        self.input_text(specprice, '价格',
                        *(self.mall_spec_price_loc)
                        )

    def input_spec_onhand(self, speconhand):
        """输入多规格库存数量"""
        if speconhand != '%NONE%':
            self.clear_input_text(*(self.mall_spec_onhand_loc))
        self.input_text(speconhand, '库存数量',
                        *(self.mall_spec_onhand_loc)
                        )

    def input_price(self, price):
        """输入标准价格"""
        if price != '%NONE%':
            self.clear_input_text(*(self.mall_price_loc))
        self.input_text(price, '标准价格', *(self.mall_price_loc))

    def inpiut_integral(self, integral):
        """输入积分"""
        if integral != '%NONE%':
            self.clear_input_text(*(self.mall_integral_loc))
        self.input_text(integral, '积分',
                        *(self.mall_integral_loc)
                        )

    def select_gradePrice(self, gradePrice, gradeindex, singleGradePrice):
        """选择等级折扣"""
        self.click_btn_index('等级折扣', gradePrice,
                             *(self.mall_gradePrice_loc)
                             )
        if gradePrice == 1:
            self.select_and_input_grade(gradeindex, singleGradePrice)

    def select_and_input_grade(self, gradeindex, singleGradePrice):
        """选择等级，输入折扣"""
        self.select_list(*(self.mall_grade_name_loc)).\
            select_by_index(gradeindex)
        self.input_text(singleGradePrice, '折扣',
                        *(self.mall_singleGradePrice_loc))

    def click_add_grade(self):
        """添加等级"""
        self.click_button('添加等级', *(self.mall_add_grade_loc))

    def click_del_grade(self):
        """删除等级"""
        self.click_button('删除等级', *(self.mall_del_grade_loc))

    def input_product_onhand(self, productonhand):
        """输入库存数量"""
        self.clear_input_text(*(self.mall_product_onhand_loc))
        self.input_text(productonhand, '库存数量',
                        *(self.mall_product_onhand_loc)
                        )

    def select_limit_buy(self, limitbuy, limitbuycount):
        """选择限购设置"""
        self.click_btn_index('限购设置', limitbuy,
                             *(self.mall_limit_buy_loc)
                             )
        if limitbuy == 1:
            self.clear_input_text(*(self.mall_limit_buycount_loc))
            self.input_text(limitbuycount, '限购数量',
                            *(self.mall_limit_buycount_loc)
                            )

    def click_good_way(self):
        """选择商品类别"""
        self.click_button('商品类别', *(self.mall_good_way_loc))

    def click_next(self):
        """点击下一步"""
        self.click_button('下一步', *(self.mall_next_loc))

    def click_submit(self):
        """点击保存"""
        self.click_button('保存', *(self.mall_submit_loc))

    def click_returnToStep1(self):
        """点击返回"""
        self.click_button('返回', *(self.mall_returnToStep1_loc))

    def click_remove(self):
        """点击删除"""
        self.click_button('删除', *(self.mall_delProduct_loc))

    def click_sure(self):
        """点击确定"""
        self.click_button('确定', *(self.mall_sure_loc))

    def get_name(self):
        """获取保存后的商品名称"""
        name = self.get_tag_text('text', *(self.mall_name_loc))
        self.get_image
        return name

    def select_grade_cardid(self, gradeCardId):
        """选择会员等级"""
        self.select_list(*(self.mall_grade_CardId_loc)).\
            select_by_index(gradeCardId)

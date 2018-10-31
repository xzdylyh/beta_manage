#_*_coding=utf8_*_
"""
__doc__:
create:2018/10/27
by: yhleng
"""
import os

import time
from PIL import Image
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    UnexpectedAlertPresentException
)

from pos.lib import gl
from pos.lib.scripts import (
    getYamlfield,
    Replay,
    hightlightConfig
)


class BasePage:
    """PO公共方法类"""
    def __init__(self, baseurl, driver, pagetitle):
        """
        初始化,driver对象及数据
        :param baseurl: 目标地址
        :param driver: webdriver对象
        :param pagetitle: 用来断言的目标页标题
        """
        self.base_url = baseurl
        self.driver = driver
        self.pagetitle = pagetitle



    #－－－－－－－－－－－－－－－－－
    # 功能描述：所有公共方法，都写在以下
    # －－－－－－－－－－－－－－－－－

    #打开浏览器
    def _open(self, url, pagetitle):
        """
        打开浏览器，并断言标题
        :param url: 目标地址
        :param pagetitle: 目标页标题
        :return: 无
        """
        self.driver.maximize_window()
        self.driver.get(url)

        self.driver.implicitly_wait(10)
        self.getImage
        assert self.driver.title, pagetitle
        self.driver.implicitly_wait(0)


    def isDisplayTimeOut(self, element, timeSes):
        """
        在指定时间内，轮询元素是否显示
        :param element: 元素对象
        :param timeSes: 轮询时间
        :return: bool
        """
        start_time = int(time.time()) #秒级时间戳
        timeSes = int(timeSes)
        while (int(time.time())-start_time) <= timeSes:
            if element.is_displayed():
                return True
            self.wait(500)

        self.getImage
        return False


    def find_element(self, *loc):
        """
        在指定时间内，查找元素；否则抛出异常
        :param loc: 定位器
        :return: 元素 或 抛出异常
        """
        TimeOut = 20
        try:
            self.driver.implicitly_wait(TimeOut) #智能等待；超时设置

            element = self.driver.find_element(*loc) #如果element没有找到，到此处会开始等待
            if self.isDisplayTimeOut(element, TimeOut):
                self.hightlight(element)  #高亮显示
                self.driver.implicitly_wait(0)  # 恢复超时设置
            else:
                raise ElementNotVisibleException #抛出异常，给except捕获
            return element
        except (NoSuchElementException, ElementNotVisibleException) as ex:
            self.getImage
            raise ex
        else:
            self.getImage


    @hightlightConfig('HightLight')
    def hightlight(self, element):
        """
        元素高亮显示
        :param element: 元素对象
        :return: 无
        """
        # arguments[0] 为element
        # arguments[1]为"border: 2px solid red;"
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;" #边框border:2px; red红色
        )


    def getElementImage(self, element):
        """
        截图,指定元素图片
        :param element: 元素对象
        :return: 无
        """
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(
            gl.imgPath,
            '%s.png' % str(timestrmap)
        )

        #截图，获取元素坐标
        self.driver.save_screenshot(imgPath)
        left = element.location['x']
        top = element.location['y']
        elementWidth = left + element.size['width']
        elementHeight = top + element.size['height']

        picture = Image.open(imgPath)
        picture = picture.crop(
            (
                left,
                top,
                elementWidth,
                elementHeight
            )
        )
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(
            gl.imgPath, '%s.png' % str(timestrmap)
        )
        picture.save(imgPath)
        print('screenshot:', timestrmap, '.png')


    @property
    def getImage(self):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join(
            gl.imgPath,
            '%s.png' % str(timestrmap)
        )

        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png')



    def find_elements(self, *loc):
        '''批量找标签'''
        TimeOut = 20 #智能等待时间
        try:
            self.driver.implicitly_wait(TimeOut) #智能等待；此贯穿self.driver整个生命周期
            elements = self.driver.find_elements(*loc)

            self.driver.implicitly_wait(0) #恢复等待
            return elements

        except NoSuchElementException as ex:
            self.getImage  # 截取图片
            raise ex


    def iterClick(self, *loc):
        '''批量点击某元素'''
        element = self.find_elements(*loc)
        for e in element:
            e.click()


    def iterInput(self, text=None, *loc):
        """
        批量输入
        :param text: 输入内容;为list
        :param loc: 定位器(By.XPATH,'//*[@id='xxxx']/input')
        :return: 无
        """
        elements = self.find_elements(*loc)
        for i, e in enumerate(elements):
            self.wait(1000)
            #e.clear()
            e.send_keys(list(text)[i])


    #文本框输入
    def send_keys(self, content, *loc):
        '''
        :param content: 文本内容
        :param itype: 如果等1，先清空文本框再输入。否则不清空直接输入
        :param loc: 文本框location定位器
        :return:
        '''
        inputElement = self.find_element(*loc)
        #inputElement.clear()
        inputElement.send_keys(content)

    def clearInputText(self, *loc):
        '''清除文本框内容'''
        self.find_element(*loc).clear()



    def addCookies(self, ck_dict):
        '''
        增加cookies到浏览器
        :param ck_dict: cookies字典对象
        :return: 无
        '''
        for key in ck_dict.keys():
            self.driver.add_cookie(
                {
                    "name":key,
                    "value":ck_dict[key]
                }
            )

    def isExist(self, *loc):
        #isDisable
        '''
        元素存在,判断是否显示
        :param loc: 定位器
        :return: 元素存在并显示返回True;否则返回False
        '''
        TimeOut = 20
        try:
            self.driver.implicitly_wait(TimeOut)

            element = self.driver.find_element(*loc)
            if self.isDisplayTimeOut(element, TimeOut):
                self.hightlight(element)
                return True
            else:
                return False
            self.driver.implicitly_wait(0)
        except (
                NoSuchElementException,
                ElementNotVisibleException,
                UnexpectedAlertPresentException) as ex:
            self.getImage #10秒还未找到显示的元素
            return False



    def isOrNoExist(self, *loc):
        """
        判断元素,是否存在
        :param loc: 定位器(By.ID,'kw')
        :return: True 或 False
        """
        TimeOut = 60
        try:
            self.driver.implicitly_wait(TimeOut)
            e = self.driver.find_element(*loc)

            """高亮显示,定位元素"""
            self.hightlight(e)

            self.driver.implicitly_wait(0)
            return True
        except NoSuchElementException as ex:
            self.getImage #10秒还未找到元素，截图
            return False


    def isExistAndClick(self, *loc):
        '''如果元素存在则单击,不存在则忽略'''
        print('Click:{0}'.format(loc))

        TimeOut = 3 #超时 时间
        try:
            self.driver.implicitly_wait(TimeOut)

            element = self.driver.find_element(*loc)
            self.hightlight(element)
            element.click()
            self.driver.implicitly_wait(0)
        except NoSuchElementException as ex:
            pass

    def isExistAndInput(self, text, *loc):
        '''如果元素存在则输入,不存在则忽略'''
        print('Input:{0}'.format(text))

        TimeOut = 3
        try:
            self.driver.implicitly_wait(TimeOut)

            element = self.driver.find_element(*loc)
            self.hightlight(element) #高亮显示
            element.send_keys(str(text).strip())

            self.driver.implicitly_wait(0)
        except (NoSuchElementException, ElementNotVisibleException) as ex:
            pass


    def getTagText(self, txtName, *loc):
        """
        获取元素对象属性值
        :param propertyName: 属性名称
        :param loc: #定位器
        :return: 属性值 或 raise
        """
        Timeout = 20
        try:
            self.driver.implicitly_wait(Timeout)

            element = self.find_element(*loc)
            self.hightlight(element) #高亮显示

            #获取属性
            proValue = getattr(element, str(txtName))
            self.driver.implicitly_wait(0)
            return proValue
        except (NoSuchElementException, NameError) as ex:
            self.getImage #错误截图
            raise ex




    @property
    def switch_window(self):
        """
        切换window窗口,切换一次后退出
        :return: 无
        """
        curHandle = self.driver.current_window_handle
        allHandle = self.driver.window_handles
        for h in allHandle:
            if h != curHandle:
                self.driver.switch_to.window(h)
                break


    def wait(self, ms):
        """
        线程休眼时间
        :param ms: 毫秒
        :return: 无
        """
        ms = float(ms) / 1000
        time.sleep(ms)

    @Replay
    def jsClick(self, desc, *loc):
        """通过js注入的方式去，单击元素"""
        print('Click{}:{}'.format(desc, loc))
        element = self.find_element(*loc)
        self.driver.execute_script("arguments[0].click();", element)


    @Replay
    def inputText(self, text, desc, *loc):
        """
        输入文本操作
        :param text:
        输入文本内容;如果为%BLANK%，为清除输入框默认值;
        输入文本内容；如果为%NONE%,为不做任何操作
        :param desc:
        :param loc:
        :return:
        """
        print('Input{}:{}'.format(desc, text))
        if str(text).strip().upper() == '%BLANK%':
            self.clearInputText(*loc)
        elif str(text).strip().upper() == '%NONE%':
            pass
        else:
            self.send_keys(text, *loc)


    @Replay
    def clickBtn(self, desc, *loc):
        """点击操作"""
        print('Click:{}{}'.format(desc, loc))
        if str(desc).strip().upper() == '%NONE%':
            pass
        else:
            self.find_element(*loc).click()


    @Replay
    def clickBtnIndex(self, desc, index, *loc):
        """
        点击操作，按索引，适用于findelemens方法
        :param desc: 描述
        :param index: 点击索引
        :param op: 如果是True则，不执行点击操作，为False则点击
        :param loc: 定位器
        :return: 无
        """
        print('Clicks:{}{}'.format(desc, loc))
        if index == '%NONE%':
            pass
        else:
            ele = self.find_elements(*loc)[int(index)]
            # 元素高亮显示
            self.hightlight(ele)
            # 元素单击
            ele.click()


    @Replay
    def selectTab(self, *loc):
        '''选择tab操作'''
        print('Select:{}'.format(loc))
        self.find_element(*loc).click()


    @property
    def open(self):
        """打开浏览器，写入cookies登录信息"""
        yamldict = getYamlfield(gl.configFile)
        ck_dict = yamldict['CONFIG']['Cookies']['LoginCookies']
        self._open(self.base_url, self.pagetitle)
        self.addCookies(ck_dict)
        self._open(self.base_url, self.pagetitle)


if __name__ == "__main__":
    pass

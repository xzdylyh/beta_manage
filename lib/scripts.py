"""
create:2018/10/23
by:yhleng
"""
import time
import os
import zipfile
from selenium import webdriver
import yaml
from lib import gl


def select_Browser_WebDriver():
    """
    根据config.yaml配置文件，来选择启动的浏览器
    :return:
    """
    #读取config.yam配置文件中，浏览器配置
    bro_name = get_yaml_field(gl.configFile)
    bro_name = bro_name['CONFIG']['Browser']

    #根据borName决定，启动，哪个浏览器
    if str(bro_name).strip().lower() == 'chrome':
        driver = webdriver.Chrome()
    elif str(bro_name).strip().lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    return driver



def write_ymal(path, data):
    """
    写YAML文件内容
    :param path: YAML文件路径
    :param data: 写入的数据
    :return: 无
    """
    with open(path, 'wb') as fp:
        yaml.dump(data, fp)


def get_yaml_field(path):
    """
    读取YAML内容
    :param path: xxxx.YAML文件所在路径
    :return: 指定节点内容
    """
    with open(path, 'rb') as fp:
        cont = fp.read()

    ret = yaml.load(cont)
    return ret


def get_run_flag(scenario_key, casename):
    """
    获取运行标记，来决定是否执行
    :param scenario_key:
    :return: Y 或 N
    """
    yamldict = get_yaml_field(
        os.path.join(gl.configPath,'config.yaml')
    )
    return yamldict['RUNING'][scenario_key]['Flag'][casename]['Flag']



def cook_info(func):
    """
    从配置文件获取cookies信息
    :param func: 函数名
    :return: 函数
    """
    def warpper(*args, **kwargs):
        yamldict = get_yaml_field(
            os.path.join(gl.configPath, 'config.yaml')
        )
        cook1= yamldict['CONFIG']['Cookies']['LoginCookies']
        return func(cook=cook1, *args, **kwargs)
    return warpper


def replay(func):
    """
    回放速度
    :param func: 函数名
    :return: wrapper
    """
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        yamldict = get_yaml_field(os.path.join(gl.configPath, 'config.yaml'))
        sleeptime = float(yamldict['RUNING']['REPLAY']['Time']) / 1000
        time.sleep(sleeptime)
        return func
    return wrapper



def hight_light_conf(key):
    """
    配置元素，是否高亮显示
    :param key: config.yaml 中关键字 HightLight:1 高亮 其它忽略
    :return:
    """
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            config = get_yaml_field(gl.configFile)
            ret = None
            if config[key] == 1:
                ret = func(*args, **kwargs)
            return ret
        return wrapper
    return _wrapper



def remove_all_files(dirpath):
    """
    删除目标,目录下文件及文件夹
    :param dirpath: 目标目录
    :return: 无
    """
    listdir = os.listdir(dirpath)
    if listdir:
        for f in listdir:
            filepath = os.path.join(dirpath, f)
            if os.path.isfile(filepath):
                os.remove(filepath)
            if os.path.isdir(filepath):
                os.rmdir(filepath)


def zip_dir(dirpath,out_fullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(out_fullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(
                os.path.join(path, filename),
                os.path.join(fpath, filename)
            )
    zip.close()


def reply_case_fail(num=3):
    """
    测试case失败后，重新执行功能
    :param num: 失败最多可以执行次数，默认为3次
    :return: fun本身或者抛出异常
    """
    def _warpper(func):
        def warpper(*args, **kwargs):
            raise_info = None
            rnum = 0
            for _ in range(num):
                rnum +=1
                try:
                    ret = func(*args, **kwargs)
                    if rnum > 1:
                        print('重试{}次成功'.format(rnum))
                    return ret
                except Exception as ex:
                    raise_info = ex
            print('重试{}次,全部失败'.format(rnum))
            raise raise_info
        return warpper
    return _warpper


def get_data(file, field):
    """
    从data目录下的yaml文件读取指定字段(field)CASE数据
    :param file:yaml数据文件
    :param field: 指定字段读取
    :return: 结构数据
    """
    yaml_end = str(file).endswith('.yaml')
    yam_end = str(file).endswith('.yam')
    if not (yaml_end or yam_end):
        file = '{}.yaml'.format(file)

    field = str(field).strip().upper()
    data = get_yaml_field(
        os.path.join(
            gl.dataPath, file
        )
    )[field]
    return data


def is_exist_dir(path):
    """
    如果文件夹不存在，则创建
    :param path:
    :return:
    """
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


if __name__ == "__main__":
    demo(cook='')
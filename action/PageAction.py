# -*- encoding: utf-8 -*-
# @Time    : 2017-12-03 21:41
# @Author  : mike.liu
# @File    : PageAction.py


#定义全局driver变量
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from config.VarConfig import chromeDriverFilePath, ieDriverFilePath, firefoxDriverFilePath
from util.ClipboardUtil import Clipboard
from util.DirAndTime import getCurrentTime, createCurrentDateDir
from util.KeyBoardUtil import KeyboardKeys
from util.ObjectMap import getElement
from util.WaitUtil import WaitUtil

driver = None
# 全局的等待类实例对象
waitUtil = None

def open_browser(browserName,*arg):
    #打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path = ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            #创建Chrome浏览器的一个options实例对象
            chrome_options = Options()
            #添加屏蔽--ignore-certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignore-certificate-errors"])
            driver = webdriver.Chrome(
                executable_path = chromeDriverFilePath,
                chrome_options = chrome_options)
        else:
            driver = webdriver.Firefox(executable_path = firefoxDriverFilePath)
        #driver对象创建成果后，创建等待类实例对象
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url,*arg):
    #访问某个网址
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

def close_browser(*arg):
    #关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*arg):
    # 强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e
def clear(locationType,locatorExpression,*arg):
    #清除输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except BaseException as e:
        raise e
def input_string(locationTpye,locatorExpression,inputContent):
    #在页面输入框输入数据
    global driver
    try:
        getElement(driver,locationTpye,locatorExpression).send_keys(inputContent)
    except BaseException as e:
        raise e

def click(locationTpye,locatorExpression,*arg):
    #单击页面元素
    global driver
    try:
        getElement(driver, locationTpye, locatorExpression).click()
    except Exception as e:
        raise  e

def assert_string_in_pagesource(assertString,*arg):
    #断言页面源码是否存在某关键字或关键字字符串
    global driver
    try:
        assert assertString in driver.page_source,"%s not found in page source!" %assertString
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def assert_title(titleStr,*arg):
    #断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title,"%s not found in title!" %titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def assert_text(titleStr,*arg):
    #断言页面标题是否存在给定的关键字符串
    global driver
    try:
        aElement = driver.find_element_by_class_name("l-dialog-content")
        a_text = aElement.text
        #print("a_text:"+a_text)
        assert titleStr in a_text,"%s not found in text!" %titleStr
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def getTitle(*arg):
    #获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getPageSoure(*arg):
    #获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def getText(*arg):
    #获取页面文本信息
    global driver
    try:
        aElement = driver.find_element_by_class_name("l-dialog-content")
        a_text = aElement.text
        print("a_text:" + a_text)
        return aElement.text
    except Exception as e:
        raise e

def switch_to_frame(locationTpye,frameLocatorExpression,*arg):
    #切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locationTpye,frameLocatorExpression))
    except Exception as e:
        print("frame error")
        raise  e

def switch_to_default_content(*arg):
    #切出frame
    global driver
    try:
        driver.switch_to_default_content()
    except Exception as e:
        raise e

def paste_string(pasteString,*arg):
    #模拟ctrl+v操作
    try:
        Clipboard.setText(pasteString)
        #等待2秒，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*arg):
    #模拟Tab键
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise  e


def press_enter_key(*arg):
    # 模拟enter键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    #窗口最大化
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

def capture_screen(*args):
    #获取屏幕图片
    global driver
    curtTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + "\\" + str(curtTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath
def waitPresenceOfElementLocated(locationTpye,locatorExpression,*arg):
    '''显式等待页面元素出现在dom中，但并不一定可见
    则返回改页面元素对象'''
    global driver
    try:
        waitUtil.presenceOfElementLocated(locationTpye,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationTpye,locatorExpression,*args):
    '''检查frame是否存在，存在则切换进frame控件中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationTpye,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationTpye,locatorExpression,*args):
    '''显式等待页面元素出现dom中，并且可见，存在返回改页面元素对象'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationTpye,locatorExpression)
    except Exception as e:
        raise e

def current_window_handle(*args):
    global driver
    try:
        #  得到当前窗口的句柄
        now_handle = driver.current_window_handle
        #print("当前窗口句柄：" + now_handle)
        # 得到所有窗口的句柄
        all_handles = driver.window_handles
        #print("++++", driver.window_handles[-1])
        # 循环遍历所有新打开的窗口句柄，也就是说不包括主窗口
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                #print("新的窗口句柄:" + handle)
    except Exception as e:
        raise e

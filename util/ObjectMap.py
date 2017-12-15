# -*- encoding: utf-8 -*-
# @Time    : 2017-11-13 21:53
# @Author  : mike.liu
# @File    : ObjectMap.py

#获取单个页面元素对象
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by = locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e

#获取多个相同页面元素对象，以list返回
def getElements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by = locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '___main__':

    #进行单元测试
    driver = webdriver.Chrome(executable_path="D:\\Python34\\chromedriver")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,"id","kw")
    #打印页面对象的标签名
    aList = getElements(driver,"tag name","a")
    print(len(aList))
    driver.quit()

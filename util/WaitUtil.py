# -*- encoding: utf-8 -*-
# @Time    : 2017-11-28 22:21
# @Author  : mike.liu
# @File    : WaitUtil.py
from telnetlib import EC

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WaitUtil(object):

    def __init__(self,driver):
         self.locationTypeDictt = {
             "xpath":By.XPATH,
             "id":By.ID,
             "name":By.NAME,
             "css_selector":By.CSS_SELECTOR,
             "class_name":By.CLASS_NAME,
             "tag_name":By.TAG_NAME,
             "link_text":By.LINK_TEXT,
             "partial_link_text":By.PARTIAL_LINK_TEXT
         }
         self.driver = driver
         self.wait = WebDriverWait(self.driver,30)

    def presenceOfElementLocated(self,locatorMethod,locatorExpression,* arg):
        '''显式等待页面元素出现在DOM中，但并不一定可见,
        存在则返回改页面元素对象'''
        try:
            if self.locationTypeDict.has_key(locatorMethod.lower()):
                self.wait.until(
                    EC.presence_of_all_elements_located((
                        self.locationTypeDictt[locatorMethod.lower()],locatorExpression)))
            else:
                raise TypeError("未找到定位方式，请确认定位方法是否写正确")
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self,locationTpye,locatorExpression,*arg):
        '''检查fram是否存在，存在则切换金frame控件中'''
        try:
            self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDictt[locationTpye.lower()],
                    locatorExpression)))
        except Exception as e:
            #抛出异常信息给上层调用者
            raise e
    def visibilityOfElementLocated(self,locationType,locatorExpression,*arg):
        '''显示等待页面元素的出现'''
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((
                    self.locationTypeDict[locationType.lower()],
                    locatorExpression)))
        except Exception as e:
            raise e

if __name__ == '___main__':
    from selenium import webdriver
    #进行单元测试
    driver = webdriver.Chrome(executable_path="D:\\Python34\\chromedriver")
    driver.get("http://mail.126.com")
    waitUtil = WaitUtil(driver)
    waitUtil.frame_available_and_swith_to_it("id","x-URS-iframe")
    e = waitUtil.visibility_element_located("xpath","//input[@name='email']")
    e.send_keys("success")

    driver.quit()

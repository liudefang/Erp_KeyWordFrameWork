# -*- encoding: utf-8 -*-
# @Time    : 2017-12-03 17:28
# @Author  : mike.liu
# @File    : DirAndTime.py


#获取当前的日期
import time,os
from datetime import  datetime

from config.VarConfig import screenPicturesDir


def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" + str(timeTup.tm_mon) + "-" +str(timeTup.tm_mday)
    return currentDate

#获取当前的时间
def getCurrentTime():
    timeStr = datetime.now()
    nowTime = timeStr.strftime('%H-%M-%S-%f')
    return nowTime

def getnowTime():
    # 获取当前时间
    now = datetime.datetime.now()
    nowTime = now.strftime("%Y-%m-%d") #直接截取当前时间的年月日
    return nowTime

def getvalidityTime():
    # 获取当前时间
    now = datetime.datetime.now()
    # 协议有效时间 可使用hours,days,minutes，seconds，weeks等等


    validityTime = (now + datetime.timedelta(days=-20)).strftime("%Y-%m-%d")  # 当前天数减去20天
    return validityTime


def getvalidityToTime():
    # 获取当前时间
    now = datetime.datetime.now()
    validityToTime = (now + datetime.timedelta(days=+30)).strftime("%Y-%m-%d")  # 当前天数加上30天
    return validityToTime

#创建截图存放的目录
def createCurrentDateDir():
    dirName = os.path.join(screenPicturesDir,getCurrentDate())
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    return dirName

if __name__ == '__main__':
    print(getCurrentDate())
    print(getCurrentTime())
    print(createCurrentDateDir())
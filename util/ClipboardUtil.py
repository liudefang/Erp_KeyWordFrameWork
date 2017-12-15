# -*- encoding: utf-8 -*-
# @Time    : 2017-11-28 23:14
# @Author  : mike.liu
# @File    : ClipboardUtil.py

class Clipboard(object):
    '''模拟Windows设置粘贴板'''

    #读取粘贴板
    @staticmethod
    def getText():
        #打开剪贴板
        w.OpenClipboard()
        #获取剪贴板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        #关闭剪贴板
        w.CloseClipboard()
        #返回剪贴板数据个调用者
        return d
    #设置剪贴板内容
    @staticmethod
    def setText(aString):
        #打开剪贴板
        w.OpenClipboard()
        #清空剪贴板
        w.EmptyClipboard()
        #将数据astring写入剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        #关闭剪贴板
        w.CloseClipboard()
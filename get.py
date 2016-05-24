# -*- coding: utf-8 -*-

# Build-in / Std
import os, sys, time, platform, random
import re, json, cookielib

# requirements
import requests, termcolor, html2text
try:
    from bs4 import BeautifulSoup
except:
    import BeautifulSoup

# module
from auth import islogin
from auth import Logging



requests = requests.Session()
requests.cookies = cookielib.LWPCookieJar('cookies')
try:
    requests.cookies.load(ignore_discard=True)
except:
    Logging.error(u"你还没有登录知乎哦 ...")
    Logging.info(u"执行 `python auth.py` 即可以完成登录。")
    raise Exception("无权限(403)")


if islogin() != True:
    Logging.error(u"你的身份信息已经失效，请重新生成身份信息( `python auth.py` )。")
    raise Exception("无权限(403)")


def str_save(mystr,filename):
	with open(filename,'w') as fp:
		fp.write('%s\n'%mystr)

def _start():
	print 'type in the url of the question:'
	url=raw_input()	
	#url='https://www.zhihu.com/question/23994286'
	print 'type in the author\'s name:'	
	author_name=raw_input()
	print 'author_name:',author_name
	r=requests.get(url)
	
	bsObj=BeautifulSoup(r.text,'lxml')
	
	#my_text=bsObj.find(('div',{'data-author-name':author_name}),{'class':'zm-editable-content clearfix'})
	my_text=bsObj.find('div',{'data-author-name':author_name}).find('div',{'class':'zm-editable-content clearfix'}).text
	print my_text#unicode

	str_save(my_text.encode('utf-8'),author_name+'.txt')




if __name__ == "__main__":
	_start()










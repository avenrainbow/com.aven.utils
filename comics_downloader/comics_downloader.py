
#coding=utf-8


import re
import requests
import os
import sys

#目录中文输出
reload(sys)
sys.setdefaultencoding("utf-8")

'''
从指定地址批量下载漫画图片
'''
def download_imgs_from_each_id(url,cpt):
    print url
    html = requests.get(url).text
    pic_url = re.findall('<img src="(http.*?)"',html,re.S)
    i = 0
    for each in pic_url:
        #过滤掉acfun站图
        if 1 == 1 :
            print each
            try:
                pic= requests.get(each, timeout=100)
            except requests.exceptions.ConnectionError:
                print '【错误】当前图片无法下载'
                continue

            #路径组装
            relative_path = '少女终末旅行第' + cpt + '话'
            absolute_path = 'D:/acfun_down/'
            path = absolute_path + relative_path.encode('gb2312')

            #下载图片
            if not(os.path.exists(path)):
                os.makedirs(path)
            fp = open(path+'/'+str(i) + '.jpg','wb')
            fp.write(pic.content)
            fp.close()
            i += 1



if __name__ == '__main__':
    comics_urls = []
    comics_urls.append('http://www.acfun.cn/a/ac3983832@23')
    comics_urls.append('http://www.acfun.cn/a/ac4020224@24')
    comics_urls.append('http://www.acfun.cn/a/ac4020257@25')
    comics_urls.append('http://www.acfun.cn/a/ac4020327@26')
    comics_urls.append('http://www.acfun.cn/a/ac4021204@27')
    comics_urls.append('http://www.acfun.cn/a/ac4020448@29')
    comics_urls.append('http://www.acfun.cn/a/ac4020540@30')
    comics_urls.append('http://www.acfun.cn/a/ac4020652@31')
    comics_urls.append('http://www.acfun.cn/a/ac4020714@32')
    comics_urls.append('http://www.acfun.cn/a/ac4020751@33')
    comics_urls.append('http://www.acfun.cn/a/ac4020859@34')
    comics_urls.append('http://www.acfun.cn/a/ac4020908@35')
    comics_urls.append('http://www.acfun.cn/a/ac4021165@36')
    comics_urls.append('http://www.acfun.cn/a/ac4021173@37')
    comics_urls.append('http://www.acfun.cn/a/ac4021175@38')
    comics_urls.append('http://www.acfun.cn/a/ac4021192@39')

    for url in comics_urls:
        download_imgs_from_each_id(url.split('@')[0],url.split('@')[1])

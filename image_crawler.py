# coding=utf-8
'''
    通过提供一个url，去抓取此url下的所有图片并且转存到oss中
    示例：invk crawler_image -s "{\"url\":\"http://www.xxxx.com\"}"
    代码中，请用您的真实变量替换掉<' var '> 
'''

import re
import urllib
import json
import datetime
import oss2
import logging


# 函数服务主函数
def handler(event, context):
    logger = logging.getLogger()
    logger.info('start worker')
    evt = json.loads(event)
    url = evt['url']
    logger.info('url:' + url)
    endpoint = 'oss-cn-< your regin>.aliyuncs.com'
    creds = context.credentials
    auth = oss2.StsAuth(creds.accessKeyId, creds.accessKeySecret, creds.securityToken)
    bucket = oss2.Bucket(auth, endpoint, '<your bucket name>')
    try:
        html = getHtml(url)
        img_list = getImg(html)
        for item in img_list:
            logging.info(item)
            # 获取每一张图片
            pic = urllib.urlopen(item)
            # 以时间毫秒为key，把所有的图片存储到oss中的bucket里
            bucket.put_object(str(datetime.datetime.now().microsecond) + '.jpg', pic.read())
    except Exception, e:
        logging.error(e)
        return 'error'
    return 'ok'


# 获取url内容
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


# 找出所有jpg的地址
def getImg(html):
    reg = r'http:\/\/[^\s,"]*\.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    logger = logging.getLogger()
    logger.info(imglist)
    return imglist



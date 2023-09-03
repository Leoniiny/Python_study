# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import hashlib


def MD5_dealing(string):
    # 1、创建MD5对象
    md5_obj = hashlib.md5()
    # 2、指定需要加密的字符串
    md5_obj.update(string.encode('utf-8'))
    # 3、获取加密之后的字符串
    md5_rest = md5_obj.hexdigest()
    print(f'md5_rest 的值为：{md5_rest}')
    return md5_rest


if __name__ == '__main__':
    channelid = "8"
    sysnum = "3837cca3bda44f88b5a065c72c0ba62d"
    secret = "zxgv2c487vgch6x7g523ukvcrih5fit3"         #
    partnerid = "1102"     #
    ini_url = "https://us.sobot.com/chat/pc/v6/index.html?"
    string = sysnum + secret + partnerid
    rest = MD5_dealing(string)
    url = f"{ini_url}sysnum={sysnum}&channelid={channelid}&sign={rest}&partnerid={partnerid}"
    url1= f"{ini_url}sysnum={sysnum}&channelid={channelid}&sign={rest}&partnerid={partnerid}1"
    print(url)
    print(url1)
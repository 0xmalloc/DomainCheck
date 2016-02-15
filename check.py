#!/usr/bin/python
# coding: utf-8
# author: Weixiong Yin
# date: 2016/2/25
# mail: 0xmalloc@gmail.com

import time
import urllib2
import re
import webbrowser

api = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=%s"  # api地址
ISOTIMEFORMAT='%Y-%m-%d %X'

def check_new_domain(data):
    ava_pattern = re.compile(r'<original>(.*) : .*</original>')
    result = ava_pattern.findall(data)
    print result
    if '210' in result:
        return True
    elif '211' in result:
        return False
    else:
        print "return value err:" + data
        return False

def domain_info(domain):
    data = urllib2.urlopen(api % domain).read()
    print data
    return check_new_domain(data)

if __name__ == '__main__':
    domainsfile = open('domains.txt')
    str =  domainsfile.read()
    domains = str.split('\n')
    while True:
        for domain in domains:
            if(len(domain) == 0):
                continue
            print time.strftime(ISOTIMEFORMAT, time.localtime()) + " check " + domain
            if True == domain_info(domain):
                print "Found one available domain."
                webbrowser.open('http://music.163.com/#/outchain/2/34998961/m/use/html')
        time.sleep(5)

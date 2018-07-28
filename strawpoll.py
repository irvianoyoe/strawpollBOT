#/usr/bin/python
# -*- coding: utf-8 -*-
'''

===================================
|  Strawpoll bots Increase survey |
===================================
Developer and coder by _irv (c) 2018

Don't forget for change this variable
also don't forget change selenium path
self.pooling_id = ""
self.element_id = ""

pooling_id is https://strawpoll/thisname
radio_btn_id is check2 chekc3 etc

'''
import re
import os
import random
import time
import sys
import mechanicalsoup
from platform import system
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType
IS_LINUX = True if system() == "Linux" or system() == "Linux2" else False
if IS_LINUX:
    from pyvirtualdisplay import Display


class postclick(object):
    def __init__(self):
        # id pooling from URL
        self.pooling_id = "f28hpcgg"
        # check radio button option
        self.radio_btn_id = "check2"
        self.PROXYDB = "proxy.txt"
        self.PROXYUSED = "usedproxy.txt"
        self.site_target = "https://strawpoll.com/"+self.pooling_id
        # renew proxy
        renewProxy()
        # running
        self.boomclick()

    def writeUsedProxy(self, proxyIp):
        with open(self.PROXYUSED, "a") as myfile:
            myfile.write(proxyIp+"\n")

    def boomclick(self):
        tagValue = ""
        results_str = []
        results_used = []
        proxy_used = []
        with open(self.PROXYUSED, 'r') as output_proxy:
            proxy_used = output_proxy.readlines()
        for used_proxy in proxy_used:
            results_used.append(used_proxy.strip())
        with open(self.PROXYDB, 'r') as output_file:
            results_str = output_file.readlines()
        s = 0
        for res in results_str:
            proxy = res.strip()
            print("[*] proxy remain: %s" % (len(results_str)-s))
            s += 1
            if proxy in results_used:
                print('[+] Already used: %s' % proxy)
                continue
            else:
                print('[*] proxy now: %s' % proxy)
                self.writeUsedProxy(proxy)
                chromedriver_path = 'chromedriver'
                dir_path = os.path.dirname(os.path.abspath(__file__))
                #
                # this chromedriver selenium path change with your
                #
                chromedriver = "/usr/lib/chromium-browser/chromedriver"
                os.environ["webdriver.chrome.driver"] = chromedriver
                chromeOptions = webdriver.ChromeOptions()
                prefs = {"profile.managed_default_content_settings.images":2}
                chromeOptions.add_experimental_option("prefs",prefs)
                chromeOptions.add_argument('--user-agent='+USERAGENT().random())
                chromeOptions.add_argument('--proxy-server=%s' % proxy)
                try:
                    if IS_LINUX:
                        display = Display(visible=0, size=(800, 800))
                        display.start()
                    driver = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
                    driver.get(self.site_target)
                    driver.find_element_by_xpath("//label[@for='"+self.radio_btn_id+"']").click()
                    time.sleep(1)
                    driver.find_element_by_xpath("//button[@id='votebutton']").click()
                    time.sleep(3)
                    htm_source = BeautifulSoup(driver.page_source, 'html.parser')
                    sukses = htm_source.find("span",{"class":"success"})
                    if sukses:
                        print("[+] %s" % sukses.text)
                    else:
                        print("[x] You already voted on this poll")
                    driver.close()
                    if IS_LINUX:
                        display.stop()
                except Exception as err:
                    try:
                        driver.close()
                        if IS_LINUX:
                            display.stop()
                    except:
                        pass


class USERAGENT(object):
    def __init__(self):
        self.USER_AGENT_CHOICES = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.0alpha4',
            'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050513 Galeon/1.3.20 (Debian package 1.3.20-1)',
            'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120819 Firefox/15.0 PaleMoon/15.0',
            'Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020822)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080316 SUSE/2.0.0.13-0.1 Firefox/2.0.0.13',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT; rv:1.7.5) Gecko/20060127 Netscape/8.1',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.116 Chrome/7.0.517.44 Safari/534.7',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/419 (KHTML, like Gecko) Shiira/1.2.3 Safari/125',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.209 Chrome/11.0.696.71 Safari/534.24',
            'Mozilla/5.0 (X11; U; Linux x86_64; es-MX; rv:1.9.2.12) Gecko/20101027 Ubuntu/10.04 (lucid) Firefox/3.6.12',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.8) Gecko/20061107 Fedora/1.5.0.8-1.fc6 Firefox/1.5.0.8',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20090102 Ubuntu/9.04 (jaunty) Minefield/3.2a1pre',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.0.1) Gecko/20020823 Netscape/7.0',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060313 Debian/1.5.dfsg+1.5.0.1-4 Firefox/1.5.0.1',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197 Safari/532.0',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.2) Gecko/20040805 Netscape/7.2',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.2228.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/525.18 (KHTML, like Gecko, Safari/525.20) OmniWeb/v622.6.1.0.111015',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070227 BonEcho/2.0.0.2',
            'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.3 Chrome/11.0.700.3 Safari/534.24',
            'Mozilla/5.0 (compatible; Konqueror/3.0-rc5; i686 Linux; 20020910)',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16',
            'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/533.3',
            'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9a1) Gecko/20060520 SeaMonkey/1.5a',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Iron/13.0.800.1 Chrome/13.0.800.1 Safari/535.1'
        ]

    def random(self):
        return self.USER_AGENT_CHOICES[random.randint(0,len(self.USER_AGENT_CHOICES)-1)]

class renewProxy:
    def __init__(self):
        self.site_proxy = "https://www.sslproxies.org"
        self.USERAGENT = USERAGENT().random()
        self.DATA = "proxy.txt"
        self.Get()


    def Get(self):
        print("[+] Renewing proxy.")
        try:
            os.remove(self.DATA)
        except Exception as err:
            print(err)
            pass
        browser = mechanicalsoup.StatefulBrowser(user_agent=self.USERAGENT)
        html_code = browser.open(self.site_proxy)
        soup = BeautifulSoup(html_code.text, 'html.parser')
        divs = soup.findAll("tbody")
        td = []
        fix = []
        for content in divs:
            rows = content.findAll('tr')
            for row in rows :
                td.append(row.findAll('td'))
        for tds in td:
            PATTER_TD = re.findall(
                '([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})</td>,\s*<td>([0-9]{2,6})</td>',
                str(tds))
            fix.append(PATTER_TD[0])
        print("[+] Found Total New Proxy: "+str(len(fix)))
        for fx2 in fix:
            proxiesfix = str(fx2[0]+":"+fx2[1]+"\n")
            with open(self.DATA, 'a') as the_file:
                the_file.write(proxiesfix)







if __name__ == '__main__':
    postclick()

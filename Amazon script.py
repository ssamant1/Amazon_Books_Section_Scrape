from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from scrapy import Selector
from selenium.webdriver.support.ui import Select, WebDriverWait
import csv
import time
import requests
import os

a = lambda x: sel.xpath(x).extract()

driver = webdriver.Firefox()
driver.get("http://www.amazon.com/New-Used-Textbooks-Books/b/ref=sv_b_5?ie=UTF8&node=465600")
source = driver.page_source
sel = Selector(text=source,type="html")
links = a('//li[@style="margin-left: 6px"]//@href')

try:
    for each in links:
        each = "http://www.amazon.com"+each
        driver.get(each)
        source1 = driver.page_source
        sel1 = Selector(text=source1,type="html")
        cats = sel1.xpath('//li[@style="margin-left: 14px"]//@href').extract()
        for subcat in cats:
            subcat = "http://www.amazon.com"+subcat
            print subcat
            driver.get(subcat)
            i = 0
            while i < 101:
                url = driver.current_url
                time.sleep(2)
                r = requests.get(url)
                time.sleep(2)
                sel2 = Selector(text=r.text,type="html")
                linked = sel2.xpath('//a[@class="title"]//@href').extract()
                linker = sel2.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]//@href').extract()
                time.sleep(2)
                print linker, linked
                with open("C:\Drive F data\Client\Wilfred\data.csv","ab")as export:# use your own path
                    for each in linked:
                        export.write('{}\n'.format(each))
                    for each1 in linker:
                        export.write('{}\n'.format(each1))
                driver.find_element_by_xpath('//*[@id="pagnNextString"]').click()
                time.sleep(2)
                i=i+1
except Exception:
    sys.exc_clear()

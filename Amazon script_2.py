import requests
import urllib2
import urllib
import csv
from scrapy import Selector
import os
import time

x = lambda x: response.xpath(x).extract()

try:
    lists = open(r'C:\Drive F data\Client\Wilfred\links.txt')
    with open('C:\Drive F data\Client\Wilfred\\output.csv','ab') as export:
        fields = ['Textbook_Name', 'ISBN', 'Link', 'Lowest_New_Price', 'Quantity', 'Lowest_Used_Price', 'Quanttity', 'Trade_In_Now_Price']
        writer = csv.DictWriter(export, fieldnames=fields)
        writer.writeheader()
        for each in lists:
            time.sleep(1)
            each = each.strip()
            r = requests.get(each)
            time.sleep(1)
            response = Selector(text=r.text,type="html")
            Textbook_Name = x('//span[@id="productTitle"]/text()')
            ISBN = x('//*[@id="bylineBullets_feature_div"]/div/span[4]/text()')
            Lowest_New_Price = x('//*[@id="olp_feature_div"]/div/span[1]/span/text()')
            Quantity = x('//*[@id="olp_feature_div"]/div/span[1]/a/text()')
            Lowest_Used_Price = x('//*[@id="olp_feature_div"]/div/span[2]/span/text()')
            Quanttity = x('//*[@id="olp_feature_div"]/div/span[2]/a/text()')
            Trade_In_Now_Price = x('//span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()')
            print Textbook_Name, ISBN, each, Lowest_New_Price, Quantity, Lowest_Used_Price, Quanttity, Trade_In_Now_Price    
            writer.writerow({'Textbook_Name':Textbook_Name,'ISBN':ISBN,'Link':each,'Lowest_New_Price':Lowest_New_Price,'Quantity':Quantity,'Lowest_Used_Price':Lowest_Used_Price,'Quanttity':Quanttity,'Trade_In_Now_Price':Trade_In_Now_Price})
except Exception:
    pass

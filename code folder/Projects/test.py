from bs4 import BeautifulSoup
import requests
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# def get_chinese_font():
#     return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


def getrate(start, end, kind, pgnum):
    url = 'http://srh.bankofchina.com/search/whpj/search.jsp?erectDate='\
          + start + '&nothing=' + end + '&pjname=' + kind + '&page=' + pgnum
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    raw_price_tag = soup.select('body > div > div.BOC_main.publish > table > tr > th')
    raw_price = soup.select('body > div > div.BOC_main.publish > table > tr > td')[:-1]

    price_dict = {}
    raw_price = [i.text for i in raw_price]
    for i in range(len(raw_price_tag)):
        price_dict[raw_price_tag[i].text] = raw_price[i::len(raw_price_tag)]

    urls = [url[:-1] + str(i) for i in range(2, 3)]  # 一共81页
    for each_url in urls:
        wb_data = requests.get(each_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        raw_price = soup.select('body > div > div.BOC_main.publish > table > tr > td')[:-1]
        raw_price = [i.text for i in raw_price]
        for i in range(len(raw_price_tag)):
            price_dict[raw_price_tag[i].text] += raw_price[i::len(raw_price_tag)]

    print(price_dict)

    print(url)


getrate('2019-07-01', '2019-07-12', '1316', '1')




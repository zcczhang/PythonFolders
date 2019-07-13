# Author: CZ
# Time: 2019-07-13 00:07

import requests
from bs4 import BeautifulSoup
from easygui import *


def get_one_page(city):
    url = "http://www.air-level.com/air/" + city + '/'
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    s = soup.find("span")
    return s.string


def main():
    ipt = multenterbox(msg='Fill the Chinese City Name in Pinyin', title='Get the AQI',
                       fields=['City Name: '])
    msgbox(msg=get_one_page(ipt[0]), title='AQI in %s'%ipt[0])


if __name__ == '__main__':
    main()

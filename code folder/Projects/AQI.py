# Author: CZ
# Time: 2019-07-13 23:23

import requests
from bs4 import BeautifulSoup
import csv


def get_city_aqi(url):
    aqi_list = []
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_val = soup.find_all('td', {'class': 'aqiwgt-table-aqicell'})[0]
    aqivalue = div_val.find('div', {'class': 'aqivalue'}).text
    aqi_list.append(aqivalue)

    timediv = soup.find_all('div', {'style': 'font-size:16px;font-weight:light;;'})[0]
    tdiv = timediv.find('script').text
    timestr = tdiv.split("'")[1].strip()
    aqi_list.append(timestr)
    return aqi_list


def get_cities_url():
    allaqilist = []
    url = 'http://aqicn.org/city/all'
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_all = soup.find_all('div', {'class': 'main-cities'})[0]
    citylinklist = div_all.find_all('a')
    for i in range(392):
        allaqilist.append((citylinklist[i].get('href'), citylinklist[i].text))   # (url, cityname)
    return allaqilist


def main():
    city_list = get_cities_url()
    header = ['City', 'AQI', 'Update Time(local time)']

    with open('Real Time AQI of Major Cities in the World.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('Already got {} data. ({} in total)'.format(i + 1, len(city_list)))
            url = city[0]
            name = city[1]
            city_aqi = get_city_aqi(url)
            row = [name] + city_aqi
            writer.writerow(row)


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup

def trade_spider():
    url = 'http://bj.lianjia.com/fangjia/'
    source_code = requests.get(url)
    source_code.encoding = 'utf-8' #显式地指定网页编码，一般情况可以不用
    plain_text = source_code.text
    # print(plain_text)
    soup = BeautifulSoup(plain_text,"html.parser")
    get_area_sum_data(soup)
    for link in soup.find_all('div',{'class':'hide'}):
        for location in link.find_all('a'):
            location_url = "http://bj.lianjia.com"+location.get('href')
            print(location.string,location_url)
            get_single_area_data(location_url)

def get_area_sum_data(all_soup):
    print(all_soup.title.string)

def get_single_area_data(area_url):
    source_code = requests.get(area_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for director in soup.find_all('a',{"rel":"v:directedBy"}):
        print("导演:",director.string)

trade_spider()
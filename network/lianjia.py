import requests
from bs4 import BeautifulSoup

def trade_spider():
    url = 'http://bj.lianjia.com/fangjia/'
    source_code = requests.get(url)
    plain_text = source_code.text
    # print(plain_text)
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.find_all('div',{'class':'hide'}):
        # print(link)
        for location in link.find_all('a'):
            location_url = "http://bj.lianjia.com"+location.get('href')
            print(location.string,location_url)
            get_single_area_data(location_url)


def get_single_area_data(area_url):
    source_code = requests.get(area_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for director in soup.find_all('a',{"rel":"v:directedBy"}):
        print("导演:",director.string)

trade_spider()
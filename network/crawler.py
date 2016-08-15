import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page < max_pages:
        url = 'https://movie.douban.com/top250?start=' + str(page*25) + '&filter='
        # print(url)
        source_code = requests.get(url)
        # print(source_code)
        plain_text = source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text,"html.parser")
        # print(soup.title.string)
        for link in soup.find_all('div',{'class':'pic'}):
            # print(link)
            print(link.em.string)
            print(link.a.img.get('alt'))
            # print(link.a.get('href'))
            get_single_item_data(link.a.get('href'))
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for director in soup.find_all('a',{"rel":"v:directedBy"}):
        print("导演:",director.string)

trade_spider(2)



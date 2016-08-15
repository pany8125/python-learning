import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 0
    while page < max_pages:
        url = 'https://movie.douban.com/top250?start=' + str(page*25) + '&filter='
        print(url)
        source_code = requests.get(url)
        print(source_code)
        plain_text = source_code.text
        # print(plain_text)
        soup = BeautifulSoup(plain_text,"html.parser")
        print(soup.title.string)
        for link in soup.find_all('div',{'class':'pic'}):
            # print(link)
            print(link.em.string)
            print(link.a.img.get('alt'))
            print(link.a.get('href'))
        page += 1

trade_spider(1)



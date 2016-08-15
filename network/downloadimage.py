import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("http://ww2.sinaimg.cn/mw690/7e7742fbgw1f6r0rsfrszj209e0cy3zf.jpg")

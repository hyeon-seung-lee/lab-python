
from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from web_crawl_self import hanyu_list


def get_hsk_words():
    while True:
        try:
            # driver = webdriver.Chrome("D:/dev/chromedriver.exe")
            pass
            # return chr_link['href']

        except AttributeError:
            driver.close()
            pass


# get_hsk_words()
driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
url = 'https://zh.dict.naver.com/#/entry/zhko/3991a2a5344e40cbb91d4b08c3e36e26'
driver.get(url)
driver.minimize_window()
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")

# -> HSK _X_급 단어 추출
chr_link_title = soup.find('div', id='container').find('div', class_='section_hsk').find_all('div', class_='row')

for titles in chr_link_title:
    try:
        hsk_level = titles.find('div', class_='category')
        hsk_words_url = titles.find('a', class_='link')
        if hsk_level:
            print(hsk_level.text)  # -> 'HSK _X_급 단어' 출력 가능 -> key?
        else:
            pass
        print(hsk_words_url['href'])  # -> url 추출

    except AttributeError:
        pass

# -> HSK _X_급 단어 추출

driver.close()

"""
<div class="category">HSK 1급 단어</div>
<a class="link" href="#/entry/zhko/c202b65ab2b04646bd90bd7bad00aea2">星期</a>
<div class="category">HSK 5급 단어</div>
<a class="link" href="#/entry/zhko/57b6d821b45c4b60b89742b2f799e439">明星</a>
<div class="category">HSK 6급 단어</div>
<a class="link" href="#/entry/zhko/22f9a79bacf24628af6ccfd37cac70e1">卫星</a>
None         ->>     6급 단어 안에 포함되게 해야함
<a class="link" href="#/entry/zhko/eaade97be8ac4114a8b6ef3d63975f39">零星</a>
"""
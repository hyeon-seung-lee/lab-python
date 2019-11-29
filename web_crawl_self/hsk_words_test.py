import csv
import os

from selenium import webdriver
import json
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from web_crawl_self.csv_reader import my_csv_reader


def get_hsk_words(chr, letter_link):
    driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
    # driver = webdriver.Chrome("D:/dev/chromedriver.exe")
    url = f'https://zh.dict.naver.com/{letter_link}'
    driver.get(url)
    driver.minimize_window()
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "html.parser")

    chr_link_title = soup.find('div', id='container').find('div', class_='section_hsk').find_all('div', class_='row')

    for titles in chr_link_title:
        try:
            hsk_level = titles.find('div', class_='category')
            hsk_words_url = titles.find('a', class_='link')

            if hsk_level:
                hsk_word[chr].append(hsk_level.text)
                # print(hsk_level_title)  # -> 'HSK _X_급 단어' 출력 가능 -> key?

            else:
                pass
            hsk_word[chr].append(hsk_words_url['href'])
            print(hsk_word)
            driver.close()

        except AttributeError:
            pass
            driver.close()


# get_hsk_words()

input_file = os.path.join('dic_link.csv')
chn_words_link = my_csv_reader(input_file)

chn_hsk_link = []
hsk_word = {}
for row in chn_words_link:
    get_hsk_words(row[1], row[2])


# 저장
hsk_word_link_data = pd.DataFrame(hsk_word.items())
hsk_word_link_data.to_csv('hsk_words_link.csv', encoding='utf-8')


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

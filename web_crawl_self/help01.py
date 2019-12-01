import os
from web_crawl_self.csv_reader import my_csv_reader
import pandas as pd
from web_crawl_self import hanyu_list
from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
# https://zh.dict.naver.com/#/search?range=all&query='문자'
# for chn_character in hanyu_list.hanyu:
# html = urlopen(f"https://zh.dict.naver.com/#/search?range=all&query={chn_character}")

# driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

input_file = os.path.join('dic_link.csv')
chn_words_link = my_csv_reader(input_file)  # input_file로부터 주소를 받아온다
chn_words_link = chn_words_link[304:]
new_list = []
for list in chn_words_link:
    new_list.append(list[1:])

print(new_list)
data_frame = pd.DataFrame(new_list)  # import pandas as pd
data_frame.to_csv('hsk_words_304.csv', encoding='utf-8')
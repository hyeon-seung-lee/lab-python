from web_crawl_self import hanyu_list
from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
# https://zh.dict.naver.com/#/search?range=all&query='문자'
# for chn_character in hanyu_list.hanyu:
# html = urlopen(f"https://zh.dict.naver.com/#/search?range=all&query={chn_character}")

driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
url = 'https://zh.dict.naver.com/#/search?range=all&query=好'
driver.maximize_window()
driver.get(url)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, "html.parser")
chr_link = soup.find('div', id='container')
# print(f'chrlink: {chr_link}')

print(chr_link)

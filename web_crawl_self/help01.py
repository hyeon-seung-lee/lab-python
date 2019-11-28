from web_crawl_self import hanyu_list
from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
# https://zh.dict.naver.com/#/search?range=all&query='문자'
# for chn_character in hanyu_list.hanyu:
# html = urlopen(f"https://zh.dict.naver.com/#/search?range=all&query={chn_character}")

# driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

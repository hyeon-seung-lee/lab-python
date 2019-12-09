"""
icrawler 패키지를 이용해서, Google 이미지 검색 결과의 이미지들을 다운로드
> pip install icrawler
"""
from icrawler.builtin import GoogleImageCrawler
import os

# 이미지 저장 폴더 경로
save_dir = os.path.join('..', '..', 'images')

# 검색 필터링(filter) 조건들
filters = {
    'size': 'large',
    'license': 'noncommercial,modify',  # 비상업용도, 수정 가능
    'color': 'blackandwhite'
}
# GoogleImageCrawler 객체 생성
google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
google_crawler.crawl(keyword='바나프레소 캐릭터', max_num=50)

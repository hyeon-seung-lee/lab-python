"""
1) csv 파일(stock_price.csv) write
6/20/2019,AAPL,90.91
6/20,2019,MSFT,41.68
6/21/2019,AAPL,90.86
6/21/2019,MSFT,41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력
"""
import csv

data = [
    ['6/20/2019', 'AAPL', 90.91],
    ['6/20,2019', 'MSFT', 41.68],
    ['6/21/2019', 'AAPL', 90.86],
    ['6/21/2019', 'MSFT', 41.51],
]

with open('stock_price.csv', mode='w',
          encoding='UTF-8', newline='') as f:
    # csv writer 객체 생성
    writer = csv.writer(f)
    for item in data:
        writer.writerow(item)
with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    # csv.reader 객체를 생성
    reader = csv.reader(f)
    # 파일에 한 줄씩 반복하면 읽어서 리스트에 추가
    df = [row for row in reader]
print(df)


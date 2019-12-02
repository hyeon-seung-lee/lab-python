"""
1) csv 파일(stock_price.csv) write
6/20/2019, AAPL, 90.91
6/20/2019, MSFT, 41.68
6/21/2019, AAPL, 90.86
6/21/2019, MSFT, 41.51

2) CSV 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
    각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
    각 주식 종목의 주식 가격 평균을 계산해서 출력
"""
import csv
import os


def dict_mean(dict, key):
    d_sum = 0
    for list in dict[key]:
        d_sum+=float(list[1])

    return d_sum / (len(dict[key]))


if __name__ == '__main__':

    write_csv = [
        ['6 / 20 / 2019', 'AAPL', 90.91],
        ['6 / 20 / 2019', 'MSFT', 41.68],
        ['6 / 21 / 2019', 'AAPL', 90.86],
        ['6 / 21 / 2019', 'MSFT', 41.51]
    ]

    with open('stock_price.csv', mode='w', encoding='UTF-8', newline='') as f:
        # csv writer 객체 생성
        writer = csv.writer(f, delimiter=',')
        for row in write_csv:
            # writter 객체의 writerrow() 메소드를 사용해서 한 줄씩 쓰기
            writer.writerow(row)

    file_path = os.path.join('stock_price.csv')
    with open(file_path, mode='r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        df = [line for line in reader]
        # print(df)
        stock_price = {}
        for row in df:
            stock_price[row[1]] = []
        for row in df:
            print(f'row:{row}')
            stock_price[row[1]].append([row[0], row[2]])
        print(stock_price)

    with open(file_path, mode='r', encoding='UTF-8') as f:
        # 사전(dict) 타입으로 데이터들을 읽어주는 reader 객체
        reader = csv.DictReader(f, delimiter=',', fieldnames=['date','name','price'])
        df = [row for row in reader]
        print(df[0]['date'])

    # 실행
    print(f'AAPL mean: {dict_mean(stock_price, "AAPL")}')
    print(f'MSFT mean: {dict_mean(stock_price, "MSFT")}')

    aapl_sum = 0
    msft_sum = 0
    aapl_num, msft_num = 0, 0
    print(df[1]['name'])
    for row in df:
        if row['name']=='AAPL':
            aapl_sum += float(row['price'])
            aapl_num += 1
        else:
            msft_sum += float(row['price'])
            msft_num += 1

    print(f'aapl_avg: {aapl_sum/ aapl_num}')
    print(f'msft_avg: {msft_sum/ msft_num}')

"""
lecture06_class\class07.py 파일에서 작성한 Account 클래스를 사용 해서
은행 어플리케이션을 만들자
1) 본인확인 :
2) 거래내역 조회
3) 예금, 적금
4) 대출
5) 신용조회
6) 전계좌 조회
7) 자동이체
"""
from lec06_class.class07 import Account

print("Banking Application")
# 여러 계좌들을 관리하기 위한 dictionary를 선언
# key : 계좌번호, value : Account 객체
accounts = {}

while True:  # 무한 루프
    # 메인 메뉴
    print('[0] 종료')
    print('[1] 계좌 개설')
    print('[2] 입금')
    print('[3] 출금')
    print('[4] 이체')
    print('[5] 계좌 정보 출력')
    print('-----------------------')
    menu = input('선택하세요 >> ')

    if menu == '0':
        print('Banking App 종료')
        break

    elif menu == '1':
        print('신규 계좌 개설 화면')
        account_no = int(input('계좌 번호 입력 >> '))
        money = int(input('잔액 입력 >> '))
        accounts[account_no] = Account(account_no, money)
        print(accounts)

    elif menu == '2':
        print('--- 입금 화면 ---')
        account_no = int(input('입금할 계좌 번호 >> '))
        money = int(input('입금 금액 >> '))
        accounts[account_no].deposit(money)

    elif menu == '3':
        print('--- 출금 화면 ---')
        account_no = int(input('출금할 계좌 번호 >> '))
        money = int(input('출금 금액 >> '))
        accounts[account_no].withdraw(money)

    elif menu == '4':
        print('--- 이체 화면 ---')
        from_acc = int(input('보낼 계좌 번호 >> '))
        to_acc = int(input('받을 계좌 번호 >> '))
        money = int(input('보낼 금액 >> '))
        accounts[from_acc].transfer(accounts[to_acc], money)

    elif menu == '5':
        print('--- 계좌 조회 화면 ---')
        account_no = int(input('조회할 계좌 번호 입력 >> '))
        print(accounts[account_no])

    else:
        print('잘못 입력 하셨습니다.')
        continue

"""
lec08_ database 패키지의 내용을 참고해서,
오라클 데이터베이스에서 emp 테이블의 모든 레코드를 검색(select) -> 2차원 리스트
csv 모듈을 사용해서, csv 파일(emp.csv)로 저장
"""
import csv

import cx_Oracle


# 사용자 이름
user = 'scott'

# 비밀번호
pwd = 'tiger'

# 데이터베이스 서버 주소: DSN(Data Source Name)
dsn = 'localhost:1521/orcl'

# 데이터베이스 서버와 연결 설정 - 접속(로그인) - .connect(userid, passward, ip address)
connection = cx_Oracle.connect(user, pwd, dsn)

# 접속한 데이터베이스 버전 정보
print('DB version:', connection.version)

# SQL 문장을 실행시키기 위해서 cursor 객체를 생성
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')  # 끝에 세미콜론(;) 을 붙이면 안됨
emp_table = []
while True:
    row = cursor.fetchone()
    if row is None:  # select의 결과가 더 이상 없다면
        break
    else:
        emp_table.append(row)
print(emp_table)

with open('emp.csv', mode='w', encoding='UTF-8', newline='') as f:
    # csv writer 객체 생성
    writer = csv.writer(f, delimiter=',')
    for row in emp_table:
        # writter 객체의 writerrow() 메소드를 사용해서 한 줄씩 쓰기
        writer.writerow(row)
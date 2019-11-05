"""
python if 구문(statement)
1
if 조건식:
    조건식이 참일 때 실행할 문장
2
if 조건식:
    참일 때 실행할 문장
else:
    거짓일 때 실행할 문장
3
if 조건식1:
    조건식1이 참일 때 실행할 문장
elif 조건식2:
    조건식2가 참일 때 실행할 문장
...
else:
    조건식이 모두 거짓일 때 실행할 문장

"""
"""
# 숫자를 입력받아서 양수인 경우에만 출력
num = float(input(">>> 숫자를 입력: "))
if num>0:
    print(f'num = {num}')
if num>0:
    print('양수')
else:
    print('음수')
print('프로그램 종료')


# if-elif-else
score = int(input('점수를 입력하세요 : '))
if score>90:
    print('A')
elif score>80:
    print('B')
elif score>70:
    print('C')
else:
    print('F')
"""
# if, elif, else 블록 안에서 또 다른 if 구문을 사용할 수 있음.
num = int(input(">>> 숫자를 입력: "))
if num%2 == 0: # 짝수이면
    if num%4 == 0: #
        print('4의 배수')
    else:
        print('4의 배수가 아닌 짝수')
    pass # TODO : 짝수이면 할 일, pass : 일단 아무 일도 안하고 넘어가기 위한 명령문
else: # 홀수이면
    print('홀수')


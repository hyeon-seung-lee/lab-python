"""
명시적 데이터 타입 변환(casting) : int(), float(), str()
"""
# print("3.1"+ 1.2)  # 실행 불가능
# 문자열과 숫자는 산술 연산을 할 수 없음
# 숫자 타입으로 변환 후 산술 연산을 실행
print(float("3.1")+1.2)
print("3.1"+str(2.2))

# 간단한 계산기
x = float(input('>>> 숫자(x) 입력:'))
y = float(input('>>> 숫자(y) 입력:'))
print(x+y)


# 계산기
x = input('>>> 숫자(x) 입력:')
y = input('>>> 숫자(y) 입력:')
x = float(x)
y = float(y)
print(f'{x}+{y} = {x+y}')
print(f'{x}-{y} = {x-y}')
print(f'{x}*{y} = {x*y}')
print(f'{x}/{y} = {x/y}')

# Ctrl + D : 커서가 있는 줄을 복사&붙여넣기

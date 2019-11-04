"""
연산자(Operator)
- 할당(assignment):    =
- 산술연산(numerical operator): +, -, *, **(제곱), /, //(몫), %(나머지)
- 복합 할당: +=, -=, *=, /=, ...\
- 비교 연산: >, >=, <=, <, ==, !=
- 논리 연산: and, or, not
- identity 확인: is, is not
"""
x = 1 # 연산자(=) 오른쪽 값을 왼쪽 변수에 저장
print(2**3) # 2*2*2 : 2의 3승
print(3//2) # 몫
print(13%3) # 나머지

x = 1
print('x = ', x)

x += 10             # x = x + 10
print('x = ', x)

print(1==2)
print(1!=2)

x = 50
y = 100
print(0 < x < 200)
print(x<0 or x>30)
print(x is y)
"""
문자열(str) 타입
"""

s = ''' oo 
    def my_function(x:int) ->int:
        return x+1
'''
t = """xx
    y"""

print(s)
print(t)

u = '''\
    첫 줄 줄바꿈 없애기 : \\
'''
print(u)

v = """문자열 중간에 줄바꿈 하기 \n
-> \\n  : 한 줄 추가되어서 두 줄이 떨어지게 됨.
"""
print(v)

# 문자열의 index, 자르기(slicing)
s = 'hello'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
# print(s[5]) : Index Error 발생

print(s[0:2])

# x:y - from x(포함, include) to y(미포함, exclude)

print(s[1:5])
print(s[1:]) # 범위 연산자에서 끝 인덱스가 없는 경우는 배열의 끝까지
print(s[:4]) # 범위 연산자에서 시작 인덱스가 없는 경우 첫 배열부터 시작

print(s[-3:-1]) # hello 에서 오른쪽부터 -1로 시작해서 왼쪽으로 센다.

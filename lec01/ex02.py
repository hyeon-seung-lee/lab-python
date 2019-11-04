"""
    여러가지 print() 방법
"""
print('Hello Python')

age = 16
name = '오쌤'
print('이름 :', name, '나이 :', age)
print(f'나이: {age}, 이름: {name}') # formatted string,
                                    # 앞에 'f'를 넣어주면 formatted string 이라는 뜻
print('나이는 {}, 이름은 {}'.format(age,name))
print('age:%d, name:%s' %(age,name))

# %d : 정수, %f : 실수, %s : 문자열
# digit, floating-point number, string

"""
사용자 입력(키보드 입력) 처리
"""
print('>>> 이름을 입력하세요 : ')
name = input()
print(f'name: {name}')

age = input('>>> 나이 입력:')
print(f'age: {age}')
print(age+1)
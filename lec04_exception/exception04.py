"""
사용자 정의 오류를 발생시키는 방법
"""
try:
    age = int(input('나이를 입력 >>'))
    if age < 0:
        raise ValueError('나이는 0 이상의 양의 정수여야 합니다.')
    print(f'입력한 나이 : {age}')
except ValueError as e:
    print(e.args) # .args : 에러의 내용을 볼 수 있다.

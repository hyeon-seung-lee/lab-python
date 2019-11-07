# 함수 정의
def test(x, y):
    print(f'x = {x}, y = {y}')
    return x + y, x - y


# 함수 호출
# test() # 실행중에 TypeError 발생
# 파이썬은 함수의 파라미터 타입은 검사하지 않지만,
# 파라미터 갯수는 검사한다.
# positional argument : 함수를 호출할 때 전달하는 값(argument)들이
# 함수 정의에 선언된 파라미터 순서대로 전달되는 방식

plus, minus = test(1, 2)
print(plus)
print(minus)

# keyword argument: 함수를 호출할 때, argument를
# 파라미터=값 형식으로 전달하는 방식

plus, minus = test(x = -1, y = 2)
print(plus)
print(minus)

# default argument: 함수를 정의하는 시점에 파라미터의 기본값을 설정하는 것


def show_msg(msg : str, times: int= 2)-> None:
    print(msg*times)


show_msg('졸리세요?')
show_msg('아니아니요',3)


# def test2(x =  1, y):
#     return x + y



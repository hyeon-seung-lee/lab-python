"""
람다 표현식(lambda expression)
함수의 이름 없이, 함수의 매개변수 선언과 리턴 값으로만 표현하는 방법!!
Lambda [ p1, p2, ... ] : 식(expression)
"""


multiplication = lambda x, y: x*y
result = multiplication(11, 12)
print(result)

division = lambda x, y: x/y
result = division(121, 11)
print(result)


# 람다 표현식은 함수의 매개변수에 함수를 전달할 때 많이 사용함
# def calc(x, y, op):
#     return op(x, y)
#     result calc(1, 2, lambda x, y: x + y)

# 람다 표현식을 사용한 함수 예
def my_filter(values, func):
    """
    리스트의 원소들 중에서 필터링 조건을 만족하는 원소들만으로
    이루어진 새로운 리스트를 생성해서 리턴하는 함수

    :param values: 리스트
    :param func: True/ False를 리턴하는 함수
    :return: 필터링된 새로운 리스트
    """

    result = [] # 빈 리스트를 생성
    for item in values:  # 리스트의 모든 원소들에 대해서 반복
        if func(item):   # 필터링 조건 함수
            result.append(item) # 조건이 참인 경우에만 리스트에 추가
        return result

numbers = [1, -2, 3, 4, -5, -6, 7, 8]

positives = my_filter(numbers, lambda x: x > 0)
print(positives)

evens = my_filter(numbers, lambda x: x%2 ==0)
print(evens)
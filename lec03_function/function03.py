"""
또 다른 함수 정의 방법:
def 함수이름(파라미터: 타입, 파라미터2: 타입) -> 리턴타입:
    함수 기능(body)
"""


def subtract(x:int , y:int) -> int:
    return x-y

result = subtract(1, 2)


result2 = subtract(1.2, 2.7)
print(result2)


def my_sum(numbers: list) -> float:
    """
    숫자들(int, float)이 저장된 리스트를 전달받아서,
    모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장된 리스트
    :return: 리스트의 모든 원소들의 합
    """
    total = 0
    for i in numbers:
        total += i
    return total

num_list = [1, 2, 5, 7, 9]
print(f'my_sum :  {my_sum(num_list)}')


def my_mean(numbers: list) -> float:
    """
    숫자들을 저장하는 리스트를 전달 받아서,
    모든 원소들의 평균을 계산해서 리턴
    :param numbers:  숫자들을 저장한 리스트
    :return: 리스트의 모든 원소들의 평균
    """

    return my_sum(numbers)/len(numbers)


print(my_mean([1, 4, 6, 7, 8]))

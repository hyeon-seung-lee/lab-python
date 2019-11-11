import numpy as np


def find_min(numbers):
    """
    주어진 리스트에서 최솟값과 최솟값의 인덱스를 찾아서 리턴

    :param numbers: 숫자들의 리스트
    :return: (최솟값의 인덱스, 최솟값)의 쌍(tuple)
    """
    min_id, min_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v < min_value:
            min_id, min_value = i, v
    return min_id, min_value


def find_max(numbers):
    """
    주어진 리스트에서 최댓값과 최댓값의 인덱스를 찾아서 리턴

    :param numbers: 숫자들의 리스트
    :return: (최솟값의 인덱스, 최솟값)의 쌍(tuple)
    """
    max_id, max_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v > max_value:
            max_id, max_value = i, v
    return max_id, max_value


def sel_sort(numbers_1: list, reverse:bool = False) -> list:
    """

    :param numbers_1:
    :param reverse: False 면 오름차순
    :return:
    """
    numbers_copy = numbers_1.copy()
    result = []  # 빈 리스트 생성
    if not reverse:
        while numbers_copy:  # numbers의 원소가 있는 동안에
            # print('numbers=', numbers)
            # print('result=', result)
            _, min_value = find_min(numbers_copy)  # 최솟값을 찾음
            result.append(min_value)  # 결과 리스트에 추가
            numbers_copy.remove(min_value)  # 카피에서 최솟값 삭제
    else:
        while numbers_copy:  # numbers의 원소가 있는 동안에
            # print('numbers=', numbers)
            # print('result=', result)
            _, max_value = find_max(numbers_copy)  # 최댓값을 찾음
            result.append(max_value)  # 결과 리스트에 추가
            numbers_copy.remove(max_value)  # 카피에서 최댓값 삭제

    return result







def sel_sort2(numbers_2: list, reverse: bool = False) -> None:
    length = len(numbers_2)

    if not reverse:
        for i in range(0, length - 1):
            # i: 최솟값을 옮길 위치
            for j in range(i + 1, length):
                # j: 최솟값을 찾기 위해서 비교할 원소들의 인덱스
                if numbers_2[i] > numbers_2[j]:
                    numbers_2[i], numbers_2[j] = numbers_2[j], numbers_2[i]
                   # print(numbers_2)

    else:
        for i in range(0, length - 1):
            # i: 최댓값을 옮길 위치
            for j in range(i + 1, length):
                # j: 최댓값을 찾기 위해서 비교할 원소들의 인덱스
                if numbers_2[i] < numbers_2[j]:
                    numbers_2[i], numbers_2[j] = numbers_2[j], numbers_2[i]
                    # print(numbers)
    return numbers_2


numbers = [np.random.randint(0, 100) for _ in range(10)]
print(f'sorted numbers1 : {sel_sort(numbers, reverse=False)}')
# numbers = [np.random.randint(0, 100) for _ in range(10)]
print(f'sorted numbers2 : {sel_sort2(numbers, reverse=True)}')
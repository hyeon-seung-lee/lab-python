"""
mymath01.py
"""
pi = 3.14


def add(x : int, y: int) -> int:
    """
    두 정수 x, y가 주어졌을 때, x + y 를 리턴하는 함수
    :param x: 정수(int)
    :param y: 정수(int)
    :return: x + y
    """
    return x + y


def subtract(x: int, y: int) -> int:
    """
        두 정수 x, y가 주어졌을 때, x - y 를 리턴하는 함수
        :param x: 정수(int)
        :param y: 정수(int)
        :return: x - y
        """
    return x - y


if __name__ =='__main__':
    print(__name__)
    print('pi =', pi)
    print('add =', add(1, 2))
    print('sub =', subtract(1, 2))




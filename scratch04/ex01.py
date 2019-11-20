"""
선형 대수(Linear Algebra)
"""
from math import sqrt


def add(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 더하기를 해서,
    새로운 n차원 벡터를 리턴
    :param v: n차원 vector(성분이 n개인 벡터)
    :param w: n차원 vector(성분이 n개인 벡터)
    :return: 각 성분의 합을 원소로 갖는 n차원 vector
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함')
    x = []
    for i in range(len(v)):
        x.append(v[i] + w[i])
    return x


def subtract(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 뺄셈을 수행

    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: n차원 벡터
    """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함')
    x = []
    for i in range(len(v)):
        x.append(v[i] - w[i])
    return x


def vector_sum(vectors):
    """
    모든 벡터들에서 각 성분별 더하기를 수행
    vector_sum[[1, 2, 3], [3, 4, 5], [5, 6, 7]] = [9, 12, 15]
    :param vectors: n차원 벡터들의 리스트(2차원 리스트)
    :return: n차원 벡터
    """
    x = []
    for i in vectors[0]:
        x.append(0)

    for j in vectors:
        for l in range(len(j)):
            x[l] += j[l]
    return x


def vector_sum2(vectors):
    """
    vector_sum과 같지만 add 함수를 이용
    """
    x = []
    for i in vectors[0]:
        x.append(0)

    for i in range(len(vectors)):
        x = add(x, vectors[i])
    return x


def scalar_multiply(c, vector):
    """
    c * [x1, x2, x3, .. ] = [c*x1, c*x2, c*x3, ..)
    :param c: 숫자(스칼라, scalar)
    :param vector: n차원 벡터
    :return: n차원 벡터
    """
    # x = []
    # for i in vector:
    #     x.append(0)
    # for i in range(len(vector)):
    #     x[i] = vector[i] * c
    # return x
    return [c * x_i for x_i in vector]


def dot(v, w):
    """
    [v1, v2, v3, ... ] @ [w1, w2, w3, ... ] = v1*x1 + v2w2 + v3w3 ...
    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자(스칼라)
    # """
    if len(v) != len(w):
        raise ValueError('v와 w는 같은 length를 가져야 함.')

    sum = 0

    for v_i, w_i in zip(v, w):
        sum += v_i * w_i
    return sum


def vector_mean(vectors):
    """
    주어진 벡터들의 리스트 에서 각 항목별 평균으로 이루어진 벡터
    :param vectors: n차원 벡터들의 리스트
    (길이가 n인 1차원 리스트를 아이템으로 갖는 2차원 리스트)
    [   [x1, x2, ... ,xn],
        [y1, y2, ... ,yn]      ]
    :return: n차원 벡터(길이가 n인 1차원 리스트)
    """

    return [scalar_multiply(1 / len(vectors), vector_sum(vectors))]


def sum_of_squares(vector):
    """
    v = [x1, x2, ..., xn]일 때,
    x1 ** 2 + x2 ** 2 + ... + nx ** 2 리턴
    :param vector: n차원 벡터
    :return: 숫자
    """
    f_sum = 0
    for x in vector:
        f_sum += x ** 2
    return f_sum


def magnitude(vector):
    """
    벡터의 크기를 리턴
    :param vector:
    :return:
    """
    return sqrt(sum_of_squares(vector))


def squared_distance(v, w):
    """(v1 - w1)**2 + (v2-w2)**2 + ... + (vn - wn)**2 리턴
    v = [v1, v2, ... vn ... ]
    w =  w = [ w1, w2, ... ]

    :param v: n차원 벡터 ( 길이가 n인 1차원 리스트 )
    :param w: n차원  벡터 ( 길이가 n인 1차원 리스트)
    :return:
    """

    return sum_of_squares(subtract(v, w))


def distance(v, w):
    """
    두 벡터 v와 w 사이를 리턴 - sqrt(squared_distance)
    :param v:
    :param w:
    :return:
    """
    return sqrt(squared_distance(v, w))


if __name__ == '__main__':
    vector1 = [x for x in range(2, 8)]
    vector2 = [2 * y for y in range(5, 11)]
    print(vector1)
    print(vector2)
    print(scalar_multiply(3, vector1))
    print(dot(vector1, vector2))
    v = [2, 3]
    unit_x = [1, 0]
    unit_y = [0, 1]
    dot1 = dot(v, unit_x)
    print('dot1 =', dot1)
    dot2 = dot(v, unit_y)
    print('dot2 =', dot2)

    vector3 = [[1, 2, 3],
               [4, 5, 7]]
    print(vector_mean(vector3))
    print(sum_of_squares(vector1))
    print(magnitude(vector1))
    print(squared_distance(vector1, vector2))
    print(distance(vector1, vector2))

"""
선형 대수(Linear Algebra)
"""


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


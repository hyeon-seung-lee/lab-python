"""
통계

중심 경향성: 평균, 중앙값, 분위수(4분위, 100분위=퍼센트)
"""
# from scratch04.ex01 import dot
from math import sqrt


def mean(x):
    """
    리스트 x의 모든 원소들의 평균을 계산해서 리턴

    :param x: 원소 n개인 (1차원) 리스트
    :return: 평균
    """

    f_sum = 0
    n = len(x)

    for i in x:
        f_sum += i

    return f_sum / n


def median(x):
    """
    리스트 x를 정렬 했을 때 중앙에 있는 값을 찾아서 리턴
    n이 홀수이면, 중앙값을 찾아서 리턴
    n이 짝수이면, 중앙에 있는 두 개의 값의 평균을 리턴
    :param x:
    :return:
    """
    # 1, 2, 3             1, 2, 3, 44
    x.sort()
    n = len(x)  # 3                     4
    print('median')
    if (n) % 2 == 1:  # 1 2 3
        print(f'x[{n // 2}]')
        return x[n // 2]  # x[1]
    else:  # 1 2 3 4
        print(f'(x[{(n // 2) - 1}] + x[{n // 2}])/2')  # x[1]  + x[2] 나누기 2
        return (x[(n // 2) - 1] + x[n // 2]) / 2


def quantile(x, p):
    """
    리스트 x의 p분위에 속하는 값을 찾아서 리턴
    :param x: 원소 n개인 (1차원) 리스트
    :param p: 0 ~ 1.0 사이의 값
    :return:
    """
    x.sort()
    n = len(x)
    pct = int(n * p) - 1
    print(f'[{n}x{p} - 1 = int{n * p - 1} -1]')
    return x[pct]


def mode(x):
    """
    리스트에서 가장 자주 나타나는 값을 return.
    최빈값이 여러개인 경우, 최빈값들의 리스트를 리턴.
    :param x: 원소가 n개인 (1차원) 리스트
    :return: 최빈값들의 리스트를 return
    """
    # y = sorted(x)
    # numbers = {}
    #
    # for i in range(len(x)):
    #     if y[i] == y[i+1]:
    #         numbers[y[i]] += 1
    #     else:
    #         continue
    # return max(numbers)

    counts = Counter(x)  # Counter 객체(인스턴스) 생성
    print(counts)
    print(counts.keys(), counts.values())
    # Counter.keys(): 데이터(아이템),  Counter.values(): 빈도수
    print(counts.items())  # (값, 빈도수) 튜플들의 리스트

    max_count = max(counts.values())  # 빈도수의 최대값
    freq = []  # 최빈값들을 저장할 리스트
    for val, cnt in counts.items():
        if cnt == max_count:
            freq.append(val)
    # return freq
    return [val for val, cnt in counts.items()
            if cnt == max_count]


def data_range(x):
    """

    :param x: 원소 n개인 (1차원) 리스트
    :return: 리스트의 최댓값 - 리스트의 최솟값
    """
    return max(x) - min(x)


def de_mean(x):
    """

    :param x: 원소가 n개인 (1차원) 리스트
    :return: 편차(deviation)들의 리스트
    """

    mu = mean(x)  # 평균
    return [x_i - mu for x_i in x]


def variance(x):
    """
    편차들(데이터 - 평균)의 리스트
    :param x: 원소가  n개인 (1차원) 리스트
    :return: 분산
    """
    # 편차 제곱합 / (n-1)
    avg = mean(x)
    var_sum = 0
    for i in x:
        var_sum += (i - avg) ** 2
    return var_sum / (len(x) - 1)


def standard_deviation(x):
    """
    sqrt(variance)
    :param x:  원소가  n개인 (1차원) 리스트
    :return: 표준편차
    """
    # from math import sqrt
    return sqrt(variance(x))


def covariance(x, y):
    """

    :param x: 원소 n개인 (1차원) 리스트
    :param y: 원소 n개인 (1차원) 리스트
    :return:
    """
    avg_x = mean(x)
    avg_y = mean(y)
    cov_sum = 0
    n = len(x)

    for i, j in zip(x, y):
        # print(f'i = {i}, j = {j}')
        cov_sum += (i - avg_x) * (j - avg_y)
    return cov_sum / (n - 1)


def correlation(x, y):
    """
    상관 계수(Correlation)
    :param x:
    :param y:
    :return:
    """
    sd_x = standard_deviation(x)
    sd_y = standard_deviation(y)

    if sd_x != 0 and sd_y != 0:
        corr = covariance(x, y) / (standard_deviation(x) * standard_deviation(y))
    else:
        corr = 0

    return corr


if __name__ == '__main__':
    # a = [10, 21, 32, 4, 70, 40, 60, 56, 73, 100, 1]
    # a = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6]
    # b = [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6]
    # b = [2, 3, 3, 3, 5, 5, 6, 4, 5, 6, 6, 9, 8]
    a = [-2, -1 ,0, 1, 2]
    b = [2, 1, 0, -1, -2]
    print(sorted(a))
    print('mean : ', mean(a))
    print('median :', median(a))
    print(quantile(a, 0.8))

    print('--------------')
    print('covariance = ', covariance(a, b))
    print('correlation = ', correlation(a, b))


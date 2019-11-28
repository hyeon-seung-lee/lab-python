"""
gradient descent 연습
"""
# import random
import matplotlib.pyplot as plt


def g(x):
    """y = (1/3) x**3 - x"""
    return x ** 3 / 3 - x


def tangent(x, a, x1, y1):
    """기울기가 a이고 점(x1, y1)을 지나는 직선의 방정식
       y - y1 = a(x - x1)
    """
    return a * (x - x1) + y1


def difference_quotient(f, x, h):
    """함수 f의 도함수의 근사값 """
    return (f(x + h) - f(x - h)) / (2 * h)


def move(x, direction, step=-0.1):
    """좌표를 새로운 X좌표로 이동.
        direction: 접선의 기울기.

        step>0인 경우는 접선과 같은 방향으로 이동 -> 최댓값 찾기
        step<0인 경우는 접선과 반대 방향으로 이동 -> 최솟값 찾기"""
    return x + step * direction


if __name__ == '__main__':
    # ex01에서 작성한 함수들을 이용
    # 함수 g(X)의 그래프를 그림
    # 극값(local 최소/최대)를 경사하강법으로 찾자

    xs = [x / 10 for x in range(-30, 31)]
    # 그래프를 그릴 y 좌표들
    ys = [g(x) for x in xs]
    h = 0.0000001
    tolerance = 0.0001
    # 두 개의 x좌표 사이의 거리가 tolerance 이하이면 반복문 종료
    count = 0
    init_x = -1.9  # 시작 값

    while True:  # 반복문최대
        count += 1
        # x좌표에서의 접선의 기울기를 계산
        gradient = difference_quotient(g, init_x, h=0.001)
        # 찾은 기울기를 사용해서 x좌표를 이동
        next_x = move(init_x, gradient, step=+0.2)  # 최소값은 (-), 최대값은 (+)
        print(f'{count}: x = {next_x}')
        tangent_estimates = [tangent(x, gradient, init_x, g(init_x)) for x in xs]
        plt.plot(xs, tangent_estimates, label=f'x={init_x}', color='pink')
        if abs(next_x - init_x) < tolerance:
            # 이동 전과 이동 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점이 다음 반복에서는 시작점이 되어야 한다
            init_x = next_x
    count = 0
    init_x = 1.9  # 시작 값
    while True:  # 반복문최소
        count += 1
        # x좌표에서의 접선의 기울기를 계산
        gradient = difference_quotient(g, init_x, h=0.001)
        # 찾은 기울기를 사용해서 x좌표를 이동
        next_x = move(init_x, gradient, step=-0.2)  # 최소값은 (-), 최대값은 (+)
        print(f'{count}: x = {next_x}')
        tangent_estimates = [tangent(x, gradient, init_x, g(init_x)) for x in xs]
        plt.plot(xs, tangent_estimates, label=f'x={init_x}', color='skyblue')
        if abs(next_x - init_x) < tolerance:
            # 이동 전과 이동 후의 x값의 차이가 tolerance 미만이면 반복문 종료
            break
        else:
            # 이동한 점이 다음 반복에서는 시작점이 되어야 한다
            init_x = next_x

    plt.axhline(y=0, color='black')  # y=0인 수직보조선
    plt.axvline(x=0, color='black')  # x=0인 수직보조선
    plt.ylim(bottom=-2, top=2)
    plt.plot(xs, ys)

    plt.show()

    """   for _ in range(12):
            # x = init_x에서의 접선의 기울기
            gradient = difference_quotient(g, init_x, h=0.01)
            # 접선을 그래프로 그리기 위해서
            tangent_estimates = [tangent(x, gradient, init_x, g(init_x)) for x in xs]
            plt.plot(xs, tangent_estimates, label=f'x={init_x}')
            # x 좌표를 새로운 좌표로 이동
            init_x = move(init_x, gradient, step=-0.2)  # 기울기가 (-)이면 step이 양의 방향으로, (+)이면 음의 방향으로 이동

        plt.axhline(y=0, color='black')  # y=0인 수직보조선
        plt.axvline(x=0, color='black')  # x=0인 수직보조선
        plt.plot(xs, ys)

        plt.show()"""

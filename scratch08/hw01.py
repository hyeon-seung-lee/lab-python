import os
import random

from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step
from scratch08.ex04 import linear_gradient, minibatches
import matplotlib.pyplot as plt


def my_csv_reader(fn: str, header=True, encoding='utf-8') -> list:
    """
    csv 파일의 데이터를 2차원 행렬 형태로 리턴

    :param fn: 읽을 csv 파일 이름(예: data\\exam.csv)
    :param header: csv 파일의 헤더 존재 여부
    :param encoding: 파일 인코딩
    :return: csv 파일에서 헤더는 제외한 데이터들로 이루어진 2차원 리스트
    """
    data = []  # 빈 리스트를 만든다.
    with open(fn, mode='r', encoding=encoding) as f:
        if header:  # csv 파일에 컬럼 이름들이 헤더에 있으면
            f.readline()  # 한 줄을 읽고 지나간다.
        for line in f:  # 파일 끝까지 한 줄씩 읽어서
            # 읽은 줄의 앞/뒤 공백문자를 제거하고(strip),
            # 문자열을 쉼표(,)로 분리(split)해서 문자열 리스트를 만들고,
            # 리스트 data에 추가한다.
            data.append(line.strip().split(','))


    return data


# 작성한 함수들을 테스트
input_file = os.path.join('mpg.csv')
mpg_data = my_csv_reader(input_file)
print(mpg_data)
displ_cty = []

for row in mpg_data:
    x = [float(row[3]), float(row[8])]
    displ_cty.append(x)
dataset = [(x, y) for x, y in displ_cty]

if __name__ == '__main__':

    print(displ_cty)

    theta = [1, 1]  # [기울기, 절편], y = x + 1
    # 파라미터의 값을 변경할 때 사용할 가중치(학습률, learning rate)
    step = 0.001  # next_x = init_x + step * gradient

    for epoch in range(200):  # 임의의 회수(epoch)만큼 반복
        random.shuffle(dataset)  # 데이터 세트를 랜덤하게 섞음
        # 각각의 epoch마다
        # 데이터 세트에서 샘플(x, y)를 추출
        for x, y in dataset:
            # 각 점에서 gradient를 계산
            gradient = linear_gradient(x, y, theta)
            # 파라미터 theta(직선의 기울기와 절편)를 변경
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 10 == 0:
            print(f'{epoch}: {theta}')

    print('\n=== 배치 경사 하강법 ===')
    step = 0.001
    theta = [1, 1]  # 임의의 값으로 [기울기, 절편] 설정
    for epoch in range(5000):
        # 모든 샘플에서의 gradient를 계산
        gradients = [linear_gradient(x, y, theta)
                     for x, y in dataset]
        # gradients의 평균을 계산
        gradient = vector_mean(gradients)
        # 파라미터 theta(기울기, 절편)을 변경
        theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')

    print('\n=== 미니 배치 경사 하강법 ===')
    theta = [1, 1]  # 임의의 파라미터 시작값
    step = 0.001  # 학습률
    for epoch in range(1000):
        mini_batches = minibatches(dataset, 20, True)
        for batch in mini_batches:
            gradients = [linear_gradient(x, y, theta)
                         for x, y in batch]
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -step)
        if (epoch + 1) % 100 == 0:
            print(f'{epoch}: {theta}')

    for x,y in dataset:
        plt.scatter(x, y, c='green')
    xs = [x / 10 for x in range(0, 80)]
    ys = [theta[0]*x+theta[1] for x in xs]
    plt.title('dspl & cty')
    plt.xlabel('dspl')
    plt.ylabel('cty')
    plt.plot(xs, ys)
    plt.show()

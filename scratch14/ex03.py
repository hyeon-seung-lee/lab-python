import math
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def logistic(x):
    """Logistic Sigmoid 함수"""
    return 1 / (1 + math.exp(-x))


def predict(row, betas):
    """row의 x1, x2 값과 betas의 b0, b1, b2를 사용해서
    회귀식 y = b0 + b1 * x1 + b2 * x2를 만들고,
    회귀식을 로지스틱 함수의 파라미터에 전달해서 예측값(y_hat)을 알아냄."""
    # y_hat = betas[0] + betas[1] * row[0] + betas[2] * row[1]
    y_hat = betas[0]
    for i in range(len(betas) - 1):
        y_hat += betas[i + 1] * row[i]
    return logistic(y_hat)


def coefficient_sgd(dataset, learning_rate, epochs):  # coefficient_ Stochastic Gradient Descent
    """회귀식 y = b0 + b1 * x1 + b2 * x2의 계수들(b0, b1, b2)을
        stochastic gradient descent 방법으로 근사값을 추정(estimate)
        최소값 : gradient 반대 방향으로, 최대값이면 gradient 방향으로 움직이도록 설계"""
    # 회귀식에서 처음에 사용할 betas의 초깃값을 0으로 시작
    betas = [0 for _ in range(len(dataset[0]))]  # 컬럼 개수만큼 0으로 채운다
    for epoch in range(epochs):  # epochs 회수만큼 반복
        # sse: sum of squared errors
        sse = 0
        for sample in dataset:  # 데이터 세트에서 row 개수만큼 반복
            prediction = predict(sample, betas)  # betas로 추정한 예측값
            y_hat = predict(sample, betas)  # betas로 추정한 예측 값
            error = sample[-1] - y_hat  # 오차 = 실제값 - 예측값
            sse += error ** 2
            # 계수들(b0, b1, b2)를 아래와 같은 방법으로 업데이트
            # b_new = b + learning_rate * error * prediction * (1 - prediction) * x
            betas[0] = betas[0] + learning_rate * error * prediction * (1 - prediction)  # Error을 미분한 식임
            for i in range(len(sample) - 1):
                betas[i + 1] = betas[i + 1] + learning_rate * error * prediction * (1 - prediction) * sample[i]
        print(f'>>>  epoch={epoch}, learning_rate={learning_rate}, sum_of_squared_errors={sse}')
    # 모든 epoch가 끝난 다음 최종 beta를 return
    return betas


if __name__ == '__main__':
    iris = load_iris()
    print(iris.keys())
    print(iris.DESCR)

    X = iris.data
    y = iris.target
    features = iris.feature_names  # iris['feature_names']

    for i in range(len(features)):
        plt.scatter(X[:, i], y, label=features[i])

    plt.legend()
    plt.show()

    # petal-length, petal-width가 class(품종)을 분류할 때 상관 관계가 높아 보임.
    X = X[:, 2:4]  # pl, pw만 선택
    print(X[:5])

    # setosa 5개, setosa가 아닌 품종 5개를 샘플링
    indices = [x for x in range(0, 100, 10)]  # 테스트 할 x축 값
    sample_data = np.c_[X[indices, :], y[indices]]  # Dataset
    print(sample_data)

    np.random.seed(1218)
    betas = np.random.random(3)
    print('betas: ', betas)

    for sample in sample_data:
        prediction = predict(sample, betas)
        # 오류 = 실제값 - 예측값
        error = sample[-1] - prediction
        # print(f'True: {sample[-1]}, Prediction: {prediction}, Error: {error}')

    learning_rate = 0.3
    epochs = 100
    betas = coefficient_sgd(sample_data, learning_rate, epochs)
    print('beta = ', betas)

    # 모델 성능 측정
    test_sample1 = np.r_[X[1, :], y[1]]
    prediction = predict(test_sample1, betas)
    print(f'True: {test_sample1[-1]}, Predict: {prediction}')

    test_sample2 = np.r_[X[51, :], y[51]]
    print(test_sample2)
    prediction = predict(test_sample2, betas)
    print(f'True: {test_sample2[-1]}, Predict: {prediction}')

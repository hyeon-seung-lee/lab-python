"""
Boston house prices dataset
"""

# 보스턴 집값 데이터 세트 로딩
# 데이터 탐색 -> 그래프
# 학습 세트/검증 세트 나눔
# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# 검증 세트를 사용해서 예측 -> 그래프
# Mean Square Error 계산
# R2-score 계산
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

skl_data = sklearn.datasets.load_boston(return_X_y=False)
print(skl_data.keys())
print(skl_data.feature_names)
features = skl_data.feature_names
X = skl_data.data
y = skl_data.target
print('len(X):',len(X))
print('len(y):',len(y))
fig, ax = plt.subplots(3, 5)
# ax: 3x4 형태의 2차원 배열(ndarray)
ax_flat = ax.flatten()
for i in range(len(features)):
    subplot = ax_flat[i]
    subplot.scatter(X[:, i], y)
    subplot.set_title(features[i])
plt.show()

# 목표 데이터 : RM, LSTAT
rm_data = skl_data['data'][:, 5].reshape(len(skl_data['data']), 1)
lstat_data = skl_data['data'][:, 12]
# print(skl_data.DESCR)
rm_target = skl_data['target']
lstat_target = skl_data['target']

# poly_feature = PolynomialFeatures(degree=2, include_bias=False)
lin_reg = LinearRegression()  # LR 객체 생성 !!
lin_reg.fit(rm_data, rm_target)  # model fitting
print('절편(intercept): ', lin_reg.intercept_)
print('계수(coefficients): ', lin_reg.coef_)
X_test = np.linspace(4, 10, 50).reshape(50, 1)
y_pred = lin_reg.predict(X_test)
# plt.scatter(rm_data, rm_target)
# plt.plot(X_test, y_pred, 'r')  # predict한 결과를 그래프로 구현
# plt.show()


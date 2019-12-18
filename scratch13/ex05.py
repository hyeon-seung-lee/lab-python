"""
Boston house prices dataset
"""

import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 보스턴 집값 데이터 세트 로딩

skl_data = sklearn.datasets.load_boston(return_X_y=False)
print(type(skl_data))  # Bunch: 파이썬의 Dict와 비슷한 타입
print(skl_data.keys())
print(skl_data.feature_names)

# 데이터와 타겟을 구분
X = skl_data.data
y = skl_data.target
print('X shape: ', X.shape)
print('y shape: ', y.shape)

print('len(X):', len(X))
print('len(y):', len(y))

features = skl_data.feature_names
# 데이터 탐색 -> y ~ feature 산점도 그래프

fig, ax = plt.subplots(3, 5)
# ax: 3x4 형태의 2차원 배열(ndarray)
print('fig: ', fig)
# print('ax: ', ax)
ax_flat = ax.flatten()
for i in range(len(features)):
    subplot = ax_flat[i]
    subplot.scatter(X[:, i], y)
    subplot.set_title(features[i])
plt.show()

# 학습 세트/ 검증 세트 나눔
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(f'X_train len: {len(X_train)}, X_test len:{len(X_test)}, y_train len:{len(y_train)}, y_test len:{len(y_test)}')

# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# price = b0 ++ b1 * rm: 주택 가격 ~ 방의 개(rm)
X_train_rm = X_train[:, np.newaxis, 5]  # np.newaxis:
X_test_rm = X_test[:, np.newaxis, 5]  # 2차원 배열로 만들어줌
print(f'X_train_rm: {X_train_rm.shape}, X_test_rm: {X_test_rm.shape} ')

lin_reg = LinearRegression()  # Linear Regression 객체 생성
lin_reg.fit(X_train_rm, y_train)  # fit(학습)  -> b0, b1 찾음
print(f'intercept: {lin_reg.intercept_}, coefficient: {lin_reg.coef_}')

# 검증 세트를 사용해서 예측 -> 그래프
y_pred_rm = lin_reg.predict(X_test_rm)

# 실제값(scatter), 예측값(plot) 그래프
plt.scatter(X_test_rm, y_test)  # 실제값 y_test
plt.plot(X_test_rm, y_pred_rm, 'r-')
plt.title('Price ~ RM')
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()

# MSE: Mean Square Error 계산
# 오차 제곱들의 평균: MSE
# error =  y - y_hat, error**2 = (y-y_hat)**2
# MSE = sum(error**2 = (y-y_hat)**2) / 개수
mse = mean_squared_error(y_test, y_pred_rm)

# RMSE(Squared-Root MSE)
rmse = np.sqrt(mse)
print('Price ~ RMSE=', rmse)

# R2-score 계산
r2_1 = lin_reg.score(X_test_rm, y_test)  # score 함수: R-Square 값 계산
print('Price ~ r2_1: ', r2_1)
r2_2 = r2_score(y_test, y_pred_rm)  # 결정 계수 계산 Coefficient of determination
print('Price ~ r2_2: ', r2_2)

# Price ~ LSTAT 선형회귀: price = b0 + b1 * lstat
# b0, b1 ?
X_train_lstat = X_train[:, np.newaxis, 12]  # 학습 세트
X_test_lstat = X_test[:, np.newaxis, 12]  # 검증 세트

lin_reg.fit(X_train_lstat, y_train)  # 모델 fit, train
print(f'intercept:{lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat = lin_reg.predict(X_test_lstat)  # 예측, 테스트
plt.scatter(X_test_lstat, y_test)  # 실제값 산점도 그래프
plt.plot(X_test_lstat, y_pred_lstat, 'r-')
plt.title('Price ~ LSTAT')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat)
rmse = np.sqrt(mse)
print('Price ~ RMSE=', rmse)
r2_1 = lin_reg.score(X_test_lstat, y_test)  # score 함수: R-Square 값 계산
print('Price ~ r2_1: ', r2_1)
r2_2 = r2_score(y_test, y_pred_lstat)  # 결정 계수 계산 Coefficient of determination
print('Price ~ r2_2: ', r2_2)

# Price ~ LSTAT + LSTAT**2 선형 회귀
# Price = b0 + b1 * lstat + b2 * lstat**2
poly = PolynomialFeatures(degree=2, include_bias=False)
# 데이터에 다항식 항들을 컬럼으로 추갖해주는 클래스 객체
X_train_lstat_poly = poly.fit_transform(X_train_lstat)
# 검증 세트에 다항식 항을 추가
X_test_lstat_poly = poly.fit_transform(X_test_lstat)

lin_reg.fit(X_train_lstat_poly, y_train)
print(f'intercept:{lin_reg.intercept_}, coefficient:{lin_reg.coef_}')
y_pred_lstat_poly = lin_reg.predict(X_test_lstat_poly)

plt.scatter(X_test_lstat, y_test)  # 실제값
xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100, 1))
xs_poly = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')
# plt.plot(X_test_lstat, y_pred_lstat_poly, 'r')  # 예측값
plt.title('Price ~ lstat + lstat^2')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat_poly)
rmse = np.sqrt(mse)
print('Price ~ RMSE=', rmse)

r2_1 = lin_reg.score(X_test_lstat_poly, y_test)  # score 함수: R-Square 값 계산
print('Price ~ r2_1: ', r2_1)
r2_2 = r2_score(y_test, y_pred_lstat_poly)  # 결정 계수 계산 Coefficient of determination
print('Price ~ r2_2: ', r2_2)

# Price ~ RM + LSTAT 선형 회귀: price = b0 + b1 * rm + b2 * lstat
X_train_rm_lstat = X_train[:, [5, 12]]
X_test_rm_lstat = X_test[:, [5, 12]]
print(X_train_rm_lstat[:5])

lin_reg.fit(X_train_rm_lstat, y_train)  # fit/train
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)  # predict/test
print(y_test[:5], y_pred_rm_lstat[:5])

mse = mean_squared_error(y_test, y_pred_rm_lstat)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat)
print(f'Price ~ RM + LSTAT: RMSE = {rmse}, R**2 = {r2}')
print('-====================================')
# Price ~ RM + LSTAT + RM**2 + RM * LSTAT + LSTAT**2
# Price = b0 + b1 * rm + b2 * lstat + b3 * rm**2 + b4 * rm * lstat + b5 * lstat **2
# 학습 세트에 다항식항(컬럼)을 추가
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
# 테스트 세트에 다항식항(컬럼)을 추가
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)
print(X_test_rm_lstat_poly[:2])
lin_reg.fit(X_train_rm_lstat_poly, y_train)
print(f'intercept: {lin_reg.intercept_}, coef: {lin_reg.coef_}')

y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)

mse = mean_squared_error(y_test, y_pred_rm_lstat_poly)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat_poly)
print(f'Price ~ RM + LSTAT: RMSE = {rmse}, R**2 = {r2}')

print('y true:', y_test[:5])
print('y pred:', y_pred_rm_lstat_poly[:5])

# Price ~ RM + LSTAT + STAT**2
# Price = b0 + b1 * rm + b2 * lstat + b3 * lstat**2

X_train_last = np.c_[X_train_rm, X_train_lstat_poly]
X_test_last = np.c_[X_test_rm, X_test_lstat_poly]
print('X_train_last:', X_train_last[:2], '\n X_test_last: ', X_test_last[:2])

lin_reg.fit(X_train_last, y_train)  # fit/train
print(f'Price ~ RM + LSTAT + LSTAT**2: intercept: {lin_reg.intercept_}, coef {lin_reg.coef_}')

y_pred_last = lin_reg.predict(X_test_last)  # 예측/테스트
print('y true:', y_test[:5])
print('y predict:', y_pred_last[:5].round(2))


mse = mean_squared_error(y_test, y_pred_last)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_last)
print(f'Price ~ RM + LSTAT: RMSE = {rmse}, R**2 = {r2}')


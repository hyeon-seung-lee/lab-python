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
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train_lstat = X_train[:, np.newaxis, 12]  # 학습 세트
X_test_lstat = X_test[:, np.newaxis, 12]  # 검증 세트


# Price = b0 + b1 * rm + b2 * lstat + b3 * rm**2 + b4 * rm * lstat + b5 * lstat **2
# Price ~ RM + LSTAT + RM**2 + RM * LSTAT + LSTAT**2

X_train_rm_lstat = X_train[:, [5, 12]]
X_test_rm_lstat = X_test[:, [5,12]]


poly = PolynomialFeatures(degree=2, include_bias=False)
# 데이터에 다항식 항들을 컬럼으로 추갖해주는 클래스 객체
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
# 검증 세트에 다항식 항을 추가
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)
lin_reg = LinearRegression()  # Linear Regression 객체 생성

lin_reg.fit(X_train_rm_lstat_poly, y_train)
print(f'intercept:{lin_reg.intercept_}, coefficient:{lin_reg.coef_}')
y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)



# Price ~ RM + LSTAT + STAT**2
# Price = b0 + b1 * rm + b2 * lstat + b3 * lstat**2

"""
R을 활용한 머신 러닝 - 암 데이터 파일(csv)
Scikit-learn 패키지 활용, kNN 결과
"""
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

bc_data = pd.read_csv('wisc_bc_data.csv', encoding='UTF-8')
print(bc_data.head())

# X: id, diagnosis 제외한 데이터
X = bc_data.iloc[:, 2:].to_numpy()
# y: 두번째 열 데이터
y = bc_data.iloc[:, 1].to_numpy()
# print(X.iloc[:5])
# print(y.iloc[:5])

# 전체 데이터 세트를 학습 세트(training set)와 검증 세트(test set)로 나눔
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(len(X_train), len(X_test))
print(X_train[:3])
print(y_train[:3])

# 3. 거리 계산을 위해서 각 특성들을 스케일링(표준화)
    # Z-score 표준화: 평균을 0, 표준편차 1로 변환
scaler = StandardScaler()  # Scaler 객체 생성
scaler.fit(X_train)  # 스케일링(표준화)를 위한 평균과 표준 편차 계산
X_train = scaler.transform(X_train)  # 스케일링(표준화 수행)
X_test = scaler.transform(X_test)
print('== X_train ==')
for col in range(4):
    print(f'평균 = {X_train[:, col].mean()}, 표준편차= {X_train[:, col].std()}')

print('== X_test ==')
for col in range(4):
    print(f'평균 = {X_test[:, col].mean()}, 표준편차= {X_test[:, col].std()}')

    # 4. 학습/예측(Training/Pradiction)
    # k-NN 분류기를 생성
classifier = KNeighborsClassifier(n_neighbors=5)

# 분류기 학습
classifier.fit(X_train, y_train)
# 예측
y_pred = classifier.predict(X_test)
print(y_pred)

# 5. 모델 평가
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

report = classification_report(y_test, y_pred)
print(report)

# 정확도(accuracy) = (전체 정답 수) / (전체 문제 수)
# 6. 모델 개선 - k값을 변화시킬 때, 에러가 줄어드는 지
errors = []
for i in range(1, 31):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    errors.append(np.mean(pred_i != y_test))
print(errors)

plt.plot(range(1, 31), errors, marker='o')
plt.title('Mean error with K-Value')
plt.xlabel('k-value')
plt.ylabel('mean error')
plt.show()

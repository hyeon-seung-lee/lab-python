import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
X = boston['data']  # boston.data
y = boston['target']  # boston.target
features = boston['feature_names']  # boston.feature_names

# DataFrame으로 변환
boston_df = pd.DataFrame(X, columns = features, index= None)

boston_df['Price'] = y
print(boston_df.head())
print(boston_df.shape)
print(boston_df.describe())

columns = ['LSTAT', 'INDUS', 'NOX', 'RM', 'Price']
subset_df = boston_df[columns]

sns.pairplot(subset_df)
plt.show()

# 상관 행렬(correlation matrix) : 상관계수들로 이루어진 행렬
# 상관 계수(correlation coefficientE)가 클 수록 진한 색으로 표시됨

corr_matrix = subset_df.corr(round(2))

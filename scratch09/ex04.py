"""
pandas 패키지를 사용한 csv 파일 읽기
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
file_path = os.path.join('..', 'scratch08', 'mpg.csv')
df = pd.read_csv(file_path)
print(df)
print(df.head())  # 데이터 프레임의 앞의 일부분 데이터 출력
print('shape:', df.shape)  # 관측값: 234, 변수: 11
print('data types:', df.dtypes)

# DataFrame.dtypes: 각 컬럼(변수)의 데이터 타입
# pandas의 데이터 타입: object(문자열), float(실수), int(정수)

print(df.describe()) # 기술 통계 요약 통계량

# df['column_name']: DataFrame에서 특정 컬럼의 모든 데이터를 선택
displ = df['displ']
print(displ)
cty = df['cty']

plt.scatter(displ, cty)
# plt.show()
print(' ')
# DataFrame에서 행(row)을 선택할 때,
# df.iloc[행 번호(인덱스)], df.loc[행 레이블]
print('행번호 0: ',df.iloc[0])
print(df.iloc[0:3]) # row index 0 이상 3 미만인 행 선택

print('---d---')
# 데이터 프레임에서 여러개의 컬럼(변수)들을 선택
cols = ['displ', 'cty', 'hwy']  # []: 리스트
print('dfcols', df[cols])  # []: 인덱스 연산자

print('??')
# 데이터 프레임에서 여러개의 행(관측값)과 컬럼(변수)들을 선택
# df.loc[row_labels, col_labels]: 행과 열의 레이블(이름)
# df.iloc[row_indices, col_indices]: 행과 열의 인덱스(숫자)
print(df.loc[0:3, cols])
print(df.iloc[0:3, 0:3])
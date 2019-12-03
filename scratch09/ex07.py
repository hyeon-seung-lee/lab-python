"""
pandas 데이터 타입
Series: 1차원 리스트. 인덱스가 한 개.
DataFrame: 2차원 리스트. 인덱스가 행과 열 두 개를 갖음.
"""
import numpy as np
import pandas as pd

a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(a))  # Series
print('----')
# Series에서 특정 인덱스의 아이템 선택: Series[index]
print(a[0])  # a[0]의 데이터 타입: float64
# 인덱스 연산자([]) 안에서 범위 연산자(:)를 사용할 수도 있음
print(a[0:3])  # a[0:3]의 데이터 타입: Series
# 인덱스 연산자([]) 안에서 리스트 연산자([])을 사용할 수도 있음.
print(a[[0, 2, 4]])  # print(a[[0, 2, 4]]) 데이터 타입: Series

# dict 타입({key: value, ...})의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no': [3, 13, 23],
    'name': ['김영광', '이은지', '조유경'],
    'gender': ['M', 'F', 'F']
})
print(df)

# 2차원 리스트([ [...], [...], [...] ]) 타입의 데이터에서 DataFrame을 생성
students = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
], columns=['no', 'name', 'gender'])
print(students)

# DataFrame.iloc[row_index, column_index]
print(students.iloc[0, 0])  # 0번 row, 0번 column의 아이템
print(students.iloc[0, 0:3])  # 0번 row, 0, 1, 2 column의 아이템
print(type(students.iloc[0, 0:3]))  # Series
print(students.iloc[0:2, 0:2])
print(type(students.iloc[0:2, 0:2]))

print(students.iloc[:, 1:3])  # 행은 생략 불가능
print(students.iloc[1:3, :])
print(students.iloc[1:3])  # 열은 생략 가능

print("-----")

# boolean indexing
# print(students[[False, True, False]])
condition = (students['gender'] == 'M')
print(condition)

print(students[condition])
print('=-=-=-=')
students.columns = ['no', 'name', 'gender']  # column 이름 수정

stu_df2 = pd.concat([df, students], axis=0, ignore_index=True)  # 데이터프레임 합치기, axis = 0 :  cbind , axis = 1 : rbind
# print(stu_df)
#
# print(stu_df.iloc[0])
# print(stu_df.loc[0])

# DataFrame.sort_values(정렬 기준 컬럼 이름)
print(stu_df2.sort_values('no'))
print('mmmmmmmmmmmmmmm')
# 두 개 이상의 조건으로 boolean indexing
cond1 = stu_df2['no'] % 2 == 1  # no 컬럼의 값이 홀수이면
cond2 = stu_df2['gender'] == 'F'  # gender 컬럼의 값이 'F'이면
subset = stu_df2[cond1 & cond2]  # and 를 사용하면 안된다
print(subset)

# boolean 인덱싱에서는 and, or 연산자는 사용할 수 없고,
# 각 성분별로 연산을 하는 (bitwise 연산자)는 &, |를 사용해야 한다

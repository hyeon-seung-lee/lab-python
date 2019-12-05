"""
pandas groupby, aggregate, apply
"""
import numpy as np
import pandas as pd

# 데이터 프렝림 생성
np.random.seed(1)
df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randint(0, 10, 5),
    'data2': np.random.randint(0, 10, 5)
})
print(df)

grouped1 = df.groupby(by='key1')
print(grouped1)  # DataFrameGroupBy 객체 - 그룹 연산을 적용하기 위해 만든 객체
# 그룹 연산: count, sum, mean, median, var, std, min, max, ...
cnt = grouped1['data1'].count()
print(type(cnt))
print(cnt)
print(cnt['a'], cnt['b'])

print(grouped1['data1'].mean())
print(grouped1.mean())  # 숫자 데이터 컬럼들에만 mean()함수를 적용해줌
print(grouped1[['data1', 'data2']].mean())

grouped2 = df.groupby(by='key2')
print(grouped2.mean())

# groupby의 기준(by)이 2개 이상의 컬럼일 때는 리스트를 전달
grouped3 = df.groupby(by=['key1', 'key2'])
print(grouped3['data1'].count())

people = pd.DataFrame(np.random.randint(0, 10, (5, 5)),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
print(people)
print(people.groupby(len).sum())
print(people.groupby(lambda x: x.startswith('J')).sum())


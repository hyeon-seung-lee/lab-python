"""
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서
DataFrame으로 변환.
DataFrame의 행과 열의 개수 확인
DataFrame의 앞의 데이터 5개를 출력
DataFrame의 뒷쪽 데이터 5개를 출력
DataFrame의 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame의 'country', 'lifeExtp', 'gdpPercap'컬럼들만 출력
DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력
DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력
DataFrame에서 연도(year)별 기대 수명의 평균을 출력
DataFrame에서 연도(year)별 대륙(continent)별 기대 수명의 평균
"""

import os
import pandas as pd
# gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서
# DataFrame으로 변환.
file_path = os.path.join('gapminder.tsv')
df = pd.read_csv(file_path, sep='\t')
print(df)
# DataFrame의 행과 열의 개수 확인
print('shape:', df.shape)
ncols, nrows = df.shape
# DataFrame의 앞의 데이터 5개를 출력
print('head:', df.head())
# DataFrame의 뒷쪽 데이터 5개를 출력
print('tail:', df.tail())
print(df.iloc[nrows-5:nrows])
# DataFrame의 컬럼 이름들을 출력
print('columnname:', df.columns)
# DataFrame의 각 컬럼의 데이터 타입들을 출력
print('dtypes:', df.dtypes)
# DataFrame의 'country', 'lifeExtp', 'gdpPercap'컬럼들만 출력
cols = ['country', 'lifeExp', 'gdpPercap']
print("'country', 'lifeExtp', 'gdpPercap'만 출력: \n")
print(df[cols])
# DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력
print('DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력')
print(df.iloc[[0, 99, 999], ])
# DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력
print('DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력')
print(df.loc[840:851, cols])
# DataFrame에서 연도(year)별 기대 수명의 평균을 출력
print('DataFrame에서 연도(year)별 기대 수명의 평균을 출력')
print(df.groupby('year').mean())
# DataFrame에서 연도(year)별 대륙(continent)별 기대 수명의 평균
print('DataFrame에서 연도(year)별 대륙(continent)별 기대 수명의 평균')
print(df.groupby(['year','continent'])['lifeExp'].mean())

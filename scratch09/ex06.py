# gapminder.tsv 파일을 읽어서 데이터 프레임 생성
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
print(df.iloc[0:5])
# boolean indexing:
# 컬럼의 값을 이용해서 특정 레코드(행, row)들을 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
# SQL: select * from DataFrame where column == '';
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print(df_korea)

# 대한민국(Korea, Rep.)의 인구(pop)와 1인당 GDP(gdpPercap)을 출력
df_korea_pop_gdp = df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']]
print(df_korea_pop_gdp)
print('------------------------------------------------------------')
# mpg.csv 파일을 읽어서 DataFrame을 생성
# cty 컬럼의 값이 cty 평균보다 큰 자동차들의 model, displ, cty, hwy를 출력
# cty 컬럼 평균 계산
# cty 컬럼 값이 평균보다 큰 레코드들 출력
# cty 컬럼 값이 평균보다 큰 자동차들의 model, cty, hwy 컬럼 출력
mpg = pd.read_csv('../scratch08/mpg.csv')
cty_mean = mpg['cty'].mean()

print(mpg[mpg['cty'] > cty_mean])
print(cty_mean)
print('---------------------------')
print(mpg['cty'], mpg['model'])
print(mpg[['cty', 'model']])

# print(type(mpg[1]))

mean_cty_df = mpg[['cty']].mean()
mean_cty_series = mpg['cty'].mean()
print(mean_cty_df)
print(mean_cty_series)
print('*-*********************************')
# cty 컬럼의 값이 평균보다 큰 레코드들을 출력
print(mpg[mpg['cty']> mean_cty_series][['model', 'cty', 'hwy']])
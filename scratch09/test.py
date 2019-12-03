import pandas as pd
df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
# df_afg = df[df['country'] == 'Afghanistan']
print(df[['country']])
print(type(df[['country']]))

"""
          country
0     Afghanistan
1     Afghanistan
2     Afghanistan
3     Afghanistan
4     Afghanistan
...           ...
1699     Zimbabwe
1700     Zimbabwe
1701     Zimbabwe
1702     Zimbabwe
1703     Zimbabwe
"""

print(df['country'])
print(type(df['country']))
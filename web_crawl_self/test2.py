import pandas as pd

abc = {'a': 'abc', 'b': 'bcd'}
link_data = pd.DataFrame(abc.items(), columns=['chr', 'link'])
link_data.to_csv('dic_link.csv', encoding='cp949')

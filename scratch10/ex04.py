import pandas as pd

from scratch10.ex02 import peak_to_peak

if __name__ == '__main__':
    # tips.csv 파일을 읽어서 데이터 프레임을 생성
    tips = pd.read_csv('tips.csv', encoding='UTF-8')
    print(type(tips))
    print(tips.iloc[0:5])
    # DataFrame에 tip_pct 컬럼 추가: 팁금액 / 총금액
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    print(tips.iloc[0:5])
    # day, smoker별 그룹을 지어서,
    grouped = tips.groupby(['day', 'smoker'])
    grouped_tip_pct = grouped['tip_pct']
    # tip_pct의 평균을 출력
    # print(grouped_tip_pct.mean())
    print(grouped_tip_pct.agg('mean'))

    # day, smoker별 그룹의 tip_pct의 평균, 표준편차, 최대/최소 차이를 출력
    print(grouped_tip_pct.agg(mean='mean', std='std', max_min=lambda x: x.max() - x.min()))

    # day, smoker별 그룹의 tip_pct, total_bill 컬럼의 평균, 표준편차, 최대/최소 차이
    grouped_pct_bill = grouped[['tip_pct', 'total_bill']]
    # print(grouped_pct_bill.agg(average='mean',
    #                            std_dev='std',
    #                            range=lambda x: x.max() - x.min()))
    print('--------------')
    print(grouped_pct_bill.agg([('mean', 'mean'),
                                ('std_dev', 'std'),
                                ('range', lambda x: x.max() - x.min())]))

    # GroupBy 객체의 컬럼들마다 다른 함수를 agg로 적용할 때
    # agg({'col_name':[functions], ... })
    # 그루핑된 데이터 프레임의 tip 컬럼에는 max() 함수를 aggregate하고,
    # size 컬럼에는 sum()함수를 aggregate 하겠다.
    result = grouped.agg({'tip': 'max', 'size': 'sum'})
    print(result)
    functions = ['mean',  'std', ('range', lambda x: x.max() - x.min())]
    result = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(result)
    print(grouped['tip'].mean())
    # grouping 컬럼들을 인덱스로 사용하지 않고자 할 때,
    grouped = tips.groupby(['day', 'smoker'], as_index=False)
    print(grouped['tip'].mean())
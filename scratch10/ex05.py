import numpy as np
import pandas as pd


def squares(x):
    return x ** 2


def doubles(x):
    return x * 2


if __name__ == '__main__':
    result1, result2 = squares(3), doubles(3)
    print(result1, result2)

    array = np.array([1, 2, 3])
    result1 = squares(array)  # np.array ** 2
    result2 = doubles(array)  # np.array * 2
    print(result1, result2)

    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })
    print(df)
    print(squares(df))

    result = [[1, 2, 3], [4, 5, 6]]
    print(doubles(result))

    result = df.apply(squares, axis=1)  # 데이터프레임을 함수의 파라미터로 넣는 함수 apply
    print(result)

    # print(np.sum([1, 2, 3]))
    result = df.apply(np.sum, axis = 0)
    print(result)

        # 함수의 리턴값을 돌려받음
        # agg(aggregate) 함수는 GroupBy 객체에서만 사용 가능
        # apply는 DataFrame과 GroupBy 객체 모두에서 사용 가능

    emp = pd.read_csv('emp_df.csv')
    print(emp.agg(np.mean))  # 집계 함수는 숫자 타입의 컬럼만 자동으로 선택
    # emp.apply(np.mean)
    # apply 함수는 모든 컬럼 또는 행을 함수의 파라미터에 전달하기 때문에,
    # 집계 함수(mean, sum, ...)가 제대로 동작하지 않을 수도 있음.
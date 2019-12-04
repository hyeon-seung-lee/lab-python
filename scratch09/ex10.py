import cx_Oracle
import pandas as pd


def get_column_names_of(table, cursor_):
    sql1 = """select column_name from user_tab_columns
                where table_name = :table_name
                order by column_id"""
    # sql2 = 'select  * from :table_name'
    cursor_.execute(sql1, table_name=table.upper())  # 끝에 세미콜론(;) 을 붙이면 안됨
    # cursor_.execute(f'select * from {table}')
    col_names = [row[0] for row in cursor]
    return col_names


def select_all_from(table, cursor_):
    # print(table.upper())
    sql1 = f"select * from {table.upper()}"  # from 뒤의 컬럼명에는 '' 콜론이 오면 안되므로 데이터 바인딩을 사용할 수 없고, formatted string을 사용해야 한다
    cursor_.execute(sql1)
    # cursor_.execute(f'select * from {table}')
    req_table = cursor.fetchall()
    df_table = pd.DataFrame(req_table)
    df_table.columns = get_column_names_of(table, cursor)
    return df_table


if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # Cursor 객체 생성
        with connection.cursor() as cursor:
            print(get_column_names_of('emp', cursor))  # ['empno', 'ename', 'job']
            # connection.commit()

            emp_df = select_all_from('emp', cursor)
            print(emp_df)

            dept_df = select_all_from('dept', cursor)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            connection.commit()
            # DataFrame에 새로운 컬럼을 추가
            # DataFrame['컬럼 이름'] = List, pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['sal'] 개수만큼에 대해서 반복:
            # 선택한 행의 sal 값이 salgrade_df 어느 grade에 속하는지를 찾아야 함.
            # -> salgrade_df의 행 개수만큼 반복하면서 LO, HI 와 비교
            # -> DataFrame.iterrows() 함수 이용
    # print(len(emp_df.iloc[:, 0]))
    emp_df_salgrade = []
    for i in range(len(emp_df.iloc[:, 0] + 1)):
        print('i: ', i)
        print('salary: ', emp_df['SAL'][i])
        for j in range(len(salgrade_df.iloc[:, 0] + 1)):
            # print('j: ',j)
            if (emp_df['SAL'][i] <= salgrade_df['HISAL'][j]) and (emp_df['SAL'][i] >= salgrade_df['LOSAL'][j]):
                emp_df_salgrade.append(salgrade_df['GRADE'][j])
                print('grade:', salgrade_df['GRADE'][j])
            else:
                continue
    print(emp_df_salgrade)
    print(len(salgrade_df.iloc[:, 0]))
    emp_df['SALGRADE'] = emp_df_salgrade
    print(emp_df)

# SQL join - pandas.merge

emp_dept = pd.merge(emp_df, dept_df, on='DEPTNO', how = 'left')
print(emp_dept)
